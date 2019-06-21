import webapp2
import jinja2
import os
import random

namesDict = {}

dares = {
"d1": "Sing a song in a funny voice, 1, 1, 1, 1, 1, 1, 1, 1, 1",
"d2": "Lick your elbow, 1, 1, 1, 1, 1, 1, 1, 1, 1",
"d3": "Do chicken dance, 1, 1, 1, 1, 1, 1, 1, 1, 1",
"d4": "Use a American accent for the next hour, 0, 1, 1, 1, 1, 1, 1, 1, 1",
"d5": "Do 10 push ups, 0, 1, 1, 1, 0, 0, 1, 1, 1",
"d6": "Sing ABC backwards, 1, 1, 1, 1, 1, 1, 1, 1, 1",
"d7": "Tell someone to tickle you for 30 seconds, 1, 1, 1, 1, 1, 0, 1, 1, 1",
"d8": "Talk and act like a robot, 0, 1, 1, 1, 1, 1, 1, 1, 1",
"d9": "Do a impressive cat walk, 0, 0, 1, 1, 1, 1, 0, 1, 1",
"d10": "Do the floss dance, 1, 1, 1, 1, 0, 0, 1, 1, 1",
"d11": "Do a front roll, 1, 1, 1, 1, 0, 0, 1, 1, 1",
"d12": "Pretend to slip over a banana, 0, 1, 1, 1, 0, 0, 1, 1, 1",
"d13": "Add the words 'I'm dumb' after all ur sentences for the rest of the game, 0, 1, 1, 1, 1, 1, 1, 1, 1",
"d14": "Act like a old person, 1, 1, 1, 1, 0, 0, 1, 1, 1",
"d15": "Act like you have helium gas in ur mouth and sing twinkle twinkle little start, 1, 1, 1, 1, 1, 1, 1, 1, 1",
"d16": "Do 5 jumping jacks while singing a song, 0, 1, 1, 1, 1, 0, 1, 1, 1"}

truths = {}

#print(namesDict)

jinjaEnv = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ["jinja2.ext.autoescape"],
    autoescape = True)

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
        global namesDict, numberOfNames
        try:
            namesDict.update({"randomName": namesDict["a" + str(random.randint(0, numberOfNames - 1)) + "0"]})
        except:
            self.redirect("/main")
        else:
            self.response.write(jinjaEnv.get_template("templates/generate.html").render(namesDict))
        #self.redirect("/main")
        
    def post(self): ##change most "" to actual name of input
        global namesDict, numberOfNames
        i = 0
        filtersEnabled = False
        numberOfNames = 0
        namesDict.update({"dares": [], "truth": []})
        namesDict.update({"filters": self.request.get("filters")})
        while True: #get all the names and age input
            try: 
                self.request.get(str(i))
            except KeyError:
                if i == 0:
                    self.redirect("/main")
                    return
                break
            if self.request.get(str(i)) == "":
                break
            namesDict.update({
                "a" + str(i) + "0": self.request.get(str(i)).split(", ")[0],
                "a" + str(i) + "1": self.request.get(str(i)).split(", ")[1]
            })
            i += 1
            numberOfNames += 1
        namesDict.update({"numberOfLength": numberOfNames})
        for i in namesDict["filters"]:
            if i == 1:
                filtersEnabled = True
        if filtersEnabled:
            for item in dares:
                #print("Line: " + dares[item])
                item = dares[item].split(", ")
                #print(item)
                for i in range(9):
                    if item[i + 1] == "1" and namesDict["filters"][i] == 1 and item[0] not in namesDict["dares"]:
                        namesDict["dares"].append(item[0])
                        break

            for item in truths:
                #print("Line: " + dares[item])
                item = truths[item].split(", ")
                #print(item)
                for i in range(9):
                    if item[i + 1] == "1" and namesDict["filters"][i] == 1 and item[0] not in namesDict["truth"]:
                        namesDict["truth"].append(item[0])
                        break
        else:
            for item in dares:
                #print("Line: " + dares[item])
                item = dares[item].split(", ")
                #print(item)
                for i in range(9):
                    if item[i + 1] == "1" and item[0] not in namesDict["dares"]:
                        namesDict["dares"].append(item[0])
                        break

            for item in truths:
                #print("Line: " + dares[item])
                item = truths[item].split(", ")
                #print(item)
                for i in range(9):
                    if item[i + 1] == "1" and item[0] not in namesDict["truth"]:
                        namesDict["truth"].append(item[0])
                        break

        print(namesDict)
        namesDict.update({"randomName": namesDict["a" + str(random.randint(0, numberOfNames - 1)) + "0"]})
        self.response.write(jinjaEnv.get_template("templates/generate.html").render(namesDict)) #00 -> name 1, 01 -> age 1, 10 -> name 2, 11 -> age 2, 20 -> name 3, 21 -> age 3, etc. call filters for filters in binary

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
