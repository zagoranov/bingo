import pytest
from bingos import *


@pytest.fixture
def generate_npc():
    npc = NPC("Arthur")
    npc.set_card(npc.get_card())
    return npc


def generate_human(generate_npc):
    player = Human('John')
    player.set_card(generate_npc.get_card())
    player.hand.append(player.card)
    return player

