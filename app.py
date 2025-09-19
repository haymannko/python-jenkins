from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
            background-color: #f0f0f0;
        }
        .calculator {
            display: inline-block;
            background: #dde1e7;
            padding: 20px;
            border-radius: 10px;
        }
        input[type="text"] {
            width: 210px;
            height: 40px;
            font-size: 20px;
            margin-bottom: 10px;
            text-align: right;
        }
        .buttons button {
            width: 50px;
            height: 50px;
            margin: 5px;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <h2>Python Calculator</h2>
    <div class="calculator">
        <form method="post">
            <input type="text" name="expression" value="{{ expression }}" readonly><br>
            <div class="buttons">
                {% for row in layout %}
                    {% for button in row %}
                        <button type="submit" name="button" value="{{ button }}">{{ button }}</button>
                    {% endfor %}
                    <br>
                {% endfor %}
            </div>
        </form>
    </div>
</body>
</html>
"""


layout = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", "C", "=", "/"]
]

@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = ""
    if request.method == "POST":
        expression = request.form.get("expression", "")
        btn = request.form["button"]

        if btn == "C":
            expression = ""
        elif btn == "=":
            try:
                expression = str(eval(expression))
            except:
                expression = "Error"
        else:
            expression += btn

    return render_template_string(HTML, expression=expression, layout=layout)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

