__author__ = 'Davide Monfrecola'

from managers.manager import Manager

class OpenStackManager (Manager):
    
    def __init__(self):
        print("Instance of class", OpenStackManager.__name__)