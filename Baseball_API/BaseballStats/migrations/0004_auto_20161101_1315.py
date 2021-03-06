# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 13:15
from __future__ import unicode_literals

from django.db import migrations


import csv


def add_my_files(apps, schema_editor):
    Master = apps.get_model("BaseballStats", "Master")
    Batting_record = apps.get_model("BaseballStats", "Batting_record")
    Pitching_record = apps.get_model("BaseballStats", "Pitching_record")
    Fielding_record = apps.get_model("BaseballStats", "Fielding_record")
# Master
    with open('Master.csv') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            Master.objects.create(playerID=row["playerID"],
                                  birthYear=row["birthYear"], birthMonth=row["birthMonth"],
                                  birthDay=row["birthDay"], birthCountry=row["birthCountry"],
                                  birthState=row["birthState"],
                                  birthCity=row["birthCity"], deathYear=row["deathYear"],
                                  deathMonth=row["deathMonth"], deathDay=row["deathDay"],
                                  deathCountry=row["deathCountry"], deathState=row["deathState"],
                                  deathCity=row["deathCity"],
                                  nameFirst=row["nameFirst"], nameLast=row["nameLast"], nameGiven=row["nameGiven"],
                                  weight=row["weight"], height=row["height"], bats=row["bats"],
                                  throws=row["throws"], debut=row["debut"], finalGame=row["finalGame"],
                                  retroID=row["retroID"], bbrefID=row["bbrefID"])
# Batting
    with open('Batting.csv') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            playerID = Master.objects.get(playerID=row["playerID"])
            Batting_record.objects.create(playerID=playerID, yearID=row["yearID"],
                                          stint=row["stint"], teamID=["teamID"],
                                          lgID=row["lgID"], G=row["G"],
                                          AB=row["AB"], R=row["R"],
                                          H=row["H"],
                                          doubles=row["2B"], triples=row["3B"], HR=row["HR"],
                                          RBI=row["RBI"], SB=row["SB"], CS=row["CS"],
                                          BB=row["BB"], SO=row["SO"], IBB=row["IBB"],
                                          HBP=row["HBP"], SH=row["SH"], SF=row["SF"], GIDP=row["GIDP"])
# Pitching
    with open('Pitching.csv', encoding='latin1') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            playerID = Master.objects.get(playerID=row["playerID"])
            Pitching_record.objects.create(playerID=playerID, yearID=row["yearID"],
                                           stint=row["stint"], teamID=["teamID"],
                                           lgID=row["lgID"], W=row["W"],
                                           L=row["L"], G=row["G"],
                                           GS=row["GS"],
                                           CG=row["CG"], SHO=row["SHO"], SV=row["SV"],
                                           IPouts=row["IPouts"], H=row["H"], ER=row["ER"],
                                           SO=row["SO"], BAOpp=row["BAOpp"], ERA=row["ERA"],
                                           IBB=row["IBB"], WP=row["WP"], BK=row["BK"], BFP=row["BFP"],
                                           GF=row["GF"], R=row["R"], SH=row["SH"], SF=row["SF"],
                                           GIDP=row["GIDP"])
# Fielding
    with open('Fielding.csv', encoding='latin1') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            playerID = Master.objects.get(playerID=row["playerID"])
            Fielding_record.objects.create(playerID=playerID,
                                           stint=row["stint"], teamID=row["teamID"],
                                           lgID=row["lgID"], POS=row["POS"], G=row["G"],
                                           GS=row["GS"], InnOuts=row["InnOuts"],
                                           PO=row["PO"], A=row["A"], E=row["E"],
                                           DP=row["DP"], PB=row["PB"], WP=row["WP"],
                                           SB=row["SB"], CS=row["CS"], ZR=row["ZR"])


class Migration(migrations.Migration):

    dependencies = [
        ('BaseballStats', '0003_auto_20161101_1305'),
    ]

    operations = [
            migrations.RunPython(add_my_files)
    ]
