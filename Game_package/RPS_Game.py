import cv2
import mediapipe as mp
import numpy as np
import random
import time

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize win counters
user_wins = 0
computer_wins = 0


# Function to classify the gesture based on distance
def classify_gesture(landmarks):
    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]

    distance = ((middle_tip.x - index_tip.x) ** 2 + (middle_tip.y - index_tip.y) ** 2) ** 0.5

    if distance < 0.05:  # Threshold for rock gesture
        gesture = "Rock"
    elif distance > 0.05 and distance < 0.1:  # Threshold for scissors gesture
        gesture = "Paper"  # "Paper"
    elif distance > 0.1 and distance < 0.2:  # Threshold for scissors gesture
        gesture = "Scissors"  # "Paper"
    else:
        gesture = "None"
    return gesture



# Function to determine the winner
def determine_winner(user_gesture, computer_gesture):
    global user_wins, computer_wins
    if user_gesture == computer_gesture:
        return "It's a tie!"
    elif (user_gesture == "Rock" and computer_gesture == "Scissors") or \
            (user_gesture == "Paper" and computer_gesture == "Rock") or \
            (user_gesture == "Scissors" and computer_gesture == "Paper"):
        user_wins += 1
        return "You win!"
    else:
        computer_wins += 1
        return "Computer wins!"


# Initialize video capture
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Display instructions
        # Display countdown
        for i in range(5, 0, -1):
            ret, frame = cap.read()
            if not ret: break
            frame_copy = frame.copy()
            cv2.rectangle(frame_copy, (10, 10), (200, 50), (0, 0, 0), -1)
            cv2.putText(frame_copy, f"Show your gesture in {i}...", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.imshow("Rock Paper Scissors Game", frame_copy)
            if cv2.waitKey(1000) & 0xFF == ord('q'):
                print("Key pressed: q")
                break

        # Check if 'q' key was pressed to exit during countdown
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting during countdown")
            break

        # Convert the image to RGB and process it
        # After the countdown, capture the image and classify the gesture
        ret, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        user_gesture = "None"
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                user_gesture = classify_gesture(hand_landmarks.landmark)

        if user_gesture == "None":
            cv2.rectangle(frame, (10, 60), (800, 120), (0, 0, 0), -1)
            cv2.putText(frame, "Please make an acceptable gesture!", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 0, 255), 2)
        else:
            # Generate computer's gesture
            computer_gesture = random.choice(["Rock", "Paper", "Scissors"])

            # Determine the winner
            result_text = determine_winner(user_gesture, computer_gesture)

            # Display results
            #cv2.rectangle(frame, (10, 60), (800, 180), (0, 0, 0), -1)
            cv2.putText(frame, f"Your Gesture: {user_gesture}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(frame, f"Computer's Gesture: {computer_gesture}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 0, 0), 2)
            cv2.putText(frame, result_text, (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display win counts
        cv2.putText(frame, f"User Wins: {user_wins}", (frame.shape[1] - 200, frame.shape[0] - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 2)
        cv2.putText(frame, f"Computer Wins: {computer_wins}", (frame.shape[1] - 200, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 2)

        cv2.imshow("Rock Paper Scissors Game", frame)

        # Wait for a few seconds to show the result or prompt
        # cv2.waitKey(3000)

        if cv2.waitKey(3000) & 0xFF == ord('q'):
            print("Quitting after result display")

            # Display final score
            final_frame = frame.copy()
            cv2.rectangle(final_frame, (10, 60), (800, 180), (0, 0, 0), -1)
            cv2.putText(final_frame, f"Final Score - User: {user_wins}, Computer: {computer_wins}", (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Rock Paper Scissors Game", final_frame)
            cv2.waitKey(5000)
            break

cap.release()
cv2.destroyAllWindows()
