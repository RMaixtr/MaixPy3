import _maix_display
from PIL import Image
from _maix_display import Display
canvas = Image.new("RGB", (240, 240), "#ff1b50")
__fastview__ = Display(240, 240)
mk = canvas.tobytes()
__fastview__.draw(mk,240,240)

'''
import _maix_camera
from _maix_display import Display
cam = _maix_camera.R329Camera(240,240,0)
__fastview__ = Display(240, 240)


while True:
    img_bytes = cam.read()
    if img_bytes[0]:
        __fastview__.draw(img_bytes[1],240,240)



'''