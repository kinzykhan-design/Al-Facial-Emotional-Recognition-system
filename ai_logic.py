import google.generativeai as genai

# 1. Apni API Key yahan lagayein
API_KEY = "AIzaSyAtz9yADwoxMJUlBlZJ8wDMfLnV28nCvkQ"
genai.configure(api_key=API_KEY)

# 2. MASTER PROMPT (As per PDF Instructions)
# Is mein Roman Urdu aur Bullet points ki instruction add kar di hai
MASTER_PROMPT = """
You are a compassionate AI wellness guide and an expert Psychologist. 
Help users navigate their emotions through supportive, friendly conversation.

RULES (IMPORTANT):
1. LANGUAGE: Always respond in Roman Urdu/Hindi (Urdu/Hindi written in English letters).
2. STRUCTURE:-Keep responses under 400 words. 
- STRICT RULE: Do NOT use asterisks (*) or dashes (-) for lists.
- Use ONLY emojis (like ✨, 🌱, 🧘) as bullet points at the start of each line.
- Ensure there is a space after the emoji and before the text.
3. ACKNOWLEDGE: Naturally mention the user's detected emotion with empathy.
4. TRUST: If user's words contradict detected emotion, trust their words.
5. ANTI-REPETITION: Never repeat advice already given. Check history and offer something new.
6. PROGRESSIVE DEPTH:
   - Turns 1-2: Validate feelings, offer 1 simple technique.
   - Turns 3-5: Explore triggers, offer different strategies.
   - Turns 6+: Action plans and long-term coping.
7. FOLLOW-UP: Always end your response with exactly ONE follow-up question.

SAFETY:
- If user mentions self-harm or crisis: Provide helpline numbers immediately.
- Never diagnose or prescribe medication.

STYLE:
- Friendly, caring, and professional (like a human peer, not a textbook).

CURRENT CONTEXT:
- Detected Emotion: {detected_emotion}
- Confidence: {confidence}%
- Conversation Turn: {turn_number}
"""

def get_ai_response(user_message, emotion_data, chat_history):
    # Dynamic values for the prompt [cite: 71, 72]
    turn_num = len(chat_history) + 1
    
    prompt = MASTER_PROMPT.format(
        detected_emotion=emotion_data["label"],
        confidence=emotion_data["confidence"],
        turn_number=turn_num
    )

    # Model Configuration (Gemini Flash 2.5) [cite: 75]
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=prompt
    )

    # SLIDING WINDOW: Last 20 messages for memory [cite: 79]
    history = []
    for turn in chat_history[-20:]:
        history.append({"role": "user", "parts": [turn["user"]]})
        history.append({"role": "model", "parts": [turn["bot"]]})

    # Start chat and get response [cite: 84, 85]
    chat = model.start_chat(history=history)
    response = chat.send_message(user_message)
    
    return response.text