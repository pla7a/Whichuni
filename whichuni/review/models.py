from django.db import models


# Table for list of universities
class University(models.Model):
    class Meta:
        verbose_name_plural = "Universities"
    uni_name = models.CharField(max_length=50)
    def __str__(self):
        return self.uni_name

# Table for subjects
class Subject(models.Model):

    subject_name = models.CharField(max_length=50)
    def __str__(self):
        return self.subject_name

# Table for the reviews
class UniReview(models.Model):
    YEARS = (
        (2000,"2000"),
        (2001,"2001"),
        (2002,"2002"),
        (2003,"2003"),
        (2004,"2004"),
        (2005,"2005"),
        (2006,"2006"),
        (2007,"2007"),
        (2008,"2008"),
        (2009,"2009"),
        (2010,"2010"),
        (2011,"2011"),
        (2012,"2012"),
        (2013,"2013"),
        (2014,"2014"),
        (2015,"2015"),
        (2016,"2016"),
    )

    RATING = (
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
        (6,"6"),
        (7,"7"),
        (8,"8"),
        (9,"9"),
        (10,"10"),

    )

    CURRENT = (
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
    )

    university = models.ForeignKey(University, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    year_started = models.IntegerField(choices=YEARS)
    current_year = models.IntegerField(choices=CURRENT)
    review = models.CharField(max_length=300)
    rating = models.IntegerField(choices=RATING)
    email = models.EmailField()

    def __str__(self):
        return str(self.id)
