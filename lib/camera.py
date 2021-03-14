import numpy as np
from picamera import PiCamera

class Camera():
    def __init__(self, resolution=(320, 240)):
        self.resolution = resolution
        self.image_size = (self.resolution[0], self.resolution[1], 3)
        self.camera = PiCamera()
        self.camera.resolution = self.resolution
        self.camera.framerate = 16

    def get_frame(self):
        data = np.empty(self.image_size, dtype=np.uint8)
        self.camera.capture(data, 'rgb')
        return data
