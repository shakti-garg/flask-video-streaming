import os
import time
from base_camera import BaseCamera


class Camera(BaseCamera):
    """An emulated camera implementation that stream the images in a
     specified directory at a rate of one frame per second."""
    if os.environ.get("IMAGES_SOURCE_DIR"):
        imgsIter = os.listdir(os.environ.get("IMAGES_SOURCE_DIR"))
    elif os.environ.get("IMAGES_SOURCE_PATH"):
        imgsIter = [f.strip() for f in os.environ.get("IMAGES_SOURCE_PATH").split(',')]
    else:
        raise RuntimeError("Needed environment variable: IMAGES_SOURCE_PATH")

    imgs = [open(f, 'rb').read() for f in imgsIter]

    @staticmethod
    def frames():
        for img in Camera.imgs:
            time.sleep(1)
            yield img
