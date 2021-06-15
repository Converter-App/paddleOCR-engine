#!/usr/bin/env python3

"""
PaddleOCR engine example provided by https://converter.app/.
   
You can run the OCR engine with the command:

python ocr_engine.py --language en --output result.txt --image_path example.jpg   

It will print the detected text together with its bounding box and also
visualize the bounding boxes on top of the initial image.

No warranty of any kind.
"""


from paddleocr import PaddleOCR, draw_ocr
import time
import argparse
import re
from PIL import Image

# argument parser initialization
parser = argparse.ArgumentParser(description='get input data')
parser.add_argument("--image_path", default="example.jpg")
parser.add_argument("--language", default='en')
parser.add_argument("--output", default="result.txt")
parser.add_argument("--boxes", default="boxes.txt")
parser.add_argument('--visualize', dest='visualize', action='store_true')
parser.set_defaults(visualize=False)

def post_process_box(box_text):

    # adds space before capital letters
    capital_corrected = re.sub(r'(\w)([A-Z])', r'\1 \2', str(box_text))
    
    # adds white-space after white-space
    punctuation_corrected = re.sub(r'([.:,!;?])([^\s])', r'\1 \2', str(capital_corrected))
    return punctuation_corrected

if __name__ == "__main__":

    # parse command line arguments
    args = parser.parse_args()

    # create output files
    output_file = open(args.output, "w", encoding="utf-8")
    box_file = open(args.boxes, "w", encoding="utf-8")
    
    language = args.language

    # record the start time for benchmark 
    t1 = time.time()

    # set the language by modifying the lang parameter
    # The model file will be downloaded automatically when executed for the first time if not available
    ocr_loaded_object = PaddleOCR(lang=language)

    # get result from paddle OCR
    result = ocr_loaded_object.ocr(args.image_path)

    # write result into files
    print("\n-------------------------------------------")
    for each_box in result:

        detected_text = post_process_box(each_box[1][0])
        print(detected_text)
        output_file.write(detected_text+'\n')
        box_file.write(detected_text + " " + str(each_box[0]) + '\n')

    # end time for  benchmark 
    t2 = time.time()

    # visualization of the boxes
    if args.visualize==True:
        image = Image.open(args.image_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores,
                       font_path='font/Roboto-Black.ttf')
        im_show = Image.fromarray(im_show)
        im_show.show()
        im_show.save('result.jpg')
  
    # close output files
    output_file.close()
    box_file.close()

    print("\n-------------------------------------------")
    print("Total processing time: ", t2-t1)
