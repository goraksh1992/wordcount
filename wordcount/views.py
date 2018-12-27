from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    # return HttpResponse("This is Homepage")
    return render(request, 'home.html')

def count(request):

    data = request.GET['fulltext']

    lst = data.split()

    total_word = len(lst)

    worddict = {}

    for word in lst:
        if word in worddict:
            cnt = int(worddict[word]) + 1
            worddict[word] = cnt
        else:
            worddict[word] = 1
    
    sorted_dict = sorted(worddict.items(), key = operator.itemgetter(1), reverse = True)
     
    return render(request, 'count.html', {'fulltext': data, 'total_word': total_word, 'cnt' : sorted_dict})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return HttpResponse("This is contact us page")