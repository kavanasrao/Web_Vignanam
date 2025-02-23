from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Reply
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required

@login_required
def feed(request, post_id=None):
    posts = Post.objects.all().order_by('-content_at')  # Fetch all posts, ordered by latest
    post_form = PostForm(request.POST or None, request.FILES or None)
    reply_form = ReplyForm(request.POST or None)

    
    if request.method == 'POST' and 'post_submit' in request.POST:
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user  
            post.save()
            return redirect('feed')

    
    post = None
    replies = None
    if post_id:
        post = get_object_or_404(Post, id=post_id)
        replies = post.replies.filter(parent__isnull=True)  

        if request.method == 'POST' and 'reply_submit' in request.POST:
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.user = request.user  
                reply.post = post  

               
                parent_id = request.POST.get('parent_id')
                if parent_id:
                    reply.parent = Reply.objects.get(id=parent_id)

                reply.save()
                return redirect('feed', post_id=post.id)

    return render(request, 'feed.html', {
        'posts': posts,
        'post_form': post_form,
        'post': post,
        'replies': replies,
        'reply_form': reply_form,
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    replies = post.replies.filter(parent__isnull=True)
    reply_form = ReplyForm(request.POST or None)

    
    if request.method == 'POST' and 'reply_submit' in request.POST:
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.user = request.user
            reply.post = post

            parent_id = request.POST.get('parent_id')
            if parent_id:
                reply.parent = Reply.objects.get(id=parent_id)

            reply.save()
            return redirect('post_detail', id=post.id)

    return render(request, 'feed_detail.html', {
        'post': post,
        'replies': replies,
        'reply_form': reply_form,
    })
