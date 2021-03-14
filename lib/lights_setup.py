from strip import Strip
from camera import Camera

LIGHTS = 50

camera = Camera()
strip = Strip(size=LIGHTS)

for i in range(LIGHTS):
   off_frame = camera.get_frame()
   strip[i] = (0, 255, 0)
   on_frame = camera.get_frame()
   strip[i] = (0, 0, 0)
