from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def help(request):
    my_dic = {'insert_timmy':'here is the timmy code'}
    return render(request, 'second_app/help.html',context=my_dic)

def index(request):
    index_dict = {'insert_index':"Here is some code to insert"}
    return render(request, 'second_app/index.html',context=index_dict)
