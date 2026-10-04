from DataLoader import DataLoader
from Preprocessor import Preprocessor
from ModelTrainer import ModelTrainer
from ModelEvaluator import ModelEvaluator
from Predictor import  Predictor
import numpy as np
from config import DATA_PATH

def main():
    # Load data
    loader = DataLoader(DATA_PATH)
    df = loader.load_data()

    # Preprocess
    preprocessor = Preprocessor()
    X_train, X_test, y_train, y_test = preprocessor.split_and_transform(df)

    # Train
    trainer = ModelTrainer()
    trainer.train(X_train, y_train)
    model = trainer.get_model()

    # Evaluate
    evaluator = ModelEvaluator()
    mse, r2 = evaluator.evaluate(model, X_test, y_test)
    print(f"Evaluation:\n   MSE = {mse:.2f}\n  R² = {r2:.2f}")

    # Predict
    #create sample data for prediction
    sample_1 = {
        "longitude": -122.23,
        "latitude": 37.88,
        "housing_median_age": 41.0,
        "total_rooms": 880.0,
        "total_bedrooms": 129.0,
        "population": 322.0,
        "households": 126.0,
        "median_income": 8.3252,
        "ocean_proximity": "NEAR BAY"
    }

    sample_2 = {
        "longitude": -118.49,
        "latitude": 34.26,
        "housing_median_age": 30.0,
        "total_rooms": 2000.0,
        "total_bedrooms": 400.0,
        "population": 850.0,
        "households": 300.0,
        "median_income": 4.5125,
        "ocean_proximity": "<1H OCEAN"
    }

    sample_3 = {
        "longitude": -119.04,
        "latitude": 36.06,
        "housing_median_age": 18.0,
        "total_rooms": 1000.0,
        "total_bedrooms": 250.0,
        "population": 500.0,
        "households": 180.0,
        "median_income": 2.875,
        "ocean_proximity": "INLAND"
    }

    # Combine all 3 samples into a single nparray
    batch_array = np.array([
        [s[col] for col in df.columns if col != "median_house_value"]
        for s in [sample_1, sample_2, sample_3]
    ], dtype=object)
    predictor = Predictor(model, preprocessor)
    prediction = predictor.predict(batch_array)
    print(f"Sample Prediction: {prediction}")

# this is the main entry point of the program. It loads the data, preprocesses it, trains a model, evaluates it, and makes predictions on sample data. The sample data consists of three different housing scenarios, and the predictions are printed to the console.
if __name__ == "__main__":
    main()