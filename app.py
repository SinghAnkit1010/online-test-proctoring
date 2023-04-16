from flask import Flask,render_template,request,redirect,url_for,session,Response
from flask_mysqldb  import MySQL
import MySQLdb.cursors
import pickle
import cv2
import os
from face import Embeddings
from keras_facenet import FaceNet
from mtcnn.mtcnn import MTCNN
import numpy as np
import mysql.connector as db_connector
from datetime import date,time
from werkzeug.utils import secure_filename
from eye_detector import eye_detection
from phone_detector import phone_detection


my_db = db_connector.connect(host = "localhost",user = "root",passwd = "deeplearning",
database = "groot_database",auth_plugin="mysql_native_password",autocommit = True)

app = Flask(__name__,template_folder="template") 
app.secret_key = os.urandom(22)


UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

file = open("encoded_data.p","rb")
face_embeddings = pickle.load(file)


streaming = True

def video_streaming():
    global not_detected
    global other_person
    global phone_sus
    global eye_sus
    not_detected = 0
    other_person = 0
    phone_sus = 0
    eye_sus = 0
    curr_email = email
    curr_face = face_embeddings[curr_email]
    face_encoder = FaceNet()
    face_detector = MTCNN()
    global capture
    capture = cv2.VideoCapture(0)
    while streaming:
        print(not_detected)
        print(other_person)
        print(phone_sus)
        print(eye_sus)
        isTrue,image = capture.read()
        if not isTrue:
            continue
        img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        bbox = face_detector.detect_faces(img)
        if len(bbox) == 0:
            not_detected +=1
        else:
            box = bbox[0]["box"]
            x,y,w,h = box
            x1,y1,x2,y2 = x,y,x+w,y+h
            face = img[y1:y2,x1:x2]
            face = face.reshape(1,face.shape[0],face.shape[1],face.shape[2])
            embeddings = face_encoder.embeddings(face)
            distance = face_encoder.compute_distance(embeddings[0],curr_face[0])
            if distance > 0.4:
                other_person += 1
            obj = eye_detection()
            eye_move = obj.result(face_detector,image)
            if eye_move == 0:
                c = 0
            elif(eye_move ==1):
                c+=1
            else:
                c=0
            if(c>=10):
                eye_sus+=1
                c=0
        object = phone_detection()
        phone = object.result(image)
        if phone == 1:
            phone_sus += 1
        ret,buffer = cv2.imencode(".jpg",image)
        image = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')     
    capture.release()
    cv2.destroyAllWindows()






@app.route('/')
def landing_page():
    return render_template('home.ejs')

@app.route('/random')
def random():
    return render_template("login.ejs")

@app.route("/register")
def register():
    return render_template("register.ejs")


@app.route("/test-page")
def test_page():
    return render_template("test-page.ejs")

@app.route('/testing')
def testing():
    return render_template("testing.ejs")

@app.route('/documentation')
def documentation():
    return render_template("documentation.ejs")

@app.route('/contact',methods = ["GET","POST"])
def contact():
    if request.method == "POST":
        return render_template("thankyou.ejs")
    return render_template("contact.ejs")

@app.route('/post-test-page')
def post_test_page():
    return render_template("post-test-page.ejs")

@app.route('/invalid-credentials')
def invalid_credentials():
    return render_template("invalid-credentials.ejs")

@app.route('/proctoring')
def proctoring():
    return Response(video_streaming(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        global email
        email = request.form["email"]
        password = request.form["passwd"]
        my_cursor = my_db.cursor()
        my_cursor.execute('SELECT * FROM accounts WHERE email = %s AND passwd = %s;', (email, password))
        account = my_cursor.fetchone()[0]
        if account:
            session["loggedin"] = True
            #session["username"] = account["email"]
            return redirect("/test-page")
        else:
            return redirect("/invalid-credentials")

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    email = None
    print(email)
    #session.pop('id', None)
    #session.pop('username', None)
    return redirect("/")

@app.route("/add_user",methods = ["GET","POST"])
def add_user():
    if request.method == "POST":
        username = request.form['username']
        passwd = request.form['passwd']
        email = request.form['email']
        institute = request.form['institute']
        image = request.files["image"]
        img_filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
        img_file_path = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
        embeddings = Embeddings()
        embeddings.adding_new_face(img_file_path,email)
        my_cursor = my_db.cursor()
        my_cursor.execute("INSERT INTO accounts VALUES (%s, %s, %s, %s);", (username, passwd, email,institute))
        msg = "Successfully registered!"
        return render_template("login.ejs",msg = msg)
    return render_template("login.ejs.")

@app.route('/stopcamera', methods=["GET",'POST'])
def stopcamera():
    streaming = False 
    if(not_detected >= 10 or other_person >= 8 or phone_sus >= 10 or eye_sus > 25):
        my_cursor = my_db.cursor()
        my_cursor.execute("INSERT INTO rejected VALUES (%s);", (email))
    else:
        my_cursor = my_db.cursor()
        my_cursor.execute("INSERT INTO successful VALUES (%s);", (email))
    capture.release()
    cv2.destroyAllWindows()
    return redirect("/post-test-page")


if __name__ == '__main__':
    app.run(debug=True)

