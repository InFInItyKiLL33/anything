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

    def post(self):
        pass

class GenerateHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("/main")
        
    def post(self): ##change most "" to actual name of input
        print("LUL")
        global namesDict
        i = 0
        while True: #get all the names and age input
            if self.request.get(str(i)) == "":
                print(self.request.get(str(i)))
                if i == 0:
                    self.redirect("/main")
                    return
                break
            #00 -> name 1, 01 -> age 1, 10 -> name 2, 11 -> age 2, 20 -> name 3, 21 -> age 3, etc.
            namesDict.update({
                str(i) + "0": self.request.get(str(i)).split(", ")[0],
                str(i) + "1": self.request.get(str(i)).split(", ")[1]
            })
            i += 1
        namesDict.update({"filters": self.request.get("filters")})
        print(namesDict)
        self.response.write(jinjaEnv.get_template("templates/generate.html").render(namesDict))

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
