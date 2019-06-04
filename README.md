# get-mobi-cover-image

This is a Python script that gets the cover image from ebooks in the `.mobi` format.

![An arrow from a blank document to a yellowing book cover](README_illustration.jpg)

Book cover: *Captain Billy's Whiz Bang*, from [Project Gutenberg](https://www.gutenberg.org/ebooks/59664).



## Installation

Clone or download this repository:

```console
$ git clone https://github.com/alexwlchan/get-mobi-cover-image.git
```

You also need to [install Python](https://www.python.org/).
I've tested the script with Python 2.7 and 3.6.



## Usage

Run the script `get_mobi_cover.py`, passing the path to the MOBI file you want a thumbnail for.
It saves the thumbnail to the current directory, and prints the name of the thumbnail file:

```console
$ python get_mobi_cover.py pg59664-images.mobi
cover-41bFd.jpeg
```



## License

GPL v3.
