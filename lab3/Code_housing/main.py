from DataLoader import DataLoader
from Preprocessor import Preprocessor
from ModelTrainer import ModelTrainer
from ModelEvaluator import ModelEvaluator
from PredictionController import PredictionController
from UI import TerminalUI
from config import DATA_PATH

def main():
    # 1. Load data
    loader = DataLoader(DATA_PATH)
    df = loader.load_data()

    # 2. Preprocess data and split
    preprocessor = Preprocessor()
    X_train, X_test, y_train, y_test = preprocessor.split_and_transform(df)

    # 3. Train model
    trainer = ModelTrainer()
    trainer.train(X_train, y_train)
    model = trainer.get_model()

    # 4. Evaluate model
    evaluator = ModelEvaluator()
    mse, r2 = evaluator.evaluate(model, X_test, y_test)
    print(f"Model Evaluation:\n   MSE = {mse:.2f}\n   R² = {r2:.2f}\n")

    # 5. Initialize Architecture Components (Controller & Terminal UI)
    controller = PredictionController(model, preprocessor)
    ui = TerminalUI(controller)

    # 6. Launch the interactive terminal UI loop
    ui.start()

if __name__ == "__main__":
    main()