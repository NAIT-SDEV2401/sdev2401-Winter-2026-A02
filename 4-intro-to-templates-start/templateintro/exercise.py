import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateintro.settings")
django.setup()

print("Django environment set up successfully.")
# everything above this line is needed to create a runnable django file.

# we're going to create an 8 ball question app.
# install requests (with pip)
# 1. I want you to prompt the user to ask a question.
# 2. Perform a get request to endpoint "https://www.eightballapi.com/api" and save the reading key
# 3. Perform a get request to endpoint "https://www.eightballapi.com/api/categories"
# 4. see if the sentiment of the reading is in the "positive", "negative", "neutral"
# 5. format the data like so
'''
data = {
    "question": ....
    "reading": ....
    "sentiment": .....

}

'''