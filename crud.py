from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

#YOUR FUNCTIONS HERE



@app.route('/')
def index():
    #return "Hello World";
    
    data = {'company_name': "TCET"}
    return render_template('hello.html', data = data)




@app.route('/sqr', methods=['GET'])
def getSqr():
    
    num1 = int(request.args.get('num1'));
    return f"Square of {num1} is {num1 * num1}"




@app.route('/add', methods=['GET'])
def add():
    num1 = int(request.args.get('num1'));
    num2 = int(request.args.get('num2'));
    
    return f"{num1} + {num2} = {num1 + num2}";




@app.route('/sub', methods=['POST'])
def sub():
    num1 = int(request.form.get('num1'));
    num2 = int(request.form.get('num2'));
    
    return f"{num1} - {num2} = {num1 - num2}";




@app.route('/mul', methods=['POST'])
def mul():
    raw_json = request.get_json();
    num1 = int(raw_json['num1']);
    num2 = int(raw_json['num2']);
    
    return f"{num1} * {num2} = {num1 * num2}";


















if __name__ == "__main__":
    app.run(debug=True);
    #app.run(host="0.0.0.0", port=int("1234"), debug=True)
