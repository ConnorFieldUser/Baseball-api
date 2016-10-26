from django.db import models

# Create your models here.
# char/blank
# int/null

# MASTER - Player names, DOB, and biographical info


class MASTER(models.Model):
    playerID = models.IntegerField()
    # A unique code asssigned to each player.  The playerID links
    # the data in this file with records in the other files.
    birthYear = models.IntegerField()
    # Year player was born
    birthMonth = models.IntegerField()
    # Month player was born
    birthDay = models.IntegerField()
    # Day player was born
    birthCountry = models.CharField(max_length=30)
    # Country where player was born
    birthState = models.CharField(max_length=30)
    # State where player was born
    birthCity = models.CharField(max_length=30)
    # City where player was born
    deathYear = models.IntegerField(max_length=30)
    # Year player died
    deathMonth = models.IntegerField(max_length=30)
    # Month player died
    deathDay = models.IntegerField()
    # Day player died
    deathCountry = models.CharField()
    # Country where player died
    deathState = models.CharField(max_length=30)
    # State where player died
    deathCity = models.CharField(max_length=30)
    # City where player died
    nameFirst = models.CharField(max_length=25)
    # Player's first name
    nameLast = models.CharField(max_length=25)
    # Player's last name
    nameGiven = models.CharField(max_length=40)
    #   Player's given name (typically first and middle)
    weight = models.IntegerField()
    # Player's weight in pounds
    height = models.IntegerField()
    # Player's height in inches
    bats = models.CharField(max_length=1)
    # Player's batting hand (left, right, or both)
    throws = models.CharField(max_length=1)
    # Player's throwing hand (left or right)
    debut = models.CharField(max_length=15)
    # Date that player made first major league appearance
    finalGame = models.CharField(max_length=15)
    # Date that player made first major league appearance (blank if still active)
    retroID = models.CharField(max_length=20)
    # ID used by retrosheet
    bbrefID = models.CharField(max_length=20)
    # ID used by Baseball Reference website

    def __str__(self):
        return self.nameFirst

# Batting - batting statistics
# Pitching - pitching statistics
# Fielding - fielding statistics
#
# obp ==  H + BB + HBP
#        _____________
#        AB + BB + HBP + SF
