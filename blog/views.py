import logging

from django.core import paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from .models import Post
from django.core.paginator import Paginator
from .forms import contactform

# Create your views here.
#static demo data
#posts = [
#       {'id':1, 'title':'Post 1','content':'Content of Post 1'},
#      {'id':2,  'title':'Post 2','content':'Content of Post 2'},
#{  'id':4,'title':'Post 4','content':'Content of Post 4'},
#    {  'id':5,'title':'post 5','content':'content of post 5'},
#]
def index(request):
    blog_title = "Latest Posts"

    all_posts = Post.objects.all().order_by('-created_at')

    paginator = Paginator(all_posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {
        'blog_title': blog_title,
        'post_obj': page_obj,
        'page_obj': page_obj,
    })

def detail(request, slug):
    #getting static data 
    #post = next((item for item in posts if item["id"] == post_id), None)

    #getting data from database
    try:
        posts = Post.objects.get(slug=slug)
        related_posts=Post.objects.filter(category=posts.category).exclude(pk=posts.pk)[:3]
    except Post.DoesNotExist:
        return render(request,'404.html', status=404,)

   # logger = logging.getLogger("TestLogger")
   # logger.info(f"Accessing detail view for post_id: {post_id}")
    return render(request,'detail.html', {'post': posts, 'related_posts': related_posts})

def old_url_redirct(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("your viewing new url")

def contact(request):
        if request.method == 'POST':
             contact_form = contactform(request.POST)   
             contact_form.cleaned_data['name']
             contact_form.is_valid()
             logger = logging.getLogger("TestLogger")
             logger.debug(f"Contact form submitted with name: {contact_form.cleaned_data['name']}, email: {contact_form.cleaned_data['email']}, message: {contact_form.cleaned_data['message']}")
        return render(request,'contact.html')
