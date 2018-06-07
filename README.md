# Project Script

Programs for scrapping, cleaning and then building the model.


This repo consists of programs to scrap data from sites , clean that data and models based on them.
Slideshare API's are also used to scrap information regarding slides and to download pdf files.

For using Slideshare API's,
check this link
 
https://www.slideshare.net/developers

Sites used are : quotes.toscrape.com
               : nith.ac.in
               : glassdoor.com
               : slideshare.com
               : toptal.com
               : talentlyft.com
               : resources.workable.com
API's used : Slideshare

Scrapy module is used to scrap data.

Request module is used in case of scrapping with slideshare API's.

Json file is maintained for storing data and reading data from.

In case of pages with Javascript, scrapy-splash module is used.

Scripts in extra folder are used to download pdf files from nith.ac.in site.

Nltk, string module is used for cleaning data.

To extract text from pdfs, two modules are used.
1. PyPDF2
2. pdfminer

To study about pdfminer, check the following links --

1. https://www.unixuser.org/~euske/python/pdfminer/programming.html
2. https://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa


clean_data folder is there to preprocess the data collected before feeding it to the models.
Cleaning and preprocessing is necessary to get better results and overfitting is not there.

Models --
1. Multinomial Naive Bayes Classifier

....... more are coming :)




