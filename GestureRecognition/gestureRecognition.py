import cv2
import mediapipe as mp

# Initialize MediaPipe Hands and Drawing modules
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Function to process video and recognize gestures
def process_video(video_path):
    # Open video file
    cap = cv2.VideoCapture(video_path)

    # Initialize MediaPipe Hands
    with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert the BGR image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame and get hand landmarks
            results = hands.process(image)

            # Convert the image back to BGR
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Draw hand landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Display the result
            cv2.imshow('Gesture Recognition', image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

# Find the specific video file in the project folder
import os

def find_video_file(project_folder, video_name):
    for root, dirs, files in os.walk(project_folder):
        if video_name in files:
            return os.path.join(root, video_name)
    return None

if __name__ == "__main__":
    # Replace 'your_project_folder' with the actual path and 'your_video.mp4' with your video file name
    project_folder = 'D:/Users/BroMikey/Documents/BasicTools/Python-learning/GestureRecognition'
    video_name = 'gesture.mp4'

    video_path = find_video_file(project_folder, video_name)
    if video_path:
        process_video(video_path)
    else:
        print("Video file not found.")
