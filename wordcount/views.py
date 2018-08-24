from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import operator

@csrf_exempt
def home(request):
    return render(request, 'home.html')


@csrf_exempt
def about(request):
    return render(request, 'about.html')

@csrf_exempt
def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split()
    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
        sortedWordList = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse = True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordList), 'wordDictionary':sortedWordList})
