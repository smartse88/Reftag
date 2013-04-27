import unittest
from splinter import Browser 

site = "http://localhost:8080/"

browser = Browser()
def tearDownModule():
    browser.quit()

class TestArticleExists(unittest.TestCase):
    subsite = site + "wparticleexists.py"
    def test_exists(self):
        url = self.subsite + "?title=Africa"
        browser.visit(url) 
        self.assertTrue(browser.is_text_present('1'))
        self.assertFalse(browser.is_text_present('0'))

    def test_no_exists(self):
        url = self.subsite + "?title=UyUgyuygsdfuyggyu34t6js"
        browser.visit(url) 
        self.assertTrue(browser.is_text_present('0'))
        self.assertFalse(browser.is_text_present('1'))

    def test_no_title(self):
        url = self.subsite
        browser.visit(url) 
        self.assertFalse(browser.is_text_present('0'))
        self.assertFalse(browser.is_text_present('1'))
        self.assertTrue(browser.is_text_present('No title specified'))

class TestNytWeb(unittest.TestCase):
    subsite = site + "nytweb.py"
    def test_start(self):
        browser.visit(self.subsite)
        self.assertTrue(browser.is_text_present('New York Times Wikipedia reference generator'))
    
    def test_example(self):
        browser.visit(self.subsite + "?url=http%3A%2F%2Fwww.nytimes.com%2F2009%2F03%2F26%2Fgarden%2F26slow.html") 
        self.assertTrue(browser.is_text_present('cite news|last=Kurutz'))

    def test_flow(self):
        browser.visit(self.subsite)
        browser.fill('url', 'http://www.nytimes.com/2009/03/26/garden/26slow.html')
        browser.find_by_value('Load').click()
        self.assertTrue(browser.is_text_present('cite news|last=Kurutz'))

class TestDoiWeb(unittest.TestCase):
    subsite = site + "doiweb.py"
    def test_start(self):
        browser.visit(self.subsite)
        self.assertTrue(browser.is_text_present('DOI Wikipedia reference generator'))
    
    def test_example(self):
        browser.visit(self.subsite + "?doi=10.1111%2Fj.1600-0404.1986.tb04634.x")
        self.assertTrue(browser.is_text_present('title=Survival and cause'))

    def test_flow(self):
        browser.visit(self.subsite)
        browser.fill('doi', '10.1111/j.1600-0404.1986.tb04634.x')
        browser.find_by_value('Load').click()
        self.assertTrue(browser.is_text_present('title=Survival and cause'))
                



if __name__ == '__main__':
    unittest.main()
