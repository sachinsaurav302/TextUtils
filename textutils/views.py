# I have created this file - sachin

from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')

def analyze(request):

    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newline_remove=request.POST.get('newline_remove', 'off')
    sapaceremover=request.POST.get('sapaceremover', 'off')
    charcount=request.POST.get('charcount', 'off')
    
    if  removepunc=="on":

        punctuation='''/;''[]{()},.'":\|?><'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed + char
        prams={'pupose': 'Remove punction', 'analyze_text':analyzed}
        djtext=analyzed
        
    if fullcaps == 'on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        prams={'pupose': 'convert into upper case', 'analyze_text':analyzed}
        djtext=analyzed

    if newline_remove=='on':
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r": 
                analyzed=analyzed + char
            else:
                print("no")
        prams={'pupose': 'remove new line', 'analyze_text':analyzed}
        djtext=analyzed

    if sapaceremover == 'on':  
        analyzed = ""
        for index in range(len(djtext)):
            if index == 0 or not (djtext[index] == " " and djtext[index - 1] == " "):
                analyzed = analyzed + djtext[index] 

        prams = {'purpose': 'Extra Space Remover', 'analyze_text': analyzed}
        djtext=analyzed

    if (removepunc !='on' and fullcaps != 'on' and newline_remove !='on' and sapaceremover != 'on'):
        return render(request, 'error.html')
 

    return render(request, 'analyze.html', prams)

    
             