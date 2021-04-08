"The Remote Syslogger Integration."

import logging

from . import sysloggercommon
from . import syslogger_tcp
from . import syslogger_udp
#syslogger = syslogger_udp
#log = syslogger.Syslog("192.168.21.201", 50516, syslogger.Facility.USER,"MyTester")

DOMAIN = "remote_syslog"

_LOGGER = logging.getLogger(__name__) 

ATTR_HOST = "host"
ATTR_PORT = "port"
ATTR_PROTOCOL = "protocol"
ATTR_FACILITY = "facility"
ATTR_PROGRAM = "program"
DEFAULT_PROGRAM = "hascript"
#ATTR_ = ""

ATTR_MESSAGE = "message"
DEFAULT_MESSAGE = "Default Log Message"

ATTR_LOGLEVEL = "loglevel"
DEFAULT_LOGLEVEL = "info"

#def sysfacility(i):
#    switcher2={
#            "KERN":sysloggercommon.Facility.KERN,
#            "USER":sysloggercommon.Facility.USER,
#            "MAIL":sysloggercommon.Facility.MAIL,
#            "DAEMON":sysloggercommon.Facility.DAEMON,
#            "AUTH":sysloggercommon.Facility.AUTH,
#            "SYSLOG":sysloggercommon.Facility.SYSLOG,
#            "LPR":sysloggercommon.Facility.LPR,
#            "NEWS":sysloggercommon.Facility.NEWS,
#            "UUCP":sysloggercommon.Facility.UUCP,
#            "CRON":sysloggercommon.Facility.CRON,
#            "AUTHPRIV":sysloggercommon.Facility.AUTHPRIV,
#            "FTP":sysloggercommon.Facility.FTP,
#            "LOCAL0":sysloggercommon.Facility.LOCAL0,
#            "LOCAL1":sysloggercommon.Facility.LOCAL1,
#            "LOCAL2":sysloggercommon.Facility.LOCAL2,
#            "LOCAL3":sysloggercommon.Facility.LOCAL3,
#            "LOCAL4":sysloggercommon.Facility.LOCAL4,
#            "LOCAL5":sysloggercommon.Facility.LOCAL5,
#            "LOCAL6":sysloggercommon.Facility.LOCAL6,
#            "LOCAL7":sysloggercommon.Facility.LOCAL7
#    }
#    return switcher2.get(i, sysloggercommon.Facility.USER)


#def sysloglevel(i):
#    switcher={
#            "debug":sysloggercommon.Level.DEBUG,
#            "info":sysloggercommon.Level.INFO,
#            "notice":sysloggercommon.Level.NOTICE,
#            "warning":sysloggercommon.Level.WARNING,
#            "err":sysloggercommon.Level.ERR,
#            "crit":sysloggercommon.Level.CRIT,
#            "alert":sysloggercommon.Level.ALERT,
#            "emerg":sysloggercommon.Level.EMERG
#    }
#    return switcher.get(i, sysloggercommon.Level.INFO)


def setup(hass, config):
    hass.states.set("remote_syslog.title", "Remote Syslogger")

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