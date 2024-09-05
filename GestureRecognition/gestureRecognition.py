import cv2
import mediapipe as mp

# 初始化MediaPipe手部和绘图模块
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


# 基于手部地标识别简单手势的功能
# def recognize_gesture(hand_landmarks):
#     # 每个手指的标志性位置
#     thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
#     index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
#     middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
#     ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
#     pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

#     # 基于手指位置的手势识别
#     fingers = [
#         thumb_tip < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y,
#         index_tip < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y,
#         middle_tip < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y,
#         ring_tip < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y,
#         pinky_tip < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
#     ]

#     # 数伸出的手指的数目
#     finger_count = fingers.count(True)

#     # 根据伸出的手指数返回手势名称
#     if finger_count == 0:
#         return "Fist"
#     elif finger_count == 1:
#         return "1 Finger"
#     elif finger_count == 2:
#         return "2 Fingers"
#     elif finger_count == 3:
#         return "3 Fingers"
#     elif finger_count == 4:
#         return "4 Fingers"
#     elif finger_count == 5:
#         return "Open Hand"
#     else:
#         return "Unknown Gesture"


# 基于手部关键点识别复杂手势的函数
def recognize_gesture(hand_landmarks):
    # 获取每根手指的关键点位置
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    middle_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    # 根据手指位置进行手势识别
    fingers = [
        thumb_tip < thumb_ip,  # 拇指
        index_tip < index_mcp,  # 食指
        middle_tip < middle_mcp,  # 中指
        ring_tip < middle_mcp,  # 无名指
        pinky_tip < middle_mcp  # 小拇指
    ]

    # 统计伸出的手指数量
    finger_count = fingers.count(True)

    # 复杂手势识别
    if fingers[0] and not fingers[1] and not fingers[2] and not fingers[3] and not fingers[4]:
        return "Thumbs Up"
    elif fingers[2] and fingers[3] and fingers[4] and not fingers[0] and not fingers[1]:
        return "OK"
    elif fingers[1] and fingers[2] and not fingers[3] and not fingers[4] and not fingers[0]:
        return "Yeah"
    elif finger_count == 0:
        return "Fist"
    elif finger_count == 1:
        return "1 Finger"
    elif finger_count == 2:
        return "2 Fingers"
    elif finger_count == 3:
        return "3 Fingers"
    elif finger_count == 4:
        return "4 Fingers"
    elif finger_count == 5:
        return "Open Hand"
    else:
        return "Unknown Gesture"


# 实时处理视频并识别手势的函数
def process_video():
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 初始化MediaPipe手部
    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # 将BGR图像转换为RGB图像
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 处理帧并获取手部关键点
            results = hands.process(image)

            # 将图像转换回BGR格式
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # 绘制手部关键点并识别手势
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # 识别手势
                    gesture_name = recognize_gesture(hand_landmarks)

                    # 在视频中显示手势名称
                    cv2.putText(image, gesture_name,
                                (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1,
                                (0, 255, 0),
                                2,
                                cv2.LINE_AA)

            # 显示结果
            cv2.imshow('Gesture Recognition', image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    process_video()
