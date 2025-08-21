from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from vector import get_clean_reviews

# Initialize the model
model = OllamaLLM(model="llama3.2")

# Define the prompt template
template = """
You are an expert pizza consultant in a friendly pizza restaurant.
Use a natural, human-like tone. Summarize the reviews with pros and cons in simple language.
Here are some relevant reviews: {reviews}
Here is the question you need to answer: {question}
Respond as if you are talking to a customer, giving helpful advice and recommendations.
"""

prompt = ChatPromptTemplate.from_template(template)

# Wrap the model and prompt in an LLMChain
chain = LLMChain(llm=model, prompt=prompt)

# Interactive loop
# while True:
#     print("\n-----------------")
#     question = input("Ask your question(s) | q to QUIT: ")
#     print("-----------------")
#     if question.lower() == "q":
#         break
#     else: 
#         reviews = get_clean_reviews(question)
#         result = chain.run({"reviews": reviews, "question": question})  # <-- run() returns clean text
#         print("\nResponse:\n")
#         print(result)
