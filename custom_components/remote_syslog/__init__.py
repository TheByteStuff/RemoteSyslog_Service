"The Remote Syslogger Integration."

import logging

from . import sysloggercommon
from . import syslogger_tcp
from . import syslogger_udp

DOMAIN = "remote_syslog"

_LOGGER = logging.getLogger(__name__) 

ATTR_HOST = "host"
ATTR_PORT = "port"
ATTR_PROTOCOL = "protocol"
ATTR_FACILITY = "facility"
ATTR_PROGRAM = "program"
DEFAULT_PROGRAM = "hascript"

ATTR_MESSAGE = "message"
DEFAULT_MESSAGE = "Default Log Message"

ATTR_LOGLEVEL = "loglevel"
DEFAULT_LOGLEVEL = "info"


def setup(hass, config):
    #hass.states.set("remote_syslog.title", "Remote Syslogger")

    def handle_logmessage(call):
#     "Handle the service call."
        host = call.data.get(ATTR_HOST, "127.0.0.1")        
        port = call.data.get(ATTR_PORT, "514")        
        protocol = call.data.get(ATTR_PROTOCOL, "XXX")
        _LOGGER.info("Protocol passed is ", protocol)
        facility = call.data.get(ATTR_FACILITY, "USER")
        program = call.data.get(ATTR_PROGRAM, DEFAULT_PROGRAM)

        messagetext = call.data.get(ATTR_MESSAGE, DEFAULT_MESSAGE)
        loglevel = call.data.get(ATTR_LOGLEVEL, DEFAULT_LOGLEVEL)     
        
        try:
          if ("TCP" == protocol):
            log = syslogger_tcp.Syslog(host, port, sysloggercommon.sysfacility(facility), program)
            log.send(messagetext, sysloggercommon.sysloglevel(loglevel))
          else:
            log = syslogger_udp.Syslog(host, port, sysloggercommon.sysfacility(facility), program)
            log.send(messagetext, sysloggercommon.sysloglevel(loglevel))
        except Exception as e:
          _LOGGER.error("Problem sending to Remote Syslog server, ", str(e))

    hass.services.register(DOMAIN, 'logmessage', handle_logmessage)

    # Return boolean to indicate that initialization was successful.
    return True