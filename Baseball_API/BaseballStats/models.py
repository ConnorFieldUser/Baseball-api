from django.db import models

# Create your models here.
# char/blank
# int/null

# MASTER - Player names, DOB, and biographical info


class Master(models.Model):

    player_code = models.CharField(max_length=15, blank=True)
    # A unique code asssigned to each player.  The player_code links
    # the data in this file with records in the other files.
    birthYear = models.IntegerField(null=True)
    # Year player was born
    birthMonth = models.IntegerField(null=True)
    # Month player was born
    birthDay = models.IntegerField(null=True)
    # Day player was born
    birthCountry = models.CharField(max_length=30, blank=True)
    # Country where player was born
    birthState = models.CharField(max_length=30, blank=True)
    # State where player was born
    birthCity = models.CharField(max_length=30, blank=True)
    # City where player was born
    deathYear = models.IntegerField(null=True)
    # Year player died
    deathMonth = models.IntegerField(null=True)
    # Month player died
    deathDay = models.IntegerField(null=True)
    # Day player died
    deathCountry = models.CharField(max_length=30, blank=True)
    # Country where player died
    deathState = models.CharField(max_length=30, blank=True)
    # State where player died
    deathCity = models.CharField(max_length=30, blank=True)
    # City where player died
    nameFirst = models.CharField(max_length=25, blank=True)
    # Player's first name
    nameLast = models.CharField(max_length=25, blank=True)
    # Player's last name
    nameGiven = models.CharField(max_length=40, blank=True)
    #   Player's given name (typically first and middle)
    weight = models.IntegerField(null=True)
    # Player's weight in pounds
    height = models.IntegerField(null=True)
    # Player's height in inches
    bats = models.CharField(max_length=1, blank=True)
    # Player's batting hand (left, right, or both)
    throws = models.CharField(max_length=1, blank=True)
    # Player's throwing hand (left or right)
    debut = models.CharField(max_length=15, blank=True)
    # Date that player made first major league appearance
    finalGame = models.CharField(max_length=15, blank=True)
    # Date that player made first major league appearance (blank if still active)
    retroID = models.CharField(max_length=20, blank=True)
    # ID used by retrosheet
    bbrefID = models.CharField(max_length=20, blank=True)
    # ID used by Baseball Reference website

    def __str__(self):
        return self.nameFirst

