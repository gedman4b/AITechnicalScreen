import streamlit as st
import json
from openai import OpenAI

# Sample dataset (predefined questions and answers)
data = {
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}


# Function to get fallback response from GPT
def get_fallback_response(user_question):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. If you don't know the answer then respond by saying: I dont know"},
            {"role": "user", "content": user_question}
            ]
        )
    return response.choices[0].message.content.strip()

# Modify the main logic to use GPT fallback
def get_predefined_response(user_question):
    for item in data['questions']:
        if user_question.lower() == item['question'].lower():
            return item['answer']
    # If no predefined answer, call GPT for a fallback response
    return get_fallback_response(user_question)

# Streamlit app UI
st.title("Customer Support AI Agent")

# User input
user_input = st.text_input("Ask a question about Thoughtful AI:")

# Display output when user enters a question
if user_input:
    # Get the predefined answer
    response = get_predefined_response(user_input)
    st.write(f"Answer: {response}")

