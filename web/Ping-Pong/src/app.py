from flask import request ,Flask , render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/ping', methods=['GET'])
def ping():
    target = request.args.get('ip')
    target = ''.join(target.split())
    output = os.popen("ping -c 4 " + target ).read()
    print(output)
    return render_template('ping.html', output="Pinged successfully!!  :)")

if __name__ == '__main__':
    app.run()