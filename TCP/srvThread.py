import threading
import time

class SrvThread(threading.Thread):
	def __init__(self, threadID, nome):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.nome = nome

	def run(self):
		print "Iniciando thread", self.threadID
		time.sleep(5)
		print "Rodando thread", self.threadID
		time.sleep(5)
		print "Finalizando thread", self.threadID