import streamlit as st
import openai

# إعداد عنوان الصفحة
st.title("Chat AI Advanced 🚀")

# حطي مفتاح الـ API بتاعك هنا بين العلامتين
openai.api_key = "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"

# تهيئة مخزن الرسائل
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال سؤال المستخدم
if prompt := st.chat_input("اسألني أي شيء..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # طلب الرد من OpenAI
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        answer = response.choices[0].message.content
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
