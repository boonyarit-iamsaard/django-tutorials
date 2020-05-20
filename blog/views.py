from django.shortcuts import render

posts = [
    {
        "author": "BoonyaritI",
        "title": "Blog Post 1",
        "content": "content 1",
        "date_posted": "May 20, 2020",
    },
    {
        "author": "BoonyaritI",
        "title": "Blog Post 2",
        "content": "content 2",
        "date_posted": "May 20, 2020",
    },
]

# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
