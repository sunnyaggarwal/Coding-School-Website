from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Tutorial
from .models import Topic
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.shortcuts import render
from .models import Author
from .forms import TutorialForm

def tut1(request):
	#tutorials = Tutorials.objects.all()
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    #contents = Tutorials.objects.filter(contentId__contentId=12345)
    return render(request, 'nittutorial/check.html', {'tutorials': tutorials})
def forums(request):
    #tutorials = Tutorials.objects.all()
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    #contents = Tutorials.objects.filter(contentId__contentId=12345)
    return render(request, 'nittutorial/forums.html', {'tutorials': tutorials})
def blogs(request):
    #tutorials = Tutorials.objects.all()
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    #contents = Tutorials.objects.filter(contentId__contentId=12345)
    return render(request, 'nittutorial/blogs.html', {'tutorials': tutorials})
def contributors(request):
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/contributors.html',{'tutorials': tutorials})
def about(request):
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/about.html',{'tutorials': tutorials})
def contact(request):
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/contact.html',{'tutorials': tutorials})

def manage_authors(request):
    AuthorFormSet = modelformset_factory(Author, fields=('name', 'title','birth_date'))
    if request.method == "POST":
        formset = AuthorFormSet(request.POST, request.FILES,
                                queryset=Author.objects.filter(name__startswith='O'))
        if formset.is_valid():
            formset.save()
            # Do something.
    else:
        formset = AuthorFormSet(queryset=Author.objects.filter(name__startswith='O'))
    return render(request, 'nittutorial/registration.html', {'formset': formset})

def post_content(request, title, id):
    tutorial = get_object_or_404(Tutorial, pk=id)
    tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'nittutorial/post_content.html', { 'tutorials': tutorials, 'tutorial': tutorial})

def tutorial_new(request):
    if request.method == "POST":
        form = TutorialForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publishedDate = timezone.now()
            post.save()
            tutorials = Tutorial.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
            print(tutorials)
            return redirect('post_content', title=post.title, id=post.pk)
    else:
        form = TutorialForm()
    return render(request, 'nittutorial/post_edit.html', {'form': form})
