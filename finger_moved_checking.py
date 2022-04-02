import cv2
from cvzone.HandTrackingModule import HandDetector
# https://google.github.io/mediapipe/solutions/hands.html 손바닥 , 가락 순서 사이즈

#mediapipe hand
# 카메라를 VideoCapture 객체로 가져온다.
# https://github.com/cvzone
cap = cv2.VideoCapture(0)
# Minimum Detection Confidence Threshold
detector = HandDetector(detectionCon=0.8)
while True:
    # 계속해서 이미지를 불러와서 영상을 보여준다.
    success, img = cap.read()
    # Find the hand and its landmarks
    # 이미지 좌우 반전
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img) # with draw
    # hands = detector.findHands(img, draw=False) # without draw
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"] # List of 21 Landmark points
        bbox1 = hand1["bbox"] # Bounding box info x,y,w,h
        centerPoint1 = hand1['center'] # center of the hand cx,cy
        handType1 = hand1["type"] # Handtype Left or Right
        fingers1 = detector.fingersUp(hand1)
        l, _, _ = detector.findDistance((lmList1[6][0], lmList1[6][1]), (lmList1[8][0], lmList1[8][1]), img)

        if (lmList1[5][1] < lmList1[0][1]) and (lmList1[6][1] < lmList1[8][1]) and (lmList1[6][1] <= lmList1[5][1]):
            print("bend")
        elif (lmList1[5][1] > lmList1[0][1]) and (lmList1[6][1] > lmList1[8][1]) and (lmList1[6][1] <= lmList1[5][1]):
            print("bend2")
        else:
            print("fail")
    #     l1, info, _ = detector.findDistance((lmList1[8][0], lmList1[8][1]), (lmList1[6][0], lmList1[6][1]), img)
    #     l, info2, _ = detector.findDistance((lmList1[12][0], lmList1[12][1]), (lmList1[10][0], lmList1[10][1]), img)
    #     l2, info3, _ = detector.findDistance((lmList1[16][0], lmList1[16][1]), (lmList1[14][0], lmList1[14][1]), img)
    #     l3, info4, _ = detector.findDistance((lmList1[20][0], lmList1[20][1]), (lmList1[18][0], lmList1[18][1]), img)
    #     #if (info2[1] < info2[3]) and (info[1] > info[3]) and (info3[1] > info[3]) and (info4[1] > info4[3]):
    #     if (l > 50) and (l1 < 50) and (l2 < 50) and (l3 < 50):
    #         print("욕 감지 됨")
    #     else:
    #         print("욕 감지 되지 않음")
    #     #l, info, _ = detector.findDistance((lmList1[11][0], lmList1[11][1]), (lmList1[12][0], lmList1[12][1]), img)
    # #그냥 상자 그리기
    # # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
#거리를 계산하는 것은 이슈가 있을것 임
#좌표를 계산해야하는데 모든 방향으로 할때 잘 되지 않기 때문에 손의 중심(0)을 가지고 다듬기로 함
#지금 오류가 있음
