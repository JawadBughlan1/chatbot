from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined responses based on your financial data analysis
responses = {
    "total revenue": "The total revenue in 2023 was $211 billion for Apple, $232 billion for Microsoft, and $96 billion for Tesla.",
    "net income": "In 2023, Apple earned $57 billion, Microsoft $72 billion, and Tesla $12 billion in net income.",
    "revenue growth": "Compared to 2022, Apple grew by 5%, Microsoft by 8%, and Tesla by 19% in revenue.",
    "cash flow": "Operating cash flow in 2023: Apple - $110B, Microsoft - $95B, Tesla - $17B.",
    "total assets": "Total assets in 2023: Apple - $384B, Microsoft - $430B, Tesla - $95B."
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("query", "").lower()
        answer = responses.get(user_input, "Sorry, I can only answer predefined financial queries.")
        return render_template("index.html", response=answer, user_input=user_input)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)