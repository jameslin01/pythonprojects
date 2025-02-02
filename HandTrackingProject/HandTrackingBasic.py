import cv2
import mediapipe as mp
import time

# Choose Webcam

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
# default parameters fpr Hands(): static_image_mode = False
# max_num_hands = 2
# min_detection_confidence = 0.5
# min_tracking_confidence = 0.5
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Framerate

# Previous and current time

pTime = 0
cTime = 0


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                # Center of x and y
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                #if id == 4:
                # Draws a circle around every landmark id
                cv2.circle(img, (cx, cy), 25, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # To run Webcam

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)