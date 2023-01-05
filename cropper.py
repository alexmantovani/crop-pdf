import argparse
# import sys
import datetime

from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import (
    RectangleObject,
)


def rect_inset(page, offset):
    box = page.mediabox
    page.cropbox = RectangleObject(
        [box[0]+offset, box[1]+offset, box[2]-offset, box[3]-offset])
    return page


# if len(sys.argv) <= 1:
#     print('Argoomenti mancanti.\nUso: python3 cropper.py "<pdf file>" "<pdf file>" ...')
#     raise SystemExit(2)

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-f','--files', help='File or files to merge and crop', required=True, nargs='+')
parser.add_argument('-o','--output', help='Output file', required=False, default='result.pdf')
args = vars(parser.parse_args())

writer = PdfWriter()
# timestamp = int(datetime.datetime.now().timestamp())

for index, file_name in enumerate(args['files']):
    reader = PdfReader(file_name)

    for page in reader.pages:
        page.cropbox.upper_left = (0, 0)
        writer.add_page(rect_inset(page, 50))

    with open(args['output'], 'wb') as fp:
        print(f"Write file {args['output']}")
        writer.write(fp)
