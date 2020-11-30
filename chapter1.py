# Read Images - Videos - Webcam
import cv2

# Leitura de Imagem

# print('Package Imported')
#
# img = cv2.imread('./resources/lena.png')
#
# cv2.imshow("Output", img)
#
# cv2.waitKey(0)

# Leitura de Vídeo

# cap = cv2.VideoCapture('./resources/video.mp4')
#
# while True:
#     sucess, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(45) & 0xFF == ord('q'):
#         break

# Leitura de Câmera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    sucess, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(45) & 0xFF == ord('q'):
        break
