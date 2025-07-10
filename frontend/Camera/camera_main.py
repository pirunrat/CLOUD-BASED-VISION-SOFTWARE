import cv2

class WebCam:
    def __init__(self):
        self.isCamOpen = False
        self.cap = None

    def _start_camera(self):
        self.cap = cv2.VideoCapture(0)

        if not self.cap or not self.cap.isOpened():
            print('[ERROR] Failed to open camera')
            self.cap = None
            self.isCamOpen = False
            return

        print('[INFO] Camera started successfully')
        self.isCamOpen = True

    def _stop_camera(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()
            print('[INFO] Camera Stopped')
        self.cap = None
        self.isCamOpen = False

    def _read_frame(self):
        if self.cap and self.cap.isOpened() and self.isCamOpen:
            ret, frame = self.cap.read()
            if ret:
                return frame
        return None
