from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def college(requst):
    return HttpResponse('<p>this is sample text</p> <h1> heading </h1> <h2> heading </h2><h3> heading </h3><h4> heading </h4><h5> heading </h5> <h6> heading </h6>  <ul type="circle"><li>php: this is backend</li><br> <li>  aoop </li><li>  php  </li></ul>  <ol type="i"><li>  java </li>  <li>  aoop </li> <li>  php  </li></ol>')

def principal(requst):
    return HttpResponse('rocky')

def faculty(requst):
    return HttpResponse('chokey')

def admin(requst):
    return HttpResponse('priya')

def student(requst):
    return HttpResponse('jakey')
