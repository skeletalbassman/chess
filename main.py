#I'm keeping everything in here for now just for simplcity's sake.
#If I decide to make this into something bigger I'll break it out into more files
#This is intended to be a simple interactive chess AI using some simple heuristics for
#board value and maybe using pruning if it runs to slow. 

class Board():
	def __init__(self):
		self.ranks = {
			"a": 0,
			"b": 1,
			"c": 2,
			"d": 3,
			"e": 4,
			"f": 5,
			"g": 6,
			"h": 7,
			"1": 0,
			"2": 1,
			"3": 2,
			"4": 3,
			"5": 4,
			"6": 5,
			"7": 6,
			"8": 7
		}

		self.scores = {
			"p": 1,
			"N": 3,
			"B": 3,
			"R": 5,
			"Q": 9
		}

		self.board = self._buildBoard()

	def _buildBoard(self):
		black_start = [["bR","bN","bB","bQ","bK","bB","bN","bR"]
		,["bp"]*8]

		white_start = [["wp"]*8,
		["wR","wN","wB","wQ","wK","wB","wN","wR"]]
		board = []
		for i in xrange(6):
			if i == 0:
				board.extend(black_start)
				continue
			elif i == 5:
				board.extend(white_start)
				continue
			board.append([])
			for j in xrange(8):
				board[i+1].append("__")
		return board

	def move(self, start, target):
		si, sj = start[2], start[3]
		ti, tj = target[0], target[1]
		start_piece = start[:2]
		print si, sj, start_piece

	def printBoard(self):
		base = ["A_","B_","C_","D_","E_","F_","G_","H_"]
		for i in xrange(8):
			string = str(i+1)+" "+str(self.board[i]).strip("[]")
			print string+"\n"
		base_string = str(base).strip("[]")
		print "  "+base_string

if __name__ == "__main__":
	board = Board()
	board.printBoard()

	board.move("wpd2","d4")














