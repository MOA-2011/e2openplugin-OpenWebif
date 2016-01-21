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

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1453357629.168867
__CHEETAH_genTimestamp__ = 'Thu Jan 21 15:27:09 2016'
__CHEETAH_src__ = '/home/babel/Build/Test/OpenPLi5/openpli5.0/build/tmp/work/tmnanoseplus-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+186ea358f6-r0/git/plugin/controllers/views/web/external.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jan 21 15:27:08 2016'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class external(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(external, self).__init__(*args, **KWs)
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
        
        _orig_filter_81334656 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<?xml version="1.0" encoding="UTF-8"?>
<e2webifexternals>
''')
        for plugin in VFFSL(SL,"plugins",True): # generated from line 4, col 2
            write(u'''\t<e2webifexternal>
\t\t<e2path>''')
            _v = VFFSL(SL,"plugin",True)[0] # u'$plugin[0]' on line 6, col 11
            if _v is not None: write(_filter(_v, rawExpr=u'$plugin[0]')) # from line 6, col 11.
            write(u'''</e2path>
\t\t<e2name>''')
            _v = VFFSL(SL,"plugin",True)[2] # u'$plugin[2]' on line 7, col 11
            if _v is not None: write(_filter(_v, rawExpr=u'$plugin[2]')) # from line 7, col 11.
            write(u'''</e2name>
\t\t<e2externalversion>''')
            _v = VFFSL(SL,"plugin",True)[3] # u'$plugin[3]' on line 8, col 22
            if _v is not None: write(_filter(_v, rawExpr=u'$plugin[3]')) # from line 8, col 22.
            write(u'''</e2externalversion>
\t</e2webifexternal>
''')
        write(u'''</e2webifexternals>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_81334656
        
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

    _mainCheetahMethod_for_external= 'respond'

## END CLASS DEFINITION

if not hasattr(external, '_initCheetahAttributes'):
    templateAPIClass = getattr(external, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(external)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=external()).run()


