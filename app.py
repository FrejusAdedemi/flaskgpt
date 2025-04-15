import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, Response

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prompt', methods=['POST'])
def prompt():
    messages = request.json['messages']
    conversation = build_conversation_dict(messages=messages)

    return Response(event_stream(conversation), mimetype='text/event-stream')


def event_stream(conversation: list[dict]) -> str:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        stream=True
    )

    for line in response:
        text = getattr(line.choices[0].delta, 'content', '')
        if text:
            yield text
#
#
def build_conversation_dict(messages: list) -> list[dict]:
    return [
        {"role": "user" if i % 2 == 0 else "assistant", "content": message}
        for i, message in enumerate(messages)
    ]


if __name__ == "__main__":
    app.run(debug=False)
