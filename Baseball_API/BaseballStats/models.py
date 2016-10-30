from django.db import models

# Create your models here.
# char/blank
# int/null

# MASTER - Player names, DOB, and biographical info


class Master(models.Model):

    playerID = models.CharField(max_length=15, null=True, blank=True)
    # A unique code asssigned to each player.  The player_code links
    # the data in this file with records in the other files.
    birthYear = models.CharField(max_length=15, null=True, blank=True)
    # Year player was born
    birthMonth = models.CharField(max_length=15, null=True, blank=True)
    # Month player was born
    birthDay = models.CharField(max_length=15, null=True, blank=True)
    # Day player was born
    birthCountry = models.CharField(max_length=30, null=True, blank=True)
    # Country where player was born
    birthState = models.CharField(max_length=30, null=True, blank=True)
    # State where player was born
    birthCity = models.CharField(max_length=30, null=True, blank=True)
    # City where player was born
    deathYear = models.CharField(max_length=15, null=True, blank=True)
    # Year player died
    deathMonth = models.CharField(max_length=15, null=True, blank=True)
    # Month player died
    deathDay = models.CharField(max_length=15, null=True, blank=True)
    # Day player died
    deathCountry = models.CharField(max_length=30, null=True, blank=True)
    # Country where player died
    deathState = models.CharField(max_length=30, null=True, blank=True)
    # State where player died
    deathCity = models.CharField(max_length=30, null=True, blank=True)
    # City where player died
    nameFirst = models.CharField(max_length=25, null=True, blank=True)
    # Player's first name
    nameLast = models.CharField(max_length=25, null=True, blank=True)
    # Player's last name
    nameGiven = models.CharField(max_length=40, null=True, blank=True)
    #   Player's given name (typically first and middle)
    weight = models.CharField(max_length=15, null=True, blank=True)
    # Player's weight in pounds
    height = models.CharField(max_length=15, null=True, blank=True)
    # Player's height in inches
    bats = models.CharField(max_length=1, null=True, blank=True)
    # Player's batting hand (left, right, or both)
    throws = models.CharField(max_length=1, null=True, blank=True)
    # Player's throwing hand (left or right)
    debut = models.CharField(max_length=15, null=True, blank=True)
    # Date that player made first major league appearance
    finalGame = models.CharField(max_length=15, null=True, blank=True)
    # Date that player made first major league appearance (blank if still active)
    retroID = models.CharField(max_length=20, null=True, blank=True)
    # ID used by retrosheet
    bbrefID = models.CharField(max_length=20, null=True, blank=True)
    # ID used by Baseball Reference website

    def __str__(self):
        return self.nameFirst


# Batting - batting statistics

class Batting_record(models.Model):

    playerid = models.ForeignKey(Master)
    # player ID
    player_code = models.CharField(max_length=15, null=True,  blank=True)
    # Player code
    yearid = models.CharField(max_length=15, null=True, blank=True)
    # Year
    stint = models.CharField(max_length=15, null=True, blank=True)
    # player's stint (order of appearances within a season)
    teamid = models.CharField(max_length=5, null=True,  blank=True)
    #  Team
    lg = models.CharField(max_length=15, null=True,  blank=True)
    # League
    g = models.CharField(max_length=15, null=True, blank=True)
    # Games
    ab = models.CharField(max_length=15, null=True, blank=True)
    # At Bats
    r = models.CharField(max_length=15, null=True, blank=True)
    # Runs
    h = models.CharField(max_length=15, null=True, blank=True)
    # Hits
    doubles = models.CharField(max_length=15, null=True, blank=True)
    #  Doubles
    triples = models.CharField(max_length=15, null=True, blank=True)
    # Triples
    hr = models.CharField(max_length=15, null=True, blank=True)
    # Homeruns
    rbi = models.CharField(max_length=15, null=True, blank=True)
    # Runs Batted In
    sb = models.CharField(max_length=15, null=True, blank=True)
    # Stolen Bases
    cs = models.CharField(max_length=15, null=True, blank=True)
    # Caught Stealing
    bb = models.CharField(max_length=15, null=True, blank=True)
    # Base on Balls
    so = models.CharField(max_length=15, null=True, blank=True)
    # Strikeouts
    ibb = models.CharField(max_length=15, null=True, blank=True)
    # Intentional walks
    hbp = models.CharField(max_length=15, null=True, blank=True)
    # Hit by pitch
    sh = models.CharField(max_length=15, null=True, blank=True)
    # Sacrifice hits
    sf = models.CharField(max_length=15, null=True, blank=True)
    # Sacrifice flies
    gidp = models.CharField(max_length=15, null=True, blank=True)
    # Grounded into double plays


