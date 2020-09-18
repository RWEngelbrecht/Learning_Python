import math, sys

class Pieces:

	def __init__(self, pieces):
		for _ in range(0, 9):
			self.whitePawns.append(Pawn('white'))
			self.blackPawns.append(Pawn('black'))
			# self.blackRooks
			# self.whiteRooks

class Pawn:

	def __init__(self, color):
		self.color = color
		self.weight = 1  # TODO: figure out weights

	def getColor(self):
		return self.color

if __name__ == '__main__':
	try:
		configFile = open(sys.argv[1], "r")
	except:
		print("Where's your config file? Get your shit together...")

	config = []
	for line in configFile.read().splitlines():
		if not line.startswith("#"): config.append(line)
	# print(config)
	playColor = config[0].split("=")[1]
	print(playColor)
