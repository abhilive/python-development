import matplotlib.pyplot as plt
#%matplotlib inline

#The above line is not working in Jupyter notebook so added below two lines to get this working
#Ref: https://stackoverflow.com/questions/35595766/matplotlib-line-magic-causes-syntaxerror-in-python-script

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

class Circle(object):
    
    def __init__(self,radius=3,color='blue'):
        
        self.radius=radius
        self.color=color 
    
    def add_radius(self,r):
        
        self.radius=self.radius+r
        return(self.radius)
    def drawCircle(self):
        
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

RedCircle=Circle(10,'red')
#dir(RedCircle) #dir command to get the list of object's method

#We can look data attributes of the object
#RedCircle.radius
#RedCircle.color

#Change the data attribute value
#RedCircle.radius=1

#Call the method
RedCircle.drawCircle()
