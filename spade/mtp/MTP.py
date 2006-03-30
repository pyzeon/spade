
from spade import SpadeConfigParser

CONFIGFILE = "/etc/spade/spade.xml"


class MTP:


	def __init__(self, name):

		parser = SpadeConfigParser.ConfifParser()
		self.config = parser.parse(CONFIGFILE)

		self.name = name

		self.protocol = self.config.acc[name].protocol
		self.instance = self.config.acc[name].instance

		#other parameters must be overloaded