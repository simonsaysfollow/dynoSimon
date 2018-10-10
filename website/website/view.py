import request
from django.http import HttpResponse
from django.shortcuts import render
import templates
import glob
import os 

mailgun_api_key = os.environ["MAILGUN_API_KEY"]

holder = []
all_html_files = glob.glob("content/*.html")
for single in all_html_files:
    file_name = os.path.basename(single)
    name_only, extension = os.path.splitext(file_name)
    holder.append(name_only)


def index(request):
    # home = open("content/home.html").read()
    context = {
        'title': 'Simon Tekeste',
        "y": holder,
        # "content_insert": home,
        "checker":"home"
            }
    return render(request, 'home.html', context)


def second(request):

    # content = open("content/travel.html").read()
    context = {
        "title": "Projects",
        "y": holder,
        # "content_insert": content,
        "checker":"travel"
    }
    return render(request, "travel.html", context)

def connect_with_me(request):
    # contact = open("templates/contact.html").read()
    
    if request.method == "POST":

        first = request.POST["user_first"]
        last = request.POST["user_last"]
        email = request.POST["user_mail"]
        message = request.POST["user_message"]
        phone = request.POST["phone_number"]
        company = request.POST["company_name"]
        

    else:
    
        context = {
            "title": "Contact Me",
            "y": holder,
            # "content_insert": contact,
            "checker": "contact"

        }
        return render(request, "contact.html", context)

