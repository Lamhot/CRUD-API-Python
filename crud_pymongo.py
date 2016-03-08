#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import binascii
import datetime

from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.mydb

col = db.posts

post = {'author' : 'Mike',
        'text' : 'My first blog post!',
        'tags': ['mongodb', 'python', 'pymongo'],
        'count': 1,
        'date': datetime.datetime.utcnow()}

#Insert
post_id = col.insert(post)
print post_id
#Bulk Inserts
new_posts = [
        {'author': 'Lamhot',
         'text': 'Post!',
         'tags': ['bulk', 'insert'],
         'count': 1,
         'date': datetime.datetime(2009, 11, 12, 11, 14)},
            {'author': 'lorem ipsum',
             'title': 'MongoDB is fun',
             'text': 'andpretty easy too!',
             'date': datetime.datetime(2009, 11, 10, 10, 45)}
            ]
print col.insert(new_posts)

#Find
print col.find_one()
print col.find_one({'author': 'Mike'})
print col.find_one({'author': 'Eliot'})
print col.find_one({'_id': post_id})
print col.find_one({'_id': str(post_id)}) #No result
print col.find_one({'_id': ObjectId(str(post_id))}) #Convert str to ObjectId
for post in col.find({'title': 'MongoDB is fun'}):
    print post
d = datetime.datetime(2009, 11, 12, 12)
for post in col.find({'date': {'$lt': d}}).sort('author'):
    print post

#Update
print col.update({'author': 'Mike'}, {'$inc': {'count': 1}}, multi=True)
for doc in col.find({'author': 'Mike'}):
    print doc

#FindAndModify
print col.find_and_modify({'author': 'Mike'}, {'$push': {'tags': 'modify'}}, new=True)

#Remove
col.remove({'author': 'Mike'})

#Counting
print col.count()
print col.find({'title': 'MongoDB is fun'}).count()