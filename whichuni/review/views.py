from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .forms import searchForm, submitForm

from .models import University, UniReview, Subject

# Index page for the website
def index(request):
    return render(request, 'review/index.html')

def contact(request):
    return render(request, 'review/contact.html')

def search(request):
    form = searchForm(request.POST or None)

    return render(request, 'review/search.html',{'form':form})

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

# Allows user to search by university and subject
def review_uni_subject(request):
    form = searchForm(request.POST)
    if form.is_valid():
        i1 = form.cleaned_data['university']
        i2 = form.cleaned_data['subject']


        reviews = UniReview.objects.filter(university=i1, subject=i2)
        if reviews:
            return render(request, 'review/searchresults.html', {'reviews':reviews,'university':i1,'subject':i2})
        else:
            return render(request, 'review/notfound.html', {'subject':i2,'university':i1})

    else:
        return render(request, 'review/searcherror.html')



# Displays submit form
def submit(request):
    form = submitForm(request.POST or None)

    return render(request, 'review/submit.html',{'form':form})

# Cleans data from the submitted form and allows it to be inputted into the table
def submitted(request):
    form = submitForm(request.POST)
    if form.is_valid():
        i1 = form.cleaned_data['university']
        i2 = form.cleaned_data['subject']
        i3 = form.cleaned_data['year_started']
        i4 = form.cleaned_data['current_year']
        i5 = form.cleaned_data['review']
        i6 = form.cleaned_data['rating']
        i7 = form.cleaned_data['email']
        p = UniReview(university=i1,subject=i2,year_started=i3,current_year=i4,review=i5,rating=i6,email=i7)
        p.save()

        url = "/u/" + str(i1.id)
        return render(request, 'review/submitted.html',{'url':url})

    else:
        return render(request, 'review/error.html')
