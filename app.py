from flask import Flask, render_template, request, jsonify
from main import chain
from vector import get_clean_reviews

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    # Get clean reviews from vector store
    reviews = get_clean_reviews(question)
    
    # Get response from LLM
    response = chain.run({"reviews": reviews, "question": question})
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
