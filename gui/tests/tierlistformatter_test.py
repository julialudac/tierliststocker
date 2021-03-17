from mock import patch
from tierlistformatter import TierlistFormatter


@patch('tierlist_manipulator.TierlistManipulator.load_tier_list')
def test_fill(mocked_function):
    mocked_function.return_value = {
        'S': [],
        'A': [],
        'B': [],
        'C': [],
        'D': ['Caca au pot'],
        'E': [],
        'F': []
    }
    expected = [
        'S: ',
        'A: ',
        'B: ',
        'C: ',
        'D: Caca au pot',
        'E: ',
        'F: '
    ]
    tierlist_formatter = TierlistFormatter("whatever")
    assert tierlist_formatter.tier_items_list == expected

