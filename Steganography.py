# Evangellos Wiegers
# Note: be sure to have stegano installed

#zbar issues again

from stegano import lsbset
from stegano.lsbset import generators
import inspect
from stegano import exifHeader as exi

gen = generators.eratosthenes() # the generator to use for hiding text not in specification

def hide_text(image, message, new_image):
    '''
    Hide text
    :param image: image name to use
    :param message: message to hide
    :param new_image: new image name
    :return: N/A
    '''
    assert ".png" in image.lower() or ".jpg" in image.lower() or ".jpeg" in image.lower(), "image is wrong data type!"
    if ".png" not in new_image and ".jpg" not in new_image:
        new_image = new_image + ".png"
    lsbset.hide(image, message, gen).save(new_image)

def hide_in_spec(image, message, new_image):
    '''
    Hide text in specification
    :param image: image name to use
    :param message: message to hide
    :param new_image: new image name
    :return: N/A
    '''
    assert ".png" in image.lower() or ".jpg" in image.lower() or ".jpeg" in image.lower(), "image is wrong data type!"
    if ".png" not in new_image and ".jpg" not in new_image:
        new_image = new_image + ".png"
    exi.hide(image, new_image, message)

def reveal_text(image):
    '''
    Reveal text
    :param image: image with hidden text
    :return: hidden text
    '''
    assert ".png" in image.lower() or ".jpg" in image.lower() or ".jpeg" in image.lower(), "image is wrong data type!"
    return lsbset.reveal(image, gen)

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
    return ["{0} - {1}".format(str(g[0]), str(g[1])) for g in all_generators]

if __name__ == '__main__':
    image1 = "superintendent1.png"
    image2 = "superintendent2.png"

    hide_text(image1, "Tamam Shud", "hidden1.png")
    hide_in_spec(image2, "Epstein didnt kill himself", "hidden2.png")

    print(get_generators())
    print(reveal_text(image1))
    print(reveal_in_spec(image2))
