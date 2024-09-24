# AITechnicalScreen

### Purpose

This can be used by any potential employer for a technical screening of basic programming capability utizing AI.

### Objective

Imagine you are working at Power AI. The team has tasked you with building a simple customer support AI Agent to assist users with basic questions about Power AI. The agent will use predefined, hardcoded responses to answer common questions.

### Rules

Your agent should follow these guidelines:

- The agent must accept user input and answer the question like a conversational AI Agent.
- The agent should retrieve the most relevant answer from a hardcoded set of responses about Power AI.
- The agent should display the answer to the user in a user-friendly format.

### Implementation

- You may use any programming language and framework you're comfortable with. This is an opportunity to showcase your skills in a language you are proficient in.
- For the chat UI, you can use any CLI or web-based framework, such as Gradio, Streamlit, Chainlit, etc.
- The agent should use the predefined dataset to answer the questions about Power AI and fallback to generic LLM responses for everything else.

### **Predefined Data**

Here’s a sample dataset of questions and answers about Thoughtful AI’s Agents that your agent should be able to respond to:
```
{
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
            "question": "Tell me about Power AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Power AI's agents?",
            "answer": "Using Power AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}
```
### Submission Guidance

- **Time Management**: Allocate no more than 20 - 30 minutes to complete this challenge.
- **Submission Format**:
    - **Option 1**: Submit a public GitHub repository with clear README instructions.
    - **Option 2 (Preferred)**: Host your solution on an online IDE like [Repl.it](http://repl.it/) for immediate code review. (yeah, but you will pay $ to use it)

### Evaluation Criteria

1. **Functionality**: The code correctly implements the conversation logic.
2. **Code Quality**: The code is clean, readable, and well-structured, demonstrating knowledge of current tools and technologies.
3. **Robustness**: The code includes error handling for invalid or unexpected inputs. It gracefully handles scenarios where no search results are found.

### Run Code
 - if you don't have the required python libraries:
 - download ai_agent.py and requirements.txt.
 - run: ```pip install -r requirements.txt```
 - then run: ```streamlit run ai_agent.py```
 - enter your question in the text box, hit enter, and see the response.
 - Note: as per the requirement, the code compares the exact text of the user's question with the text from the predefined data.
