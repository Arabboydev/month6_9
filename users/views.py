from django.shortcuts import render
from django.views import view

class LondingPageView(View):
    def get(self, request):
        return render(request, "main/index.html")

# Create your views here.
