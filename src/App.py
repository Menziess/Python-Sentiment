
import tensorflow as tf
import sys
import os
import numpy as np
from flask import Flask, abort, jsonify, request

MODEL_PATH = '../models/model'

# Disabling tensorflow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if not os.path.exists(SAVE_MODEL_PATH):
	print("The model folder is empty:", SAVE_MODEL_PATH)
	sys.exit()

# Load estimator
dirname = os.path.dirname(__file__)
relative_model_path = os.path.join(dirname, MODEL_PATH)
predict_fn = tf.contrib.predictor.from_saved_model(relative_model_path)

app = Flask(__name__)

@app.route('/')
def make_home():
	return jsonify({
		'info': "Enter your review behind the '/' in the url bar",
		'review': "",
		'stars': "",
		'certainty': "",
	})

@app.route('/<review>')
def make_predict(review):

	predictions = predict_fn({"inputs": [review]})
	score_index = np.argmax(predictions['scores'])
	certainty = np.max(predictions['scores']) * 100
	stars = predictions['classes'][0][score_index].decode("utf-8")

	return jsonify({
		'review': review,
		'stars': stars,
		'certainty': "{}%".format(certainty),
	})

if __name__ == '__main__':
	app.run(port = 9000, debug = True)
