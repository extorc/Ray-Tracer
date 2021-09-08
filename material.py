import numpy as np

class Material:
    def __init__(self,ambient, diffuse, specular,shininess, reflection):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection
        self.shininess = shininess