## Installation :     
Tip : Make sure to install [Numpy](https://pypi.org/project/numpy/), [Pandas](https://pypi.org/project/pandas/), [Matplotlib](https://pypi.org/project/matplotlib/) first and then proceed next.     
* [Torch package](https://pytorch.org/get-started/locally/)    
* [Tkinter](https://tkdocs.com/tutorial/install.html)     
* [HeidiSQL](https://www.heidisql.com/download.php)          
Grab a cup of coffee as these will take some time !   
* [click here](https://support.hypernode.com/knowledgebase/use-heidisql/#Download_HeidiSQL) to start server in HeidiSQL and configure settings by setting username and password.    
## Get, set and go :    
* Download complete Project files using following command from git bash/ cmd (terminal):     
```
git clone https://github.com/souravs17031999/Retinal_blindness_detection_Pytorch   

```   
[Note you need mainly these four things to get started :]    
> [blindness.py]("G:\My Drive\DR_Project\blindness.py")
> [model.py]("G:\My Drive\DR_Project\dr_model.py")
> [classifier.pt](#)
  

* Create a new database and table accordingly.    
* Then, Go to 'blindness.py' file and change some configuration settings according to your database.
```
connection = sk.connect(
    host="localhost",
    user="root",
    password="********",
    database="********"
)
```
* Now, your DB server must be connected.   
* Finally, you also want 'classifier.pt' file which contains model's dictionary required when it is to be loaded.    
[Download here](https://www.kaggle.com/souravs17031999/blindness-detection-pretrained-weights-pytorch) and put that file in the same directory and then modify the path accordingly in the 'model.py' file.
```
model = load_model('../Desktop/classifier.pt')

```
* Finally, execute your 'blindness.py' file and your GUI must start (recommended to start this from your terminal and keep all your project files in same directory).   
* Upload the image and get your predictions.




[Note : You can use sample images in the folder [sampleimages]("G:\My Drive\DR_Project\sampleimages") which is taken from the original test dataset to test the system]
