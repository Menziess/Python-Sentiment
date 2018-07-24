
import tensorflow as tf
import sys
import os
import numpy as np

# Disabling tensorflow logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def main(args):

	if (len(args) < 2):
		print("Please provide the model path and your input string.")
		sys.exit()

	model_path = args[0]
	input_string = args[1]
	dirname = os.path.dirname(__file__)
	relative_model_path = os.path.join(dirname, model_path)

	# Restoring the model
	print("Trying to find the model...")
	predict_fn = tf.contrib.predictor.from_saved_model(relative_model_path)

	# Make a prediction with the restored model
	print("Making prediction...")
	predictions = predict_fn({"inputs": [input_string]})

	# Retrieve index of highest score corresponding with class
	highest_score_index = np.argmax(predictions['scores'])
	highest_score = np.max(predictions['scores'])
	rating = predictions['classes'][0][highest_score_index].decode("utf-8")

	print('scores: ', predictions['scores'])
	print('Star rating for this review: (',
				rating,
				') having score: ',
				highest_score)


if __name__ == '__main__':
	main(sys.argv[1:])
