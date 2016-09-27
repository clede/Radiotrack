from django.db import models

class Program(models.Model):
    """A radio program to be tracked."""
    title = models.CharField(max_length=200)
    channel = models.CharField(max_length=40, blank=True)

    # Days of the week.
    mon = models.BooleanField()
    tue = models.BooleanField()
    wed = models.BooleanField()
    thu = models.BooleanField()
    fri = models.BooleanField()
    sat = models.BooleanField()
    sun = models.BooleanField()

    # Time (PT).
    # No attempt to account for DST, or time zones.
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
