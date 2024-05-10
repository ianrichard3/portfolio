import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import move_mouse
import time
import keyboard

SENSITIVITY = (1,1)
OFFSET = .3
MOUSE_REFRESH_TIME = 1
WIDTH = 1920
HEIGHT = 1080



def main():
    prev_time = 0
    cur_time = 0
    video = cv2.VideoCapture(0)



    mp_draw = mp.solutions.drawing_utils
    # mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands


    with mp_hands.Hands(

        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

        i = -1
        while True:
            i += 1
            ret, image = video.read()


            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


            results = hands.process(image_rgb)



            
            
            # image.flags.writeable = True


            if results.multi_hand_landmarks:
                # for hand_landmarks in results.multi_hand_landmarks:
                    # for numb, landmark in enumerate(hand_landmarks.landmark):
                    #     x = landmark.x
                    #     y = landmark.y

                    #     shape = image.shape 
                    #     relative_x = int(x * shape[1])
                    #     relative_y = int(y * shape[0])

                    #     # cv2.circle(image, (relative_x, relative_y), radius=1, color=(225, 0, 100), thickness=1)
                    #     cv2.putText(image,f"{numb}", (relative_x,relative_y), 
                    #                 cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, 2)
                

                hand_landmarks = results.multi_hand_landmarks[0]
                # mp_draw.draw_landmarks(image, # Not the rgb
                #                     hand_landmarks,
                #                     mp_hands.HAND_CONNECTIONS)
                
                if i % MOUSE_REFRESH_TIME == 0:

                    pointer = hand_landmarks.landmark[9]

                    x = (pointer.x * 1.5 - OFFSET) * WIDTH
                    # x -= x*OFFSET//2
                    y = (pointer.y * 1.5 - OFFSET) * HEIGHT
                    # y -= y*OFFSET//2
                
                    move_mouse.move(x, y)
                    i = 0

                    index = hand_landmarks.landmark[8]
                    thumb = hand_landmarks.landmark[4]

                        


            # cur_time = time.time()
            # fps = 1/(cur_time-prev_time)
            # prev_time = cur_time


            # cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,
            #             3, (255, 8, 255), 3)





            # cv2.imshow("Hand tracking", image)


            # k = cv2.waitKey(1)
            # if k == ord("q"):
            #     break
                    
            if keyboard.is_pressed("esc"): break

        video.release()

        cv2.destroyAllWindows()



# def send_coordinates():


if __name__ == "__main__":
    main()
    