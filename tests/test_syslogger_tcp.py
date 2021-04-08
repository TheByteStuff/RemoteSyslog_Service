"""Tests for remote_syslog syslogger_tcp."""
# pytest  test_syslogger_tcp.py --log-cli-level=10
#  https://pymotw.com/2/socket/tcp.html
import pytest

import logging
testlog = logging.getLogger()

from custom_components.remote_syslog import sysloggercommon
from custom_components.remote_syslog import syslogger_tcp
syslogger = syslogger_tcp

import socket

localIP     = "127.0.0.1"
localPort   = 20002
bufferSize  = 1024

defaultProgram = "MyTester"


@pytest.fixture(scope="function")
def ServerSocket():
  ServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
  ServerSocket.bind((localIP, localPort))
  ServerSocket.listen(1)
  yield ServerSocket
  ServerSocket.close()
  

def GetMessageFromServer(ServerSocket):
  connection, client_address = ServerSocket.accept()
  message = connection.recv(bufferSize)
  return message


def test_SysFacility_DEFAULT(ServerSocket):
   
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.USER,defaultProgram)
  log.send("Test From Python TCP Syslogger", sysloggercommon.Level.INFO)  
  
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  assert(sysloggercommon.sysfacility("XXX") == sysloggercommon.Facility.USER)
    
  
def test_Program(ServerSocket):
  assert(sysloggercommon.sysfacility("XXX") == sysloggercommon.Facility.USER)
  
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL0,defaultProgram)
  message_sent = "syslogger_tcp info local0"
  log.send(message_sent, sysloggercommon.Level.INFO)  

  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))  
  expected_message = "<134> {0} {1}".format(defaultProgram, message_sent) 
  assert(expected_message.encode()==message)  
  
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL0,"AnotherProgram")
  message_sent = "syslogger_tcp info local0"
  log.send(message_sent, sysloggercommon.Level.INFO)   
  
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))    
  expected_message = "<134> {0} {1}".format("AnotherProgram", message_sent)
  assert(expected_message.encode()==message)  



# Tests to confirm SysFacility  
def test_TCP_KERN(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.KERN, defaultProgram)
  message_sent = "syslogger_tcp kern"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<0> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_TCP_USER(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.USER, defaultProgram)
  message_sent = "syslogger_tcp user"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<8> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_TCP_MAIL(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.MAIL, defaultProgram)
  message_sent = "syslogger_tcp mail"
  log.send(message_sent, sysloggercommon.Level.EMERG)
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<16> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_TCP_DAEMON(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.DAEMON, defaultProgram)
  message_sent = "syslogger_tcp daemon"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<24> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_TCP_AUTH(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.AUTH, defaultProgram)
  message_sent = "syslogger_tcp auth"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<32> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_TCP_SYSLOG(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.SYSLOG, defaultProgram)
  message_sent = "syslogger_tcp syslog"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<40> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_TCP_LPR(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LPR, defaultProgram)
  message_sent = "syslogger_tcp lpr"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<48> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
   
   
def test_TCP_NEWS(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.NEWS, defaultProgram)
  message_sent = "syslogger_tcp news"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<56> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)              

  
def test_TCP_UUCP(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.UUCP, defaultProgram)
  message_sent = "syslogger_tcp uucp"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<64> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_TCP_CRON(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.CRON, defaultProgram)
  message_sent = "syslogger_tcp cron"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<72> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_TCP_AUTHPRIV(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.AUTHPRIV, defaultProgram)
  message_sent = "syslogger_tcp authpriv"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<80> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)      
   
  
def test_TCP_FTP(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.FTP, defaultProgram)
  message_sent = "syslogger_tcp ftp"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<88> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)      
  
  
def test_TCP_LOCAL0_INFO(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL0, defaultProgram)
  message_sent = "syslogger_tcp local0"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<128> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)
  
  
def test_TCP_LOCAL1(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_tcp local1"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<136> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message)  
  
  
def test_TCP_LOCAL2(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL2, defaultProgram)
  message_sent = "syslogger_tcp local2"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<144> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_TCP_LOCAL3(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL3, defaultProgram)
  message_sent = "syslogger_tcp local3"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<152> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_TCP_LOCAL4(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL4, defaultProgram)
  message_sent = "syslogger_tcp local4"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<160> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_TCP_LOCAL5(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL5, defaultProgram)
  message_sent = "syslogger_tcp info local5"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<168> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_TCP_LOCAL6(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL6, defaultProgram)
  message_sent = "syslogger_tcp info local6"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<176> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 
  
  
def test_TCP_LOCAL7(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL7, defaultProgram)
  message_sent = "syslogger_tcp info local7"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<184> {0} {1}".format(defaultProgram, message_sent)
  print(expected_message)
  assert(expected_message.encode()==message) 

  
  
# Tests to confirm LogLevel  
def test_TCP_LOCAL1_DEBUG(ServerSocket): 
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_tcp debug local1"
  log.send(message_sent, sysloggercommon.Level.DEBUG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<143> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)    
  
  
def test_TCP_LOCAL1_INFO(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_tcp info local1"
  log.send(message_sent, sysloggercommon.Level.INFO)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<142> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)  
  
  
def test_TCP_LOCAL1_NOTICE(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_tcp notice local1"
  log.send(message_sent, sysloggercommon.Level.NOTICE)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<141> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)    
  
  
def test_TCP_LOCAL1_WARNING(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_tcp warning local1"
  log.send(message_sent, sysloggercommon.Level.WARNING)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<140> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)


def test_TCP_LOCAL1_ERR(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_tcp err local1"
  log.send(message_sent, sysloggercommon.Level.ERR)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<139> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)
  

def test_TCP_LOCAL1_CRIT(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_tcp crit local1"
  log.send(message_sent, sysloggercommon.Level.CRIT)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<138> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)
  

def test_TCP_LOCAL1_ALERT(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_tcp alert local1"
  log.send(message_sent, sysloggercommon.Level.ALERT)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<137> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)
  

def test_TCP_LOCAL1_EMERG(ServerSocket):
  log = syslogger.Syslog(localIP, localPort, sysloggercommon.Facility.LOCAL1, defaultProgram)
  message_sent = "syslogger_tcp emerg local1"
  log.send(message_sent, sysloggercommon.Level.EMERG)  
 
  message = GetMessageFromServer(ServerSocket)
  testlog.info("Received message was: {}".format(message))
  
  expected_message = "<136> {0} {1}".format(defaultProgram, message_sent)
  assert(expected_message.encode()==message)      