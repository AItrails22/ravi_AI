import streamlit as st


# 🔐 SET YOUR OPENAI API KEY HERE
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 🔹 Your personal info used by the AI
personal_info = """
Full Name: Test AI king
Date of Birth: 1990-01-01
Current Location: Germany

Education:
- Degree: BE
- Institution: Open AI
- Year of Graduation: 2000
- Grades / GPA: 10
- Certifications: PMP

Work Experience:
- Job Title: AI Specialist
"""

# --- Web UI ---
st.set_page_config(page_title="My Personal AI", page_icon="🤖")
st.title("🤖 Ask Me About Myself!")

st.markdown("Type a question below to get answers based on my background.")

user_question = st.text_input("Ask a question about me:")

if user_question:
    with st.spinner("Thinking..."):
        prompt = f"You are an AI that knows everything about me. Based on the following personal information:\n\n{personal_info}\n\nAnswer this question:\n{user_question}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}]
        )

        answer = response.choices[0].message["content"]
        st.success(answer)
