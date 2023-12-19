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

To run BayesAge, add the directory containing BayesAge.py to your path, then import BayesAge into a Python script or Jupyter notebook as shown in the example notebook. 

In order to use the functions provided in <b>BayesAge</b>, the following packages need to be installed:

`numpy` (tested with version 1.24.3) <br>
`pandas` (tested with version 2.1.1) <br>
`scipy` (tested with version 1.11.2) <br>
`tqdm` (tested with version 4.66.1) <br>
`statsmodels` (tested with version 0.14.0) <br>

This tool was developed in Python 3.10.12 in a Jupyter Notebook environment, running on Ubuntu 22.04.3 LTS.

To visualize epigenetic age predictions, installation of `seaborn`, `matplotlib` and `statannot` is also recommended.

Predicted epigenetic age output dataframes are conveniently written to .tsv files, and can therefore also be analyzed in any other environment (R, Excel, etc...).

## Speed, Memory Use and Parallelization <br>
The three main functions(*construct_reference*, *process_cgmap_file* and *bdAge*) are fully functional running on a single core (the default is n_cores = 1). Since this package is a direct extension of scAge, they should experience linear speedup with multiprocessing. Increasing the number of cores (n_cores) will improve the speed and efficiency of the pipeline. While developing this package, I used a System76 and a MacBook Pro laptop with max CPUs of 12 cores but most of my testing was done with n_cores < 10.

process_cgmap_file and bdAge could eat up a lot of RAM depending on how many samples are being processed simulatenously, so one can monitor the memory allocation when running the algorithm. 

## Example Notebooks  <br>
The notebook *How_to_Run_BayesAge.ipynb* contains instructions on how to run the BayesAge pipeline.<br>
Please refer to this main notebook on how to train the model (*construct_reference*), load the methylomes (*process_cgmap_file*), and predict epigenetic age (*bdAge*).<br>

Below is a brief overview of the parameters that each functions require to run properly. 

### Training using construct_reference <br>

In order to train the reference matrix for the BayesAge pipeline, you can run the function:

```
construct_reference(training_matrix="/Users/lajoyce/Documents/genomics/epiage/BayesAge/examples/reduced_DNAm_matrix.csv",
reference_name="reference_model",
output_path="/Users/lajoyce/Documents/genomics/epiage/BayesAge/examples/output_files/",
zero_met_replacement=0.001,
one_met_replacement=0.999,
min_age=0,
max_age=100,
age_step=1,
tau=0.7)
```
where: 
* `training_matrix` --> full path to the reference matrix you want to create the reference matrix. <br>
* `reference_name` --> name of the processed reference matrix dataset. <br>
* `output_path` --> the full path where to output the reference matrix files. <br>
* `zero_met_replacement` --> value to replace the extreme methylation probabilities with. <br>
* `one_met_replacement` --> value to replace to extreme methylation. <br>
* `min_age` --> minimum age of the reference model. <br>
* `max_age` --> maximum age of the reference model. <br>
* `age_step` --> age step between minimum age and maximum age. <br>
* `tau` --> Tau value of the lowess fit. <br>

### Loading methylomes using process_cgmap_file <br>
CGmap or Bismark files need to be processed into a format compatible wih BayesAge prediction function. The code used to convert CGmap to Bismark files in the BayesAge folder. This code can also modified to convert Bismark files to CGmap files. 

The function *process_cgmap_file* converts the CGmap files to the processed *.tsv* files the prediction function expects. 
```
process_cgmap_file(cgmap_directory="/Users/lajoyce/Documents/genomics/epiage/BayesAge/examples/CG_map_try2/",
output_path = "/Users/lajoyce/Documents/genomics/epiage/BayesAge/examples/processed_samples/",
n_cores = 1,
split = ".",
chunksize = 1)
```
* `cgmap_directory` --> The path to the directory containing .CGmap files.
*  `output_path` --> The path to the ouput directory in which to write .tsv files. 
*  `n_cores` --> The number of CPU cores to use for parallel processing
*  `split` --> The symbol/letter/number to split by when generating samples/subjects from files.
*  `chunksize` --> The number of elements to feed to each worker during parallel processing.

This returns a *.tsv* file(s) with the following columns:
`ChrPos`,`Mc`, `Nc`. `Mc` is the Methylated count and `Nc` is the total count (methylated + thymine count).  

ChrPos | Mc | Nc |
:---: | :---: | :---:
CpG1 | 5 | 5
CpG2 | 10 | 15
... | ... | ...

### Predicting age using bdAge <br>
Once the files are processed, we can predict the age of samples using the `bdAge` function:

```
bdAge(sample_dir_or_dict="/Users/lajoyce/Documents/genomics/epiage/BayesAge/examples/processed_samples/",
    sample_set_name="test",
    reference_data="/Users/lajoyce/Documents/genomics/epiage/BayesAge/examples/output_files/reference_model",
    output_path="/Users/lajoyce/Documents/genomics/epiage/BayesAge/examples/predictions/",
    selection_mode="numCpGs",
    CpG_parameter=8,
    min_age=0,
    max_age=100,
    age_step=1,
    n_cores = 1,
    chunksize = 5)
```
where:
* `sample_dir_or_dict` --> directory containing processed cgmap files.
* `sample_set_name` --> the desired name of the sample files with predicted ages.
* `reference_data` --> The full file path to the desired reference data.
* `output_path` --> path of directory to store the files with predicted ages.
* `selection_mode` --> One of the selection modes to select the top cpg sites (numCpGs, percentile, cutoff).
* `CpG_parameter` --> Parameter to specifically choose the number of CpG sites.
* `min_age` --> The minimum age for which to build a probability profile
* `max_age` --> The maximum age for which to build a probability profile
* `age_step` --> The step value for computing probability profiles
* `n_cores` --> The number of cores to use for parallel processing
* `chunk_size` --> The number of elements to feed to each worker during parallel processing.

## Data <br>


## Troubleshooting <br>

If you encounter any issues when trying to run BayesAge, or if you have suggestions, please feel free to contact me by email: lajoycemboningatucla.edu.


