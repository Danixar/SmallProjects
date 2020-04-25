# Evangellos Wiegers
# Note: be sure to have stegano installed

#zbar issues again

from stegano import lsb
from stegano.lsbset import generators
import inspect
from stegano import exifHeader as exi
from pathlib import Path

# gen = generators.eratosthenes() # the generator to use for hiding text not in specification

def hide_text(image, message, new_image):
    '''
    Hide text
    :param image: image name to use
    :param message: message to hide
    :param new_image: new image name
    :return: N/A
    '''
    assert ".png" in image.lower() or ".jpg" in image.lower() or ".jpeg" in image.lower(), "image is wrong data type!"
    my_file = Path(image)
    if my_file.is_file():
        lsb.hide(image, message).save(new_image)

def hide_in_spec(image, message, new_image):
    '''
    Hide text in specification
    :param image: image name to use
    :param message: message to hide
    :param new_image: new image name
    :return: N/A
    '''
    assert ".png" in image.lower() or ".jpg" in image.lower() or ".jpeg" in image.lower(), "image is wrong data type!"
    my_file = Path(image)
    if my_file.is_file():
        exi.hide(image, new_image, message)

def reveal_text(image):
    '''
    Reveal text
    :param image: image with hidden text
    :return: hidden text
    '''
    assert ".png" in image.lower() or ".jpg" in image.lower() or ".jpeg" in image.lower(), "image is wrong data type!"
    return lsb.reveal(image)

def reveal_in_spec(image):
    '''
    Reveal text in specification
    :param image: image with hidden text
    :return: hidden text
    '''
    assert ".png" in image.lower() or ".jpg" in image.lower() or ".jpeg" in image.lower(), "image is wrong data type!"
    return exi.reveal(image)

def get_generators():
    '''
    get all available generators
    :return: a string list of all available generators
    '''
    all_generators = inspect.getmembers(generators, inspect.isfunction)
    return ["{0}".format(str(g[0])) for g in all_generators]

if __name__ == '__main__':
    image1 = "superintendent1.png"
    image2 = "superintendent2.png"
    new_image1 = "hidden1.png"
    new_image2 = "hidden2.png"

    hide_text(image1, "Tamam Shud", new_image1)
    hide_in_spec(image2, "Epstein didnt kill himself", new_image2)

    print(get_generators())
    print(reveal_text(new_image1))
    print(reveal_in_spec(new_image2))
