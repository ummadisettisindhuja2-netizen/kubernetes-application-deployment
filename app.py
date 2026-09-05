from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Kubernetes Application Deployment</h1>
    <p>Hello from Sindhuja's containerized application!</p>
    <p>Deployed using Docker, Kubernetes and GitHub Actions.</p>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
