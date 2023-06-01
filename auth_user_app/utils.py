from django.core.mail import EmailMessage

from django.conf import settings

import threading
import datetime


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
import os


def image_decoder(base64_image, image_extension, userid,path):


    directory = path
    if not os.path.exists(directory):
        os.makedirs(directory)
        print('directory created')
    else:
        print('directory already exists')

    print('path::::', path)
    
    # Decode base64 string to bytes
    image_data = base64.b64decode(base64_image)

    # Open image using PIL
    image = Image.open(io.BytesIO(image_data))

#    # path
    # MEDIA_ROOT = settings.MEDIA_ROOT
    # prifile_picture_path = '/profilepic/'
    # path = MEDIA_ROOT + prifile_picture_path + str(userid)
#    # take current date and time as image name
    dtt = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    imageName = str(userid)+'_'+str(dtt)+'.'+str(image_extension)
    # Save image to file
    image.save(path+imageName, str(image_extension))
    print('path::::', path)
    # return str(path)




def get_all_images_name(path):

    MEDIA_ROOT = settings.MEDIA_ROOT
    file_names = []
    for root, dirs, files in os.walk(MEDIA_ROOT + path):
        for file in files:
            file_names.append(path+file)
            print('file_names::::', file_names)
            print('file::::', file)
            print('path::::', path)
    return file_names




def remove_list_of_images(path ,list_of_images):

    # print('file removed 1::::', MEDIA_ROOT + file)
    # print('path 1::::', MEDIA_ROOT + path)
    # MEDIA_ROOT = settings.MEDIA_ROOT
    # for root, dirs, files in os.walk(MEDIA_ROOT + path):
    #     for file in files:
    #         if file in list_of_images:
                
    #             os.remove(MEDIA_ROOT + file)
    #             print('file removed::::', MEDIA_ROOT + file)
    #             print('path::::', MEDIA_ROOT + path)


    MEDIA_ROOT = settings.MEDIA_ROOT
    for file_path in list_of_images:
        file_path = MEDIA_ROOT + file_path
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        except OSError as e:
            print(f"Error deleting file: {file_path} - {e}")

    return True




