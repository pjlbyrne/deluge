#
# pluginmanager.py
#
# Copyright (C) 2009 Damien Churchill <damoxc@gmail.com>
#
# Deluge is free software.
#
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# deluge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with deluge.    If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA    02110-1301, USA.
#

import logging

from deluge.component import Component
from deluge.pluginmanagerbase import PluginManagerBase
from deluge.ui.client import client
from deluge.configmanager import ConfigManager

log = logging.getLogger(__name__)

class PluginManager(PluginManagerBase, Component):
    def __init__(self):
        Component.__init__(self, "PluginManager")
        self.config = ConfigManager("web.conf")
        PluginManagerBase.__init__(self, "web.conf", "deluge.plugin.web")

    def start(self):
        """Start up the plugin manager"""
        
        # Update the enabled plugins from the core
        d = client.core.get_enabled_plugins()
        d.addCallback(self._on_get_enabled_plugins)
    
    def stop(self):
        self.disable_plugins()
    
    def update(self):
        pass