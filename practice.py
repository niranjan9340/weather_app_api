from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("product.html")

@app.route('/<product>')
def pro(product):
    return {
        "product": product,
    }

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
