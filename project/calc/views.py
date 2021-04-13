from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request, num1, num2):
	return HttpResponse('Suma = ' + str(num1+num2)) 
	
def resta(request, num1, num2):
	return HttpResponse('Resta = ' + str(num1-num2)) 
	
def multi(request, num1, num2):
	return HttpResponse('Multiplicación = ' + str(num1*num2)) 
	
def div(request, num1, num2):
	return HttpResponse('División = ' + str(num1/num2)) 
	
	

