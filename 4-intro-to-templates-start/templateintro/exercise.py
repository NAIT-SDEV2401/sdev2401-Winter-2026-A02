import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateintro.settings")
django.setup()

print("Django environment set up successfully.")
# everything above this line is needed to create a runnable django file.
# we're going to create an 8 ball question app.
# install requests (with pip)

from django.template import Template, Context
import requests
# 1. I want you to prompt the user to ask a question.
question = input("Ask the 8 ball a question: ")
# below uses the docs here: https://www.eightballapi.com/docs
# 2. Perform a get request to endpoint "https://www.eightballapi.com/api" and save the reading key
data_from_api = requests.get("https://www.eightballapi.com/api").json()
reading = data_from_api["reading"]
# 3. Perform a get request to endpoint "https://www.eightballapi.com/api/categories"
categories = requests.get("https://www.eightballapi.com/api/categories").json()

# 4. see if the sentiment of the reading is in the "positive", "negative", "neutral"
sentiment = ""
for category in categories.keys():
    if reading in categories[category]:
        sentiment = category
# 5. format the data like so
'''
data = {
    "question": ....
    "reading": ....
    "sentiment": .....
}
'''
data = {
    "question": question,
    "reading": reading,
    "sentiment": sentiment
}
breakpoint()
# 6. create a template that looks like this
'''
You asked QUESTIONHERE
the 8 ball reading is ANSWERHERE it's a SENTIMENT reading.
you should be worried/happy/not bothered by the answer
'''
template = template
# where worried/happy/not is based on the sentiment
# 7. create a context based on the data and render the template.