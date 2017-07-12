import predict_flower_service as pd
import digit_prediction_service as dpd
import convert_images_to_json as cv
import digit_image_to_json as dcv
import util
import os

def predict_flower(image_file_path):
    print
    print ("Predicting Flower...")
    print
    cv.make_request_json(image_file_path, 'request.json', False)
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

def get_flower(category):
    params = util.get_flower_params()
    return params[str(category)]

def main():
    predict_flower('0.jpg')

if __name__ == '__main__':
  main()
