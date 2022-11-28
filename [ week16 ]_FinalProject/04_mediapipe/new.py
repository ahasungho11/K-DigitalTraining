import cv2
import time
import PoseModule as pm
cap = cv2.VideoCapture('test.mp4')
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)  # 포즈를 찾으면 img를 주고
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) !=0:
        # print(lmlist)
        print(lmlist[14])
        # cv2.circle(img, lmlist[14][1], lmlist[14][2], 15, (0, 0, 255), cv2.FILLED)
        # 14번에 해당하는 것에서 x,y (?) / y,z (?) 빼서 빨강으로 찍는

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (78, 58), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    cv2.imshow('Image', img)
    cv2.waitKey(1)