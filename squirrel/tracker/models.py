from django.db import models

class Squirrel(models.Model):
    longitude = models.FloatField()

    latitude = models.FloatField()

    unique_squirrel_id = models.CharField(
        max_length=50,
        primary_key=True
    )

#    hectare = models.CharField(
#        max_length=10
#    )

    SHIFT_CHOICES = (
        ('AM','AM'),
        ('PM','PM')
    )

    shift = models.CharField(
        max_length=10,
        choices=SHIFT_CHOICES
    )

    date = models.DateField()

 #   hectare_squirrel_number = models.IntegerField()
    
    AGE_CHOICES = (
        ('Adult','Adult'),
        ('Juvenile','Juvenile'),
    )

    age = models.CharField(
        max_length=10,
        choices=AGE_CHOICES
    )
    
    PRIMARY_FUR_COLOR_CHOICES = (
        ('Gray','Gray'),
        ('Cinnamon','Cinnamon'),
        ('Black','Black'),
    )

    primary_fur_color = models.CharField(
        max_length=10,
        choices=PRIMARY_FUR_COLOR_CHOICES
    )

#    highlight_fur_color = models.CharField(
#        max_length=50,
#        blank=True
#    )

#    combination_of_primary_and = models.CharField(
#        max_length=50,
#        blank=True
#    )

#    color_notes = models.CharField(
#        max_length=200,
#        blank=True
#    )

    LOCATION_CHOICES = (
        ('Ground Plane','Ground Plane'),
        ('Above Ground','Above Ground'),
    )

    location = models.CharField(
        max_length=50,
        choices=LOCATION_CHOICES
    )
    
#    above_ground_sighter = models.CharField(
#        max_length=10,
#        blank=True
#    )

    specific_location = models.CharField(
        max_length=100,
        blank=True
    )

    running = models.BooleanField(default=False)

    chasing = models.BooleanField(default=False)
    
    climbing = models.BooleanField(default=False)
    
    eating = models.BooleanField(default=False)
    
    foraging = models.BooleanField(default=False)
    
    other_activities = models.CharField(
        max_length=200,
        blank=True
    )
    
    kuks = models.BooleanField(default=False)
    
    quaas = models.BooleanField(default=False)
    
    moans = models.BooleanField(default=False)
    
    tail_flags = models.BooleanField(default=False)
    
    tail_twitches = models.BooleanField(default=False)
    
    approaches = models.BooleanField(default=False)
    
    indifferent = models.BooleanField(default=False)
    
    runs_from = models.BooleanField(default=False)
    
#    other_interactions = models.CharField(
#        max_length=200,
#        blank=True
#    )
    
    def __str__(self):
        return self.unique_squirrel_id
