TEST_ARGS?=ttt/tests.py $(T)

auto-test:
	ptw -- $(TEST_ARGS) 

test:
	pytest $(TEST_ARGS)

run:
	python -m ttt.game
