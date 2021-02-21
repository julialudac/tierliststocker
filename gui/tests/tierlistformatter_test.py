from mock import patch
from tierlistformatter import TierlistFormatter


@patch.object(TierlistFormatter, 'load_tier_list')
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
    tierlist_formatter = TierlistFormatter()
    assert tierlist_formatter.tier_items_list == expected

