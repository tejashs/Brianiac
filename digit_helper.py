import digit_prediction_service as dpd
import digit_image_to_json as conv
import util
import os

def predict_digit(image_file_path):
    print
    print ("Predicting...")
    print
    conv.make_request_json(image_file_path, 'request.json')
    predictions = dpd.predict('request.json')
    category = predictions[0]['classes']
    os.remove('request.json')
    return category
