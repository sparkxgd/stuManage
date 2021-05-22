import cv2
import sys
from PIL import Image


def CatchUsbVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)

    # 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    cap = cv2.VideoCapture(camera_idx)

    # 告诉OpenCV使用人脸识别分类器
    fasesFier = cv2.CascadeClassifier("haarcascades\\OpenCV_xml\\haarcascade_frontalface_alt.xml")
    eyesFier = cv2.CascadeClassifier("haarcascades\\OpenCV_xml\\haarcascade_eye.xml")
    mouthsFier = cv2.CascadeClassifier("haarcascades\\OpenCV_xml\\haarcascade_mcs_mouth.xml")
    nosesFier = cv2.CascadeClassifier("haarcascades\\OpenCV_xml\\haarcascade_mcs_nose.xml")
    # 识别出人脸后要画的边框的颜色，RGB格式
    faseColor = (100,149,237)
    eyeColor = (255,0,0)
    mouthColor = (255,110,180)
    noseColor = (0,255,127)

    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break
            # 将当前帧转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = fasesFier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), faseColor, 2)
                eyes = eyesFier.detectMultiScale(frame)
                # 文字提示
                cv2.putText(frame, 'face',
                            (x + 30, y + 30),  # 坐标
                            cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                            1,  # 字号
                            faseColor,  # 颜色
                            2)  # 字的线宽

                for eye in eyes:
                    ex, ey, ew, eh = eye
                    cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), eyeColor, 2)
                    # 文字提示
                    cv2.putText(frame, 'eye',
                                (ex + 10, ex + 10),  # 坐标
                                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                0.5,  # 字号
                                eyeColor,  # 颜色
                                1)  # 字的线宽
                mouths = mouthsFier.detectMultiScale(frame)
                for mouth in mouths:
                    ex, ey, ew, eh = mouth
                    cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), mouthColor, 2)
                    # 文字提示
                    cv2.putText(frame, 'mouth',
                                (ex + 10, ex + 10),  # 坐标
                                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                0.5,  # 字号
                                mouthColor,  # 颜色
                                2)  # 字的线宽
                noses = nosesFier.detectMultiScale(frame)
                for nose in noses:
                    ex, ey, ew, eh = nose
                    cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), noseColor, 2)
                    # 文字提示
                    cv2.putText(frame, 'nose',
                                (ex + 10, ex + 10),  # 坐标
                                cv2.FONT_HERSHEY_SIMPLEX,  # 字体
                                0.5,  # 字号
                                noseColor,  # 颜色
                                2)  # 字的线宽

                # roi_gray = grey[y:y + h, x:x + w]
                # eyes = eyesFier.detectMultiScale(roi_gray)
                # roi_color = frame[y:y + h, x:x + w]
                # for (ex, ey, ew, eh) in eyes:

                # mouths = mouthsFier.detectMultiScale(roi_gray)
                # for (ex, ey, ew, eh) in mouths:
                #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), mouthColor, 2)

        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

            # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s camera_id\r\n" % (sys.argv[0]))
    else:
        CatchUsbVideo("识别人脸区域", 0)
