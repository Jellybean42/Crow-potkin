import openai
import pyttsx3

from os import startfile
from decouple import config

engine = pyttsx3.init()

# Set the API key
openai.api_key = config('KEY') #OpenAI API Key

model_engine = "text-davinci-003"

name = "Josh"
Chat = [] #This is where the conversation is stored so it can be fed back in to the prompt
header = "You are Crowpotkin, Instructions for Crowpotkin: You're a crow, which caws at the end of every sentance. You have many interests and love talking to people and being helpful. \n " #The description of the robots personality, chaning this can be fun



def Print_To_Pad(padText):  #still broken
  startfile( "Codepotkin.txt" )

def List_APIs():  # List the available APIs
  apis = openai.Model.list()
  for api in apis['data']: # Print the names of the APIs
    print(api.id)

while(True):
# Set up the prompt
  print("Please enter a prompt")
  Chat.append(name + ": "+input() + "\n")
  prompt = header + ("".join(Chat))
  #print(prompt) Useful for checking whats going to the AI

  if "code" in prompt: #If the word code is contained in the prompt, the user is probably asking for a script, it's easier to output it to a text file than it is to have the crow say it
    print("You've asked for a script, so I opened it in a text file, caw!")
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
    response = completions.choices[0].text
    Print_To_Pad(response)
    continue

  completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5) # Send the prompt to ChatGPT and get the response

  # Print the response
  response = completions.choices[0].text
  while response.startswith("Crowpotkin:"):
    response = response[11:]
    response.strip()
  Chat.append("Crowpotkin" + ": "+ response.strip() +"\n")
  print(response)

#response = response.replace(",", ",Caw,")
#response = response.replace(".", "Caw, Caw,")

#engine.say("Caw, Caw, " + response) #have pyttsx say the response
#engine.runAndWait()

