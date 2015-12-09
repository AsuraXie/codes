#!/usr/bin/env python
try:
	print 'try...'
	r=10/0
	print 'result',r
except ZeroDivisionError,e:
	print 'except:',e
finally:
	print 'finally...'
print 'end'
