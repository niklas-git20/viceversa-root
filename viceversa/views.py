from django.http import HttpResponse
from django.shortcuts import render


def viceversa(request):
	return render(request, 'viceversa.html')

def reverse(request):
	user_text = request.GET['usertext']
	len_text = len(user_text.split())
	rev_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext': user_text,
		'reversedtext':rev_text,
		'lentext':len_text})