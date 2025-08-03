from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

app = Flask(__name__)
CORS(app)

# Load processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    file = request.files['image']
    image = Image.open(file.stream).convert('RGB')

    inputs = processor(image, return_tensors="pt")

    output = model.generate(
        **inputs,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
        max_length=50,
        num_return_sequences=3,
        repetition_penalty=1.5
    )

    captions = [processor.decode(c, skip_special_tokens=True) for c in output]
    return jsonify({'captions': captions})


if __name__ == '__main__':
    app.run(debug=True)
