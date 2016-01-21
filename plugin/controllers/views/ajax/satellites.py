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
from Plugins.Extensions.OpenWebif.local import tstrings

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1453357629.715208
__CHEETAH_genTimestamp__ = 'Thu Jan 21 15:27:09 2016'
__CHEETAH_src__ = '/home/babel/Build/Test/OpenPLi5/openpli5.0/build/tmp/work/tmnanoseplus-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+186ea358f6-r0/git/plugin/controllers/views/ajax/satellites.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jan 21 15:27:08 2016'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class satellites(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(satellites, self).__init__(*args, **KWs)
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
        
        write(u'''<script>
$(function() { InitAccordeon("#accordionS");});
</script>
<div id="accordionS">
''')
        for satellite in VFFSL(SL,"satellites",True): # generated from line 7, col 1
            write(u'''\t<h1><a href="#" id="ajax/channels?id=''')
            _v = VFFSL(SL,"quote",False)(VFFSL(SL,"satellite.service",True)) # u'$quote($satellite.service)' on line 8, col 39
            if _v is not None: write(_filter(_v, rawExpr=u'$quote($satellite.service)')) # from line 8, col 39.
            write(u'''&stype=''')
            _v = VFFSL(SL,"stype",True) # u'$stype' on line 8, col 72
            if _v is not None: write(_filter(_v, rawExpr=u'$stype')) # from line 8, col 72.
            write(u'''">''')
            _v = VFFSL(SL,"satellite.name",True) # u'$satellite.name' on line 8, col 80
            if _v is not None: write(_filter(_v, rawExpr=u'$satellite.name')) # from line 8, col 80.
            write(u'''</a></h1>
<div>
''')
            _v = VFFSL(SL,"tstrings",True)['loading'] # u"$tstrings['loading']" on line 10, col 1
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['loading']")) # from line 10, col 1.
            write(u''' ...
\t</div>
''')
        write(u'''</div>''')
        
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

    _mainCheetahMethod_for_satellites= 'respond'

## END CLASS DEFINITION

if not hasattr(satellites, '_initCheetahAttributes'):
    templateAPIClass = getattr(satellites, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(satellites)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=satellites()).run()


