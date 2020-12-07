from django.shortcuts import render, redirect 

def index(request):
    return render(request,"index.html")





# def create_survey(request):
#     print("Got Post Info....................")
#     print(request.POST)
#     return render(request,"index.html")


def create_survey(request):
    print("Got Post Info....................")

    name_from_form = request.POST['name']
    first_drop = request.POST['dropdown']
    second_drop = request.POST['second-dropdown']
    context = {
    	"name_from_form" : name_from_form,
    	"favorite_langauge_on_template" : second_drop,
        "location_dojo" : first_drop,
        }
    print(name_from_form)

    return render(request,"result.html",context)