from PIL.Image import Image
from stegano import lsb
import os


def encode_img(src: str, dest: str, txt: str):
    """Encoding 'txt' to 'src' image and save it to 'dest'. Returns False (success) or True (for errors)"""
    if not all(isinstance(arg, str) for arg in [src, dest, txt]) or not os.path.exists(src):
        return True
    secret_img: Image = lsb.hide(src, txt, encoding='UTF-8')
    secret_img.save(dest)
    return False


def decode_img(src: str) -> str:
    """Decoding image from 'src' path. Returns str or None (if image does not exist or doest not have encrypted text)"""
    if not os.path.exists(src):
        return None
    try:
        decoded_txt = lsb.reveal(src, encoding='UTF-8')
    except IndexError:
        return None
    return decoded_txt

