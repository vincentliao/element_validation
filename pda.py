#! /usr/bin/env python
# encoding    : utf-8
# author      : vincentliao
# date        : 20140510 
# description : Use Pushdown automata to reconize the string.
# 
# the transition rules of PDA:  
# d(q0, [, z) = (q0, xz)
# d(q0, [, x) = (q0, xx)
# d(q0, ], x) = (q1, e)
# d(q1, ], x) = (q1, e)
# d(q1, [, z) = (q0, xz)
# d(q1, [, x) = (q0, xx)
# d(q1, e, z) = (f, z)

import sys

rule = { (0, '[', 'z'):(0, 'xz'),
		 (0, '[', 'x'):(0, 'xx'), 
		 (0, ']', 'x'):(1, ''),
		 (1, ']', 'x'):(1, ''),
		 (1, '[', 'z'):(0, 'xz'),
		 (1, '[', 'x'):(0, 'xx'),
		 (1, 'e', 'z'):(2, 'z') }

def checker(state, test_string, stack, rule):
	for (i, x) in enumerate(test_string):
		(state, rep) = rule[(state, x, stack[0])] if rule.has_key((state, x, stack[0])) else (-1, '')
		stack = stack[0].replace(stack[0], rep) + stack[1:]
		print '(%d, %s, %s)' % (state, test_string[i:], stack)
		if state == -1:	
			return False

	if state == 2:
		return True

if __name__ == '__main__':
	test_string = (sys.argv[1] if len(sys.argv) >= 2 else "<a></a>") + "e"  
	test_string = test_string.replace('<a>', '[').replace('</a>', ']')
	print checker(0, test_string, 'z', rule)
