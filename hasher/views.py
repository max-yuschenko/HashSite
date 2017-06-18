from django.shortcuts import render, redirect
from django.http import HttpResponse

from hasher.forms import UploadFileForm
from hasher.models import Document

import hashlib

def home(request):
    documents = Document.objects.all()
    return render(request, 'hasher/home.html', {'documents': documents, 'count_of_prev_uploaded': ""})


# Create your views here.
def handle_file(file):
    newfile = Document(document=file)

    filepath = 'documents/tmp/somefile'
    with open(filepath, 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)

    newfile.sha = get_hash(filepath)

    newfile.save()

    q = Document.objects.filter(sha__exact=newfile.sha)

    count_of_coincidence = 0

    if q.count() - 1 > 0:
        
        with open(q[q.count() - 1].document.name) as comp_f:
            comp_content = comp_f.read()


        for elem in q[:q.count() - 1]:
            with open(elem.document.name, "r") as f:
                text = f.read()
                if comp_content == text:
                    count_of_coincidence += 1

    return count_of_coincidence


def get_hash(file):
    hasher = hashlib.sha256()
    # file = Document(document=file)
    with open(file, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)

    return hasher.hexdigest()


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            count = handle_file(request.FILES['document'])
            documents = Document.objects.all()
            return render(request, 'hasher/home.html', {'documents': documents, 'count_of_prev_uploaded': count})
            #return HttpResponse('home')
    else:
        form = UploadFileForm()
    return render(request, 'hasher/upload.html', {'form': form})
