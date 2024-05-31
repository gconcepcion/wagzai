import json
import random
from collections import Counter

import nltk

nltk.download("maxent_ne_chunker")
nltk.download("averaged_perceptron_tagger")
nltk.download("words")
nltk.download("punkt")

from transformers import pipeline

from wagzai.utils.parse_akc_data import load_breed_info

# Load pet information
with open("data/pet_info.json") as f:
    pet_data = json.load(f)

# Set up Hugging Face pipeline
nlp_pipeline = pipeline("question-answering")


def load_api_key(file_path):
    with open(file_path) as f:
        api_key = f.read().strip()
    return api_key


thecatapi = "/home/gconcepcion/.ssh/thecatapi"
API_KEY = load_api_key(thecatapi)

breeds = load_breed_info()


def get_breed_info(user_query, breeds):

    def find_breed(user_query, breeds):
        for breed in breeds:
            print(type(user_query))
            print(user_query["message"], breed["breed"])
            if any(
                keyword in breed["breed"].lower()
                for keyword in user_query["message"].split()
            ):
                return breed
        return None

    user_query_dict = json.loads(user_query)
    print(type(user_query_dict))
    print(f"{user_query} userquery")
    matching_breed = find_breed(user_query_dict, breeds)
    if matching_breed:
        print(f"Found match: {matching_breed}")
    else:
        print("No matching breed found.")
    # Output: Found match: {'name': 'Golden Retriever', ...}

    breed_info = {"breed": matching_breed}

    return breed_info


def process_query(query):
    print(query)
    # Basic keyword matching
    #    for pet, info in pet_data.items():
    #        if pet.lower() in query.lower():
    ##            print(f"info:{info}")
    #           return info

    # Use Hugging Face model to find the answer in pet_data
    context = " ".join([info for info in pet_data.values()])
    breed = get_breed_info(query, breeds)
    print(breed)

    result = nlp_pipeline(question=query, context=context)
    # print(result)
    #   keywords = extract_keywords_from_query(result, train_model())
    #   print(keywords)
    return (
        result["answer"]
        if result["score"] > 0.5
        else "Sorry, I don't have information about that."
    )


# Training data for keyword extraction (replace with your own training data)
training_data = [
    ("What is the size of a dog?", ["size", "dog"]),
    ("What does a cat eat?", ["eat", "cat"]),
    ("Where does a bird live?", ["live", "bird"]),
]


# Function to extract noun phrases from the given text using NLTK's Maxent Ratio Feature extractor and classifier
def extract_keywords(text):
    tagged = nltk.ne_chunk(nltk.pos_tag(nltk.sent_tokenize(text)))
    keywords = []
    for chunk in tagged:
        if hasattr(chunk, "label"):  # Check if the chunk is a noun phrase
            if chunk.label() == "NP":
                words = [word[0] for word in chunk]
                keywords += Counter(words).most_common()
    return keywords


# Function to train keyword extraction model using NLTK's Maxent Ratio Feature extractor and classifier
def train_model():
    all_words = []
    all_tags = []

    for text, tags in training_data:
        words = nltk.word_tokenize(text)
        tagged = [(" ".join(w), t) for w, t in zip(words, nltk.pos_tag(words))]
        all_words += tagged
        all_tags += [(t, "O") for t in tagged] + [
            (t, "B-" + tags[0]) for t, tags in chunked if len(chunked) > 1
        ]

    nlp = nltk.MaxentIOBTagger(all_words, all_tags)
    nlp.train()
    return nlp


# Function to extract keywords from user queries using the trained keyword extraction model
def extract_keywords_from_query(query, model):
    tagged = model.tag(nltk.word_tokenize(query))
    keywords = []
    for word, tag in tagged:
        if tag.startswith("B-"):
            keywords.append(word)
    return keywords
