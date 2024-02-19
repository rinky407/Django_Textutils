#Self made file -- made by Rinky

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Rinky','place':'moon'}
    return render(request,'index.html',params) 

def about(request):
    return HttpResponse("About Miss Rinky Singh")

def analyze(request):
    djtext= request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalize = request.POST.get('capitalize','off')
    removenewline = request.POST.get('removenewline','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcounter = request.POST.get('charcounter','off')
    punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    count = 0
    if removepunc == 'on':
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations from string','analyzed_text':analyzed}
        djtext = analyzed
    if capitalize == 'on':
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose':'Capitalize Letters','analyzed_text':analyzed}
        djtext = analyzed
    if removenewline == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed=analyzed+char
        params ={'purpose':'Remove New Line','analyzed_text':analyzed}
        djtext = analyzed
    if spaceremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed=analyzed+char
        params ={'purpose':'Remove Space','analyzed_text':analyzed}
        djtext = analyzed
    if charcounter == 'on':
        analyzed = ""
        for char in djtext:
            count += 1
        params ={'purpose':'Count Character','analyzed_text':analyzed,'counter':count}
    if(charcounter != 'on' and spaceremover != 'on'and removenewline != 'on'and capitalize != 'on'and removepunc != 'on'):
        return HttpResponse('Error')
    return render(request,'analyze.html',params)
