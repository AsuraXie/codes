#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score

	def print_score(self):
		print "%s:%s" % (self.__name,self.__score)

class Animal(object):
	def run(self):
		print "Animal is running.."

class Dog(Animal):
	def run(self):
		print "Dog is running..."

class Cat(Animal):
	def run(self):
		print "Cat is running..."

if __name__=='__main__':
	a=Animal();
	b=Dog()
	c=Cat()
	a.run()
	b.run()
	c.run()
