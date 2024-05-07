# from flask import Flask, render_template, request, redirect, url_for, session
# import subprocess

# app = Flask(__name__)
# app.secret_key = 'your_secret_key_here' # Replace with a secret key

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         query = request.form.get('query')
#         if query.upper() == 'EXIT':
#             session.pop('ticker', None) # Clear the ticker from the session
#             return redirect(url_for('index'))
#         else:
#             if 'ticker' not in session:
#                 # This is the first query, so we're setting the ticker
#                 session['ticker'] = query
#                 # Run the initial setup with the ticker
#                 subprocess.run(['python', 'main.py', session['ticker']], capture_output=True, text=True)
#                 return render_template('index.html', result="Initial setup complete. Please enter your first query.")
#             else:
#                 # This is a subsequent query, so we're running the query chain
#                 result = subprocess.run(['python', 'main.py', session['ticker'], query], capture_output=True, text=True)
#                 return render_template('index.html', result=result.stdout)
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, session
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' # Replace with a secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        query = request.form.get('query')
        if query.upper() == 'EXIT':
            session.pop('ticker', None) # Clear the ticker from the session
            return redirect(url_for('index'))
        else:
            if 'ticker' not in session:
                # This is the first query, so we're setting the ticker
                session['ticker'] = ticker
                # Run the initial setup with the ticker and predefined query
                result = subprocess.run(['python', 'main.py', session['ticker']], capture_output=True, text=True)
                return render_template('index.html', result=result.stdout)
            else:
                # This is a subsequent query, so we're running the query chain
                result = subprocess.run(['python', 'main.py', session['ticker'], query], capture_output=True, text=True)
                return render_template('index.html', result=result.stdout)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
