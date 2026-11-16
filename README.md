# Lottery Number Prediction Using Markov Chains

A data analytics and probabilistic modeling project that applies Markov Chain theory to analyze historical two-digit lottery results and predict potential future outcomes.

## Overview

This project explores the use of Markov Chains to model sequential patterns in historical two-digit lottery data. Multiple prediction models were developed and evaluated using transition probabilities, state transitions, and different dataset configurations. 

## Objectives

- Analyze historical lottery results using probabilistic methods.
- Build transition matrices based on past outcomes.
- Predict possible future number combinations.
- Compare multiple Markov Chain models and evaluate prediction accuracy. 【1-41b42d】

## Methodology

The project implements several Markov Chain-based approaches:

- Initial Probability Calculation
- Transition Matrix Generation
- State Transition Modeling
- AM/PM Data Separation
- Digit-Level Prediction Models
- Accuracy Evaluation
- Model Comparison Framework 

## Models Implemented

### Model 1
- Uses complete historical dataset
- Builds 100×100 transition matrices
- Predicts top candidate numbers

### Model 2
- Splits results into first and second digits
- Generates separate transition matrices
- Combines digit relationships

### Model 3
- Uses filtered dataset after market anomaly period
- Separate AM and PM prediction models

### Model 4
- Combines digit-level prediction with filtered datasets

Multiple model variations were implemented and compared to identify the best-performing approach. 

## Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook
- Google Colab
- Markov Chain Modeling 

## Results

The experiments showed that Model 3.2 achieved the highest performance among all tested configurations, with separate prediction models for AM and PM datasets. 


