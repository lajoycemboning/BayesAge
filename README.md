# BayesAge

## BayesAge v1.0 (12/10/2023)

BayesAge is a framework for epigenetic age predictions. This is an extension to scAge (Trapp et al.).
BayesAge utilizes maximum likelihood estimation (MLE) to infer ages, models count data using binomial distributions,
and uses LOWESS smoothing to capture the non-linear dynamics between methylation and age.
For more information on the algorithm, please consult Mboning et al., "BayesAge: A Maximum likelihood estimation algorithm to predict epigenetic age".
If you use this software, please cite our work along with Trapp's work. 

The BayesAge pipeline consists of three key steps: <br>
    1) Computing the nonlinear models for each CpG within a DNAm matrix using LOWESS fit.  
    2) Loading in and processing sample methylation cgmap files.  
    3) Predicting age of samples given number of cytosines and coverage from cgmap files.

and can be executed with the following functions: <br>
    1) construct_reference <br>
    2) process_cgmap_file <br>
    3) bdAge <br>  

## Installation & Usage <br>

To install BayesAge and associated data, please clone the GitHub repository:

git clone https://github.com/lajoycemboning/BayesAge.git

This will download all required data to utilize and test the software. 

For ease of use, all functions needed to run the full BayesAge pipeline are directly included within the BayesAge.py script. <br>

## Speed, Memory Use and Parallelization <br>

## Example Notebooks  <br>
The notebook *How_to_Run_BayesAge.ipynb* contains instructions on how to run the BayesAge pipeline.<br>
Please refer to this main notebook on how to train the model (*construct_reference*), load the methylomes (*process_cgmap_file*), and predict epigenetic age (*bdAge*).<br>

Below is an overview of the parameters that each functions require to run properly. 

### Training using construct_reference <br>

### Loading methylomes using process_cgmap_file <br>

### Predicting age using bdAge <br>

## Data <br>


## Troubleshooting <br>

If you encounter any issues when trying to run BayesAge, or if you have suggestions, please feel free to contact me by email: lajoycemboningatucla.edu.


