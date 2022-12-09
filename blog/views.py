from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Comment
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import  User
from .forms import CommentForm
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post

    template_name = 'blog/home.html'
     
    context_object_name = 'posts'

    ordering = ['-date_posted']

    paginate_by = 5

    

class UserPostListView(ListView):
    model = Post

    template_name = 'blog/user_posts.html'
     
    context_object_name = 'posts'

    ordering = ['-date_posted']

    paginate_by = 5

    def get_queryset(self):    
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author = user)

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','book_writer','content','book']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #success_url = 'blog-home'

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content','book']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def about(request):
    return render(request,'blog/about.html',{'title':'about'})



def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched',"")
        books = Post.objects.filter(title__contains=searched)
        return render(request,'blog/search.html',{'title':'search','searched':searched,'books':books})
    else:
        return render(request,'blog/search.html',{'title':'search'})        

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'add_comment.html'
    
    form_class = CommentForm

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)
    def get_success_url(self):

        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


def favourites(request):
    posts = []
    for post in Post.objects.all():
        if request.user in post.favourite.all():
            posts.append(post)
    posts.reverse()
    context = {
        'posts' : posts
    }
    return render(request,'blog/favourites.html',context)

@csrf_exempt
def StarView(request):
    x = []
    if("id" in request.POST):
        curr_post = get_object_or_404(Post, id=request.POST.get('id'))
        if request.user not in curr_post.favourite.all():
            curr_post.favourite.add(request.user)
        else:
            curr_post.favourite.remove(request.user)
        x = list(curr_post.favourite.all())

    return HttpResponse(len(x))


@csrf_exempt
def StarView2(request):
    x = []
    check = False
    if("id" in request.POST):
        curr_post = get_object_or_404(Post, id=request.POST.get('id'))
        if request.user in curr_post.favourite.all():
            check = True
    return HttpResponse(check)