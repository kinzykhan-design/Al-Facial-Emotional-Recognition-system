from ai_logic import get_ai_response

# Turn 2: User abhi bhi gusse mein hai aur keh raha hai ke pehli technique kaam nahi ayi
sample_emotion = {"label": "Angry", "confidence": 95}
user_msg = "Nahi, yeh technique kam nahi kar rahi kuch aur batao yeh koshish b ki hai faida nahi howa writing ke elawa kuch batao."

# Hum 'history' mein pichli baat daal rahe hain taake AI ko context yaad rahay
history = [
    {"user": "Mujhe gussa aa raha hai!", "bot": "Main samajh sakti hoon... (Deep breathing suggestion)"}
]

print("Testing AI Psychologist (Angry Mode - Turn 2)...")
try:
    # Function call
    answer = get_ai_response(user_msg, sample_emotion, history)
    print("\nAI Psychologist ka Jawab:\n", answer)
except Exception as e:
    print("\nError aya hai:", e)