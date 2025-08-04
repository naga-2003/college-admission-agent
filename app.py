import json
from sentence_transformers import SentenceTransformer, util
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials
from flask import Flask, request, jsonify, render_template

API_KEY = "wIkRdowNa3hyd6tFBMuJT0FNekL9FlGNn4aMIcqA9RCu"
PROJECT_ID = "3a53d5cd-492e-4f4d-b471-80b4176d68c6"
URL = "https://us-south.ml.cloud.ibm.com"

app = Flask(__name__)

with open("data/admission_faq.json", encoding="utf-8") as f:
    faq = json.load(f)

questions = [item["question"] for item in faq]
model_sbert = SentenceTransformer("all-MiniLM-L6-v2")
faq_embeddings = model_sbert.encode(questions, convert_to_tensor=True)

credentials = Credentials(api_key=API_KEY, url=URL)
gen_model = ModelInference(
    model_id="ibm/granite-13b-instruct-v2",
    credentials=credentials,
    project_id=PROJECT_ID
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    q = request.json.get("question", "")
    q_emb = model_sbert.encode(q, convert_to_tensor=True)
    scores = util.cos_sim(q_emb, faq_embeddings)
    idx = scores.argmax().item()
    retrieved = faq[idx]["answer"]

    prompt = f"Q: {q}\nA: {retrieved}\nPlease elaborate in simple, student‑friendly terms."
    resp = gen_model.generate(prompt=prompt)
    text = resp.get("results", [{}])[0].get("generated_text", "")

    return jsonify(answer=text)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
