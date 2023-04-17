<h1 align="center">Online Test Proctoring</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Team-Loosers-orange" alt="Team Loosers">
  <img src="https://img.shields.io/badge/Status-In%20Development-green" alt="In Development">
</p>
    <h2>Problem Statement:</h2>
    <p>In online tests without proctoring, cases are often reported of impersonation and cheating. Students either ask someone else to take the test on their behalf or use methods of cheating like referring to a textbook, using smartphones or other devices to search for answers online or taking help from a friend. The two major concerns of the customer are cheating and student authentication. It ensures the candidate focuses on the test screen during the test; there is enough light in the room and checks for suspicious objects to red flag the test. It also uses face recognition to do student authentication. Develop a suitable product that can perform all these functionalities. Use suitable Computer Vision techniques for face recognition and identifying objects. The product should be able to detect each of the mentioned unfair means used by the student. Students are supposed to deploy the model using a website or Android application.</p>
    <h2>Introduction</h2>
    <p>The idea behind an online test proctoring model is to use technology to monitor and proctor online exams to prevent cheating and ensure academic integrity. In addition to ensuring academic integrity, online test proctoring models can also provide benefits such as flexibility, convenience, and cost savings. Students can take exams from anywhere with an internet connection, and institutions can save resources by not having to hire physical proctors for online exams.</p>
    <p>This project is aimed at developing a suitable product that can perform all the required functionalities, which include cheating prevention and student authentication. The product is expected to ensure that the candidate focuses on the test screen during the test, there is enough light in the room, and that suspicious objects are flagged to prevent cheating. We will be using computer vision techniques for face recognition, identifying objects, and detecting each of the unfair means used by the student.</p>
    <h2>Team</h2>
    <ul>
      <li>Ankit Singh (<a href="https://www.linkedin.com/in/ankit-singh-4a4b35132/" target ="_blank">LinkedIn</a> | <a href="https://github.com/ankit-singh-unnao" target ="_blank">Github</a>)</li>
      <li>Vivek Dev Shah (<a href="https://www.linkedin.com/in/vivek-dev-shah-654521212/" target ="_blank">LinkedIn</a> | <a href="https://github.com/vivekdev01" target ="_blank">Github</a>)</li>
      <li>Praveen Shankar (<a href="https://www.linkedin.com/in/praveen-shankar-096630212/" target ="_blank">LinkedIn</a> | <a href="https://github.com/praveen-shankar" target ="_blank">Github</a>)</li>
      <li>Mohit Yadav (<a href="https://www.linkedin.com/in/mohit-yadav-9a045b207/" target ="_blank">LinkedIn</a> | <a href="https://github.com/curious-99" target ="_blank">Github</a>)</li>
    </ul>
    <h2>Features</h2>
	<ul>
		<li>Multiple Face Detection</li>
		<p>Multiple face detection is a computer vision technique used to detect and locate multiple faces in a given image or video frame. It is used in a variety of applications, including surveillance systems, photo tagging applications, and online test proctoring.</p>
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
<h1>Tech Stacks Used</h1>
	<ul>
		<li>Deep Learning</li>
		<li>Flask</li>
		<li>MySQL</li>
		<li>JavaScript</li>
		<li>HTML/CSS</li>
		<li>Bootstrap</li>
	</ul>
<h1>Screenshot</h1>
<img src="https://user-images.githubusercontent.com/101961142/232357548-e22334e9-9bf0-4904-bd22-99e3fe6697d5.png">
<img src="https://user-images.githubusercontent.com/101961142/232357413-9647d2e7-a43a-4da9-aeb0-2f47c4db4e1c.png">
<img src="https://user-images.githubusercontent.com/101961142/232357410-7b943c13-ca4f-49ef-908e-0d17e6cc78a5.png">
<img src="https://user-images.githubusercontent.com/101961142/232357407-d8a202eb-8218-4f5e-a90d-ba146033bd0e.png">
<img src="https://user-images.githubusercontent.com/101961142/232357415-918f26e3-4ff2-43fc-b4bb-062adb5145db.png">
<img src="https://user-images.githubusercontent.com/101961142/232357402-d529ec41-430d-484b-8cf4-c2c2dc414896.png">
<img src="https://user-images.githubusercontent.com/101961142/232358378-2220c004-802c-4029-bdd1-dfeaaf6c881d.png">