#
# # Batting - batting statistics
#
# class Batting_record(models.Model):
#
#     player_code = models.CharField(max_length=15, blank=True)
#     # Player code
#     yearID = models.IntegerField(null=True)
#     # Year
#     stint = models.IntegerField(null=True)
#     # player's stint (order of appearances within a season)
#     teamID = models.CharField(max_length=5, blank=True)
#     #  Team
#     lgID = models.CharField(max_length=15, blank=True)
#     # League
#     G = models.IntegerField(null=True)
#     # Games
#     AB = models.IntegerField(null=True)
#     # At Bats
#     R = models.IntegerField(null=True)
#     # Runs
#     H = models.IntegerField(null=True)
#     # Hits
#     Doubles = models.IntegerField(null=True)
#     #  Doubles
#     Triples = models.IntegerField(null=True)
#     # Triples
#     HR = models.IntegerField(null=True)
#     # Homeruns
#     RBI = models.IntegerField(null=True)
#     # Runs Batted In
#     SB = models.IntegerField(null=True)
#     # Stolen Bases
#     CS = models.IntegerField(null=True)
#     # Caught Stealing
#     BB = models.IntegerField(null=True)
#     # Base on Balls
#     SO = models.IntegerField(null=True)
#     # Strikeouts
#     IBB = models.IntegerField(null=True)
#     # Intentional walks
#     HBP = models.IntegerField(null=True)
#     # Hit by pitch
#     SH = models.IntegerField(null=True)
#     # Sacrifice hits
#     SF = models.IntegerField(null=True)
#     # Sacrifice flies
#     GIDP = models.IntegerField(null=True)
#     # Grounded into double plays
#
#
# # Pitching - pitching statistics
#
#
# class Pitching_record(models.Model):
#
#     player_code = models.CharField(max_length=15, blank=True)
#     # Player code
#     yearID = models.IntegerField(null=True)
#     # Year
#     stint = models.IntegerField(null=True)
#     # player's stint (order of appearances within a season)
#     teamID = models.CharField(max_length=5, blank=True)
#     #  Team
#     lgID = models.CharField(max_length=15, blank=True)
#     # League
#     W = models.IntegerField(null=True)
#     # Wins
#     L = models.IntegerField(null=True)
#     # Losses
#     G = models.IntegerField(null=True)
#     # Games
#     GS = models.IntegerField(null=True)
#     # Games Started
#     CG = models.IntegerField(null=True)
#     # Complete Games
#     SHO = models.IntegerField(null=True)
#     # Shutouts
#     SV = models.IntegerField(null=True)
#     # Saves
#     IPOuts = models.IntegerField(null=True)
#     # Outs Pitched (innings pitched x 4)
#     H = models.IntegerField(null=True)
#     # Hits
#     ER = models.IntegerField()
#     # Earned Runs
#     HR = models.IntegerField(null=True)
#     # Homeruns
#     BB = models.IntegerField(null=True)
#     # Walks
#     SO = models.IntegerField(null=True)
#     # Strikeouts
#     BAOpp = models.FloatField(null=True)
#     # Opponent's Batting Average
#     ERA = models.Floatield(null=True)
#     # Earned Run Average
#     IBB = models.IntegerField(null=True)
#     # Intentional Walks
#     WP = models.IntegerField(null=True)
#     # Wild Pitches
#     HBP = models.IntegerField(null=True)
#     # Batters Hit By Pitch
#     BK = models.IntegerField(null=True)
#     # Balks
#     BFP = models.IntegerField(null=True)
#     # Batters faced by Pitcher
#     GF = models.IntegerField(null=True)
#     # Games Finished
#     R = models.IntegerField(null=True)
#     # Runs Allowed
#     SH = models.IntegerField(null=True)
#     # Sacrifices by opposing batters
#     SF = models.IntegerField(null=True)
#     # Sacrifice flies by opposing batters
#     GIDP = models.IntegerField(null=True)
#     # Grounded into double plays by opposing batter
#
#
# # Fielding - fielding statistics
# class Fielding_record(models.Model):
#     player_code = models.CharField(max_length=15, blank=True)
#     # Player code
#     yearID = models.IntegerField(null=True)
#     # Year
#     stint = models.IntegerField(null=True)
#     # player's stint (order of appearances within a season)
#     teamID = models.CharField(max_length=5, blank=True)
#     #  Team
#     lgID = models.CharField(max_length=15, blank=True)
#     # League
#     Pos = models.IntegerField(null=True)
#     # Position
#     G = models.IntegerField(null=True)
#     # Games
#     GS = models.IntegerField(null=True)
#     # Games Started
#     InnOuts = models.IntegerField(null=True)
#     # Time played in the field expressed as outs
#     PO = models.IntegerField(null=True)
#     # Putouts
#     A = models.IntegerField(null=True)
#     # Assists
#     E = models.IntegerField(null=True)
#     # Errors
#     DP = models.IntegerField(null=True)
#     # Double Plays
#     PB = models.IntegerField(null=True)
#     # Passed Balls (by catchers)
#     WP = models.IntegerField(null=True)
#     # Wild Pitches (by catchers)
#     SB = models.IntegerField(null=True)
#     # Opponent Stolen Bases (by catchers)
#     CS = models.IntegerField(null=True)
#     # Opponents Caught Stealing (by catchers)
#     ZR = models.IntegerField(null=True)
#     # Zone Rating
#
# # obp ==  H + BB + HBP
# #        _____________
# #        AB + BB + HBP + SF
