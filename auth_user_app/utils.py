from django.core.mail import EmailMessage

from django.conf import settings

import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()


import base64
from PIL import Image
import io


def image_decoder(base64_image, image_extension, userid):
    # Decode base64 string to bytes
    image_data = base64.b64decode(base64_image)

    # Open image using PIL
    image = Image.open(io.BytesIO(image_data))

    # path
    MEDIA_ROOT = settings.MEDIA_ROOT
    prifile_picture_path = '/profilepic/'
    path = MEDIA_ROOT + prifile_picture_path
    imageName = str(userid)+'.'+str(image_extension)
    # Save image to file
    image.save(path+imageName, str(image_extension))

    return str(prifile_picture_path+imageName)



