from flask import Flask, render_template, request
from flask import session
import requests
from datetime import datetime as dt
import pyhdb
import util
from google.cloud import storage
import os
import prediction_helper as pdh
import digit_helper as dph

class Brainiac(Flask):
    def __init__(self, import_name):
        super(Brainiac, self).__init__(import_name)



app = Brainiac(__name__)

CLOUD_STORAGE_BUCKET = "flaskapp-bucket-flowers"

@app.route('/predict/number', methods=['POST'])
def upload_number():
    message = 'Number Image Prediction Invoked!'
    if request:
        name = 'tempImages/numbers/number_' + str(dt.now()) + '.jpg'
        uploaded_file = request.files['digitImage']
        url = upload_to_cloud_storage(uploaded_file, name)
        number_out = predict_number(url)
        print number_out
        delete_blob(CLOUD_STORAGE_BUCKET, name)

    return render_template('upload_success.html', message=message, object='Number', result=number_out)

@app.route('/predict/flower', methods=['POST'])
def upload_flower():
    message = 'Flower Image Prediction Invoked!'
    if request:
        name = 'tempImages/flowers/flower_' + str(dt.now()) + '.jpg'
        uploaded_file = request.files['flowerImage']
        url = upload_to_cloud_storage(uploaded_file, name)
        flower_type = predict_flower(url)

        delete_blob(CLOUD_STORAGE_BUCKET, name)

    return render_template('upload_success.html', message=message, object='Flower', result=flower_type)


def predict_number(filePath):
    print('Should Predict Number\n')
    result = dph.predict_digit(filePath)
    return result

def predict_flower(filePath):
    print('Predicting Flower\n')
    result = pdh.predict_flower(filePath)
    return result

def connectToHana():
    print("Fetch Data from HANA\n")

def getConnection():
    params = util.getParamsFromFile(None)
    print(params)
    return
    hostname = params[util.HOSTNAME]
    host_port = params[util.PORT]
    username = params[util.USER]
    u_password = params[util.PASSWORD]
    myConnection = pyhdb.connect(
          # replace with the ip address of your HXE Host (This may be a virtual machine)
          host=hostname,
          # 39013 is the systemDB port for HXE on the default instance of 90.
          # Replace 90 with your instance number as needed (e.g. 30013 for instance 00)
          port=int(host_port),
          #Replace user and password with your user and password.
          user=username,
          password=u_password
          )
    return myConnection

def upload_to_cloud_storage(uploaded_file, filename):
    gcs = storage.Client()
    bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)
    blob = bucket.blob(filename)
    blob.upload_from_string(
        uploaded_file.read(),
        content_type=uploaded_file.content_type
    )
    return blob.public_url

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()


if __name__ == '__main__':
    app.run()
