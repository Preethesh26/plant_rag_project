from flask import Flask, request, jsonify
from rag_engine import get_plant_response
from chroma_loader import load_data_to_chroma

app = Flask(__name__)

# Load plant data to ChromaDB (only once)
load_data_to_chroma()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        response = get_plant_response(query)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
