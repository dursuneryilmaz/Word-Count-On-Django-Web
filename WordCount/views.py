# coding=utf-8
from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from WordCount.forms import WordCountForm
from WordCount.models import WordCount
import word_count_core

# Create your views here.
def index(request):
    word_counts = WordCount.objects.all()
    context = {
        'wcs': word_counts
    }
    return render(request, 'WordCount/index.html', context)


def detail(request, idx):
    wc = WordCount.objects.get(id=idx)

    return render(request, 'WordCount/detail.html', {'wc': wc})


def create(request):
    if request.method == 'POST':
        wc = WordCountForm(request.POST, request.FILES)
        if wc.is_valid():
            #wc.save(commit=False)
            wc.save()
            return redirect('WordCount:index')
    else:
        wc = WordCountForm()
        return render(request, 'WordCount/create.html', {'form': wc})


def edit(request, id):
    return HttpResponse("Edit")


def run(request, idx):
    wc = WordCount.objects.get(id=idx)
    lines, words = word_count_core.count(wc.app_name, str(wc.file.path))
    wc.lines = lines
    wc.words = words
    wc.active = True
    wc.save()
    return redirect('WordCount:detail', idx)


def delete(request, idx):
    wc = WordCount.objects.get(id=idx)
    wc.delete()
    return redirect('WordCount:index')

