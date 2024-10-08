from captum.attr import LayerIntegratedGradients, GradientShap
import matplotlib as mpl
import numpy as np
import torch


# Function to decode token IDs back to a clean sentence, excluding special tokens
def decode_sentence(token_ids, tokenizer):
    return tokenizer.decode(token_ids, skip_special_tokens=True)


# Function to calculate and return hexadecimal colors based on attributions
def colorize(attributions, cmap='PiYG'):
    """Generate color for each word based on its attribution score."""
    cmap_bound = np.abs(attributions).max()
    norm = mpl.colors.Normalize(vmin=-cmap_bound, vmax=cmap_bound)
    cmap = mpl.pyplot.get_cmap(cmap)

    # Convert attribution values to hexadecimal colors
    return list(map(lambda x: mpl.colors.rgb2hex(cmap(norm(x))), attributions))


# Function to generate an HTML-highlighted sentence based on attributions
def visualize_attributions(attributions, inputs, tokenizer):
    """Generate an HTML-highlighted sentence based on attributions."""
    token_ids = inputs['input_ids'].cpu().numpy()[0]

    # Normalize attributions
    attributions = attributions.sum(dim=2).squeeze(0).cpu().detach().numpy()
    attributions = attributions / np.linalg.norm(attributions)

    # Decode sentence from token IDs
    cleaned_sentence = decode_sentence(token_ids, tokenizer)
    words = cleaned_sentence.split()

    # Generate colors for words based on attributions
    colors = colorize(attributions[1:len(words) + 1])

    # Generate HTML for highlighted sentence
    highlighted_sentence = "".join([
        f"<span style='background-color: {color}'>{word}</span> "
        for word, color in zip(words, colors)
    ])

    return highlighted_sentence


# Function to explain the model's predictions
def explain_model(model, tokenizer, sentence, target_label):
    """
    Explain model predictions using different explainability methods such as Saliency,
    """

    # Set the model in evaluation mode
    model.eval()

    # Tokenize input sentence
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding="max_length", max_length=128)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    # Forward function to return model logits
    def forward_func(input_ids, attention_mask):
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        return torch.softmax(outputs.logits, dim=-1)

    # Choose the attribution method
    explainer = LayerIntegratedGradients(forward_func,  model.convbert.embeddings.word_embeddings)
    attributions, delta = explainer.attribute(input_ids, additional_forward_args=(attention_mask,), target=target_label, n_steps=10, return_convergence_delta=True)

    # Visualize and return attributions in HTML format
    explained_text = visualize_attributions(attributions, inputs, tokenizer)
    return explained_text
