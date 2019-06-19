import webapp2
import jinja2
import os
import random

jinjaEnv = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

namesDict = {}

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(jinjaEnv.get_template("templates/welcome.html").render())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(jinjaEnv.get_template("templates/main.html").render())

class GenerateHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("/Main")
        
    def post(self): ##change most "" to actual name of input
        global namesDict
        i = 0
        while True: #get all the names and age input
            try:
                namesDict.update({self.response.get("" + i): self.response.get("" + i)})
            except:
                self.redirect("/Main")
                break
            i += 1
        randValue = random.randint(0, len(namesDict)) #select random value for indexing
        namesDictSingle = {"" + randValue: namesDict["" + randValue]} #saves the indexed element to namesDictSingle
        self.response.write(jinjaEnv.get_template("templates/generate.html").render(namesDictSingle))

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(jinjaEnv.get_template("templates/aboutus.html").render())

class FeedbackHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(jinjaEnv.get_template("templates/feedback.html").render())

class FAQsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(jinjaEnv.get_template("templates/faq.html").render())


app = webapp2.WSGIApplication([
    ("/", WelcomeHandler),
    ("/main", MainHandler),
    ("/generate", GenerateHandler),
    ("/about", AboutUsHandler),
    ("/feedback", FeedbackHandler),
    ("/faq", FAQsHandler)
], debug=True)
