from django.shortcuts import render, redirect
from .models import front_end
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    if front_end.objects.all():
        data = front_end.objects.all()
        paginator = Paginator(data, 6)
        page_number = request.GET.get('page')
        data = paginator.get_page(page_number)
        if request.session.get("message"):
            msg = request.session.get("message")
            return render(request, 'home.html', {'data': data, 'msg': msg})
        else:
            return render(request, 'home.html', {'data': data})

    else:
        data = "0"
        return render(request, 'home.html', {'data': data})


def save(request):
    if request.method == "POST":
        nm = request.POST['title']
        tg = request.POST['tag']
        nt = request.POST['note']
        front_end(note_title=nm, tag_line=tg, note=nt).save()
        return redirect(home)


def update(request):
    if request.method == "POST":
        title_edit = request.POST['title_edit']
        tag_edit = request.POST['tag_edit']
        note_edit = request.POST['note_edit']
        if front_end.objects.filter(note_title=title_edit):
            front_end.objects.filter(note_title=title_edit).update(note_title=title_edit, tag_line=tag_edit,
                                                                   note=note_edit)
            Messages = "data Update"
            request.session["message"] = Messages
            return redirect('home')
        else:
            Messages = "data Not Found"
            request.session["message"] = Messages
            return redirect('home')
    else:
        return redirect('home')


