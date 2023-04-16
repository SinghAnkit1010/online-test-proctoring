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


my_db = db_connector.connect(host = "localhost",user = "root",passwd = "deeplearning",
database = "vivek-otp",auth_plugin="mysql_native_password",autocommit = True)

app = Flask(__name__,template_folder="template") 
app.secret_key = os.urandom(22)


UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

file = open("encoded_data.p","rb")
face_embeddings = pickle.load(file)


streaming = True

def video_streaming():
    face_encoder = FaceNet()
    face_detector = MTCNN()
    global capture
    capture = cv2.VideoCapture(0)
    while streaming:
        isTrue,image = capture.read()
        if not isTrue:
            continue
        try:
            img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            bbox = face_detector.detect_faces(img)[0]["box"]
            x,y,w,h = bbox
            x1,y1,x2,y2 = x,y,x+w,y+h
            face = img[y1:y2,x1:x2]
            face = face.reshape(1,face.shape[0],face.shape[1],face.shape[2])
            embeddings = face_encoder.embeddings(face)
            student_id = []
            distance = []
            for email,vector in face_embeddings.items():
                student_id.append(email)
                distance.append(face_encoder.compute_distance(embeddings[0],vector[0]))
            id = student_id[np.argmin(distance)]
            my_cursor = my_db.cursor()
            my_cursor.execute("select username from accounts where email = %s",(id,))
            name = my_cursor.fetchone()[0]
            cv2.rectangle(image,(x1,y1),(x2,y2),(255,0,0),3)
            cv2.putText(image,name,(x1,y1),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,255))
            ret,buffer = cv2.imencode(".jpg",image)
            image = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')      
        except:
            continue
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

@app.route('/post-test-page')
def post_test_page():
    return render_template("post-test-page.ejs")

@app.route('/proctoring')
def proctoring():
    return Response(video_streaming(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["passwd"]
        my_cursor = my_db.cursor()
        my_cursor.execute('SELECT * FROM accounts WHERE email = %s AND passwd = %s;', (email, password))
        account = my_cursor.fetchone()[0]
        if account:
            session["loggedin"] = True
            #session["email"] = account["email"]
            #session["id"] = account["id"]
            return redirect("/test-page")
        else:
            return redirect("/random")

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
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
        return render_template("login_page.html",msg = msg)
    return render_template("login_page.html")
@app.route('/stopcamera', methods=["GET",'POST'])
def stopcamera(): 
    capture.release()
    cv2.destroyAllWindows()
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)

