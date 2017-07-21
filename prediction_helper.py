import predict_flower_service as pd
import digit_prediction_service as dpd
import convert_images_to_json as cv
import digit_image_to_json as dcv
import util
import os
import pyhdb as db

def predict_flower(image_file_path, isLocal):
    #isLocal = 1 if local file, 0 if http path
    print
    print ("Predicting Flower...")
    print
    cv.make_request_json(image_file_path, 'request.json', False, isLocal)
    predictions = pd.predict('request.json')
    category = predictions[0]['prediction']
    flower_type = get_flower(category)
    os.remove('request.json')
    return flower_type

def predict_digit(image_file_path):
    print
    print ("Predicting Number...")
    print
    dcv.make_request_json(image_file_path, 'request.json')
    predictions = dpd.predict('request.json')
    category = predictions[0]['classes']
    os.remove('request.json')
    return category

def getConnection():
    hostname = '35.185.245.114'
    host_port = '39015'
    username = 'SYSTEM'
    u_password = 'HANAhxe2'
    myConnection = db.connect(
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

def readDataFromSAPHana(flower_id):
    connection = getConnection()
    flower_schema = "ODATASERVICES"
    flower_table = "FLOWERS"

    if not connection.isconnected():
        return 'HANA Server not accessible'
    #Connect to the database

    cursor = connection.cursor()
    #This is the data used to Train the Tensor Flow model
    sql = "SELECT * FROM " + flower_schema + "." + flower_table + " WHERE ID = " + str(flower_id)
    cursor.execute(sql)
    myData = cursor.fetchall()
    cursor.close()
    return myData[0]

def get_flower(category):
    result = readDataFromSAPHana(category)
    # params = util.get_flower_params()
    # result = params[str(category)]
    return result

def main():
    f = predict_flower('flower.jpg', 1)
    print f

if __name__ == '__main__':
  main()
