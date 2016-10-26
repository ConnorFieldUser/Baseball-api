from django.db import models

# Create your models here.
# char/blank
# int/null

# MASTER - Player names, DOB, and biographical info


class MASTER(models.Model):

    player_code = models.CharField(max_lengh=15)
    # A unique code asssigned to each player.  The player_code links
    # the data in this file with records in the other files.
    birthYear = models.IntegerField(max_length=4)
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


class Batting_record(models.Model):

    player_code = models.CharField(max_length=15)
    # Player code
    yearID = models.IntegerField(max_length=4)
    # Year
    stint = models.IntegerField(max_length=4)
    # player's stint (order of appearances within a season)
    teamID = models.CharField(max_length=5)
    #  Team
    lgID = models.CharField(max_length=15)
    # League
    G = models.IntegerField(max_length=4)
    # Games
    AB = models.IntegerField(max_length=4)
    # At Bats
    R = models.IntegerField(max_length=4)
    # Runs
    H = models.IntegerField(max_length=4)
    # Hits
    Doubles = models.IntegerField(max_length=4)
    #  Doubles
    Triples = models.IntegerField(max_length=4)
    # Triples
    HR = models.IntegerField(max_length=4)
    # Homeruns
    RBI = models.IntegerField(max_length=4)
    # Runs Batted In
    SB = models.IntegerField(max_length=4)
    # Stolen Bases
    CS = models.IntegerField(max_length=4)
    # Caught Stealing
    BB = models.IntegerField(max_length=4)
    # Base on Balls
    SO = models.IntegerField(max_length=4)
    # Strikeouts
    IBB = models.IntegerField(max_length=4)
    # Intentional walks
    HBP = models.IntegerField(max_length=4)
    # Hit by pitch
    SH = models.IntegerField(max_length=4)
    # Sacrifice hits
    SF = models.IntegerField(max_length=4)
    # Sacrifice flies
    GIDP = models.IntegerField(max_length=4)
    # Grounded into double plays


class Pitching_record(models.Model):

    player_code = models.CharField(max_length=15)
    # Player code
    yearID = models.IntegerField(max_length=4)
    # Year
    stint = models.IntegerField(max_length=4)
    # player's stint (order of appearances within a season)
    teamID = models.CharField(max_length=5)
    #  Team
    lgID = models.CharField(max_length=15)
    # League
    W = models.IntegerField(max_length=4)
    # Wins
    L = models.IntegerField(max_length=4)
    # Losses
    G = models.IntegerField(max_length=4)
    # Games
    GS = models.IntegerField(max_length=4)
    # Games Started
    CG = models.IntegerField(max_length=4)
    # Complete Games
    SHO = models.IntegerField(max_length=4)
    # Shutouts
    SV = models.IntegerField(max_length=4)
    # Saves
    IPOuts = models.IntegerField(max_length=4)
    # Outs Pitched (innings pitched x 4)
    H = models.IntegerField(max_length=4)
    # Hits
    ER = models.IntegerField(max_length=4)
    # Earned Runs
    HR = models.IntegerField(max_length=4)
    # Homeruns
    BB = models.IntegerField(max_length=4)
    # Walks
    SO = models.IntegerField(max_length=4)
    # Strikeouts
    BAOpp = models.FloatField(max_length=4)
    # Opponent's Batting Average
    ERA = models.FieldField(max_length=4)
    # Earned Run Average
    IBB = models.IntegerField(max_length=4)
    # Intentional Walks
    WP = models.IntegerField(max_length=4)
    # Wild Pitches
    HBP = models.IntegerField(max_length=4)
    # Batters Hit By Pitch
    BK = models.IntegerField(max_length=4)
    # Balks
    BFP = models.IntegerField(max_length=4)
    # Batters faced by Pitcher
    GF = models.IntegerField(max_length=4)
    # Games Finished
    R = models.IntegerField(max_length=4)
    # Runs Allowed
    SH = models.IntegerField(max_length=4)
    # Sacrifices by opposing batters
    SF = models.IntegerField(max_length=4)
    # Sacrifice flies by opposing batters
    GIDP = models.IntegerField(max_length=4)
    # Grounded into double plays by opposing batter


class Fielding_record(models.Model):
    player_code = models.CharField(max_length=15)
    # Player code
    yearID = models.IntegerField(max_length=4)
    # Year
    stint = models.IntegerField(max_length=4)
    # player's stint (order of appearances within a season)
    teamID = models.CharField(max_length=5)
    #  Team
    lgID = models.CharField(max_length=15)
    # League
    Pos = models.IntegerField(max_length=4)
    # Position
    G = models.IntegerField(max_length=4)
    # Games
    GS = models.IntegerField(max_length=4)
    # Games Started
    InnOuts = models.IntegerField(max_length=4)
    # Time played in the field expressed as outs
    PO = models.IntegerField(max_length=4)
    # Putouts
    A = models.IntegerField(max_length=4)
    # Assists
    E = models.IntegerField(max_length=4)
    # Errors
    DP = models.IntegerField(max_length=4)
    # Double Plays
    PB = models.IntegerField(max_length=4)
    # Passed Balls (by catchers)
    WP = models.IntegerField(max_length=4)
    # Wild Pitches (by catchers)
    SB = models.IntegerField(max_length=4)
    # Opponent Stolen Bases (by catchers)
    CS = models.IntegerField(max_length=4)
    # Opponents Caught Stealing (by catchers)
    ZR = models.IntegerField(max_length=4)
    # Zone Rating


# Batting - batting statistics
# Pitching - pitching statistics
# Fielding - fielding statistics
#
# obp ==  H + BB + HBP
#        _____________
#        AB + BB + HBP + SF
