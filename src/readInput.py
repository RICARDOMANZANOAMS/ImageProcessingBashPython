from abc import ABC, abstractmethod
import cv2
import pandas as pd
import numpy as np
from PIL import Image

class inputStrategy(ABC):
    @abstractmethod
    def readInput(self,path):
        pass

class jpgInputStrategy(inputStrategy):
    def readInput(self,path):
        img = Image.open(path)  
        img_gray = img.convert('L')         
        img_np = np.array(img_gray)        
        df = pd.DataFrame(img_np )
        return df

class csvInputStrategy(inputStrategy):
    def readInput(self,path):
        df=pd.read_csv(path)
        return df

class factoryInput():
    @abstractmethod
    def selectInput(input):
        if input=="csv":
            return csvInputStrategy()
        if input=="jpg":
            return jpgInputStrategy()
        else:
            return "No implemented input"
        



