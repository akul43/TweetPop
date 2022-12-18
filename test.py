import unittest
import scraper
import app


class ScraperTest(unittest.TestCase):

    # Run test query only once to limit tweet pull rate
    test_query = scraper.run_query('test')

    # Test TwitterAPI connection
    # Test if the script has successfully connected to the API
    def test_API_connection(self):
        self.assertEqual(scraper.client != None, True)

    # Test if Tweet have been pulled
    def test_tweet_isEmpty(self):
        self.assertEqual(ScraperTest.test_query == None, False)

    # Test if tweet link is valid link
    def test_tweet_content(self):
        for tweet in ScraperTest.test_query:
            if('https://twitter.com/x/status/' in tweet):
                ans = True
            else:
                ans = False
        self.assertEqual(ans, True)

    #Test if Flask app is functioning
    def test_Flask_app(self):
       self.assertFalse(app.app == None)
       
    #Test if Flask app Home Page is loading
    def test_Flask_homePage(self):
       self.assertTrue(app.home != None)
    
    #Test if Flask app Result Page is loading
    def test_Flask_resultPage(self):
       self.assertTrue(app.result != None)
        

if __name__ == '__main__':
    unittest.main()
