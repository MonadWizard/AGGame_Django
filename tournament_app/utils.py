from django.conf import settings

import base64
from PIL import Image
import io
import os


def image_decoder(base64_image, image_extension, tournament_id, tournament_logo_path):
    
    # Decode base64 string to bytes
    image_data = base64.b64decode(base64_image)

    # Open image using PIL
    image = Image.open(io.BytesIO(image_data))

    # path
    MEDIA_ROOT = settings.MEDIA_ROOT
    logo_path = MEDIA_ROOT + tournament_logo_path

    if not os.path.exists(logo_path):
        os.makedirs(logo_path)

    imageName = str(tournament_id)+'.'+str(image_extension)
    # Save image to file
    image.save(logo_path+imageName, str(image_extension))

    return str(tournament_logo_path+imageName)

