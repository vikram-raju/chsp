# Chain Sampling Analysis Project

Producer risk in manufacturing is the probability that a good product will be rejected by a consumer because a bad batch was observed in a sample that has been tested. Due to the cost of manual quality checks, often times we rely on checking the quality of products in samples, and consecutive samples and make a decision whether a lot of produced/manufactured items are acceptable to market/consumption.

Here we replicate the contributions in chain sampling plans from research in academia and make them available for consumption.

## Overview
In this project, we delve deep into the chain sampling method, a pivotal technique in quality control. Using synthetic data, we simulate two distinct real-world scenarios: 
1. Manufacturing of sneaker insoles
2. Production of LED bulbs

Our objective is to decode the criteria for batch acceptance or rejection based on defect or failure rates.

## Contents

- **Chain Sampling Analysis Notebook**: This Jupyter notebook contains a detailed analysis, from generating synthetic data to visualizing results. It's equipped with explanations at each step to ensure clarity of the approach and findings.
  
- **Sampling Code**: The core sampling functions and methodologies are derived from the code provided in the `sampling_min_sum.py` file.

## Key Highlights

- **Synthetic Data Generation**: We create realistic synthetic datasets for both scenarios, providing a foundation for our analysis.
  
- **Sampling Plans**: Utilizing the single sampling plan function, we determine the acceptance or rejection of batches.
  
- **Visualization**: A visual representation of defect rates and decisions, aiding in a clearer understanding of the results.

## Getting Started

1. Clone the repository to your local machine.
2. Navigate to the directory and open the `chain_sampling_analysis.ipynb` notebook.
3. Execute the notebook cells sequentially to understand the analysis flow.

## Requirements

- Python 3.8+
- Libraries: pandas, numpy, matplotlib

## Contributions

Feel free to fork this project and enhance it. Pull requests with improvements and optimizations are always welcome.
