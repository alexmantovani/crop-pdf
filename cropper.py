#!/usr/bin/env python3

import argparse

from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import (
    RectangleObject,
)


def rect_inset(page, offset):
    box = page.mediabox
    page.cropbox = RectangleObject(
        [box[0]+offset, box[1]+offset, box[2]-offset, box[3]-offset])
    return page


parser = argparse.ArgumentParser(description='An utility to merge and crop your PDF files')
parser.add_argument('-f','--files', help='File or files to merge and crop', required=True, nargs='+')
parser.add_argument('-o','--output', help='Output file', required=False, default='result.pdf')
parser.add_argument('-c','--crop', help='Crop size (0 = no crop)', required=False, default='50', type=int)
# parser.add_argument('-no_ss','--no_swift_scan', help='Remove SwiftScan edge', required=False, action='no_swift_scan')
parser.add_argument('--no_swift_scan', action=argparse.BooleanOptionalAction)
args = vars(parser.parse_args())
print(args)

crop = args['crop']
if args['no_swift_scan'] is True:
    crop = 50

writer = PdfWriter()

for file_name in args['files']:
    reader = PdfReader(file_name)

    for page in reader.pages:
        # page.cropbox.upper_left = (0, 0)
        writer.add_page(rect_inset(page, crop))

    with open(args['output'], 'wb') as fp:
        print(f"Write file {args['output']}")
        writer.write(fp)
