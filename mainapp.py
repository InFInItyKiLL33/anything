import webapp2
import jinja2
import os


jinjaEnv = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(jinjaEnv.get_template("templates/welcome.html").render())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(jinjaEnv.get_template("templates/main.html").render())

class GenerateHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(jinjaEnv.get_template("templates/generate.html").render())

class AboutUSHandler(webapp2.RequestHandler):
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
    ("/About_Us", AboutUsHandler),
    ("/Feedback", FeedbackHandler),
    ("/FAQ", FAQsHandler),
], debug=True)
