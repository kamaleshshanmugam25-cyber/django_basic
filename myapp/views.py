from django.shortcuts import render

def custom_404_page(request,exception):
    return render(request,'404.html',status=404)

def custom_500_page(request,exception=None):
    return render(request,'500.html',status=500)