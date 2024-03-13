from flask import Flask, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('voice_input.html')

@app.route('/voice_input', methods=['POST'])
def voice_input():
    data = request.json
    voice_text = data['voice_text']
    
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Convert voice_text to audio
    audio_data = voice_text.encode('utf-8')
    
    # Recognize speech
    try:
        # Recognize the speech
        result = recognizer.recognize_google(audio_data)
        # Process the recognized text here...
        processed_result = process_text(result)
        return jsonify({'result': processed_result})
    except sr.UnknownValueError:
        return jsonify({'error': 'Speech recognition could not understand audio'})
    except sr.RequestError as e:
        return jsonify({'error': f'Speech recognition service error: {e}'})

def process_text(text):
    # Process the recognized text here...
    # Example: Convert text to uppercase
    return text.upper()

if __name__ == '__main__':
    app.run(debug=True)
