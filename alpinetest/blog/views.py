from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Blog, BlogComment, BlogTopSection
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .forms import CommentForm
from django.contrib import messages

# Create your views here.

def blog(request):
        blogs = Blog.objects.all().order_by('-created_date')
        paginator = Paginator(blogs, 6)
        page=request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count =  blogs.count()
        blog_top = BlogTopSection.objects.all().first()
        context={
            'blogs':paged_products,
            'counts': product_count,
            'blog_top':blog_top,
        }
        return render(request, 'blog.html', context)



def blog_content(request, blog_slug):
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        form = CommentForm(request.POST)
        print("form")
        print(blog_slug)
        if form.is_valid():
            print("vaidated")
            data = BlogComment()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.comment = form.cleaned_data['comment']
            data.blog = Blog.objects.get(slug = blog_slug)
            data.save()
            messages.success(request, "Thank you! Your comment has been posted. ")
            return redirect(url)

    else:
        single_blog = Blog.objects.get(slug = blog_slug)
        blogs = Blog.objects.all().order_by('-created_date')
        
        paginator = Paginator(blogs, 6)
        page=request.GET.get('page')
        recent_post = paginator.get_page(page)


        comments = BlogComment.objects.filter(blog__slug = blog_slug).order_by('-created_date')
        comment_count= comments.count()
        comments_page = Paginator(comments, 20)
        cmt_page = request.GET.get('page')
        cmt = comments_page.get_page(cmt_page)
        context  = {
            'single_blog':single_blog,
            'recent_post':recent_post,
            'comments':comments,
            'comment_count':comment_count,
            'cmt':cmt,
        }
        return render(request, 'blog-details.html' ,context)



def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Blog.objects.order_by('-created_date').filter(Q(short_description__icontains=keyword) | Q(title__icontains = keyword))
            product_count = products.count()
            context={
                'blogs': products,
                'product_count':product_count
            }
            return render(request, 'blog.html', context)

    return render(request, 'blog.html')


