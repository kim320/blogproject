from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator
from .forms import BlogPost

def blog(request):
  blogs = Blog.objects
  blog_list = Blog.objects.all()
  paginator = Paginator(blog_list, 2)
  

  try:
      page = int(request.GET.get('page', '1'))
  except:
      page = 1

  try:
      posts = paginator.page(page)
  except(EmptyPage, InvalidPage):
      posts = paginator.page(1)

  # Get the index of the current page
  index = posts.number - 1  # edited to something easier without index
  # This value is maximum index of your pages, so the last page - 1
  max_index = len(paginator.page_range)
  # You want a range of 7, so lets calculate where to slice the list
  start_index = index - 3 if index >= 3 else 0
  end_index = index + 3 if index <= max_index - 3 else max_index
  # Get our new page range. In the latest versions of Django page_range returns 
  # an iterator. Thus pass it to list, to make our slice possible again.
  page_range = list(paginator.page_range)[start_index:end_index]

  return render(request, 'blog.html', {'blogs':blogs,'posts': posts,'page_range': page_range})


def detail(request, blog_id):
  blog_detail = get_object_or_404(Blog, pk = blog_id)
  return render(request, 'detail.html', {'blog_detail':blog_detail})

def new(request):
  return render(request, 'new.html')

def create(request):
  blog = Blog()
  blog.title = request.GET['title']
  blog.body = request.GET['body']
  blog.pub_date = timezone.datetime.now()
  blog.save()
  return redirect('/blog/'+str(blog.id))

"""
def blogpost(request):
  if request.method == "POST":
    form = BlogPost(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.pub_date
      post.save()
      return redirect('blog')
  else:
    form = BlogPost()
    return render(request, 'new.html', {'form':form})
"""