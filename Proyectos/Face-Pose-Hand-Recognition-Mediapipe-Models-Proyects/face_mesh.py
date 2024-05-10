import cv2
import mediapipe as mp
import pyautogui

DETECTION_INTERVAL = 30
opened = False

from playsound import playsound

# import os



 





mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

drawing_spec = mp_drawing.DrawingSpec(thickness=1,
                                      circle_radius=2)

video = cv2.VideoCapture(0)


with mp_face_mesh.FaceMesh(min_detection_confidence=0.5,
                           min_tracking_confidence=0.5) as face_mesh:


    while True:
        ret, image = video.read()

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False

        results = face_mesh.process(image)

        # print(results)

        cv2.imshow("Face Mesh", image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for n, face in enumerate(results.multi_face_landmarks):
                # for numb, landmark in enumerate(face.landmark):
                #     x = landmark.x
                #     y = landmark.y

                #     shape = image.shape 
                #     relative_x = int(x * shape[1])
                #     relative_y = int(y * shape[0])

                #     # cv2.circle(image, (relative_x, relative_y), radius=1, color=(225, 0, 100), thickness=1)
                #     cv2.putText(image,f"{numb}", (relative_x,relative_y), 
                #                 cv2.FONT_HERSHEY_COMPLEX, 0.3, (255, 255, 255), 1, 2)
                    
                
                if n % DETECTION_INTERVAL == 0:
                    top_lip = face.landmark[13]
                    bot_lip = face.landmark[14]

                    # ESTO SE TENDRIA QUE HACER RELATIVO A LA DISTANCIA ENTRE EL PUNTO DE LA FRENTE Y EL DE LA PERA
                    # PARA QUE NO DEPENDA SOLO DE CUANTO ES LA DISTANCIA SI NO, SI ABRE LA BOCA
                    # frente 10 Pera 162
                    if abs(top_lip.y - bot_lip.y) > 0.05:
                        if not opened:
                            print("Abrio")
                            # pyautogui.hotkey('win', 'd')






                            opened = True
                    else:
                        opened = False

                # print(top_lip.y, bot_lip.y)


            cv2.imshow("FACE MESH",image)


        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    video.release()

    cv2.destroyAllWindows()