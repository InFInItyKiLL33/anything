import webapp2
import jinja2
import os
import random

namesDict = {}

dares = {
    "d1": "Sing any song in a funny voice, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d2": "Lick your elbow, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d3": "Perform the Chicken Dance, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d4": "Use an American accent for the next hour, 0, 1, 1, 1, 1, 1, 1, 1, 1",
    "d5": "Do 10 push-ups, 0, 1, 1, 1, 0, 0, 1, 1, 1",
    "d6": "Sing ABC backwards, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d7": "Tell someone to tickle you for 30 seconds, 1, 1, 1, 1, 1, 0, 1, 1, 1",
    "d8": "Talk and act like a robot, 0, 1, 1, 1, 1, 1, 1, 1, 1",
    "d9": "Do an impressive cat walk, 0, 0, 1, 1, 1, 1, 0, 1, 1",
    "d10": "Do the floss dance, 1, 1, 1, 1, 0, 0, 1, 1, 1",
    "d11": "Do a front roll, 1, 1, 1, 1, 0, 0, 1, 1, 1",
    "d12": "Pretend to slip over a banana, 0, 1, 1, 1, 0, 0, 1, 1, 1",
    "d13": "Add the words 'I'm dumb' after all your sentences for the rest of the game, 0, 1, 1, 1, 1, 1, 1, 1, 1",
    "d14": "Act like an old person, 1, 1, 1, 1, 0, 0, 1, 1, 1",
    "d15": "Act like you have helium gas in your mouth and sing the song 'Twinkle Twinkle Little Star', 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d16": "Do 5 jumping jacks whilst singing a song, 0, 1, 1, 1, 1, 0, 1, 1, 1",
    "d17": "Describe the sky without the words 'Blue' and 'White', 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d18": "Spin around 20 times and try to walk straight, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d19": "Interrupt everyone by saying 'That's a lie' until your next turn, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d20": "Stay silent until your next turn, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d21": "Hum a song of your choice until someone correctly guesses it, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d22": "Do your best acceptance speech for an award of your choice, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d23": "Pretend to be a CEO of a company, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d24": "Show your browsing history to everyone, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "d25": "Pretend to be another player for the rest of the game, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "d26": "Write a poem for someone you know the least in the group and present it, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "d27": "Use a pickup line to the person on your right, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "d28": "Insult everyone you are playing with, 0, 1, 1, 1, 1, 1, 0, 1, 1 "
}

truths = {
    "t1": "Do you talk in your sleep?, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "t2": "Who is your secret crush?, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "t3": "What is your guilty pleasure?, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "t4": "What is your worst habit?, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "t5": "What is your favourite book?, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "t6": "What was your most embarrassing moment in public?, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    "t7": "Who do you think is cutest?, 0, 1, 1, 1, 1, 0, 1, 1, 1",
    "t8": "Describe your perfect partner, 0, 1, 1, 1, 0, 0, 1, 1, 1",
    "t9": "Who do you like the least in this room and why?, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "t10": "What does your dream partner look like?, 0, 1, 1, 1, 1, 0, 0, 1, 1",
    "t11": "What was the last thing you texted?, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "t12": "Who will you save and abandon when escaping from a burning building, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "t13": "Do you think you'll marry your current girlfriend/boyfriend if you have one?, 0, 1, 1, 1, 0, 0, 0, 1, 1",
    "t14": "Do you have a crush on someone?, 0, 1, 1, 1, 0, 0, 0, 1, 1",
    "t15": "The world ends next week and you can do anything you want. What would you do?, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "t16": "What would you do that you wouldn't do now if you had nine lives?, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "t17": "Which teacher would you fire if you have the power to?, 0, 1, 0, 0, 0, 0, 0, 1, 0",
    "t18": "Who would you invite for your prom night?, 0, 1, 0, 0,  0,  0, 0, 1, 0",
    "t19": "Tell us about the last dream you had in detail, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "t20": "Have you ever lied on your resume to get a job or internship?, 0, 0, 1, 1, 1, 1, 0, 0, 1",
    "t21": "Do you prefer the big city or country life?, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "t22": "What is your nickname when you were young?, 0, 0, 1, 1, 1, 1, 0, 0, 1",
    "t23": "What are four things you notice in a person at first glance?, 0, 1, 1, 1, 1, 1, 0, 1, 1",
    "t24": "What is the craziest thing you did?, 0, 1, 1, 1, 1, 1, 0, 1, 1"
}

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
        #print(namesDict["filters"])
        for i in namesDict["filters"]:
            #print(i)
            if i == "1":
                filtersEnabled = True
        #print(filtersEnabled)
        if filtersEnabled:
            #print("a")
            for item in dares:
                #print("Line: " + dares[item])
                item = dares[item].split(", ")
                #print(item)
                for i in range(9):
                    if item[i + 1] == "1" and namesDict["filters"][i * 2] == "1" and item[0] not in namesDict["dares"]:
                        namesDict["dares"].append(item[0])
                        break

            for item in truths:
                #print("Line: " + dares[item])
                item = truths[item].split(", ")
                #print(item)
                for i in range(9):
                    if item[i + 1] == "1" and namesDict["filters"][i * 2] == "1" and item[0] not in namesDict["truth"]:
                        namesDict["truth"].append(item[0])
                        break
        else:
            #print("b")
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

        #print(namesDict)
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
