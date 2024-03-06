import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an application for resign in office\n\nTo: [Name of Your Supervisor]\n\nFrom: [Your Name]\n\nSubject: Resignation from [Your Position]\n\nDate: [date]\n\nDear [Name of Your Supervisor],\n\nI am writing to inform you that I am resigning from my position of [Your position] with [Company Name], effective [date].\n\nI have enjoyed my time working here, but I have decided that it is time for me to move on to new possibilities. I appreciate all the time, training, and opportunities I have had while working here.\n\nI am committed to ensuring a smooth transition. I am willing to assist with training any new employees or transferring any work in progress to them. I am also willing to assist with any projects or duties needed between now and my last day.\n\nPlease let me know if there is anything else I can do to help with the transition.\n\nAgain, thank you for the opportunity to work here.\n\nSincerely, \n[Your Name]",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
