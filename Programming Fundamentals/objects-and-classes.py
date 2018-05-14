'''
Objects And Classes

An instance of an object is the realisation of a class.
'''
%matplotlib inline

import matplotlib.pyplot as plt
class Circle(object):

    def __init__(self, radius=3, color='blue'):

        self.radius=radius
        self.color=color

        def add_radius(self, r):
            self.radius=self.radius+r
            return(self.radius)

        def draw_circle(self):
            plt.gca().add_patch(plt.Circle((0,0), radius=self.radius, fc=self.color))
            plt.axis('scaled')
            plt.show()

RedCircle=Circle(10,'red')
dir(RedCircle) #dir command to get the list of object's method

#We can look data attributes of the object
RedCircle.radius
RedCircle.color

#Change the data attribute value
RedCircle.radius=1

#Call the method
RedCircle.drawCircle()
