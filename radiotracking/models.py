from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import pytz

# Helper functions
def get_streaks(iter):
    """Given an iterable, detect any consecutive True values. Returns a zip
    object of the start and end indices of each streak."""
    # There's gotta be a better way to do this...
    in_streak = False
    starts = []
    ends = []
    for i, val in enumerate(iter):
        # Starting point of a streak
        if val and not in_streak:
            starts.append(i)
            in_streak = True
        # Ending point of a streak
        elif in_streak and not val:
            ends.append(i-1)
            in_streak = False
    # If in streak at the end, the last index is an ending point.
    if in_streak:
        ends.append(len(iter) - 1)
    return zip(starts, ends)


class Station(models.Model):
    """A radio station."""
    TZ_CHOICES = [(tz, tz.replace('_', ' ')) for tz in pytz.all_timezones]
    BAND_CHOICES = ( ('AM', 'AM'),
                     ('FM', 'FM'),
                     ('NA', 'None') )

    name = models.CharField(max_length=40)
    website = models.URLField(max_length=300, blank=True, default='')
    stream_url = models.URLField(max_length=400, blank=True, default='')
    band = models.CharField(max_length=2, choices=BAND_CHOICES, default='NA')
    # Storing frequency as a string right now, as it is only used for
    # displaying to the user.
    # Consider changing it to a number later.
    freq = models.CharField(max_length=5, blank=True, default='')
    location = models.CharField(max_length=200, blank=True, default='')
    tz = models.CharField(max_length=32,
        choices=TZ_CHOICES,
        # Currently defaults to America/Los_Angeles, but ultimately should
        # default to the current user's time zone.
        default='America/Los_Angeles')

class Program(models.Model):
    """A radio program to be tracked."""
    TZ_CHOICES = [(tz, tz.replace('_', ' ')) for tz in pytz.all_timezones]
    title = models.CharField(max_length=200)

    # Station is currently a string, but eventually we need to change it to
    # an actual station entry in the database.
    station = models.CharField(max_length=40, blank=True)
    tz = models.CharField(max_length=32,
        choices=TZ_CHOICES,
        # Currently defaults to America/Los_Angeles, but ultimately should
        # default to the current user's time zone.
        default='America/Los_Angeles')

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

    owner = models.ForeignKey(User)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    def set_day_string(self):
        """Generates and stores a proper string representing the days of the
        week this program occurs."""
        days = (self.mon, self.tue, self.wed, self.thu, self.fri, self.sat,
            self.sun)
        day_names = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
        if all(days):
            self.day_string = 'Daily'
        else:
            streaks = get_streaks(days)
            result_text = []

            for start, end in streaks:
                if start == end:
                    # A single-day "streak"
                    result_text.append(day_names[start])
                else:
                    result_text.append(day_names[start] + '-' + day_names[end])
            self.day_string = ', '.join(result_text)

    def save(self, *args, **kwargs):
        """Overriding the save method to automatically populate the day_string
        field, based on the individual days checked/unchecked."""
        self.set_day_string()
        super(Program, self).save(*args, **kwargs)
