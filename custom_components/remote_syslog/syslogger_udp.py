# based on https://csl.name/post/python-syslog-client/
# delivers messages in BSD (legacy Syslog) format
import socket

from . import sysloggercommon

class Syslog:

  def __init__(self,
               host="localhost",
               port=514,
               facility=sysloggercommon.Facility.DAEMON,
               program="hascript"):
    self.host = host
    self.port = port
    self.facility = facility
    self.program = program
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  def send(self, message, level):
    "Send a syslog message to remote host using UDP."
    data = "<{priority}> {program} {logmessage}".format(priority=(level + self.facility*8), program=self.program, logmessage=message)    
    self.socket.sendto(data.encode(), (self.host, self.port))
