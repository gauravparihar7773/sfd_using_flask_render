from flask import Flask,render_template,url_for,redirect,request
app=Flask(__name__)
import numpy as np
import cv2
import os
import base64
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage #yeh bahut jaruri h agar file upload karna and uspe kaam
# UPLOAD_FOLDER = os.path.basename('uploads')
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] =UPLOAD_FOLDER
from PIL import Image
from io import BytesIO
app_root = os.path.dirname(os.path.abspath(__file__))
# target = os.path.join(app_root, 'static/img/')

@app.route('/')
def home():
    # return 'hello this is <h2>gaurav</h2>'
    return render_template('index.html')



# location =os.getcwd()
# location1=os.path.join(location,'/static/uploads')
#  The mimetype for the request is 'application/x-www-form-urlencoded' instead of 'multipart/form-data' which means 
#  that no file contents were transmitted.
#   To fix this error you should provide enctype="multipart/form-data" in your form.

@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method == 'POST':

        file = request.files['file']
        # file_name = file.filename  line 36 se41 aapke file ko save kar lega
        # # destination = '/'.join([target, file_name])
        # destination='/'.join([UPLOAD_FOLDER,file_name])
        # file.save(destination)
        #ab image toh save ho gyi ek tariha toh yeh ki voh image save ho gyi usko vapis load karo cv2
        #par voh time consuming
        image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        image =func1(image)
        image_content = cv2.imencode('.jpg', image)[1].tostring()
        encoded_image = base64.encodebytes(image_content) #encodestring depreciated h ab
        to_send = 'data:image/jpg;base64, ' + str(encoded_image, 'utf-8')
        return render_template('show.html',result=to_send)

        # f = request.files['file']
        # f.save(secure_filename(f.filename))
        # return 'file uploaded successfully'

     

        # image = cv2.imdecode(np.fromstring(file1.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        # file1.save(file1.filename)
        # image = cv2.imdecode(np.fromstring(file1, np.uint8), cv2.IMREAD_UNCHANGED)
    #  imgdata = file1.split(',')[1]
    #  decoded = base64.b64decode(imgdata)
    

    # img = np.array(Image.open(BytesIO(decoded)))
    # file1=request.files['file1']  file storage type obsject byte nhi
    
    # image = cv2.imdecode(np.fromstring(file1, np.uint8), cv2.IMREAD_UNCHANGED)
    # image=file1.npasarray(file1) #yeh isliye nhi chalega kyunki file1 ek string object h
   
    # image=func1(img)
    # In memory
    # image_content = cv2.imencode('.jpg', image)[1].tostring()
    # encoded_image = base64.encodestring(image_content)
    # to_send = 'data:image/jpg;base64, ' + str(encoded_image, 'utf-8')

  

    #mujhe yeh image dikhani h mein ek variable me dikha sakta hun mein index.html me ek variable bana dunga

def func1(img): #image deta hun as an array 
    # original_image4=cv2.imread(img) #ye nhi chalega
    original_image4=np.array(img)
    original_image4= cv2.resize(img, (256, 256))
   
    gray_img4=cv2.cvtColor(original_image4,cv2.COLOR_BGR2GRAY)
    # face_detector=cv2.CascadeClassifier('face_detector.xml') 
    face_detector=cv2.CascadeClassifier('C:/Users/Admin/OneDrive/Desktop/project/v1/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    faces=face_detector.detectMultiScale(gray_img4,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces:
        cv2.rectangle(original_image4,(x,y),(x+w,y+h),(0,255,0),2)
    # cv2.imshow(img,original_image4) #imshow do arguments leta hi h
    # cv2.waitKey(0)
    # cv2.destroyAllWindows() in teeno se kaam nhi chalega 
    # original_image4= Image.fromarray(original_image4) #
    return original_image4



if __name__ == '__main__':
    app.run(debug=True)