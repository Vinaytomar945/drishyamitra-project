from flask import Blueprint, request, jsonify
from chat_service import chat_with_ai   # ✅ Import function from chat_service.py

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/ask", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        question = data.get("question", "")
        
        if not question:
            return jsonify({"error": "No question provided"}), 400

        # Call AI service
        answer = chat_with_ai(question)
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
