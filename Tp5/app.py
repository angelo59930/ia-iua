import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("BrainTumorDetection")

with mlflow.start_run():
    # Registra hiperparámetros, métricas y modelo
    mlflow.log_param("algorithm", "random_forest")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "random_forest_model")
