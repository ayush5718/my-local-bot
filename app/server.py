from flask import Flask, request, jsonify
from flask_cors import CORS
from assistant import ask_ai

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.json
        question = data.get('question')
        
        if not question:
            return jsonify({'error': 'No question provided'}), 400

        answer = ask_ai(question)
        return jsonify({'answer': answer})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask API Server on http://localhost:8000")
    app.run(host='0.0.0.0', port=8000, debug=True)
