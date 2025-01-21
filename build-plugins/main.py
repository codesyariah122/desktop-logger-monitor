from flask import Flask, request, jsonify
from rembg import remove
from PIL import Image
import io
import base64
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/remove-background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['image']
    image = Image.open(file)
    output = remove(image)
    
    buffer = io.BytesIO()
    output.save(buffer, format="PNG")
    buffer.seek(0)
    
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return jsonify({'image': image_base64})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)