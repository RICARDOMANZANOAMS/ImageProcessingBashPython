import sys
import os
import unittest
import numpy as np
import pandas as pd
import pandas.testing as pdt
from PIL import Image
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import readInput


class TestCSVInputStrategy(unittest.TestCase):    
    def setUp(self):
        self.outputPath='test.csv'
        self.pandasDF=pd.DataFrame(np.random.rand(3,4))
        self.csvFile=self.pandasDF.to_csv(self.outputPath,index=False)        
        self.csvInputStrategyObj=readInput.factoryInput.selectInput("csv")
    def testCSVInputStrategy(self):
        df=self.csvInputStrategyObj.readInput(self.outputPath)
        df.columns = df.columns.astype("int64")  # Convert column names to integers
        pdt.assert_frame_equal(df, self.pandasDF)  
        
class TestJPGInputStrategy(unittest.TestCase):
    def setUp(self):
        self.outputPath="output.jpg"
        self.imageNP=np.random.randint(0,255,size=(3,8), dtype=np.uint8)                 
        self.imagePD=pd.DataFrame(self.imageNP)
        self.image = Image.fromarray(self.imageNP).save(self.outputPath)
        
        self.jpgInputStrategyObj=readInput.factoryInput.selectInput("jpg")
    def testJPGInputStragegy(self):
        df=self.jpgInputStrategyObj.readInput(self.outputPath)
        np.testing.assert_allclose(df.values, self.imageNP, atol=30)  


if __name__ == '__main__':
    unittest.main()