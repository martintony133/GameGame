# Ensure all models (including CommunityCategory) are imported here!
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import CommunityCategory, CommunityPost, CommunityComment


# 1. Main Landing Portal View: Fetches all threads for home.html
def community_home_view(request):
    posts = CommunityPost.objects.all().order_by('-created_at')
    return render(request, 'community/home.html', {'posts': posts})

# 2. Individual Thread Detail View: Loads a single thread webpage
def post_detail_view(request, post_id):
    post = get_object_or_404(CommunityPost, id=post_id)
    comments = post.comments.all()
    return render(request, 'community/post_detail.html', {'post': post, 'comments': comments})

# 3. HTMX Polling Endpoint: Serves raw comment list snippet every 2 seconds
def comment_list_view(request, post_id):
    post = get_object_or_404(CommunityPost, id=post_id)
    comments = post.comments.all()
    return render(request, 'community/partials/comment_list.html', {'comments': comments})

# 4. HTMX Submission Endpoint: Saves incoming comment and appends live block
def add_comment_view(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(CommunityPost, id=post_id)
        content = request.POST.get('content')
        
        if request.user.is_authenticated:
            comment = CommunityComment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
            return HttpResponse(f"""
                <div style="border-bottom: 1px solid #eee; padding: 10px 0;">
                    <p><strong>{comment.author.username}</strong>:</p>
                    <p>{comment.content}</p>
                    <small style="color: gray;">Just now</small>
                </div>
            """)
        else:
            return HttpResponse("Please log in to leave a comment.", status=401)

def post_create_view(request):
    # Security block: redirect anonymous users to prevent form submission crashes
    if not request.user.is_authenticated:
        return HttpResponse("Please log in via the admin panel before creating a post.", status=401)

    if request.method == "POST":
        category_id = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        # Pull the matching category object record
        category_obj = get_object_or_404(CommunityCategory, id=category_id)
        
        # Save into database layout mappings
        CommunityPost.objects.create(
            category=category_obj,
            author=request.user,
            title=title,
            content=content
        )
        # Smoothly send the user back to home.html to view their brand new entry card
        return redirect('community:community_home')

    # GET request handler: feeds category variants down to form select dropdown choice options
    categories = CommunityCategory.objects.all()
    return render(request, 'community/post_create.html', {'categories': categories})
