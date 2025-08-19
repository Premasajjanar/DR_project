🧠 Project: Retinal Blindness (Diabetic Retinopathy) Detection
📌 Problem Statement
Diabetic Retinopathy (DR) is a leading cause of blindness among the working-age population. With increasing diabetes cases, the risk of severe vision loss is becoming more widespread.

Early detection can significantly reduce the chances of permanent damage. However, manual diagnosis is time-consuming and resource-intensive. To tackle this, I worked on automating the detection of DR using deep learning techniques.

📂 Dataset
 [APOTS Kaggle Blindness dataset](https://www.kaggle.com/c/aptos2019-blindness-detection)
I used the APTOS 2019 Blindness Detection Dataset from Kaggle, which contains high-quality retinal images labeled by DR severity.

💡 Solution
I developed an image classification system using ResNet152, a deep convolutional neural network pretrained on ImageNet. The model predicts the severity level of DR based on retinal images:

0 – No DR

1 – Mild DR

2 – Moderate DR

3 – Severe DR

4 – Proliferative DR

Along with the model, I also built a desktop GUI using Tkinter, and used HeidiSQL for managing predictions and patient-related data in a MySQL database.

(Note: Patient information such as name and ID is sensitive. Addressing data privacy risks is part of my future plan.)

⚙️ Tech Stack
# Summary of Technologies used in this project :       
| Dev Env. | Framework/ library/ languages |
| ------------- | ------------- |
| Backend development  | PyTorch (Deep learning framework) |
| Frontend development | Tkinter (Python GUI toolkit) |
| Database connectivity | HeidiSQL (MySQL server) |
| Programming Languages | Python, SQL |
| API | Twilio cloud API| 

📊 Visualizations
🔹 Sample Input Image
![visual1](images/visual1.JPG)

🔹 ResNet152 Architecture Overview
I have only shown below the main layers of resnet and each of the 'layer1', 'layer2', 'layer3' and 'layer4' contains various more layers.      

![mat](images/mat.png)


Here are some snapshots of the GUI I developed:

![gui1](c:\Users\prema\OneDrive\Pictures\Screenshots\Screenshot 2024-12-15 194924.png)  
![gui2](c:\Users\prema\OneDrive\Pictures\Screenshots\Screenshot 2024-12-15 194948.png)  
![gui3](c:\Users\prema\OneDrive\Pictures\Screenshots\Screenshot 2024-12-15 194957.png)
![gui4](c:\Users\prema\OneDrive\Pictures\Screenshots\Screenshot 2024-12-15 195025.png)
![gui5](c:\Users\prema\OneDrive\Pictures\Screenshots\Screenshot 2024-12-15 195040.png)
![gui6](c:\Users\prema\OneDrive\Pictures\Screenshots\Screenshot 2024-12-08 154926.png)

🚀 Getting Started
Want to run this project locally?
👉 Click here to view setup instructions

🧭 Project Navigation
🧠 Model Training Code["G:\My Drive\DR_Project\Copy of training.ipynb"]

🔍 Single Image Inference["C:\Users\prema\OneDrive\Desktop\Project\Retinal_blindness_detection\Single_test_inference.ipynb"]

🖥️ GUI Script["C:\Users\prema\OneDrive\Desktop\Project\Retinal_blindness_detection\blindness.py"]

🧩 Model Loader Script["C:\Users\prema\OneDrive\Desktop\Project\Retinal_blindness_detection\model.py"]

💾 Pretrained Weights / Setup Guide

📌 Note: I trained the model for 100+ epochs to achieve ~97% accuracy. To save time and resources, only the final version and weights are shared.

🌱 Future Plans
🌐 Convert the desktop app into a lightweight WebApp

🔒 Incorporate Privacy-Preserving Techniques:

Federated Learning

Differential Privacy

Secure Multi-party Computation

👉 Check out my federated learning project here

⚙️ Add MySQL concurrency control for safe multi-user access

❗ Reduce Type-II Errors (False Negatives), which are critical in healthcare predictions

⭐ Like this project?
If you found it helpful or interesting, feel free to ⭐ it!