"""Tests for remote_syslog syslogger_udp."""
# pytest  test_syslogger_udp.py --log-cli-level=10
#  https://pythontic.com/modules/socket/udp-client-server-example
import pytest

import logging
testlog = logging.getLogger()

from custom_components.remote_syslog import sysloggercommon
from custom_components.remote_syslog import syslogger_udp
syslogger = syslogger_udp

import socket

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

defaultProgram = "MyTester"


@pytest.fixture(scope="function")
def UDPServerSocket():
  UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
  UDPServerSocket.bind((localIP, localPort))
  yield UDPServerSocket
  UDPServerSocket.close()
  

def GetMessageFromServer(UDPServerSocket):
  bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
  message = bytesAddressPair[0]
  address = bytesAddressPair[1]
  return message


def test_SysFacility_DEFAULT(UDPServerSocket):
   
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.USER,defaultProgram)
  log.send("Test From Python UDP Syslogger", sysloggercommon.Level.INFO)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  assert(sysloggercommon.sysfacility("XXX") == sysloggercommon.Facility.USER)
    
  
def test_Program(UDPServerSocket):
  assert(sysloggercommon.sysfacility("XXX") == sysloggercommon.Facility.USER)
  
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL0,defaultProgram)
  message_sent = "syslogger_udp info local0"
  log.send(message_sent, sysloggercommon.Level.INFO)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  expected_message = "<134> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)  
  
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL0,"AnotherProgram")
  message_sent = "syslogger_udp info local0"
  log.send(message_sent, sysloggercommon.Level.INFO)   
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  expected_message = "<134> {0} {1}".format("AnotherProgram", message_sent)
  assert(expected_message.encode()==message)  



# Tests to confirm SysFacility  
def test_UDP_KERN(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.KERN, defaultProgram)
  message_sent = "syslogger_udp kern"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<0> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_UDP_USER(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.USER, defaultProgram)
  message_sent = "syslogger_udp user"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<8> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_UDP_MAIL(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.MAIL, defaultProgram)
  message_sent = "syslogger_udp mail"
  log.send(message_sent, sysloggercommon.Level.EMERG)
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<16> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_UDP_DAEMON(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.DAEMON, defaultProgram)
  message_sent = "syslogger_udp daemon"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<24> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_UDP_AUTH(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.AUTH, defaultProgram)
  message_sent = "syslogger_udp auth"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<32> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_UDP_SYSLOG(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.SYSLOG, defaultProgram)
  message_sent = "syslogger_udp syslog"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<40> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_UDP_LPR(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LPR, defaultProgram)
  message_sent = "syslogger_udp lpr"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<48> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
   
   
def test_UDP_NEWS(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.NEWS, defaultProgram)
  message_sent = "syslogger_udp news"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<56> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)              

  
def test_UDP_UUCP(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.UUCP, defaultProgram)
  message_sent = "syslogger_udp uucp"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<64> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_UDP_CRON(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.CRON, defaultProgram)
  message_sent = "syslogger_udp cron"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<72> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_UDP_AUTHPRIV(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.AUTHPRIV, defaultProgram)
  message_sent = "syslogger_udp authpriv"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<80> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)      
   
  
def test_UDP_FTP(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.FTP, defaultProgram)
  message_sent = "syslogger_udp ftp"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<88> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)      
  
  
def test_UDP_LOCAL0_INFO(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL0, defaultProgram)
  message_sent = "syslogger_udp local0"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<128> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_UDP_LOCAL1(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_udp local1"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<136> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)  
  
  
def test_UDP_LOCAL2(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL2, defaultProgram)
  message_sent = "syslogger_udp local2"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<144> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_UDP_LOCAL3(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL3, defaultProgram)
  message_sent = "syslogger_udp local3"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<152> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_UDP_LOCAL4(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL4, defaultProgram)
  message_sent = "syslogger_udp local4"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<160> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_UDP_LOCAL5(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL5, defaultProgram)
  message_sent = "syslogger_udp info local5"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<168> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_UDP_LOCAL6(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL6, defaultProgram)
  message_sent = "syslogger_udp info local6"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<176> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_UDP_LOCAL7(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL7, defaultProgram)
  message_sent = "syslogger_udp info local7"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<184> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 

  
  
# Tests to confirm LogLevel  
def test_UDP_LOCAL1_DEBUG(UDPServerSocket): 
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_udp debug local1"
  log.send(message_sent, sysloggercommon.Level.DEBUG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<143> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)    
  
  
def test_UDP_LOCAL1_INFO(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_udp info local1"
  log.send(message_sent, sysloggercommon.Level.INFO)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<142> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)  
  
  
def test_UDP_LOCAL1_NOTICE(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_udp notice local1"
  log.send(message_sent, sysloggercommon.Level.NOTICE)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<141> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)    
  
  
def test_UDP_LOCAL1_WARNING(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_udp warning local1"
  log.send(message_sent, sysloggercommon.Level.WARNING)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<140> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)


def test_UDP_LOCAL1_ERR(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_udp err local1"
  log.send(message_sent, sysloggercommon.Level.ERR)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<139> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)
  

def test_UDP_LOCAL1_CRIT(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_udp crit local1"
  log.send(message_sent, sysloggercommon.Level.CRIT)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<138> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)
  

def test_UDP_LOCAL1_ALERT(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_udp alert local1"
  log.send(message_sent, sysloggercommon.Level.ALERT)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<137> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)
  

def test_UDP_LOCAL1_EMERG(UDPServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_udp emerg local1"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(UDPServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<136> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)      