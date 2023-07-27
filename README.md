<h1 align="center">Online Test Proctoring</h1>
    <h2>Introduction</h2>
    <p>The idea behind an online test proctoring model is to use technology to monitor and proctor online exams to prevent cheating and ensure academic integrity.For this we have used various functionality like face detection,face recognition,mobile phone detection,eye tracking for now.
    <h2>Features</h2>
	<ul>
		<li>Face Detection</li>
		<p>we have used MTCNN model for face detection which consists of three stages of convolutional networks that are able to recognize faces and landmark location such as eyes, nose, and mouth The 3 stages of MTCNN are P-Net, R-Net, O-Net. And with the help of this model we can detect faces and also detect if there is multiple faces which is not acceptable.</p>
		<li>Face Authentication</li>
		<p>Face authentication in online test proctoring involves using a computer vision system to capture and analyze the test taker's face during the exam. The system compares the facial features of the test taker against the reference facial features on file to ensure that they remain the same person throughout the duration of the exam.</p>
		<li>Eye Tracking</li>
		<p>Eye tracking in online test proctoring involves using a camera or sensor to track the movements of the test taker's eyes while they are taking the exam. It can detect any suspicious behavior, such as if the test taker is looking away from the screen for an extended period or if they are constantly shifting their gaze.</p>
		<li>Smart Device Detection</li>
		<p>Smart device detection in online test proctoring involves using software that can detect the presence of any electronic device within the range of the exam area, such as a mobile phone, smartwatch, or tablet. It can help prevent cheating by ensuring that the test taker is not using any electronic devices to access unauthorized resources during the exam.</p>
	</ul>
	 <h2>Implementation</h2>
<p>The proctoring system makes use of several machine learning models and techniques for effective monitoring of online tests. Here are some details about the models and techniques used:</p>
<ul>
  <li><strong>FaceNet Model:</strong> The FaceNet model is used for face recognition and authentication during the online test proctoring process. It takes an image of a person's face as input and outputs a 128-dimensional vector representation of the face. This vector is then compared with the vectors of other faces in the database to verify the identity of the person taking the test.</li>
  <li><strong>YOLOv5:</strong> YOLOv5 is a state-of-the-art object detection model that was used to train our custom object detection model to detect mobile phones within the range of the exam area. This helps prevent cheating by detecting when students attempt to use their phones during the test.</li>
  <li><strong>Convolutional Neural Network (CNN):</strong> A CNN was used for eye tracking based on the Kaggle dataset. The model takes as input a series of frames captured from a webcam and detects the location of the user's eyes. This information is used to ensure that the user is looking at the screen and not at any other devices or materials during the test.</li>
  <li><strong>Database:</strong> A database was maintained to store user information and exam data. It includes information about users who successfully submitted the test as well as those who were caught cheating during the test. This helps to track student progress and ensure the integrity of the testing process.</li>
</ul>
<h2>Enhancements</h2>
<p>There are several potential enhancements that could be made to our proctoring system:</p>
<ul>
  <li><strong>Improving accuracy:</strong> The models used in the system could be further trained and fine-tuned on larger datasets to improve their accuracy and performance.</li>
  <li><strong>Head movement detection:</strong> The addition of head movement detection could help to further prevent cheating by detecting when a user is looking away from the screen or otherwise moving their head in a way that suggests they may be attempting to cheat.</li>
</ul>
<p>By implementing these enhancements and continuing to refine the system over time, we believe that our proctoring system can become an even more effective tool for ensuring the integrity of online tests and exams.</p>
