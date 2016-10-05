from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Station(models.Model):
    """A radio station."""
    # Still working on clarifying what fields need to be here.
    # - Name
    # - URL
    # - Terrestrial Band: AM or FM
    # - Terrestrial frequency


class Program(models.Model):
    """A radio program to be tracked."""
    title = models.CharField(max_length=200)
    station = models.CharField(max_length=40, blank=True)

    # Days of the week.
    mon = models.BooleanField()
    tue = models.BooleanField()
    wed = models.BooleanField()
    thu = models.BooleanField()
    fri = models.BooleanField()
    sat = models.BooleanField()
    sun = models.BooleanField()

    # String representation of days of the week.
    day_string = models.CharField(default='', max_length=30)

    # Time (PT).
    # No attempt to account for DST, or time zones.
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    def save(self, *args, **kwargs):
        """Overriding the save method to automatically populate the day_string
        field, based on the individual days checked/unchecked."""
        weekdays = (self.mon, self.tue, self.wed, self.thu, self.fri)
        weekends = (self.sat, self.sun)
        days =     (self.mon, self.tue, self.wed, self.thu, self.fri,
                    self.sat, self.sun)
        day_names = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

        if all(days):
            self.day_string = 'Daily'
        elif all(weekdays) and not any(weekends):
            self.day_string = 'Mon-Fri'
        elif all(weekends) and not any(weekdays):
            self.day_string = 'Sat-Sun'
        else:
            # Build a string of the selected days, if they aren't one of the
            # three common patterns above.
            day_names = zip(days, day_names)
            day_list = [d[1] for d in day_names if d[0]]
            self.day_string = ', '.join(day_list)
        super(Program, self).save(*args, **kwargs)
