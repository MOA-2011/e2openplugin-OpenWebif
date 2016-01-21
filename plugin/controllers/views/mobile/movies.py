#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Plugins.Extensions.OpenWebif.local import tstrings

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1453357629.459436
__CHEETAH_genTimestamp__ = 'Thu Jan 21 15:27:09 2016'
__CHEETAH_src__ = '/home/babel/Build/Test/OpenPLi5/openpli5.0/build/tmp/work/tmnanoseplus-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+186ea358f6-r0/git/plugin/controllers/views/mobile/movies.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jan 21 15:27:08 2016'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class movies(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(movies, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''<html>\r
 <head>\r
\t<title>OpenWebif</title>\r
\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r
\t<meta name="viewport" content="user-scalable=no, width=device-width"/>\r
\t<meta name="apple-mobile-web-app-capable" content="yes" />\r
\t<link rel="stylesheet" type="text/css" href="/css/jquery.mobile-1.0.min.css" media="screen"/>\r
\t<link rel="stylesheet" type="text/css" href="/css/iphone.css" media="screen"/>\r
\t<script src="/js/jquery-1.6.2.min.js"></script>\r
\t<script src="/js/jquery.mobile-1.0.min.js"></script>\r
 </head>\r
 <body> \r
\t<div data-role="page">\r
\r
\t\t<div id="header">\r
\t\t\t<div class="button" onClick="history.back()">''')
        _v = VFFSL(SL,"tstrings",True)['back'] # u"$tstrings['back']" on line 17, col 49
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['back']")) # from line 17, col 49.
        write(u'''</div>\r
\t\t\t<h1><a style="color:#FFF;text-decoration:none;" href=\'/mobile\'>OpenWebif</a></h1>
\t\t\t<h2>''')
        _v = VFFSL(SL,"tstrings",True)['movies'] # u"$tstrings['movies']" on line 19, col 8
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['movies']")) # from line 19, col 8.
        write(u'''</h2>\r
\t\t</div>\r
\r
\t\t<div data-role="fieldcontain">\r
\t\t   <select name="select-choice-1" id="select-choice-moviedir" onChange="window.location.href=\'/mobile/movies?dirname=\'+escape(options[selectedIndex].value);">\r
\t\t\t  <option value="''')
        _v = VFFSL(SL,"directory",True) # u'$directory' on line 24, col 21
        if _v is not None: write(_filter(_v, rawExpr=u'$directory')) # from line 24, col 21.
        write(u'''">''')
        _v = VFFSL(SL,"directory",True) # u'$directory' on line 24, col 33
        if _v is not None: write(_filter(_v, rawExpr=u'$directory')) # from line 24, col 33.
        write(u'''</option>\r
''')
        for bookmark in VFFSL(SL,"bookmarks",True): # generated from line 25, col 6
            write(u'''\t\t\t  <option value="''')
            _v = VFFSL(SL,"bookmark",True) # u'$bookmark' on line 26, col 21
            if _v is not None: write(_filter(_v, rawExpr=u'$bookmark')) # from line 26, col 21.
            write(u'''">''')
            _v = VFFSL(SL,"bookmark",True) # u'$bookmark' on line 26, col 32
            if _v is not None: write(_filter(_v, rawExpr=u'$bookmark')) # from line 26, col 32.
            write(u'''</option>\r
''')
        write(u'''\t\t   </select>\r
\t\t</div>\r
\r
\t\t<div id="contentContainer">\r
\t\t\t<ul data-role="listview" data-inset="true" data-theme="d">\r
\t\t\t\t<li data-role="list-divider" role="heading" data-theme="b">''')
        _v = VFFSL(SL,"tstrings",True)['movies'] # u"$tstrings['movies']" on line 33, col 64
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['movies']")) # from line 33, col 64.
        write(u'''</li>\r
''')
        for movie in VFFSL(SL,"movies",True): # generated from line 34, col 5
            if VFFSL(SL,"movie.eventname",True) != "": # generated from line 35, col 5
                write(u'''\t\t\t\t<li>''')
                _v = VFFSL(SL,"movie.eventname",True) # u'$movie.eventname' on line 36, col 9
                if _v is not None: write(_filter(_v, rawExpr=u'$movie.eventname')) # from line 36, col 9.
                write(u'''</li>\r
''')
            else: # generated from line 37, col 5
                write(u'''\t\t\t\t<li>''')
                _v = VFFSL(SL,"movie.filename",True) # u'$movie.filename' on line 38, col 9
                if _v is not None: write(_filter(_v, rawExpr=u'$movie.filename')) # from line 38, col 9.
                write(u'''</li>\r
''')
        write(u'''\t\t\t</ul>\r
\t\t</div>\r
\r
\t\t<div id="footer">\r
\t\t\t<p>OpenWebif Mobile</p>\r
\t\t\t<a onclick="document.location.href=\'/index?mode=fullpage\';return false;" href="#">''')
        _v = VFFSL(SL,"tstrings",True)['show_full_openwebif'] # u"$tstrings['show_full_openwebif']" on line 46, col 86
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['show_full_openwebif']")) # from line 46, col 86.
        write(u'''</a>\r
\t\t</div>\r
\t\t\r
\t</div>\r
 </body>\r
</html>\r
      ''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_movies= 'respond'

## END CLASS DEFINITION

if not hasattr(movies, '_initCheetahAttributes'):
    templateAPIClass = getattr(movies, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(movies)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=movies()).run()


