from main import ask_agent  
import gradio as gr

def chat_fn(message, history):
    try:
        answer = ask_agent(message)
        return answer
    except Exception as e:
        return f"❌ Error: {e}"

demo = gr.ChatInterface(
    fn=chat_fn,  # or use chat_with_context if you want to show context
    title="📊 Finance AI Agent",
    description="Ask questions about your company's financial data!",
    theme="soft",
    examples=[
        "What is the date of issue for invoice 69638281?",
        "Who is the seller listed in invoice 37575831?",
        "What was the nitem purchased in invoice 69638281?"
    ],
    submit_btn="➡️ Submit",
    chatbot=gr.Chatbot(show_copy_button=True),
)

if __name__ == "__main__":
    demo.launch(share=True)



