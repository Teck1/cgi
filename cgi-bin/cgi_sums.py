#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()

form = cgi.FieldStorage()
listval = form.getlist('operand')

try:
    print('sum: {}'.format(sum(int(x) for x in listval)))
except (ValueError, TypeError):
    print('Unable to calculate sum, please provide integer operands.')
