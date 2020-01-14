from bingos import *


def test_generate_npc(generate_npc):
    assert generate_npc.name == "Arthur"
    assert len(generate_npc.card) == 5
    assert len(generate_npc.deq) == 89
    assert generate_npc.toss_a_number() > 9


def test_winning(generate_npc, generate_human):
    assert generate_npc.check_hand(generate_human)


def test_loosing(generate_npc, generate_human):
    generate_human.hand.clear()
    assert generate_npc.check_hand(generate_human) == False
