# Housing Price Predictor

This program uses linear regression to predict housing prices based on house sizes. It demonstrates basic machine learning concepts, data visualization, and user interaction in Python.

## Features

- Loads and analyzes housing data from CSV file
- Displays basic statistics about the dataset
- Creates visualizations of the data and regression model
- Trains a linear regression model using scikit-learn
- Provides interactive price predictions based on user input
- Handles errors gracefully

## Requirements

- Python 3.7 or higher
- Required packages:
  - pandas
  - matplotlib
  - scikit-learn

## Installation

1. Clone this repository
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure housing_data.csv is in the same directory as the script
2. Run the program:
   ```
   python housing_price_predictor.py
   ```
3. Follow the interactive prompts to get price predictions

## Data Format

The program expects a CSV file (housing_data.csv) with two columns:
- Size: House size in square feet
- Price: House price in dollars

## Error Handling

The program includes error handling for:
- Missing or invalid data files
- Invalid user input
- Negative or zero house sizes
