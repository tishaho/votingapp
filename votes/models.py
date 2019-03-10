from django.db import models

# Create your models here.
class Partylist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                    related_name='candidates',
                                    blank=True, null=True)
    partylist = models.ForeignKey(Partylist, on_delete=models.CASCADE,
                                    related_name='partylist',
                                    blank=True, null=True)
    birthdate = models.DateField()
    platform = models.TextField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(blank=True, null=True, upload_to="images/")

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Vote(models.Model):
        # class Meta:
        #     unique_m = (('userprofile', 'suggestedName'),)
        #     userprofile = models.ForeignKey(UserProfile)
        #     suggestedName = models.ForeignKey(suggestedName)
        #     event = models.ForeignKey(Event)

        #     def post(self, request, *args, **kwargs)
            
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE,
                                    related_name='votes')
    vote_datetime = models.DateTimeField(auto_now_add=True),