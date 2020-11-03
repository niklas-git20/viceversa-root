from django.http import HttpResponse
from django.shortcuts import render

def viceversa(request):
	return render(request, 'viceversa.html')

def reverse(request):
	user_text = request.GET['usertext']
	rev_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext': user_text,'reversedtext':rev_text})