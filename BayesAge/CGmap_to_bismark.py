# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 03:35:46 2022

@author: ornel
"""

import os
import pandas as pd
import sys

sys.path.append('/Users/lajoyce/Documents/genomics')


#Get current working directory
os.getcwd()


#Directory of CGmap files to be processed and converted to Bismark.cov files.
input_path = r"C:\Users\ornel\Documents\Machine Learning with Python" 

#Directory of where to save processed and converted CGmap files.
output_path = r"C:\Users\ornel\Documents\Machine Learning with Python\destination" 


files = [element for element in os.listdir(input_path) if element.endswith('.tsv')]
print("The following files are going to be processed")

print(files)


for file in files:
   df_n = pd.read_csv(file, sep = "\t", names = ["chr", "nuc", "pos", "cont", "dinuc", "meth", "mc", "nc"])
   df_n["unmet"] = df_n["nc"] - df_n["meth"]
   df = df_n.loc[:,['chr', 'pos', 'pos', 'meth', 'mc', 'unmet']]
   df.to_csv(r"C:\Users\ornel\Documents\Machine Learning with Python\destination\{}.tsv".format(file),
             sep = "\t", header = False, index = False)
   #print(df)
   
print("Processing done!")