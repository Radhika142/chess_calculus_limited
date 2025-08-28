import pytest
from chess_moves import get_moves

def test_king_center():
    result = set(get_moves("King", "D5"))
    expected = {"C4","C5","C6","D4","D6","E4","E5","E6"}
    assert result == expected

def test_pawn_start():
    assert get_moves("Pawn", "G1") == ["G2"]

def test_pawn_at_top():
    assert get_moves("Pawn", "C8") == []

def test_queen_center_contains_examples():
    moves = set(get_moves("Queen", "E4"))
    example = {"A4","B4","C4","D4","F4","G4","H4",
               "E1","E2","E3","E5","E6","E7","E8",
               "A8","B7","C6","D5","F3","G2","H1"}
    assert example.issubset(moves)

def test_case_insensitive():
    assert get_moves("king", "d5") == get_moves("King", "D5")
