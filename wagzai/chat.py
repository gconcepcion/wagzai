import json

from flask import Blueprint, jsonify, request
from transformers import (
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    pipeline,
)

from wagzai.models import Message

# from wagzai.views import app_blueprint

# model_id = "meta-llama/Meta-Llama-3-8B"
# model_id = "facebook/blenderbot-400M-distill"
# model_id = "microsoft/Phi-3-mini-128k-instruct"

# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

# chat_blueprint = Blueprint('chat', __name__, url_prefix='/chat')
chat_blueprint = Blueprint("chat", __name__, url_prefix="/chat")

model_id = "microsoft/Phi-3-mini-128k-instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cuda",
    torch_dtype="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(model_id)


chatbot_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# @chat_blueprint.as_view('chat')
# def chat():
#    data = request.get_json()
#    input_text = data['input']
#    response = chatbot_pipeline(input_text)['generated_text'][0]
#    return jsonify({'response': response})


@chat_blueprint.route("/messages")
def get_messages():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return jsonify(
        [
            {
                "id": message.id,
                "content": message.content,
                "username": message.user.username,
            }
            for message in messages
        ]
    )
