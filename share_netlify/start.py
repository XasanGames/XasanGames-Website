from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('./index.html')


@app.route('/about')
def about():
    return render_template('./about.html')

@app.route('/contactus')
def contactUs():
    return "Contact us"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('./404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=8000)
