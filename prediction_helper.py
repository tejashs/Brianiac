import predict_flower_service as pd
import convert_images_to_json as cv
import util
import os

def predict_flower(image_file_path):
    print
    print ("Predicting...")
    print
    cv.make_request_json(image_file_path, 'request.json', False)
    predictions = pd.predict('request.json')
    category = predictions[0]['prediction']
    flower_type = get_flower(category)
    os.remove('request.json')
    return flower_type

def get_flower(category):
    params = util.get_flower_params()
    return params[str(category)]

def main():
    predict_flower('0.jpg')

if __name__ == '__main__':
  main()
