# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    phone = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'customer'


class Movie(models.Model):
    movie_id = models.IntegerField(db_column='movie_ID', primary_key=True)  # Field name made lowercase.
    title_ch = models.CharField(max_length=50, blank=True, null=True)
    title_en = models.CharField(max_length=50, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    info = models.CharField(max_length=500, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    rating = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class Seat(models.Model):
    show_id = models.IntegerField(primary_key=True)  # The composite primary key (show_id, row, col) found, that is not supported. The first column is selected.
    row = models.CharField(max_length=5)
    col = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seat'
        unique_together = (('show_id', 'row', 'col'),)


class Shows(models.Model):
    show_id = models.IntegerField(db_column='show_ID', primary_key=True)  # Field name made lowercase.
    movie_id = models.ForeignKey(Movie, models.DO_NOTHING, db_column='movie_ID', blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(max_length=10, blank=True, null=True)
    room = models.IntegerField(blank=True, null=True)
    show_time = models.DateTimeField(blank=True, null=True)
    remain_seat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shows'


class Theater(models.Model):
    branch = models.CharField(primary_key=True, max_length=10)
    room_num = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theater'


class Ticket(models.Model):
    verify_code = models.CharField(primary_key=True, max_length=6)
    phone = models.CharField(max_length=10, blank=True, null=True)
    show = models.ForeignKey(Shows, models.DO_NOTHING, db_column='show_ID', blank=True, null=True)  # Field name made lowercase.
    seat_row = models.CharField(max_length=5, blank=True, null=True)
    seat_col = models.IntegerField(blank=True, null=True)
    booking_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'
