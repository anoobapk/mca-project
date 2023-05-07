
import os

import cvzone
import cv2
from cvzone.PoseModule import PoseDetector
cap=cv2.VideoCapture(0)
detector = PoseDetector()
ip="image/shirt"
listShirt=os.listdir(ip)
#print(listShirt)
FixedRatio=260/170  #widthofshitr/widthofpointe11to12
shirtratio=243/182
imgNum=0
imgButton1=cv2.imread("image/Button.png",cv2.IMREAD_UNCHANGED)
imgButton2=cv2.flip(imgButton1,1)
CounterRigtht =0
CounterLeft =0
selectionspeed=5

while True:

    success, img = cap.read()
    img = detector.findPose(img)
    #img = cv2.flip(img,1)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False,draw=False)

    if bboxInfo:
        lm11=lmList[11][1:3]
        lm12 = lmList[12][1:3]

        imgShirt=cv2.imread(os.path.join(ip,listShirt[imgNum]),cv2.IMREAD_UNCHANGED)

        widthofshirt=int((lm11[0]-lm12[0])*FixedRatio)
        print(widthofshirt)
        imgShirt = cv2.resize(imgShirt, (widthofshirt,int(widthofshirt*shirtratio)))
        currentscale=(lm11[0]-lm12[0])/170
        offset=int(44*currentscale),int(48*currentscale)

        try:
            img=cvzone.overlayPNG(img,imgShirt,(lm12[0]-offset[0],lm12[1]-offset[1]))
        except:
            pass
        img=cvzone.overlayPNG(img,imgButton1,(76,300))
        img=cvzone.overlayPNG(img,imgButton2,(500,300))

        if lmList[16][1] <110:
            CounterRigtht +=1
            cv2.ellipse(img,(99,325),(30,30),0,0,
                        CounterRigtht*selectionspeed,(0,255,0),10)
            if CounterRigtht*selectionspeed >360:
                CounterRigtht =0
                if imgNum <len(listShirt) -1:
                    imgNum +=1
        elif lmList[15][1] >550:
            CounterLeft += 1
            cv2.ellipse(img, (521, 325), (30, 30), 0, 0,
                        CounterLeft * selectionspeed, (0, 255, 0), 10)
            if CounterLeft * selectionspeed > 360:
                CounterLeft = 0
                if imgNum > 0:
                    imgNum -= 1



        else:
            CounterRigtht=0
            CounterLeft=0




        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
    if not success:
        break




    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break
cap.release()
cv2.destroyAllWindows()

