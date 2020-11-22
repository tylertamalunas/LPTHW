from nose.tools import *
from ex48 import lexicon


def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east west left right up down     back")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east'),
                          ('direction', 'west'),
                          ('direction', 'left'),
                          ('direction', 'right'),
                          ('direction', 'up'),
                          ('direction', 'down'),
                          ('direction', 'back'),])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat stop")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat'),
                          ('verb', 'stop')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of from at it")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of'),
                          ('stop', 'from'),
                          ('stop', 'at'),
                          ('stop', 'it'),])


def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess cabinet door")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess'),
                          ('noun', 'cabinet'),
                          ('noun', 'door')])

                          
def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234 1234 41 927 29340519032487 00000000000")
    assert_equal(result, [('number', 3),
                          ('number', 91234),
                          ('number', 1234),
                          ('number', 41),
                          ('number', 927),
                          ('number', 29340519032487),
                          ('number', 00000000000)])


def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"),
                [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')])