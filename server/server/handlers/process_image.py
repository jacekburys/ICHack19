from flask import Blueprint, send_file, json, jsonify, request, Response
from flask import make_response
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
import dlib
import sys
import os

curr_dir = os.path.dirname(os.path.realpath(__file__))

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(curr_dir + '/shape_predictor_68_face_landmarks.dat')

def process_image_aux(img, coeff):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  #img = smile(img, coeff)
  return img

#######################################################################

mod = Blueprint('process_image', __name__)

@mod.route("/processimage", methods=['POST'])
def process_image():
  print('got processimage request')
  if 'my_file' in request.files:
    photo = request.files['my_file']
    in_memory_file = BytesIO()
    photo.save(in_memory_file)
    data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
    color_image_flag = 1
    coeff = 0.8
    if 'emotion' in request.headers:
      if request.headers.get('emotion') == 'sad':
        coeff = -coeff
      elif request.headers.get('emotion') == 'vsad':
        coeff = -2 * coeff
      elif request.headers.get('emotion') == 'vhappy':
        coeff = 2 * coeff
    img = cv2.imdecode(data, color_image_flag)
    img = process_image_aux(img, coeff)
    print('processed image')
    img = Image.fromarray(img)
    out_memory_file = BytesIO()
    img.save(out_memory_file, format='jpeg')
    out_memory_file.seek(0)
    response = make_response(send_file(out_memory_file, mimetype='image/jpeg', attachment_filename='test_image.jpeg'))
    content_length = len(out_memory_file.getvalue())
    print(content_length)
    response.headers.add('content-length', str(content_length))
    return response

  # send black image
  data = np.zeros((100, 100, 3), dtype=np.uint8)
  f = BytesIO()
  np.save(f, data)
  im = Image.fromarray(data)
  im.convert('RGB')
  im.save('server/test_image.jpeg')
  return send_file('test_image.jpeg', mimetype='image/jpeg', attachment_filename='test_image.jpeg')
