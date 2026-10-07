import pandas as pd
from config import IRIS_DATA_URL, IRIS_OUTPUT_DIR, IRIS_OUTPUT_PATH, IRIS_OUTPUT_FILENAME
import os

# Define the column names for the Iris dataset
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

def main():
    # Read the Iris dataset from the URL
    print(f"Fetching Iris dataset from {IRIS_DATA_URL}")
    # Read the dataset into a DataFrame
    iris_df = pd.read_csv(IRIS_DATA_URL, names=column_names)
    # Display the first few rows of the DataFrame
    print("Iris dataset loaded successfully:")
    print(iris_df.head())

    # Create output directory if it doesn't exist
    output_dir = os.path.join(IRIS_OUTPUT_PATH, IRIS_OUTPUT_DIR)
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")


    # Write DataFrame to CSV file
    fullpath = os.path.join(IRIS_OUTPUT_PATH, IRIS_OUTPUT_DIR, IRIS_OUTPUT_FILENAME)
    iris_df.to_csv(fullpath, index=False)
    print(f"iris CSV file written to {fullpath}")

if __name__ == "__main__":
    main()