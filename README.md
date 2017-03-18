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
* Trivial face-detection

**Requirements**
* scrapy
* image

*Both can installed via pip*

**Customization**
* Changing file store for scrapy.
    - Go to *settings.py*
    - Change the FILES_STORE at the bottom of the file to the desired value.
* Reference for custom settings can be found here.
    - https://doc.scrapy.org/en/latest/topics/settings.html#project-settings-module

##Ameblo
**Per entry**
scrapy crawl **ameblo** -a name=*name* -a entry=*entrynumber*
* ameblo (*required*) - images will be fetched from http://ameblo.jp
* name (*required*) - name of the blog where images will be fetched from
* entrynumber (*required*) - entry number which can be extracted from links
*Example:* http://ameblo.jp/someblog/entry-*entrynumber*.html

./ameblo.sh **name** **entrynumber**

**Bulk**
scrapy crawl **ameblo** -a **first**=*first page* -a **last**=*last_page* -a **name**=*blog* -o *output file*

* ameblo (*required*) - images will be fetched from http://ameblo.jp
* name (*required*) - name of the blog where images will be fetched from
* first (*optional*) - first page where images are fetched
* last (*optional*) - last page where images are fetched
* o (*optional*) - output file where logs are kept

./ameblo.sh **name** **first** **last**

##Tumblr
scrapy crawl **tumblr** -a **first**=*first page* -a **last**=*last_page* -a **name**=*blog* -o *output file*

* ameblo (*required*) - images will be fetched from http://ameblo.jp
* name (*required*) - name of the blog where images will be fetched from
* first (*optional*) - first page where images are fetched
* last (*optional*) - last page where images are fetched
* o (*optional*) - output file where logs are kept

./tumblr.sh **name** **first** **last**

##Lineblog
scrapy crawl **lineblog** -a **first**=*first page* -a **last**=*last_page* -a **name**=*blog* -o *output file*

* ameblo (*required*) - images will be fetched from http://ameblo.jp
* name (*required*) - name of the blog where images will be fetched from
* first (*optional*) - first page where images are fetched
* last (*optional*) - last page where images are fetched
* o (*optional*) - output file where logs are kept

./lineblog.sh **name** **first** **last**

##Other Links
scrapy crawl **single** -a **link**=*url*

##Shortcuts
Scripts are added under the script folder which are basically shortcuts to the syntax, without the need for typing arguments yourself.

##Reference
-------------
* [Scraping images with Python and Scrapy] (http://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/)
* [Spiders] (https://doc.scrapy.org/en/latest/topics/spiders.html)
* [Downloading and processing files and images] (https://doc.scrapy.org/en/latest/topics/media-pipeline.html)

