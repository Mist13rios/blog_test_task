from django.shortcuts import render
from blog_app.models import Blog, User, Blog_entry

# Create your views here.
def main(request):
    return render(request, 'main_page.html', {'all_users': User.objects.all()})

def user_news(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id') 
        info = User.objects.filter(id=user_id)
        entry_list = Blog_entry.objects.filter(pk=info[0].)
        news_list=[]
        for entry in entry_list:
            news_list.append([entry.head, entry.pub_date, entry.text]) 
        news_list.sort(key=lambda t: t[1], reverse=True)
        return render(request, '_user_news.html', {'news_list': news_list})