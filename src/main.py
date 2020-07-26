#!/usr/bin/python

from __future__ import absolute_import, print_function, unicode_literals
import sys
import dbus
import dbus.service
import dbus.mainloop.glib
try:
  from gi.repository import GObject
except ImportError:
  import gobject as GObject

import phonenumbers

class Rejected(dbus.DBusException):
  _dbus_error_name = "org.phonenumbers.Error.Rejected"

class Endpoint(dbus.service.Object):
  exit_on_release = True

  def set_exit_on_release(self, exit_on_release):
    self.exit_on_release = exit_on_release

  @dbus.service.method("org.phonenumbers.Endpoint1", in_signature="", out_signature="")