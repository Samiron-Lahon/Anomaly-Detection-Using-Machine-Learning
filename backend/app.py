from flask import Flask
from flask_cors import CORS
from routes.health import health_bp
from routes.predict import predict_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(health_bp)
app.register_blueprint(predict_bp)

@app.route("/")
def home():
    return {
        "project": "IOCL Anomaly Detection Backend",
        "status": "Running"
    }

if __name__ == "__main__":
    app.run(debug=True)