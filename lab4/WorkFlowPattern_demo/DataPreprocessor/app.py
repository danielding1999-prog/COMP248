import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from config import OUTPUT_DIR, INPUT_DIR, INPUT_FILE, INPUT_PATH, OUTPUT_PATH

def load_data(filepath):
    """Load the Iris dataset from a CSV file."""
    print(f"[INFO] Loading data from {filepath}")
    return pd.read_csv(filepath)

def preprocess_features(df):
    """Preprocess features: scale numeric columns and convert 'class' column to categorical."""
    print("[INFO] Preprocessing features: scaling numeric columns")
   
    feature_cols = [col for col in df.columns if col != 'class']
    scaler = StandardScaler()
    # Scale only feature columns, leave target unchanged
    df[feature_cols] = scaler.fit_transform(df[feature_cols])
    print(f"[INFO] Features scaled: {feature_cols}")
    return df

def split_data(df, test_size=0.2, random_state=42):
    """
    Split data into train and test sets, separating features and targets.
    Returns: X_train, X_test, y_train, y_test
    """
    print("[INFO] Splitting data into train and test sets")
    X = df.drop('class', axis=1)
    y = df['class']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    print(f"[INFO] Data split: {len(X_train)} train samples, {len(X_test)} test samples")
    return X_train, X_test, y_train, y_test

def save_splits(X_train, X_test, y_train, y_test, output_dir=os.path.join(
    OUTPUT_PATH, OUTPUT_DIR)):
    """
    Save train/test splits and targets as CSV files.
    Files: X_train.csv, X_test.csv, y_train.csv, y_test.csv
    """
    print(f"[INFO] Saving splits to directory: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)
    X_train.to_csv(os.path.join(output_dir, 'X_train.csv'), index=False)
    print("[INFO] Saved X_train.csv")
    X_test.to_csv(os.path.join(output_dir, 'X_test.csv'), index=False)
    print("[INFO] Saved X_test.csv")
    y_train.to_csv(os.path.join(output_dir, 'y_train.csv'), index=False)
    print("[INFO] Saved y_train.csv")
    y_test.to_csv(os.path.join(output_dir, 'y_test.csv'), index=False)
    print("[INFO] Saved y_test.csv")

def main():
    print("[INFO] Starting data preprocessing pipeline")
    df = load_data(os.path.join(INPUT_PATH, INPUT_DIR, INPUT_FILE))
    df = preprocess_features(df)
    X_train, X_test, y_train, y_test = split_data(df)
    save_splits(X_train, X_test, y_train, y_test)
    print("[INFO] Data preprocessing completed successfully")

if __name__ == "__main__":
    main()