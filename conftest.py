import pytest
from bingos import *

@pytest.fixture
def generate_player():
    npc = NPC("Arthur")
    npc.set_card(npc.get_card())
    return npc
