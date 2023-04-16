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


my_cursor = my_db.cursor()
my_cursor.execute('SELECT * FROM accounts')

print(my_cursor.fetchone()[0])

