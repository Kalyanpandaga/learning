def get_mock(mocker, func_to_mock, return_value=None, side_effect=None):
    mock = mocker.patch(
        "{}.{}".format(func_to_mock.__module__, func_to_mock.__qualname__)
    )
    if return_value:
        mock.return_value = return_value
    if side_effect:
        mock.side_effect = side_effect
    return mock
