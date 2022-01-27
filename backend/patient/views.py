from django.shortcuts import render

def test(request):
    return render(request, 'patient/base_logined.html')
