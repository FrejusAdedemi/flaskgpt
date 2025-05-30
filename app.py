import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, Response, abort

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "your_openai_api_key_here":
    print("WARNING: OpenAI API key is not set or is using the default placeholder value.")
    print("Please set your API key in the .env file or as an environment variable.")
    print("You can get an API key from https://platform.openai.com/api-keys")

openai.api_key = api_key

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prompt', methods=['POST'])
def prompt():
    messages = request.json['messages']
    conversation = build_conversation_dict(messages=messages)

    if not api_key or api_key == "your_openai_api_key_here":
        error_message = "Error: OpenAI API key is not set or is using the default placeholder value. Please set your API key in the .env file."
        return jsonify({"error": error_message}), 500

    return Response(event_stream(conversation), mimetype='text/event-stream')


def event_stream(conversation: list[dict]) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            stream=True
        )

        for line in response:
            text = getattr(line.choices[0].delta, 'content', '')
            if text:
                yield text
    except Exception as e:
        yield f"Error: {str(e)}"
#
#
def build_conversation_dict(messages: list) -> list[dict]:
    return [
        {"role": "user" if i % 2 == 0 else "assistant", "content": message}
        for i, message in enumerate(messages)
    ]


if __name__ == "__main__":
    app.run(debug=False)