# # Pitching - pitching statistics
#
#
# class Pitching_record(models.Model):
#
#     player_code = models.CharField(max_length=15, null=True, blank=True)
#     # Player code
#     yearID = models.CharField(max_length=15, null=True, blank=True)
#     # Year
#     stint = models.CharField(max_length=15, null=True, blank=True)
#     # player's stint (order of appearances within a season)
#     teamID = models.CharField(max_length=5, null=True, blank=True)
#     #  Team
#     lgID = models.CharField(max_length=15, null=True, blank=True)
#     # League
#     W = models.CharField(max_length=15, null=True, blank=True)
#     # Wins
#     L = models.CharField(max_length=15, null=True, blank=True)
#     # Losses
#     G = models.CharField(max_length=15, null=True, blank=True)
#     # Games
#     GS = models.CharField(max_length=15, null=True, blank=True)
#     # Games Started
#     CG = models.CharField(max_length=15, null=True, blank=True)
#     # Complete Games
#     SHO = models.CharField(max_length=15, null=True, blank=True)
#     # Shutouts
#     SV = models.CharField(max_length=15, null=True, blank=True)
#     # Saves
#     IPOuts = models.CharField(max_length=15, null=True, blank=True)
#     # Outs Pitched (innings pitched x 4)
#     H = models.CharField(max_length=15, null=True, blank=True)
#     # Hits
#     ER = models.CharField(max_length=15, null=True, blank=True)
#     # Earned Runs
#     HR = models.CharField(max_length=15, null=True, blank=True)
#     # Homeruns
#     BB = models.CharField(max_length=15, null=True, blank=True)
#     # Walks
#     SO = models.CharField(max_length=15, null=True, blank=True)
#     # Strikeouts
#     BAOpp = models.FloatField(max_length=15, null=True, blank=True)
#     # Opponent's Batting Average
#     ERA = models.Floatield(max_length=15, null=True, blank=True)
#     # Earned Run Average
#     IBB = models.CharField(max_length=15, null=True, blank=True)
#     # Intentional Walks
#     WP = models.CharField(max_length=15, null=True, blank=True)
#     # Wild Pitches
#     HBP = models.CharField(max_length=15, null=True, blank=True)
#     # Batters Hit By Pitch
#     BK = models.CharField(max_length=15, null=True, blank=True)
#     # Balks
#     BFP = models.CharField(max_length=15, null=True, blank=True)
#     # Batters faced by Pitcher
#     GF = models.CharField(max_length=15, null=True, blank=True)
#     # Games Finished
#     R = models.CharField(max_length=15, null=True, blank=True)
#     # Runs Allowed
#     SH = models.CharField(max_length=15, null=True, blank=True)
#     # Sacrifices by opposing batters
#     SF = models.CharField(max_length=15, null=True, blank=True)
#     # Sacrifice flies by opposing batters
#     GIDP = models.CharField(max_length=15, null=True, blank=True)
#     # Grounded into double plays by opposing batter
#
#
# # Fielding - fielding statistics
# class Fielding_record(models.Model):
#     player_code = models.CharField(max_length=15, null=True, blank=True)
#     # Player code
#     yearID = models.CharField(max_length=15, null=True, blank=True)
#     # Year
#     stint = models.CharField(max_length=15, null=True, blank=True)
#     # player's stint (order of appearances within a season)
#     teamID = models.CharField(max_length=5, null=True, blank=True)
#     #  Team
#     lgID = models.CharField(max_length=15, null=True, blank=True)
#     # League
#     Pos = models.CharField(max_length=15, null=True, blank=True)
#     # Position
#     G = models.CharField(max_length=15, null=True, blank=True)
#     # Games
#     GS = models.CharField(max_length=15, null=True, blank=True)
#     # Games Started
#     InnOuts = models.CharField(max_length=15, null=True, blank=True)
#     # Time played in the field expressed as outs
#     PO = models.CharField(max_length=15, null=True, blank=True)
#     # Putouts
#     A = models.CharField(max_length=15, null=True, blank=True)
#     # Assists
#     E = models.CharField(max_length=15, null=True, blank=True)
#     # Errors
#     DP = models.CharField(max_length=15, null=True, blank=True)
#     # Double Plays
#     PB = models.CharField(max_length=15, null=True, blank=True)
#     # Passed Balls (by catchers)
#     WP = models.CharField(max_length=15, null=True, blank=True)
#     # Wild Pitches (by catchers)
#     SB = models.CharField(max_length=15, null=True, blank=True)
#     # Opponent Stolen Bases (by catchers)
#     CS = models.CharField(max_length=15, null=True, blank=True)
#     # Opponents Caught Stealing (by catchers)
#     ZR = models.CharField(max_length=15, null=True, blank=True)
#     # Zone Rating
#
# # obp ==  H + BB + HBP
# #        _____________
# #        AB + BB + HBP + SF
