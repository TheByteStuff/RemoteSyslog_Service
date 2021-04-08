class Facility:
  "Syslog facilities"
  KERN, USER, MAIL, DAEMON, AUTH, SYSLOG, \
  LPR, NEWS, UUCP, CRON, AUTHPRIV, FTP = range(12)

  LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7 = range(16, 24)

class Level:
  "Syslog levels"
  EMERG, ALERT, CRIT, ERR, WARNING, NOTICE, INFO, DEBUG = range(8)
  
  
def sysfacility(i):
    switcher2={
            "KERN":Facility.KERN,
            "USER":Facility.USER,
            "MAIL":Facility.MAIL,
            "DAEMON":Facility.DAEMON,
            "AUTH":Facility.AUTH,
            "SYSLOG":Facility.SYSLOG,
            "LPR":Facility.LPR,
            "NEWS":Facility.NEWS,
            "UUCP":Facility.UUCP,
            "CRON":Facility.CRON,
            "AUTHPRIV":Facility.AUTHPRIV,
            "FTP":Facility.FTP,
            "LOCAL0":Facility.LOCAL0,
            "LOCAL1":Facility.LOCAL1,
            "LOCAL2":Facility.LOCAL2,
            "LOCAL3":Facility.LOCAL3,
            "LOCAL4":Facility.LOCAL4,
            "LOCAL5":Facility.LOCAL5,
            "LOCAL6":Facility.LOCAL6,
            "LOCAL7":Facility.LOCAL7
    }
    return switcher2.get(i, Facility.USER)  
    
def sysloglevel(i):
    switcher={
            "debug":Level.DEBUG,
            "info":Level.INFO,
            "notice":Level.NOTICE,
            "warning":Level.WARNING,
            "err":Level.ERR,
            "crit":Level.CRIT,
            "alert":Level.ALERT,
            "emerg":Level.EMERG
    }
    return switcher.get(i, Level.INFO)    