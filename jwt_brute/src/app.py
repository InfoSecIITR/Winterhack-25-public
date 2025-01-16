from flask import Flask, request, jsonify, redirect, url_for, make_response, render_template
import jwt
import datetime
import uuid

app = Flask(__name__)
app.secret_key = 'diphoronpentaperoxide'

@app.route('/', methods=['GET'])
def home():
    token = request.cookies.get('jwt')
    if token:
        try:
            payload = jwt.decode(token, app.secret_key, algorithms=['HS256'])
   #         payload = jwt.decode(token, options={"verify_signature": False})
            return redirect(url_for('note_form'))  # Redirect to notes if user is logged in
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            pass  

    return redirect(url_for('register_form'))  

@app.route('/register', methods=['GET'])
def register_form():
    token = request.cookies.get('jwt')
    if token:
        try:
            payload = jwt.decode(token, app.secret_key, algorithms=['HS256'])
    #        payload = jwt.decode(token, options={"verify_signature": False})
            return redirect(url_for('note_form'))  
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            pass  

    return render_template('register.html')  

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data['username']

    token = jwt.encode({
        'username': username,
        'role': 'guest',
        'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
    }, app.secret_key, algorithm='HS256')
    
    response = make_response(redirect(url_for('note_form'))) 
    response.set_cookie('jwt', token)
    
    return response 

@app.route('/note', methods=['GET'])
def note_form():
    token = request.cookies.get('jwt')
    if not token:
        return redirect(url_for('register_form')) 

    try:
        payload = jwt.decode(token, app.secret_key, algorithms=['HS256'])
#        payload = jwt.decode(token, options={"verify_signature": False})

    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return redirect(url_for('register_form'))  

    return render_template('note.html', token=token)  

@app.route('/note/view/<string:note_id>', methods=['GET'])
def view_note_page(note_id):
    token = request.cookies.get('jwt')
    if not token:
        return redirect(url_for('register_form'))  

    try:
        payload = jwt.decode(token, app.secret_key, algorithms=['HS256'])
#        payload = jwt.decode(token, options={"verify_signature": False})

    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return redirect(url_for('register_form'))  

    return render_template('view_note.html')

@app.route('/flag', methods=['GET'])
def flag():
    token = request.cookies.get('jwt')
    try:
       payload = jwt.decode(token, app.secret_key, algorithms=['HS256'])
        # payload = jwt.decode(token, options={"verify_signature": False})
       if payload.get('role') == 'admin':
            return "winterhack{jw7_brut3_1s_3asy_w17h_h45hc4t}"
       else:
            return "sed😈 you are not admin" 
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return "sed😈 you are not admin"  

@app.route('/robots.txt',methods=['GET'])
def robots():
    return "Bro not always the flag is in robots.txt 🤖 look for /flag"
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)


