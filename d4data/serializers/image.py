import io

from PIL import Image


class ImageSerializer:
    def serialize(self, obj: Image.Image, **kwargs):
        data = obj.tobytes(**kwargs)
        return data

    def deserialize(self, data, **kwargs):
        image = Image.open(io.BytesIO(data), **kwargs)
        return image
