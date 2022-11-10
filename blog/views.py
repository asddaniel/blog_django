from django.shortcuts import redirect, render
from django.http import HttpResponse
from blog.models import Article
from blog.forms import CommentForm, CommentOriginalForm
from blog.models import Comment
# Create your views here.

 


def home(request):

    articles = Article.objects.all()
    data ='<br>'.join([str(a.title) for a in articles])
    
    text = """<h1>Bienvenue sur mon blog !</h1> <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(data)

def hello(request):
    articles = Article.objects.all()
    return render(request, 'blog/layout.html', {'articles': articles})

def article(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=article)
    return render(request, 'blog/article.html', {'article': article, 'comments': comments})

def comment(request, id):
    form = CommentForm(request.POST)
    article = Article.objects.get(id=id)
    
    return render(request, 'blog/comment.html', {'article': article, 'form': form})

def treat_comment(request, id):
    form = CommentForm(request.POST)
    article = Article.objects.get(id=id)
    if form.is_valid():
        comment = Comment(article=article, user=form.cleaned_data['user'], content=form.cleaned_data['content'])
        # comment = Comment.objects.create(id, form.cleaned_data['content'], form.cleaned_data['user'])
        comment.save()

        return redirect('article', id=id)
    else:
        return render(request, 'blog/comment.html', {'article': article, 'form': form})

def modify_comment(request, id):
    comment = Comment.objects.get(id=id)
    form = CommentOriginalForm(instance=comment)
    
    
    return render(request, 'blog/modify_commentaire.html', {'form': form})
    