from flask import Flask, jsonify, request
app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({"message": "Hello from the lab app!"})

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/api/items")
def items():
    limit = int(request.args.get("limit", 3))
    data = [{"id": i, "name": f"item-{i}"} for i in range(limit)]
    return jsonify({"items": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
