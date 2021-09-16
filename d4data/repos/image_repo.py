

class ImageRepo:
    def __init__(self, image_access, serializer):
        self.image_access = image_access
        self.serializer = serializer

    def add(self, name, image):

        self.image_access.put
