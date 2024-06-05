from flask import Flask, request, render_template
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            number1 = float(request.form['number1'])
            number2 = float(request.form['number2'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = number1 + number2
            elif operation == 'subtract':
                result = number1 - number2
            elif operation == 'multiply':
                result = number1 * number2
            elif operation == 'divide':
                if number2 == 0:
                    result = 'Сan\'t divide by zero'
                else:
                    result = number1 / number2
            else:
                result = 'Invalid Operation'

            # Log the calculation
            logging.info(f'Operation: {operation}, Number1: {number1}, Number2: {number2}, Result: {result}')
        
        except ValueError:
            result = 'Invalid input'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

