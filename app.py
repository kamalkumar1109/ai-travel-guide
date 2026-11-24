
import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# Function called by Gradio
def travel_guide(user_message):

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are a witty travel guide."
            },
            {
                "role": "user",
                "content": user_message
            },
        ],
    )

    return response.choices[0].message.content


# Gradio UI
demo = gr.Interface(
    fn=travel_guide,
    inputs=gr.Textbox(
        lines=3,
        placeholder="e.g. Suggest five things to do in Hisar",
        label="Ask your travel guide"
    ),
    outputs=gr.Markdown(label="Travel Guide Response"),
    title="🌍 AI Travel Guide",
    description="Powered by Groq GPT-OSS 120B",
    examples=[
        "Suggest one thing to do in Hisar",
        "Plan a 2-day trip to Jaipur",
        "Suggest budget-friendly places to visit in Delhi"
    ]
)

demo.launch(share=True)
