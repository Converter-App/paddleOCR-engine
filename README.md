Minimal PaddleOCR engine example provided by [Converter App](https://converter.app/).

The recommended Python version is Python 3.8.

Install the requirements with:

	pip3  install  -r 'requirements.txt'
 
Then you can run the OCR engine with the command:

	python ocr_engine.py --language en --output result.txt --image_path example.jpg   

It will print the detected text together with its bounding box and also
visualize the bounding boxes on top of the initial image.

The required training models will be downloaded automatically
once needed. Alternatively, you can also put the .paddleocr
folder in your home directory which contains all models
for running this example right away.

No warranty of any kind.
