from django.shortcuts import render, redirect
from .models import front_end
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = front_end.objects.all()
    paginator = Paginator(data, 6)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    context = {
        'data': data,
    }
    return render(request, 'home.html', context)


def save(request):
    if request.method == "POST":
        nm = request.POST['nm']
        tg = request.POST['tg']
        nt = request.POST['nt']
        front_end(note_title=nm, tag_line=tg, note=nt).save()
        return redirect('home')


def update(request, id):
    if request.method == 'POST':
        nm = request.POST['nm']
        tg = request.POST['tg']
        nt = request.POST['nt']
        front_end(id=id, note_title=nm, tag_line=tg, note=nt).save()
        return redirect('home')

    return redirect(request, 'home.html')


def edit(request):
    data = front_end.objects.all()
    context = {
        'data': data,
    }
    return redirect(request, 'home.html', context)


def delete(request, id):
    data = front_end.objects.filter(id=id)
    data.delete()
    context = {
        'data': data,
    }
    return redirect('home')
