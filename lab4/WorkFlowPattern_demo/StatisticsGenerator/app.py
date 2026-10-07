import config
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    # Assuming config.DATA_SOURCE is a CSV file path
    return pd.read_csv(os.path.join(config.IRIS_INPUT_PATH, config.IRIS_INPUT_DIR, config.IRIS_INPUT_FILENAME))

def print_statistics(df):
    print("Basic Statistics:")
    stats = df.describe(include='all')
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(config.OUTPUT_PATH, config.OUTPUT_DIR)
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    # Save statistics and missing values to a text file
    with open(os.path.join(config.OUTPUT_PATH, config.OUTPUT_DIR, "summary_statistics.txt"), "w") as f:
        f.write("Basic Statistics:\n")
        f.write(str(stats))
        f.write("\n\nMissing Values:\n")
        f.write(str(df.isnull().sum()))
    print(df.describe(include='all'))
    print("\nMissing Values:")
    print(df.isnull().sum())

def save_plot(fig, filename):
    # Create output directory if it doesn't exist
    output_dir = os.path.join(config.OUTPUT_PATH, config.OUTPUT_DIR)
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    output_path = os.path.join(config.OUTPUT_PATH, config.OUTPUT_DIR, filename)
    fig.savefig(output_path)
    print(f"Plot saved to {output_path}")

def generate_plots(df):
    # Histogram for each numeric column
    for col in df.select_dtypes(include='number').columns:
        fig = plt.figure()
        df[col].hist()
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        save_plot(fig, f"{col}_histogram.png")
        plt.close(fig)

    # Correlation heatmap
    fig = plt.figure(figsize=(8,6))
    # Convert target column to categorical codes and include in correlation
    sns.heatmap(df.loc[:, df.columns != 'class'].corr(), annot=True, fmt=".0%")  # draws heatmap with correlation matrix excluding 'class'
    plt.title('Correlation Heatmap')
    save_plot(fig, "correlation_heatmap.png")
    plt.close(fig)

    # Count plot for the target variable 'class'
    fig = plt.figure(figsize=(8,6))
    print(df["class"].value_counts())
    sns.countplot(x="class", data=df)
    plt.title('Class Distribution')
    save_plot(fig, "class_countplot.png")
    plt.close(fig)

def main():
    df = load_data()
    print_statistics(df)
    generate_plots(df)

if __name__ == "__main__":
    main()