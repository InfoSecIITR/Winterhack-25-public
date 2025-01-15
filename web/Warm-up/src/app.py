from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/robots.txt')
def robots():
    robots_txt = """User-agent: *
Disallow: /super/secret/path/
# Flag Part 2: _th3r3_w3lc0m3_
"""
    return Response(robots_txt, content_type="text/plain")

@app.route('/super/secret/path/')
def secret():
    return render_template('secret.html')

if __name__ == '__main__':
    app.run(debug=True)

