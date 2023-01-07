# PDF MERGER AND CROPPER

cropper.py is a free and open-source python utility capable of crop and merge PDF files.

# Installation

```
$ pip3 install -r requirements.txt
```

# Usage

```
$ cropper.py [-h] -f FILES [FILES ...] [-o OUTPUT] [-c CROP] [--no_swift_scan]
```

examples:

```
$ python3 cropper.py -f part_1.pdf part_2.pdf -c 50 -o merged.pdf
$ python3 cropper.py -f part_1.pdf -o merged.pdf --no_swift_scan
```
