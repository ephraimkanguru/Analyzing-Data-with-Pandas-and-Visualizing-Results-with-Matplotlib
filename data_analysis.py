import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    data = pd.read_csv('dataset.csv')
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Dataset not found. Please ensure 'dataset.csv' is in the same folder.")
    exit()

# Display the first few rows
print("First few rows of the dataset:")
print(data.head())

# Check data structure
print("\nDataset Info:")
print(data.info())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Clean the dataset (example: drop rows with missing values)
data = data.dropna()
print("\nAfter cleaning, missing values:")
print(data.isnull().sum())

# Task 2: Basic Data Analysis
# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# Group by 'Species' column and compute mean
if 'Species' in data.columns:  # Case-sensitive check
    print("\nMean values by Species:")
    print(data.groupby('Species').mean())
else:
    print("\nNo 'Species' column found for grouping.")

# Task 3: Data Visualization

# Bar chart: Average Petal Length by Species
if 'Species' in data.columns:  # Check if the column 'Species' exists
    data.groupby('Species')['PetalLengthCm'].mean().plot(kind='bar', title="Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Average Petal Length")
    plt.show()  # Show the bar chart

# Histogram: Distribution of Petal Length
if 'PetalLengthCm' in data.columns:
    data['PetalLengthCm'].plot(kind='hist', bins=20, title="Distribution of Petal Length")
    plt.xlabel("Petal Length")
    plt.show()  # Show the histogram

# Scatter plot: Sepal Length vs. Petal Length
if 'SepalLengthCm' in data.columns and 'PetalLengthCm' in data.columns:
    plt.scatter(data['SepalLengthCm'], data['PetalLengthCm'], alpha=0.5)
    plt.title("Sepal Length vs. Petal Length")
    plt.xlabel("Sepal Length")
    plt.ylabel("Petal Length")
    plt.show()  # Show the scatter plot
