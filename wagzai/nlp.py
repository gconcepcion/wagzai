import json

from transformers import pipeline

# Load pet information
with open("wagzai/data/pet_info.json") as f:
    pet_data = json.load(f)

# Set up Hugging Face pipeline
nlp_pipeline = pipeline("question-answering")


def process_query(query):
    # Basic keyword matching
    for pet, info in pet_data.items():
        if pet.lower() in query.lower():
            return info

    # Use Hugging Face model to find the answer in pet_data
    context = " ".join([info for info in pet_data.values()])
    result = nlp_pipeline(question=query, context=context)

    return (
        result["answer"]
        if result["score"] > 0.5
        else "Sorry, I don't have information about that."
    )
