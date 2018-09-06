"""
AIT 690 | Assignment 1 | Due 9/19/2018
Billy Ermlick
Nidhi
Xiaojie Guo

Description here...
check out default dict...


"""
from collections import defaultdict

pet = defaultdict(lambda: 'dog')
pet['kai'] = 'snake'

print(pet['kevin'])
