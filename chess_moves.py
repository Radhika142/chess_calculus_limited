FILES = "ABCDEFGH"
RANKS = "12345678"

def in_bounds(x: int, y: int) -> bool:
    return 0 <= x < 8 and 0 <= y < 8

def square_to_xy(square: str) -> tuple[int, int]:
    s = square.strip().upper()
    if len(s) != 2 or s[0] not in FILES or s[1] not in RANKS:
        raise ValueError(f"Invalid square '{square}'. Use A1..H8.")
    x = FILES.index(s[0])
    y = RANKS.index(s[1])
    return x, y

def xy_to_square(x: int, y: int) -> str:
    return f"{FILES[x]}{RANKS[y]}"

def pawn_moves(x: int, y: int):
    moves = []
    nx, ny = x, y + 1  # forward (increasing rank)
    if in_bounds(nx, ny):
        moves.append(xy_to_square(nx, ny))
    return moves

def king_moves(x: int, y: int):
    moves = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny):
                moves.append(xy_to_square(nx, ny))
    return moves

def queen_moves(x: int, y: int):
    moves = []
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),   # rook moves
        (1, 1), (1, -1), (-1, 1), (-1, -1)  # bishop moves
    ]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while in_bounds(nx, ny):
            moves.append(xy_to_square(nx, ny))
            nx += dx
            ny += dy
    return moves

def get_moves(piece: str, square: str):
    x, y = square_to_xy(square)
    piece = piece.strip().lower()
    if piece == "pawn":
        moves = pawn_moves(x, y)
    elif piece == "king":
        moves = king_moves(x, y)
    elif piece == "queen":
        moves = queen_moves(x, y)
    else:
        raise ValueError("Only Pawn, King, Queen supported")
    # sort for consistency
    return sorted(moves, key=lambda sq: (FILES.index(sq[0]), RANKS.index(sq[1])))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and "," in sys.argv[1]:
        piece, square = [p.strip() for p in sys.argv[1].split(",", 1)]
    elif len(sys.argv) == 3:
        piece, square = sys.argv[1], sys.argv[2]
    else:
        print("Usage:")
        print("  python chess_moves.py \"King, D5\"")
        print("  python chess_moves.py King D5")
        sys.exit(1)

    try:
        result = get_moves(piece, square)
        print(", ".join(result))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(2)
