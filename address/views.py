from django.shortcuts import render

def test_bootstrap(request):
    return render(request, 'test_bootstrap.html')