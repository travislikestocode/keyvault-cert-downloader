import sys
import dbus

class Hook:
  def __init__(self, action, service):
    self.action = action
    self.service = service + '.service'

  def _systemd_action(self):
    bus = dbus.SystemBus()
    systemd = bus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
    manager = dbus.Interface(systemd, 'org.freedesktop.systemd1.Manager')

    if self.action == 'reload':
      managerMethod = manager.ReloadUnit
    elif self.action == 'restart':
      managerMethod = manager.RestartUnit
    else:
      sys.exit('Action must be "reload" or "restart"')

    managerMethod(self.service, 'replace')

  def run(self):
    self._systemd_action()
