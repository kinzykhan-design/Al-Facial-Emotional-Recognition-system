from flask import Flask, render_template, request, jsonify
from ai_logic import get_ai_response

app = Flask(__name__)

# Ye list aapki chat memory save rakhegi jab tak server chal raha hai
chat_history = []

@app.route('/')
def home():
    # Ye aapki website ka main page khole ga
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chat():
    # 1. Frontend se data lena
    user_data = request.json
    user_message = user_data.get("message")
    
    # Fake Emotion (Abhi hum testing ke liye bhej rahe hain, baad mein YOLOv8 se connect karenge)
    detected_emotion = {"label": "Neutral", "confidence": 100}

    # 2. AI Logic ko call karna
    try:
        bot_reply = get_ai_response(user_message, detected_emotion, chat_history)
        
        # 3. History update karna (PDF Rule: Memory management)
        chat_history.append({"user": user_message, "bot": bot_reply})
        
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)