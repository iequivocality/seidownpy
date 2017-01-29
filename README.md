SeidownPy
=============
An application that will download images from selected seiyuu website.
Built-on top of Scrapy, a Python based web scrapping framework.

**Support**
* [ameblo](http://ameblo.jp)
* [tumblr](https://tumblr.com)
* [lineblog](http://lineblog.me/)
* [single] - any link
* [Other links]

**Future Support**
* Other sites such as [lineblog](http://lineblog.me) and stand-alone pages.
* Trivial face-detection

**Requirements**
* scrapy
* image

*Both can installed via pip*

**Customization**
* Changing file store for scrapy.
    - Go to *settings.py*
    - Change the FILES_STORE at the bottom of the file to the desired value.

##Ameblo
scrapy crawl **ameblo** -a **first**=*first page* -a **last**=*last_page* -a **name**=*blog* -o *output file*

* ameblo (*required*) - images will be fetched from http://ameblo.jp
* name (*required*) - name of the blog where images will be fetched from
* first (*optional*) - first page where images are fetched
* last (*optional*) - last page where images are fetched
* o (*optional*) - output file where logs are kept

##Tumblr
scrapy crawl **tumblr** -a **first**=*first page* -a **last**=*last_page* -a **name**=*blog* -o *output file*

* ameblo (*required*) - images will be fetched from http://ameblo.jp
* name (*required*) - name of the blog where images will be fetched from
* first (*optional*) - first page where images are fetched
* last (*optional*) - last page where images are fetched
* o (*optional*) - output file where logs are kept

##Lineblog
scrapy crawl **lineblog** -a **first**=*first page* -a **last**=*last_page* -a **name**=*blog* -o *output file*

* ameblo (*required*) - images will be fetched from http://ameblo.jp
* name (*required*) - name of the blog where images will be fetched from
* first (*optional*) - first page where images are fetched
* last (*optional*) - last page where images are fetched
* o (*optional*) - output file where logs are kept

##Other Links
scrapy crawl **single** -a **link**=*url*

##Reference
-------------
* [Scraping images with Python and Scrapy] (http://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/)
* [Spiders] (https://doc.scrapy.org/en/latest/topics/spiders.html)
* [Downloading and processing files and images] (https://doc.scrapy.org/en/latest/topics/media-pipeline.html)

