import os
import openai

# Test if the Open API is working.

#openai.organization = "YOUR_ORG_ID"
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())

