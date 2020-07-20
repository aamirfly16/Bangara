from django.shortcuts import render, redirect
from newsapi import NewsApiClient


# Create your views here.

def Index(request):
    return render(request,"index.html")

# def Magazine(request):
#     return render(request,"magazine.html")

# def Business(request):
#     return render(request,"business.html")

def Sports(request):
    return render(request,"sports.html")

def Art(request):
    return render(request,"art.html")

def Politics(request):
    return render(request,"politics.html")

def Travel(request):
    return render(request,"travel.html")

def Contactus(request):
    return render(request,"contactus.html")

def Times(request):
    newsapi = NewsApiClient(api_key="a8a7d751f18540c8b37d9f333620b03f")
    topheadlines = newsapi.get_top_headlines(sources='the-times-of-india')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'magazine.html',  context={"mylist": mylist})

def bbc(request):
    newsapi = NewsApiClient(api_key="a8a7d751f18540c8b37d9f333620b03f")
    topheadlines = newsapi.get_top_headlines(sources='bbc-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])


    mylist = zip(news, desc, img)

    return render(request, 'business.html', context={"mylist":mylist})
