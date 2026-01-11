import openai

# MY_SECRET_KEY
openai.api_key = "TO_BE_ADDED_LATER"

def chat_ai():
    print("Welcome to Chat AI Advanced!")
    # تعريف شخصية التطبيق
    messages = [{"role": "system", "content": "أنت مساعد ذكي واسمك Chat AI Advanced"}]
    
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit", "خروج"]:
            break
            
        messages.append({"role": "user", "content": user_input})
        
        # طلب الرد من OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        reply = response.choices[0].message.content
        print(f"Chat AI: {reply}")
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    chat_ai()
