# Ticapsoriginal site wide full text extract
Ticapsoriginal make text file with all text content of large website from large sitemap ( preparing data for nltk analysis ) 

* large sitemaps available
* detect paragraphs, titles and strong texts 

# make python environment:
* Install pip first:
<pre><code>sudo apt-get install python3-pip
</code></pre>
* Then install virtualenv using pip3
<pre><code>sudo pip3 install virtualenv 
</code></pre>
* Now create a virtual environment
<pre><code>virtualenv venv
</code></pre>
* Active your virtual environment:
<pre><code>source venv/bin/activate
</code></pre>
* Enter on environment:
<pre><code>cd venv
</code></pre>

## Install tqdm to see progress bar: 
<pre><code>pip install tqdm
</code></pre>

## Install resquests to get responses: 
<pre><code>pip install requests
</code></pre>

## Install beautifull soap to read web content data: 
<pre><code>pip install bs4
</code></pre>

## Install advertools to read large url data: 
<pre><code>pip install advertools
</code></pre>

## Clone Ticapsoriginal site wide full text extract:
<pre><code> git clone https://github.com/Tinoco/Ticapsoriginal_site_wide_reading_time.git
</code></pre>

* Change the largesitetextextract.py file with your sitemap url 

## Start scanning and calculating:
<pre><code>python largesitetextextract.py
</code></pre>

## quality:
* [`100% pycodestyle coverage`](https://pypi.org/project/pycodestyle/)

* [`0% code plagiarism detected`](https://github.com/blingenf/copydetect)

## about:
* code and resource used in [`Ticapsoriginal`](https://ticapsoriginal.com)
