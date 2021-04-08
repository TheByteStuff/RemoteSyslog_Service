"""Tests for remote_syslog sysloggercommon."""
# pytest  test_common.py --log-cli-level=10

from custom_components.remote_syslog import sysloggercommon

def test_SysFacility_DEFAULT():
  assert(sysloggercommon.sysfacility("XXX") == sysloggercommon.Facility.USER)

def test_SysFacility_KERN():
  assert(sysloggercommon.sysfacility("KERN") == sysloggercommon.Facility.KERN)

def test_SysFacility_USER():
  assert(sysloggercommon.sysfacility("USER") == sysloggercommon.Facility.USER)

def test_SysFacility_MAIL():
  assert(sysloggercommon.sysfacility("MAIL") == sysloggercommon.Facility.MAIL)
  
def test_SysFacility_DAEMON():
  assert(sysloggercommon.sysfacility("DAEMON") == sysloggercommon.Facility.DAEMON)
  
def test_SysFacility_AUTH():
  assert(sysloggercommon.sysfacility("AUTH") == sysloggercommon.Facility.AUTH)
  
def test_SysFacility_SYSLOG():
  assert(sysloggercommon.sysfacility("SYSLOG") == sysloggercommon.Facility.SYSLOG)
  
def test_SysFacility_LPR():
  assert(sysloggercommon.sysfacility("LPR") == sysloggercommon.Facility.LPR)
  
def test_SysFacility_NEWS():
  assert(sysloggercommon.sysfacility("NEWS") == sysloggercommon.Facility.NEWS)
  
def test_SysFacility_UUCP():
  assert(sysloggercommon.sysfacility("UUCP") == sysloggercommon.Facility.UUCP)
  
def test_SysFacility_CRON():
  assert(sysloggercommon.sysfacility("CRON") == sysloggercommon.Facility.CRON)
 
def test_SysFacility_AUTHPRIV():
  assert(sysloggercommon.sysfacility("AUTHPRIV") == sysloggercommon.Facility.AUTHPRIV)
  
def test_SysFacility_FTP():
  assert(sysloggercommon.sysfacility("FTP") == sysloggercommon.Facility.FTP)
  
def test_SysFacility_LOCAL0():
  assert(sysloggercommon.sysfacility("LOCAL0") == sysloggercommon.Facility.LOCAL0)

def test_SysFacility_LOCAL1():
  assert(sysloggercommon.sysfacility("LOCAL1") == sysloggercommon.Facility.LOCAL1)

def test_SysFacility_LOCAL2():
  assert(sysloggercommon.sysfacility("LOCAL2") == sysloggercommon.Facility.LOCAL2)

def test_SysFacility_LOCAL3():
  assert(sysloggercommon.sysfacility("LOCAL3") == sysloggercommon.Facility.LOCAL3)

def test_SysFacility_LOCAL4():
  assert(sysloggercommon.sysfacility("LOCAL4") == sysloggercommon.Facility.LOCAL4)

def test_SysFacility_LOCAL5():
  assert(sysloggercommon.sysfacility("LOCAL5") == sysloggercommon.Facility.LOCAL5)

def test_SysFacility_LOCAL6():
  assert(sysloggercommon.sysfacility("LOCAL6") == sysloggercommon.Facility.LOCAL6)

def test_SysFacility_LOCAL7():
  assert(sysloggercommon.sysfacility("LOCAL7") == sysloggercommon.Facility.LOCAL7)
  
 
# Facility
def test_Facility_KERN():
  assert(sysloggercommon.Facility.KERN)==0
  
def test_Facility_USER():
  assert(sysloggercommon.Facility.USER)==1
  
def test_Facility_MAIL():
  assert(sysloggercommon.Facility.MAIL)==2
  
def test_Facility_DAEMON():  
  assert(sysloggercommon.Facility.DAEMON)==3
  
def test_Facility_AUTH():
  assert(sysloggercommon.Facility.AUTH)==4
  
def test_Facility_SYSLOG():	
  assert(sysloggercommon.Facility.SYSLOG)==5
  
def test_Facility_LPR(): 
  assert(sysloggercommon.Facility.LPR)==6
  
def test_Facility_NEWS():  
  assert(sysloggercommon.Facility.NEWS)==7
  
def test_Facility_UUCP():
  assert(sysloggercommon.Facility.UUCP)==8
  
def test_Facility_CRON():
  assert(sysloggercommon.Facility.CRON)==9
  
def test_Facility_AUTHPRIV():  
  assert(sysloggercommon.Facility.AUTHPRIV)==10
  
def test_Facility_FTP(): 
  assert(sysloggercommon.Facility.FTP)==11
  
def test_Facility_LOCAL0(): 
  assert(sysloggercommon.Facility.LOCAL0)==16
  
def test_Facility_LOCAL1():  
  assert(sysloggercommon.Facility.LOCAL1)==17
  
def test_Facility_LOCAL2():  
  assert(sysloggercommon.Facility.LOCAL2)==18
  
def test_Facility_LOCAL3():  
  assert(sysloggercommon.Facility.LOCAL3)==19
  
def test_Facility_LOCAL4():  
  assert(sysloggercommon.Facility.LOCAL4)==20
  
def test_Facility_LOCAL5():  
  assert(sysloggercommon.Facility.LOCAL5)==21
  
def test_Facility_LOCAL6():  
  assert(sysloggercommon.Facility.LOCAL6)==22
  
def test_Facility_LOCAL7():  
  assert(sysloggercommon.Facility.LOCAL7)==23

  
def test_SysLevel_DEFAULT():
  assert(sysloggercommon.sysloglevel("XXX") == sysloggercommon.Level.INFO)  
  
def test_SysLevel_EMERG():
  assert(sysloggercommon.sysloglevel("emerg") == sysloggercommon.Level.EMERG)  
  
def test_SysLevel_ALERT():
  assert(sysloggercommon.sysloglevel("alert") == sysloggercommon.Level.ALERT)  
  
def test_SysLevel_CRIT():
  assert(sysloggercommon.sysloglevel("crit") == sysloggercommon.Level.CRIT)  
  
def test_SysLevel_ERR():
  assert(sysloggercommon.sysloglevel("err") == sysloggercommon.Level.ERR)  
  
def test_SysLevel_WARNING():
  assert(sysloggercommon.sysloglevel("warning") == sysloggercommon.Level.WARNING)  
  
def test_SysLevel_NOTICE():
  assert(sysloggercommon.sysloglevel("notice") == sysloggercommon.Level.NOTICE)  
  
def test_SysLevel_INFO():
  assert(sysloggercommon.sysloglevel("info") == sysloggercommon.Level.INFO)  
  
def test_SysLevel_DEBUG():
  assert(sysloggercommon.sysloglevel("debug") == sysloggercommon.Level.DEBUG)                  
  
  
# Level
def test_Level_EMERG():
  assert(sysloggercommon.Level.EMERG)==0
  
def test_Level_ALERT():  
  assert(sysloggercommon.Level.ALERT)==1
  
def test_Level_CRIT():  
  assert(sysloggercommon.Level.CRIT)==2
  
def test_Level_ERR():  
  assert(sysloggercommon.Level.ERR)==3
  
def test_Level_WARNING():  
  assert(sysloggercommon.Level.WARNING)==4
  
def test_Level_NOTICE():  
  assert(sysloggercommon.Level.NOTICE)==5
  
def test_Level_INFO():  
  assert(sysloggercommon.Level.INFO)==6
  
def test_Level_():  
  assert(sysloggercommon.Level.DEBUG)==7
  
  