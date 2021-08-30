from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def number(request):
    return render(request, 'number.html')


def numprint(request):
    num = int(request.GET["number"])
    if num > 500:
        return render(request, 'output.html', {"message": "please enter number less than or equal to 500",
                                               "link": "http://127.0.0.1:8000/app1/"})
    elif num < 0:
        return render(request, 'output.html',
                      {"message": "please enter a positive integer", "link": "http://127.0.0.1:8000/app1/"})
    else:
        output = [i for i in range(1, num + 1)]
        return render(request, 'output.html', {"num": output, "link": "http://127.0.0.1:8000/app1/"})
