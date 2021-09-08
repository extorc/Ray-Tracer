import numpy as np
from numpy.lib.function_base import diff

class Light:
    def __init__(self,position,ambient, diffuse, specular):
        self.position = position
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular