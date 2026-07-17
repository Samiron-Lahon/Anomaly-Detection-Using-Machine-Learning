def predict(data):
    """
    Temporary prediction logic.
    This will later be replaced by the ML model.
    """

    cpu = data.get("cpu_usage", 0)
    memory = data.get("memory_usage", 0)
    failed = data.get("failed_logins", 0)

    if cpu > 90 or memory > 90 or failed > 20:
        return {
            "prediction": "Anomaly",
            "confidence": 95
        }

    return {
        "prediction": "Normal",
        "confidence": 98
    }