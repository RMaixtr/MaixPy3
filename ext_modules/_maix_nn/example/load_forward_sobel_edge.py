from maix import nn
from PIL import Image, ImageDraw
from maix import camera, display
import numpy as np
import time

test_jpg = "/root/test_input/input.jpg"
model = {
    "param": "/root/models/sobel_int8.param",
    "bin": "/root/models/sobel_int8.bin"
}

input_size = (224, 224, 3)
output_size = (222, 222, 3)
camera.config(size=input_size[:2])

options = {
    "model_type":  "awnn",
    "inputs": {
        "input0": input_size
    },
    "outputs": {
        "output0": output_size
    },
    "first_layer_conv_no_pad": True,
    "mean": [127.5, 127.5, 127.5],
    "norm": [0.0078125, 0.0078125, 0.0078125],
}
print("-- load model:", model)
m = nn.load(model, opt=options)
print("-- load ok")

print("-- read image")
img = Image.open(test_jpg).resize(input_size[:2])
print("-- read image ok")
print("-- forward model with image as input")
out = m.forward(img, quantize=True)
# print("-- read image ok")
# out = out.reshape(222, 222, 3)
print("-- out:", out.shape, out.dtype)
out = ((out + 1) * 255).astype(np.uint8).reshape(output_size)
img2 = Image.fromarray(out, mode="RGB")
display.show(img2)


while 1:
    img = camera.capture()
    if not img:
        time.sleep(0.02)
        continue
    out = m.forward(img, quantize=True)
    out = out.astype(np.float32).reshape(output_size)
    scale = out.max() - out.min()
    half = scale / 2.
    out = ((out + half) / scale * 255).astype(np.uint8)
    img2 = Image.fromarray(out, mode="RGB")
    display.show(img2)