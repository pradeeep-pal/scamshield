from flask import Flask, render_template, request

app = Flask(_name_)

# Simple keyword-based logic (ML later add karenge)
SCAM_KEYWORDS = ["free", "win", "lottery", "click here", "urgent", "prize", "offer"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form.get("text").lower()

        score = sum(word in text for word in SCAM_KEYWORDS)

        if score >= 2:
            result = "❌ Scam Detected"
        elif score == 1:
            result = "⚠ Suspicious"
        else:
            result = "✅ Safe"

    return render_template("index.html", result=result)

if _name_ == "_main_":
    app.run(debug=True)
