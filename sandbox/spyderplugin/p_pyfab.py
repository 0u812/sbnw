#import imp
import sys
import os

localpath = os.path.dirname(os.path.realpath(__file__))

if sys.version_info[0] < 3:
  import __builtin__
  __builtin__.p_pyfab_spyder_env = True
else:
  import builtin
  builtin.p_pyfab_spyder_env = True

#pyfab_app = imp.load_source('pyfab_app', '/home/poltergeist/home/devel/install/graphfab-trunk/python2/site-packages/pyfab_app.py')
#print('pyfab_app loaded source')

import pyfab_app
from pyfab_cfg import PyfabConfigState, PyfabConfigStandalone, PyfabConfig, get_default_options

import spyderlib
from spyderlib.qt.QtGui import (QWidget, QVBoxLayout)
from spyderlib.plugins import SpyderPluginMixin
from spyderlib.baseconfig import get_translation
from spyderlib.utils.qthelpers import get_icon, create_action, qapplication
from spyderlib.qt.QtCore import SIGNAL, Qt
from spyderlib.py3compat import configparser as cp

from spyderlib.plugins.externalconsole import ExternalConsole

_ = get_translation("p_pyfab", dirname="spyderplugins")

class PyfabSpyderConfigState(PyfabConfigState):
  def __init__(self, parent):
    super(PyfabSpyderConfigState, self).__init__(parent)
    self.parent = None
    #print('********** PyfabSpyderConfigState set self.parent')

  def __getattr__(self, name):
    assert(name != 'table')
    assert(name != 'parent')
      #return super(PyfabSpyderConfigState, self).__getattr__(name)
    assert(u'table' not in self.table)
    #print('PyfabSpyderConfigState getattr on config state: {}'.format(name))
    #print('  PyfabSpyderConfigState config state is: {}'.format(self.table))

    #return self.table[unicode(name)]
    try:
      return self.parent.get_option(name)
    except (cp.NoOptionError, cp.NoSectionError):
      return get_default_options()[name]

  def __setattr__(self, name, value):
    if name == u'parent':
      return object.__setattr__(self, name, value)
    if name == u'table' or name == u'parent':
      return super(PyfabSpyderConfigState, self).__setattr__(name, value)
    #assert(u'table' not in self.table)
    #print('PyfabSpyderConfigState setattr on config state: {}'.format(name))
    #print('  PyfabSpyderConfigState config state is: {}'.format(self.table))

    #self.table[name] = value
    self.parent.set_option(name, value)

    #assert(u'table' not in self.table)

  def get_table(self):
    r = {}
    for k,v in get_default_options().iteritems():
      r[k] = getattr(self, k)
    return r

  def copy(self, parent):
    return super(PyfabSpyderConfigState, self).copy(parent)

class PyfabConfigSpyder(PyfabConfig):
  def __init__(self, parent=None):

    # config state
    self.ConfigStateCls = PyfabSpyderConfigState
    PyfabConfig.__init__(self, parent)
    self.state.parent = self

    if parent is None:
      #print('PyfabConfigSpyder first init')
      self.updateArrowStyles()

  def reset_defaults(self):
    super(PyfabConfigSpyder, self).reset_defaults()
    #if self.parent is None:
      #self.set_option('cust_option', 123)
      #print('get_option cust_option: {}'.format(self.get_option('cust_option')))

  def set_options(self, opts):
    #super(PyfabConfigSpyder, self).set_options(opts)
    for o, v in opts.iteritems():
      #print('  set option {} {}'.format(o,v))
      self.set_option(o, v)
    self.updateArrowStyles()

  def finalize(self):
    super(PyfabConfigSpyder, self).finalize()
    if self.parent is None:
      pass
      #print('PyfabConfigSpyder finalize last')
      #self.set_options(self.state.get_table())
    else:
      self.parent.finalize()

