import gradio as gr
from transformers import pipeline

# Initialize the classifier
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

# Function to predict emotions
def classify_emotions(sentence):
    outputs = classifier(sentence)
    results = {output["label"]: output["score"] for output in outputs[0]}  # Extract labels and scores
    return results

# Create the Gradio interface with a professional design
with gr.Blocks() as demo:
    # Header with markdown
    gr.Markdown("<h1 style='text-align: center; color: #1e3a8a;'>Emotion Classification with Transformers</h1>")
    gr.Markdown("<p style='text-align: center; color: #555;'>Enter a sentence to classify emotions.</p>")

    # Input and Output components in a clean layout
    with gr.Row():
        input_text = gr.Textbox(label="Input Sentence", placeholder="Type your sentence here...", lines=2, max_lines=3)

    with gr.Row():
        output_label = gr.Label(label="Emotion Probabilities")

    # Button with default styling, and the color will automatically be modern and clean
    with gr.Row():
        classify_button = gr.Button("Classify")
        classify_button.click(classify_emotions, inputs=input_text, outputs=output_label)

# Launch the Gradio app
demo.launch()
