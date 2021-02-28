from mock import patch

from tierlist_manipulator import TierlistManipulator


@patch.object(TierlistManipulator, 'load_tier_list')
def test_get_all_tierlist_items(mocked_function):
    mocked_function.return_value = {
        'S': [],
        'A': ['Balade quotidienne sous le soleil'],
        'B': [],
        'C': [],
        'D': ['Caca au pot'],
        'E': [],
        'F': []
    }
    manipulator = TierlistManipulator("tierlist")
    result = manipulator.get_all_items()
    assert result == ['Balade quotidienne sous le soleil', 'Caca au pot']