# chess_calculus_limited
# Chess Moves

Calculates moves of Pawn, King, and Queen on an 8×8 boarde.

### Usage

```
python chess_moves.py King D5
```

### Examples

```
King D5  -> C4, C5, C6, D4, D6, E4, E5, E6  
Pawn G1  ->  G2  
Queen E4 ->  A4, A8, B1, B4, B7, C2, C4, C6, D3, D4, D5, E1, E2, E3, E5, E6, E7, E8, F3, F4, F5, G2, G4, G6, H1, H4, H7
```

### Notes

* Pawn: one step forward only.
* King: one step in any direction.
* Queen: any number of steps in 8 directions.

### Tests

Unit tests in `test_chess_moves.py`.
Run with:

```
python -m pytest .\test_chess_moves.py
```

Note: Install PyTest before running unit tests if not installed already with command
```
python -m pip install pytest
```

