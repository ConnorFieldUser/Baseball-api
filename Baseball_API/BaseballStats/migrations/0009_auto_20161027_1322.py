# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 13:22
from __future__ import unicode_literals

from django.db import migrations

from BaseballStats.models import Master


import csv


def add_file(apps, schema_editor):
    Batting_record = apps.get_model("BaseballStats", "Batting_record")
    with open('Master.csv') as infile:
        reader = csv.DictReader(infile, delimiter=',', fieldnames=["player", "player_code", "yearid", "stint",
                                "teamid", "lgid", "g", "ab", "r", "h", "doubles", "triples", "hr",
                                                                   "rbi", "sb", "cs", "bb", "so",
                                                                   "ibb", "hbp", "sh", "sf", "gidp"])
        for row in reader:
            player = Master.objects.get(id=row["player"])
            Batting_record.objects.create(player_code=row["player_code"],
                                          yearid=row["yearid"], stint=row["stint"],
                                          teamid=row["teamid"], lgid=row["lgid"],
                                          g=row["g"],
                                          ab=row["ab"], r=row["r"],
                                          h=row["h"], doubleb=row["doubleb"],
                                          tripleb=row["tripleb"],
                                          hr=row["hr"], rbi=row["rbi"],
                                          sb=row["sb"],
                                          cs=row["cs"], bb=row["bb"], so=row["so"],
                                          ibb=row["ibb"], hbp=row["hbp"], sh=row["sh"],
                                          sf=row["sf"], gidp=row["gidp"])
        raise Exception('HOORAH')


class Migration(migrations.Migration):

    dependencies = [
        ('BaseballStats', '0008_auto_20161027_1320'),
    ]

    operations = [
        migrations.RunPython(add_file)
    ]
