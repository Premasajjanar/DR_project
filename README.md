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
![Image](https://github.com/user-attachments/assets/29e8fd00-4f0c-4382-a3fb-ca939085a14a)

🔹 ResNet152 Architecture Overview
I have only shown below the main layers of resnet and each of the 'layer1', 'layer2', 'layer3' and 'layer4' contains various more layers.      

![Image](https://github.com/user-attachments/assets/26b23101-805f-449e-8d94-895b6aa14041)


Here are some snapshots of the GUI I developed:

![Image](https://github.com/user-attachments/assets/237e28d7-6d08-4524-9f58-7a4e33bb10f0)
![Image](https://github.com/user-attachments/assets/2da1545f-af86-4148-bb41-160576295b57)
![Image](https://github.com/user-attachments/assets/da0d089d-9f43-434b-b05e-338abf67bc18)
![Image](https://github.com/user-attachments/assets/48a0b906-4a73-4ae1-97a2-41be837621dc)
![Image](https://github.com/user-attachments/assets/e071310b-8a4c-4ff9-a5b5-8b3aa511729d)
![Image](https://github.com/user-attachments/assets/cac80d3b-514f-423a-add1-f09866f0ec9f)

🚀 Getting Started
Want to run this project locally?
👉 [Click here to view setup instructions](./gettingstarted.md)

🧭 Project Navigation
🧠 Model Training Code[Training Notebook](./Copy%20of/training.ipynb)


🔍 Single Image Inference[Open Single_test_inference.ipynb](./Single_test_inference.ipynb)


🖥️ GUI Script[View blindness.py](./blindness.py)


🧩 Model Loader Script[View model.py script](./model.py)


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
