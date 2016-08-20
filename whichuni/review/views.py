from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404

from .models import University, UniReview, Subject

# Index page for the website
def index(request):
    return render(request, 'review/index.html')

# Returns a list of subjects
def subject(request):
    subjects = Subject.objects.order_by('subject_name')
    template = loader.get_template('review/subjects.html')
    context = {
        'subjects': subjects,
    }
    return HttpResponse(template.render(context, request))

# Returns a list of universities
def uni(request):
    unis = University.objects.order_by('uni_name')
    template = loader.get_template('review/universities.html')
    context = {
        'unis': unis,
    }
    return HttpResponse(template.render(context, request))

# Returns reviews for the university
def review_uni(request,uni_id):
    return render(request, 'review/index.html')

# Returns reviews for the subject
def review_subject(request,subject_id):
    return render(request, 'review/index.html')

def review_uni_subject(request, uni_id, subject_id):
    return render(request, 'review/index.html')
