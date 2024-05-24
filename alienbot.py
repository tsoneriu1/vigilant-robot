# importing regex and random libraries
import re
import random

class AlienBot:
    # potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    # keywords for exiting the conversation
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    # random starter questions
    random_questions = (
          "Why are you here? ",
          "Are there many humans like you? ",
          "What do you consume for sustenance? ",
          "Is there intelligent life on this planet? ",
          "Does Earth have a leader? ",
          "What planets have you visited? ",
          "What technology do you have on this planet? "
      )
  
    def __init__(self):
      self.alienbabble = {'describe_planet_intent': r'.*planet.*',
                          'answer_why_intent': r'.*why.*',
                          'cubed_intent': r'.*(cube|number).*([0-9]+).*'
                              }
  
    # Define .greet() below:
    def greet(self):
      input_name = input("Hello. What is your name?\n")
      self.name = input_name
      will_help = input(f"Hi {input_name}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet?\n")
      
      if will_help in self.negative_responses:
        print("Ok, have a nice Earth Day\n")
        return
      self.chat()
      pass
  
    # Define .make_exit() here:
    def make_exit(self, reply):
      for checkString in self.exit_commands:
        if reply in checkString:
          print("Ok, have a nice Earth Day\n")
          return True
      pass
  
    # Define .chat() next:
    def chat(self):
      soup = 0
      reply = input ( random.choice(self.random_questions)).lower()
      while not self.make_exit(reply) and soup < 4:
        # reply = input("How are you?")
        soup += 1
        print(soup)
        reply = input(self.match_reply(reply)+'\n')
      pass
  
    # Define .match_reply() below:
    def match_reply(self, reply):
      print("-\n")
      for intent,regex_pattern in self.alienbabble.items():
        regex = regex_pattern
        # reply = r'This is text'
        
        found_match = re.match(regex,reply)
        
        print(reply, regex, intent)
        if found_match and intent == 'describe_planet_intent':
          return self.describe_planet_intent()
        elif found_match and intent == 'answer_why_intent':
          return self.answer_why_intent()
        elif found_match and intent == 'cubed_intent':
          print(found_match)
          return self.cubed_intent()
        else:
          print("NO MATCH")
          return self.no_match_intent()
  
      pass
  
    # Define .describe_planet_intent():
    def describe_planet_intent(self):
      responses = ("My planet is a utopia of diverse organisms and species", "I am from Odipipus, the capital of Wayward Galaxies.")
      return random.choice(responses)
  
    # Define .answer_why_intent():
    def answer_why_intent(self):
      responses = ("I come in peace", "I am here to collect data on your planet and its inhabitants", "I heard the coffee is good")
      return random.choice(responses)
         
    # Define .cubed_intent():
    def cubed_intent(self, number):
      return "Inside .cubed_intent()"
  
    # Define .no_match_intent():
    def no_match_intent(self):
      responses(
        "Please tell me more",
        "Why do you say that?",
        "Interesting...",
        "I see",
        "How do you think I feel when you say that."
      )
      return random.choice(responses)

# Create an instance of AlienBot below:
bot = AlienBot()
bot.greet()
