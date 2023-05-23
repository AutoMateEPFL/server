import pytest
from src.tasks.drivers.grbl import parser


def test_welcome_parser():
    false_welcome_msg = "Hello"
    with pytest.raises(ValueError):
        parser.welcome_parser(false_welcome_msg)


def test_homing_start_parser():
    false_homing_start_msg = "Haus"
    with pytest.raises(ValueError):
        parser.homing_start_parser(false_homing_start_msg)

def test_homing_end_parser_frist_argument():
    false_argument = "jep"
    ack_homing_1 = "[MSG:]"
    with pytest.raises(ValueError):
        parser.homing_end_parser(ack_homing_1, false_argument)
def test_homing_end_parser_second_argument():
    false_argument = "jep"
    ack_homing_2 = "ok"
    with pytest.raises(ValueError):
        parser.homing_end_parser(false_argument, ack_homing_2)

def test_idle_parser_true():
    idle_msg = "Idle"
    assert parser.idle_parser(idle_msg) == True


def test_idle_parser_false():
    not_idle_msg = "Busy"
    assert parser.idle_parser(not_idle_msg) == False
