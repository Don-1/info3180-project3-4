from . import db, models
import time
import os

def insert(fname1, lname1, username1, sex1, age1, image1, highscore1, tdollar1):
  entry = models.Profile(fname=fname1, lname=lname1, username=username1, sex=sex1, age=age1, highscore=highscore1, tdollar=tdollar1, profile_add_on=time.strftime("%a %d %b %Y"), image=image1)
  db.session.add(entry)
  db.session.commit()
  