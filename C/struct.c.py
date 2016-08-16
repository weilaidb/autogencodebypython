#!/usr/bin/python
#coding:utf-8
import urllib
import sys
import re



def c_struct_element(comment, vartype, var):
	return VARNOTE + vartype + var




def c_struct(istypedef, stname, varlist ):
	if istypedef == 0:
		return DEFTYPEDEF + DEFSTRUCT + stname + SIGNLBRACE
	else
		return DEFSTRUCT + stname + SIGNLBRACE + 
		
		
