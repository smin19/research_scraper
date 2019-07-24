from googlesearch import search  # grabs URLs from google query
from newspaper import Article    # very flexible library for getting all kinds of data from a source
from newspaper import Config
import nltk                      # NLTK for performing various natural language processing operations



"""
a quick way to compile all sources related to a google search and extract data without
ever having to click on the link. you could search for a person or a company 
they are involved in and easily collect a volume of sources for background research.

sources:
Eric D. Brown, D.Sc.
https://pythondata.com/quick-tip-consuming-google-search-results-to-use-for-web-scraping/
Super cool site

Mario Vilas' Google search library
https://github.com/MarioVilas/googlesearch

"""

sources = []

for url in search('Computer History Museum', tld='com', stop=25):
    sources.append(url)
    
    
# occasionally running into issues (403 access error), so this is an attempt to change the user_agent and 
# hopefully bypass.
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent


# using a try/pass block ONLY because certain sites can't be accessed from this method. Usually this
# is poor (very poor) practice, but this is a small script and this 403 error is the only real potential error.
# Definitely make the except more specific in case I decide to add more features later. 
for link in sources:
    try:
        article = Article(link)
        article.download()
        article.parse()
        article.nlp()
        print(link)
        print(article.summary)
        print("\n")

    except:
        print(link)
        print('access blocked, check link manually')
        print("\n")
        pass
    
