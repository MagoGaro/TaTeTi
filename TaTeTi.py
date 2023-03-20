def print_board(board):
	for i in range(0,7,3):
		print(board[i] + '|' + board[i+1] + '|' + board[i+2])


board = [' ']*9
juegoTerminado = False
p1 = True

while not juegoTerminado:
	proximoMovimiento = False
	while not proximoMovimiento:
		try:
			position = int(input('Turno Jugador 1 (1-9): ') if p1 else input('Turno Jugador 2 (1-9): '))
			if board[position - 1] == ' ':
				proximoMovimiento = True
				board[position - 1] = 'x' if p1 else 'o'
			else:
				print('Jugada Invalida')
		except:
			print('Movimineto Invalido')
	
	print_board(board)
	if( board[0] == board[1] == board[2] and board[0] != ' ' or
		board[3] == board[4] == board[5] and board[3] != ' ' or
		board[6] == board[7] == board[8] and board[6] != ' ' or
		board[0] == board[3] == board[6] and board[0] != ' ' or
		board[1] == board[4] == board[7] and board[1] != ' ' or
		board[2] == board[5] == board[8] and board[2] != ' ' or
		board[0] == board[4] == board[8] and board[0] != ' ' or
		board[2] == board[4] == board[6] and board[2] != ' ' ) :
		print('El Ganador es Jugador 1' if p1 else 'El Ganador es Jugador 2')
		juegoTerminado = True
	elif ' ' not in board:
		print('Juego Empatado')
		juegoTerminado = True
	p1 = not p1