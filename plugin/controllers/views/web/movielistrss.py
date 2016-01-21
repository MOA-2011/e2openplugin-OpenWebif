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
from urllib import quote

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1453357629.147108
__CHEETAH_genTimestamp__ = 'Thu Jan 21 15:27:09 2016'
__CHEETAH_src__ = '/home/babel/Build/Test/OpenPLi5/openpli5.0/build/tmp/work/tmnanoseplus-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+186ea358f6-r0/git/plugin/controllers/views/web/movielistrss.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jan 21 15:27:08 2016'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class movielistrss(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(movielistrss, self).__init__(*args, **KWs)
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
        
        _orig_filter_36637231 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
\t<channel>
\t\t<title>Enigma2 Movielist</title>
\t\t<link>http://</link>
\t\t<description>A list of all recordings</description>
\t\t<generator>OpenWebif</generator>
''')
        for movie in VFFSL(SL,"movies",True): # generated from line 10, col 3
            write(u'''\t\t<item>
\t\t\t<title>''')
            _v = VFFSL(SL,"movie.eventname",True) # u'$movie.eventname' on line 12, col 11
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.eventname')) # from line 12, col 11.
            write(u'''</title>
\t\t\t<description>
\t\t\t\tService: ''')
            _v = VFFSL(SL,"movie.servicename",True) # u'$movie.servicename' on line 14, col 14
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.servicename')) # from line 14, col 14.
            write(u'''<br />
\t\t\t\t''')
            _v = VFFSL(SL,"movie.description",True) # u'$movie.description' on line 15, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.description')) # from line 15, col 5.
            write(u'''<br />
\t\t\t\t''')
            _v = VFFSL(SL,"movie.descriptionExtended",True) # u'$movie.descriptionExtended' on line 16, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.descriptionExtended')) # from line 16, col 5.
            write(u'''<br />
\t\t\t\t''')
            _v = VFFSL(SL,"movie.filename",True) # u'$movie.filename' on line 17, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.filename')) # from line 17, col 5.
            write(u'''<br />
\t\t\t\t''')
            _v = VFFSL(SL,"movie.tags",True) # u'$movie.tags' on line 18, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.tags')) # from line 18, col 5.
            write(u'''<br />
\t\t\t\t''')
            _v = VFFSL(SL,"movie.fullname",True) # u'$movie.fullname' on line 19, col 5
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.fullname')) # from line 19, col 5.
            write(u'''
\t\t\t</description>
\t\t\t<link>''')
            _v = VFFSL(SL,"host",True) # u'$host' on line 21, col 10
            if _v is not None: write(_filter(_v, rawExpr=u'$host')) # from line 21, col 10.
            write(u'''/file?file=''')
            _v = VFFSL(SL,"quote",False)(VFFSL(SL,"movie.filename",True)) # u'$quote($movie.filename)' on line 21, col 26
            if _v is not None: write(_filter(_v, rawExpr=u'$quote($movie.filename)')) # from line 21, col 26.
            write(u'''</link>
\t\t\t<enclosure type="video/mpeg" url="http://''')
            _v = VFFSL(SL,"host",True) # u'$host' on line 22, col 45
            if _v is not None: write(_filter(_v, rawExpr=u'$host')) # from line 22, col 45.
            write(u'''/file?file=''')
            _v = VFFSL(SL,"quote",False)(VFFSL(SL,"movie.filename",True)) # u'$quote($movie.filename)' on line 22, col 61
            if _v is not None: write(_filter(_v, rawExpr=u'$quote($movie.filename)')) # from line 22, col 61.
            write(u'''"/>
\t\t\t<pubDate>''')
            _v = VFFSL(SL,"movie.begintime",True) # u'$movie.begintime' on line 23, col 13
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.begintime')) # from line 23, col 13.
            write(u'''</pubDate>
\t\t\t<category>''')
            _v = VFFSL(SL,"movie.servicename",True) # u'$movie.servicename' on line 24, col 14
            if _v is not None: write(_filter(_v, rawExpr=u'$movie.servicename')) # from line 24, col 14.
            write(u'''</category>
\t\t\t<author>Dreambox Enigma2</author>
\t\t</item>
''')
        write(u'''\t</channel>
</rss>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_36637231
        
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

    _mainCheetahMethod_for_movielistrss= 'respond'

## END CLASS DEFINITION

if not hasattr(movielistrss, '_initCheetahAttributes'):
    templateAPIClass = getattr(movielistrss, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(movielistrss)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=movielistrss()).run()


