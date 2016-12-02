from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from blog_app.models import Blog, User, Blog_entry

# Create your views here.
def main(request):
    return render(request, 'main_page.html', {'all_users': User.objects.all()})