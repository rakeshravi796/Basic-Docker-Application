from flask import Flask, redirect, url_for, request , render_template
app = Flask(__name__,template_folder='template')
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add' , methods = ['POST'])
def adder():
    numbers = [int(x) for x in request.form.values()]
    return render_template("index.html" , adder_answer = f"{sum(numbers)}")

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
