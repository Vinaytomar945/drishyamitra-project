import pywhatkit
import os
import time

def send_photo_whatsapp(phone_number, photo_path):

    # convert to absolute path
    photo_path = os.path.abspath(photo_path)

    if not os.path.exists(photo_path):
        raise Exception(f"Image not found: {photo_path}")

    time.sleep(5)

    pywhatkit.sendwhats_image(
        receiver=phone_number,
        img_path=photo_path,
        caption="Photo from DrishyaMitra",
        wait_time=15
    )

    return "Photo sent on WhatsApp"