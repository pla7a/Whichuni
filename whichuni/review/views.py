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
    try:
        uni = University.objects.get(pk=uni_id)
        reviews = UniReview.objects.filter(university=uni)

    except University.DoesNotExist:
        raise Http404("University does not exist")

    return render(request, 'review/review_uni.html', {'university': uni, 'reviews':reviews})


# Returns reviews for the subject
def review_subject(request,subject_id):
    try:
        subject_name = Subject.objects.get(pk=subject_id)
        reviews = UniReview.objects.filter(subject=subject_name)

    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")

    return render(request, 'review/review_subject.html', {'subject': subject_name, 'reviews':reviews})


def review_uni_subject(request, uni_id, subject_id):
    return render(request, 'review/index.html')
