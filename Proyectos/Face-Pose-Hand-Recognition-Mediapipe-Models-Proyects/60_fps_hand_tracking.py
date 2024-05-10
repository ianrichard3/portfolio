import cv2
import mediapipe as mp
import time


def lol():

    cap = cv2.VideoCapture(0)


    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False, # Detection some times, tracking some others
        max_num_hands = 2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5)

    mp_draw = mp.solutions.drawing_utils



    # FRAME RATE
    prev_time = 0
    cur_time = 0


    while True:

        success, img = cap.read()
        height, width, channels = img.shape


        # Send RGB image
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # send the rgb image to the hands processer
        results = hands.process(img_rgb)


        if results.multi_hand_landmarks:
            # Each hand loop
            for hand_landmarks in results.multi_hand_landmarks:

                for id, landmark in enumerate(hand_landmarks.landmark):
                    # Each landmark of each hand
                    break



                # Draw hand landmarks
                mp_draw.draw_landmarks(img, # Not the rgb
                                    hand_landmarks,
                                    mp_hands.HAND_CONNECTIONS) 




        cur_time = time.time()
        fps = 1/(cur_time-prev_time)
        prev_time = cur_time


        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 8, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

        break













class HandDetector():
    def __init__(self, static_image_mode=False, # Detection some times, tracking some others
                max_num_hands = 2,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.results = None


        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            self.static_image_mode,
            self.max_num_hands,
            self.min_detection_confidence,
            self.min_tracking_confidence)

        self.mp_draw = mp.solutions.drawing_utils

    
    def find_hands(self, img, draw=True):
        # Send RGB image
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # send the rgb image to the hands processer
        self.results = self.hands.process(img_rgb)


        if self.results.multi_hand_landmarks:
            # Each hand loop
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    # Draw hand landmarks
                    self.mp_draw.draw_landmarks(img, # Not the rgb
                                        hand_landmarks,
                                        self.mp_hands.HAND_CONNECTIONS)
        
        return img
    

    def find_hand_positions(self, img, hand_num, draw=True):
        height, width, channels = img.shape

        if self.results and self.results.multi_hand_landmarks:
            return self.results.multi_hand_landmarks[hand_num].landmark




                    
    

def main():
    cap = cv2.VideoCapture(0)

    # FRAME RATE
    prev_time = 0
    cur_time = 0

    hand_detector = HandDetector()

    while True:


        success, img = cap.read()
        # height, width, channels = img.shape

        img = hand_detector.find_hands(img)

        cur_time = time.time()
        fps = 1/(cur_time-prev_time)
        prev_time = cur_time


        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (255, 8, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)





if __name__ == "__main__":
    main()