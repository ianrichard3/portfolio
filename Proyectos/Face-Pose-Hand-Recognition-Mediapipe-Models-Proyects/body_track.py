import mediapipe as mp
import cv2
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

TF_ENABLE_ONEDNN_OPTS=0

def calculate_angle(first, mid, end):
    first = np.array(first)
    mid = np.array(mid)
    end = np.array(end)


    rads = np.arctan2(end[1]-mid[1], end[0]-mid[0]) - np.arctan2(first[1]-mid[1], first[0]-mid[0])
    angle = np.abs(rads*180.0/np.pi)

    if angle > 180:
        angle = 360 - angle
    

    return angle




# Video Feed

cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    while cap.isOpened():
        ret, frame = cap.read()
        shape = frame.shape
        
        


        # Detect stuff
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = pose.process(image)

        # To re-render the image in bgr format
        image.flags.writeable = True
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)



        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            left_hand = landmarks[15]

            right_hand = landmarks[16]

            steering_wheel = left_hand.x-right_hand.x, left_hand.y-right_hand.y

            angle = np.arctan(steering_wheel[1]/steering_wheel[0])
            degs = np.rad2deg(angle)

            if degs > 20:
                print("Vamo pa izquierda")
            if degs < -20:
                print("Vamo pa derecha")

            shoulder = landmarks[11]
            elbow = landmarks[13]
            wrist = landmarks[15]

            angle = calculate_angle((shoulder.x, shoulder.y),
                                    (elbow.x, elbow.y),
                                    (wrist.x, wrist.y))
            

            # print(shape[0], shape[1])


            # visualize

            cv2.putText(image, str(round(angle,2)),
                        
                        (int(elbow.x*shape[0]), int(elbow.y*shape[1]))
                        ,
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            





        



        
        # if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks,
                                     mp_pose.POSE_CONNECTIONS,
                                     mp_drawing.DrawingSpec(color=(245, 117, 66),
                                                            thickness=2, circle_radius=2),
                                     mp_drawing.DrawingSpec(color=(245, 66, 230),
                                                            thickness=2, circle_radius=2))
                                            



        cv2.imshow("Mediapipe feed", image)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break


    cap.release()

    cv2.destroyAllWindows()


    # GET LANDMARKS

    # for lndmark in mp_pose.PoseLandmark:
    #     print(lndmark)