class PyfabPlugin(pyfab_app.Autolayout, SpyderPluginMixin, PyfabConfigSpyder):
  CONF_SECTION = 'pyfab_plugin'
  #LOCATION = Qt.RightDockWidgetArea #useless
  #ALLOWED_AREAS = Qt::RightDockWidgetArea #useless
  def __init__(self, parent=None):

    self.configCls = PyfabConfigStandalone
    PyfabConfigSpyder.plugin = self
    self.config = self
    PyfabConfigSpyder.__init__(self)

    pyfab_app.Autolayout.__init__(self)
    self.AppCls = qapplication().__class__
    SpyderPluginMixin.__init__(self, parent)

    # Initialize plugin
    self.initialize_plugin()

    self.raise_() #useless

  def getIconPath(self, p):
    result = str(os.path.join(localpath, 'pyfab-assets', 'icons', p))
    #print('getIconPath: {} -> {}'.format(p, result))
    return result

  def get_plugin_title(self):
    return 'Network viewer'

  def get_plugin_icon(self):
    return None

  def get_focus_widget(self):
    return None

  def get_plugin_actions(self):
    return None

  def on_first_registration(self):
    pass

  def register_plugin(self):
    self.main.add_dockwidget(self)

    print('** Looking for ExternalPythonShell')
    #from spyderlib.widgets.externalshell import pythonshell
    #print(len(self.main.extconsole.shellwidgets))
    #for sw in self.main.extconsole.shellwidgets:
      #print('sw {}'.format(sw))
      #if isinstance(sw, pythonshell.ExternalPythonShell):
        #print('    Found ExternalPythonShell: {}'.format(sw))
    print(self.main.extconsole.start)
    self.main.extconsole.__class__ = SBNWExternalConsole

    if self.main.explorer is not None:
      self.connect(self.main.explorer, SIGNAL("open_interpreter(QString)"),
                   self.sigslot)

    if self.main.projectexplorer is not None:
      self.connect(self.main.projectexplorer, SIGNAL("open_interpreter(QString)"),
                   self.sigslot)

    if self.main.extconsole is not None:
      self.connect(self.main.extconsole, SIGNAL("open_interpreter(QString)"),
                   self.sigslot)

    #print(dir(self.main.extconsole))

    self.connect(self.main.console.shell, SIGNAL('refresh()'),
                 self.sigslot)
    self.connect(self.main, SIGNAL('open_external_file(QString)'),
                 self.sigslot)
    #self.open_interpreter()
    #self.connect(self, SIGNAL('doit()'),
                 #self.doit)
    #self.emit(SIGNAL('doit()'))

    #k_act = create_action(self, _("Network viewer"),
                                #triggered=self.launch)
    #k_act.setEnabled(True)
    #self.register_shortcut(k_act, context="network",
                            #name="launch network viewer", default="F7")

    #self.main.tools_menu_actions += [None, k_act]
    #self.main.editor.pythonfile_dependent_actions += [k_act]

  def refresh_plugin(self):
    pass

  def closing_plugin(self, cancelable=False):
    return True

  def apply_plugin_settings(self, options):
    pass

  def launch(self):
    self.show()

  def open_interpreter(self, arg=None):
    print('open_interpreter')

  def sigslot(self, *args, **kwargs):
    print('slot')

  #def doit(self, *args, **kwargs):
    #print('doit')

  def getobj(self):
      print('getobj derived')

  def opensbml(self, sbml):
    if self.dockwidget is not None:
      self.dockwidget.blockSignals(True)

    # raise window
    self.eventually_raise_network_viewer(False)

    if self.dockwidget is not None:
      self.dockwidget.blockSignals(False)

    # open sbml in the raised window
    pyfab_app.Autolayout.opensbml(self, sbml)

  # Based on Spyder's __eventually_raise_inspector in inspector.py
  def eventually_raise_network_viewer(self, force=False):
      if hasattr(self.main, 'tabifiedDockWidgets'):
          # 'QMainWindow.tabifiedDockWidgets' was introduced in PyQt 4.5
          if self.dockwidget and (force or self.dockwidget.isVisible()) \
              and not self.ismaximized:
              dockwidgets = self.main.tabifiedDockWidgets(self.dockwidget)
              if self.main.console.dockwidget not in dockwidgets and \
                  (hasattr(self.main, 'extconsole') and \
                  self.main.extconsole.dockwidget not in dockwidgets):
                  self.dockwidget.show()
                  self.dockwidget.raise_()


PLUGIN_CLASS = PyfabPlugin

class SBNWExternalConsole(ExternalConsole):
  def start(self, *args, **kwds):
    print('SBNWExternalConsole start')
    ExternalConsole.start(self, *args, **kwds)