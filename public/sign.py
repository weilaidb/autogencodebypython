#!/usr/bin/python
#coding:utf-8
import urllib
import sys
import re


SIGNCOMMON      =";"
SIGNDOT         ="."
SIGNEQUAL       ="="
SIGNNOEQUAL     ="!="
SIGNADD     ="+"
SIGNSPACE     =" "
SIGNLBRACE    ="{"
SIGNRBRACE    ="}"
VARNOTE='''
    /**
     * The name of the class; usually it is the same name as the
     * context structure type to which the AVClass is associated.
     */'''

SIGNEWLINE = "\r\n"


DEFTYPEDEF="typedef "
DEFSTRUCT="struct  "