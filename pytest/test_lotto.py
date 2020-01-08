def test_generate_player(generate_player):
	assert generate_player.name == "Arthur"
	assert len(generate_player.card) == 5
	assert len(generate_player.deq) == 89
	assert generate_player.toss_a_number() > 9
