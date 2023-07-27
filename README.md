<h1 align="center">Online Test Proctoring</h1>
    <h2>Introduction</h2>
    <p>The idea behind an online test proctoring model is to use technology to monitor and proctor online exams to prevent cheating and ensure academic integrity.For this we have used various functionality like face detection,face recognition,mobile phone detection,eye tracking for now.
    <h2>Features</h2>
	<ul>
		<li>Face Detection</li>
		<p>we have used MTCNN model for face detection which consists of three stages of convolutional networks that are able to recognize faces and landmark location such as eyes, nose, and mouth The 3 stages of MTCNN are P-Net, R-Net, O-Net. And with the help of this model we can detect faces and also detect if there is multiple faces which is not acceptable.</p>
		<li>Face Authentication</li>
		<p>We have used FaceNet for face recognition in oreder to know whether the person giving exam is the 
                   registered student or different .</p>
		<li>Eye Tracking</li>
		<p>Eye tracking in online test proctoring involves utilizing a camera or sensor to monitor the student's eye movements during the exam. It aims to detect suspicious behaviors, such as prolonged periods of looking away from the screen or constant gaze shifting. This process utilizes Convolutional Neural Networks (CNNs) with transfer learning on VGG16. The model is trained on a dataset specifically designed for eye detection. The top layers of VGG16 are removed, and the weights are frozen during this process. After training for 50 epochs on this dataset https://www.kaggle.com/datasets/kayvanshah/eye-dataset, we achieved following results:</p>
		<li>Smart Device Detection</li>
		<p> During Exam smart devices are not allowed,specially mobile phones. so, we trained a yolov5 model on 
                   custom dataset to detect phones easily and we got following results:
		   </p>
			
  | Class | Images | Instances |    P    |    R    | mAP50 | mAP50-95 |
|-------|--------|-----------|---------|---------|-------|----------|
| all   |     36 |        36 |    1    |   0.97  | 0.991 |   0.845  |

we got Precision 1 which indicates that model have almost 0 false positive  that is it will not detect phones if there is no phones along whith that we have also got 97% Recall which indicates that model have minimum false negative.
  <li><strong>Database:</strong> A database was maintained to store user information and exam data. It includes information about users who successfully submitted the test as well as those who were caught cheating during the test. This helps to track student progress and ensure the integrity of the testing process.</li>
</ul>
<h2>Enhancements</h2>
<p>There are several potential enhancements that could be made to our proctoring system:</p>
<ul>
  <li><strong>Improving accuracy:</strong> The models used in the system could be further trained and fine-tuned on larger datasets to improve their accuracy and performance.</li>
  <li><strong>Head movement detection:</strong> The addition of head movement detection could help to further prevent cheating by detecting when a user is looking away from the screen or otherwise moving their head in a way that suggests they may be attempting to cheat.</li>
</ul>
<p>By implementing these enhancements and continuing to refine the system over time, we believe that our proctoring system can become an even more effective tool for ensuring the integrity of online tests and exams.</p>
