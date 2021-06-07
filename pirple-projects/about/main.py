from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('structure.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', message= "About page")

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html', message = "Dashboard")
    
@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html',message = "Privacy page")
    
@app.route('/terms', methods =['GET'])
def terms():
    return render_template('terms.html', message = "Terms of use page")
    
@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html', message = "Contact page")

if __name__=='__main__':
    app.run(port=7000, debug=True)