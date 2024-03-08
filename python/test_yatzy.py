from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/



def test_Chance_SumOfFour():
        expected = 14
        actual = Yatzy.chance(1,1,3,3,6)
        assert expected == actual

def test_Yatzy_SameNumber():
        expected = 50
        dice = [1,1,1,1,1]
        actual = Yatzy.yatzy(dice)
        assert expected == actual

def test_Yatzy_IsNotTheSameNumber():
        expected = 0
        dice = [1,1,1,2,1]
        actual = Yatzy.yatzy(dice)
        assert expected == actual

def test_Ones_placedOnOnce():
        expected = 0
        actual = Yatzy.ones(3,3,3,4,5)
        assert expected == actual

def test_Two_PlacedOnTwos():
        expected = 4
        actual = Yatzy.twos(2,3,2,5,1)
        assert expected == actual
