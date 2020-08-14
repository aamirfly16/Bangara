from django.shortcuts import render, redirect
from .models.product import Product
from .models.category import Category
from .models.home import Home
from newsapi import NewsApiClient
from .models.video import Item
from .models.videocategory import videocategory
from django.utils.translation import gettext as _

# Create your views here.

def Index(request):
    products = None
    homes = None
    items = None
    obj = None
    products_slider = Product.objects.all()
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        homes = Home.get_all_homes_by_categoryid(categoryID)
    else:
        homes = Home.get_all_homes();
    videocategories = videocategory.get_all_videocategories()
    videocategoryid = request.GET.get('videocategory')
    if videocategoryid:
        obj = Item.get_all_items_by_videocategoryid(videocategoryid)
    else:
        obj = Item.objects.all()
    context = {}
    context['products_slider'] = products_slider
    context['categories'] = categories
    context['homes'] = homes
    context['obj'] = obj
    context['items'] = items
    context['videocategories'] = videocategories
    return render(request, "index.html", context)



# def Magazine(request):
#     return render(request,"magazine.html")

# def Business(request):
#     return render(request,"business.html")

# def Sports(request):
#     return render(request,"sports.html")
def Base(request):
    products = None
    products_slider = Product.objects.all()
    context = {}
    context['products_slider'] = products_slider
    return render(request, "base.html", context)


def Testing(request):
    products = None
    homes = None
    items = None
    obj = None
    products_slider = Product.objects.all()
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        homes = Home.get_all_homes_by_categoryid(categoryID)
    else:
        homes = Home.get_all_homes();
    videocategories = videocategory.get_all_videocategories()
    videocategoryid = request.GET.get('videocategory')
    if videocategoryid:
        obj = Item.get_all_items_by_videocategoryid(videocategoryid)
    else:
        obj = Item.objects.all()
    context = {}
    context['products_slider'] = products_slider
    context['categories'] = categories
    context['homes'] = homes
    context['obj'] = obj
    context['items'] = items
    context['videocategories'] = videocategories
    return render(request, "testing.html", context)

def video(request):
    items = None
    obj = None
    products_slider = Product.objects.all()
    videocategories = videocategory.get_all_videocategories()
    videocategoryid = request.GET.get('videocategory')
    if videocategoryid:
        obj = Item.get_all_items_by_videocategoryid(videocategoryid)
    else:
        obj = Item.objects.all()
    context = {}
    context['obj'] = obj
    context['items'] = items
    context['videocategories'] = videocategories
    context = {}
    context['products_slider'] = products_slider

    return render(request,'videoyou.html',context)

def Test(request):
    products = None
    homes = None
    items = None
    obj = None
    products_slider = Product.objects.all()
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        homes = Home.get_all_homes_by_categoryid(categoryID)
    else:
        homes = Home.get_all_homes();
    videocategories = videocategory.get_all_videocategories()
    videocategoryid = request.GET.get('videocategory')
    if videocategoryid:
        obj = Item.get_all_items_by_videocategoryid(videocategoryid)
    else:
        obj = Item.objects.all()
    context = {}
    context['products_slider'] = products_slider
    context['categories'] = categories
    context['homes'] = homes
    context['obj'] = obj
    context['items'] = items
    context['videocategories'] = videocategories
    return render(request, "test.html", context)

# def Politics(request):
#     return render(request,"politics.html")

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

def Google(request):
    newsapi = NewsApiClient(api_key="a8a7d751f18540c8b37d9f333620b03f")
    topheadlines = newsapi.get_top_headlines(sources='google-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, date)

    return render(request, 'Politics.html', context={"mylist": mylist})

def Indian(request):
    newsapi = NewsApiClient(api_key="a8a7d751f18540c8b37d9f333620b03f")
    geteverything = newsapi.get_everything(sources='espn-cric-info')

    articles = geteverything['articles']

    desc = []
    news = []
    img = []
    date = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, date)

    return render(request, 'sports.html', context={"mylist": mylist})

# def Arttech(request):
#     newsapi = NewsApiClient(api_key="a8a7d751f18540c8b37d9f333620b03f")
#     geteverything = newsapi.get_everything(sources='the-verge')
#
#     articles = geteverything['articles']
#
#     desc = []
#     news = []
#     img = []
#     date = []
#
#     for i in range(len(articles)):
#         myarticles = articles[i]
#
#         news.append(myarticles['title'])
#         desc.append(myarticles['description'])
#         img.append(myarticles['urlToImage'])
#         date.append(myarticles['publishedAt'])
#
#     mylist = zip(news, desc, img, date)
#
#     return render(request, 'art.html', context={"mylist": mylist})
