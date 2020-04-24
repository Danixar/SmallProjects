# Evangellos Wiegers
# Note: be sure to have stegano installed

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
    lsbset.hide(image, message, gen).save(new_image)

def hide_in_spec(image, message, new_image):
    '''
    Hide text in specification
    :param image: image name to use
    :param message: message to hide
    :param new_image: new image name
    :return: N/A
    '''
    exi.hide(image, new_image, message)

def reveal_text(image):
    '''
    Reveal text
    :param image: image with hidden text
    :return: hidden text
    '''
    return lsbset.reveal(image, gen)

def reveal_in_spec(image):
    '''
    Reveal text in specification
    :param image: image with hidden text
    :return: hidden text
    '''
    return exi.reveal(image)

def get_generators():
    '''
    get all available generators
    :return: a string list of all available generators
    '''
    all_generators = inspect.getmembers(generators, inspect.isfunction)
    return ["{0} - {1}".format(str(g[0]), str(g[1])) for g in all_generators]
