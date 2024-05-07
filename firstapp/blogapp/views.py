from django.shortcuts import render, redirect
from django.http import HttpResponse as HT
from .forms import BlogPostForm


# Create your views here.


def home(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)  # Create a form instance with submitted data
        if form.is_valid():
            # Process valid form data here (e.g., save to database, send email)
            title = form.cleaned_data['blog_title']
            author = form.cleaned_data['author_name']
            content = form.cleaned_data['blog_content']
            # return redirect('home')  # Redirect to a 'success' page
    else:
        form = BlogPostForm()  # Create a blank form

    context = {'form': form}
    return render(request, 'blog.html', context)
