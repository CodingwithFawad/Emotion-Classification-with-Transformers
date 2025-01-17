# Emotion Classification with Transformers 

This project demonstrates emotion classification using a Transformer-based model, `SamLowe/roberta-base-go_emotions`, and a user-friendly interface built with [Gradio](https://gradio.app/). Users can input a sentence and receive a breakdown of emotion probabilities, providing insights into the emotional context of the text.

## Features 

- **Transformer Model**: Leverages the `roberta-base-go_emotions` model for accurate emotion classification.
- **User-Friendly Interface**: Powered by Gradio, with a clean and professional design.
- **Emotion Analysis**: Displays emotion probabilities instantly based on user input.

## Installation 

 **Clone the Repository**:
   
```
git clone https://github.com/CodingwithFawad/Emotion-Classification-with-Transformers

```
```
cd Emotion-Classification-with-Transformers
```

 **Install Dependencies**:

```
pip install -r requirements.txt

```
   
## Usage

1. **Run the Application**

2. **Access the Interface**  
   Open the Gradio link in a browser.

3. **Classify Emotions**  
   Type a sentence into the input box and click the **Classify** button to view the emotion probabilities.


## Example

**Input**  
*"I am so excited about the future!"*

**Output**

| **Emotion**  | **Probability** |
|--------------|------------------|
| Joy          | 0.85            |
| Surprise     | 0.10            |
| Neutral      | 0.05            |



## Model Details

- **Name**: `SamLowe/roberta-base-go_emotions`
- **Source**: [Hugging Face](https://huggingface.co/SamLowe/roberta-base-go_emotions)
- **Dataset**: Fine-tuned on the **GoEmotions** dataset by Google, which includes 27 emotion categories.



## Acknowledgments

- **Hugging Face**: For providing the pre-trained model and pipeline.
- **Gradio**: For the intuitive and easy-to-use interface.
- **Google**: For creating the **GoEmotions** dataset.






