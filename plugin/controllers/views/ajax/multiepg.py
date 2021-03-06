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
from json import dumps
from Plugins.Extensions.OpenWebif.controllers.views.ajax.renderevtblock import renderEvtBlock

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1453357629.981665
__CHEETAH_genTimestamp__ = 'Thu Jan 21 15:27:09 2016'
__CHEETAH_src__ = '/home/babel/Build/Test/OpenPLi5/openpli5.0/build/tmp/work/tmnanoseplus-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+186ea358f6-r0/git/plugin/controllers/views/ajax/multiepg.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jan 21 15:27:08 2016'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class multiepg(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(multiepg, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def channelsInBouquet(self, **KWS):



        ## CHEETAH: generated from #block channelsInBouquet at line 50, col 1.
        trans = KWS.get("trans")
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
        
        write(u'''<thead>
<tr>
''')
        for sname, eventlist in VFN(VFFSL(SL,"events",True),"iteritems",False)(): # generated from line 53, col 2
            write(u'''\t<td class="border"><div class="service"><img src="''')
            _v = VFFSL(SL,"picons",True)[VFFSL(SL,"sname",True)] # u'$(picons[$sname])' on line 54, col 52
            if _v is not None: write(_filter(_v, rawExpr=u'$(picons[$sname])')) # from line 54, col 52.
            write(u'''" /> ''')
            _v = VFFSL(SL,"sname",True) # u'$sname' on line 54, col 74
            if _v is not None: write(_filter(_v, rawExpr=u'$sname')) # from line 54, col 74.
            write(u'''</div></td>
''')
        write(u'''</tr>
</thead>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

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
        
        write(u'''<style>
\ttable { font-family: Verdana; font-size: 11px; }
\ttr { vertical-align: top }
\t.service { font-weight: bold; font-size: 12px; color:#fff; background-color: #1c47ae; line-height:30px; padding: 3px; white-space: nowrap; overflow: hidden; width: 184px}
\t.service img { width:50px; height:30px; float:left; margin-right:10px; }
\t.title { font-weight: bold; color: #061c37; }
\t.desc { font-size: 10px; color: #176093; }
\t.even { background-color: #dfeffc; }
\t.border { border-right: 1px solid #4297d7; }
\t.event { cursor: pointer; width: 190px; overflow:hidden; }
\t.bq { background-color: #1c478e; font-size: 11px; font-weight: bold; color: #fff; padding: 2px 4px; line-height: 18px; cursor: pointer; white-space: nowrap; display: inline-block; margin: 1px 1px 0px 0px;}
\t.bq.selected { color: #A9D1FA; }
\t.plus { background-color: #dfeffc; font-size: 13px; font-weight: bold; color: #1c478e; padding: 2px 4px; line-height: 21px; cursor: pointer; white-space: nowrap; }
\t.plus.selected { color: #ea7409; }
\t.timer { color: #f00; font-weight: bold; font-size: 10px; }
\t.timer.disabled { color: #f80; }
\t#eventdescription { width: 375px; height: auto; position: fixed; top: 205px; left: 350px; z-index: 1000; display: none; overflow: auto; }
.fht-table,.fht-table thead,.fht-table tfoot,.fht-table tbody,.fht-table tr,.fht-table th,.fht-table td{font-size:100%;font:inherit;vertical-align:top;margin:0;padding:0}
.fht-table{border-collapse:collapse;border-spacing:0}
.fht-table-wrapper,.fht-table-wrapper .fht-thead,.fht-table-wrapper .fht-tfoot,.fht-table-wrapper .fht-fixed-column .fht-tbody,.fht-table-wrapper .fht-fixed-body .fht-tbody,.fht-table-wrapper .fht-tbody{overflow:hidden;position:relative}
.fht-table-wrapper .fht-fixed-body .fht-tbody,.fht-table-wrapper .fht-tbody{overflow:auto}
.fht-table-wrapper .fht-table .fht-cell{overflow:hidden;height:1px}
.fht-table-wrapper .fht-fixed-column,.fht-table-wrapper .fht-fixed-body{top:0;left:0;position:absolute}
.fht-table-wrapper .fht-fixed-column{z-index:1}
}
</style>

<table style="margin:0">
<tr>
''')
        for slot in range(0,7): # generated from line 34, col 1
            write(u'''    <td class="plus ''')
            if VFFSL(SL,"slot",True)==VFFSL(SL,"day",True) : # generated from line 35, col 21
                _v =  'selected' 
                if _v is not None: write(_filter(_v))
            else:
                _v =  '' 
                if _v is not None: write(_filter(_v))
            write(u'''" js:day="''')
            _v = VFFSL(SL,"slot",True) # u'$(slot)' on line 35, col 72
            if _v is not None: write(_filter(_v, rawExpr=u'$(slot)')) # from line 35, col 72.
            write(u'''">''')
            _v = VFFSL(SL,"tstrings",True)[("day_" + (time.strftime("%w", time.localtime(time.time()+86400*slot))))] # u'$tstrings[("day_" + (time.strftime("%w", time.localtime(time.time()+86400*slot))))]' on line 35, col 81
            if _v is not None: write(_filter(_v, rawExpr=u'$tstrings[("day_" + (time.strftime("%w", time.localtime(time.time()+86400*slot))))]')) # from line 35, col 81.
            write(u'''</td>
''')
        write(u'''</tr>
</table>

<table>
<tr>
''')
        for bq in VFFSL(SL,"bouquets",True): # generated from line 42, col 1
            write(u'''<td class="bq ''')
            if VFFSL(SL,"bq",True)[0]==VFFSL(SL,"bref",True) : # generated from line 43, col 15
                _v =  'selected' 
                if _v is not None: write(_filter(_v))
            else:
                _v =  '' 
                if _v is not None: write(_filter(_v))
            write(u'''" js:ref="''')
            _v = VFFSL(SL,"quote",False)(VFFSL(SL,"bq",True)[0]) # u'$quote($bq[0])' on line 43, col 68
            if _v is not None: write(_filter(_v, rawExpr=u'$quote($bq[0])')) # from line 43, col 68.
            write(u'''">''')
            _v = VFFSL(SL,"bq",True)[1] # u'$bq[1]' on line 43, col 84
            if _v is not None: write(_filter(_v, rawExpr=u'$bq[1]')) # from line 43, col 84.
            write(u'''</td>
''')
        write(u'''</tr>
</table>

''')
        renderEventBlock = VFFSL(SL,"renderEvtBlock",False)()
        write(u'''<table cellpadding="0" cellspacing="0" id="TBL1">
''')
        self.channelsInBouquet(trans=trans)
        write(u'''<tbody>
''')
        hasEvents = False
        for slot in range(0,12): # generated from line 61, col 2
            write(u'''<tr class="''')
            _v = VFFSL(SL,"slot",True)%2 and 'odd' or 'even' # u"$(slot%2 and 'odd' or 'even')" on line 62, col 12
            if _v is not None: write(_filter(_v, rawExpr=u"$(slot%2 and 'odd' or 'even')")) # from line 62, col 12.
            write(u'''">
''')
            for sname, eventlist in VFN(VFFSL(SL,"events",True),"iteritems",False)(): # generated from line 63, col 2
                write(u'''<td class="border">
''')
                for event in VFFSL(SL,"eventlist",True)[VFFSL(SL,"slot",True)]: # generated from line 65, col 2
                    write(u'''\t\t''')
                    _v = VFN(VFFSL(SL,"renderEventBlock",True),"render",False)(VFFSL(SL,"event",True)) # u'$renderEventBlock.render($event)' on line 66, col 3
                    if _v is not None: write(_filter(_v, rawExpr=u'$renderEventBlock.render($event)')) # from line 66, col 3.
                    write(u'''
''')
                    hasEvents = True
                write(u'''</td>
''')
            write(u'''</tr>
''')
        write(u'''</tbody>
</table>
<div id="eventdescription"></div>

<script>
var picons = ''')
        _v = VFFSL(SL,"dumps",False)(VFFSL(SL,"picons",True)) # u'$dumps($picons)' on line 78, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$dumps($picons)')) # from line 78, col 14.
        write(u''';
var reloadTimers = false;
$(".bq").click(function() {
    var id = $(this).attr("js:ref");
    $("#tvcontent").html(loadspinner).load(\'ajax/multiepg?bref=\'+id);
});
$(".event").click(function() {
    var id = $(this).attr("js:id");
    var ref = $(this).attr("js:ref");
    $("#eventdescription").load(\'ajax/event?idev=\'+id+\'&sref=\'+escape(ref), function() { 
\t\t$("#eventdescription").show(200).draggable( { handle: ".handle" } );
    });
});
$(".plus").click(function() {
\tvar day = $(this).attr("js:day");
\t$("#tvcontent").html(loadspinner).load(\'ajax/multiepg?bref=''')
        _v = VFFSL(SL,"quote",False)(VFFSL(SL,"bref",True)) # u'${quote($bref)}' on line 93, col 62
        if _v is not None: write(_filter(_v, rawExpr=u'${quote($bref)}')) # from line 93, col 62.
        write(u'''&day=\'+day);
});
if(!timeredit_initialized)
\t$(\'#editTimerForm\').load(\'/ajax/edittimer\');
</script>
<script type="text/javascript" src="js/jquery.fixedheadertable.min.js"></script>

<script>
$(function() { 
$(\'#TBL1\').fixedHeaderTable({ 
\tfooter: true,
\tcloneHeadToFoot: true,
\taltClass: \'odd\',
\tautoShow: true
});
});
</script>

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

    _mainCheetahMethod_for_multiepg= 'respond'

## END CLASS DEFINITION

if not hasattr(multiepg, '_initCheetahAttributes'):
    templateAPIClass = getattr(multiepg, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(multiepg)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=multiepg()).run()


