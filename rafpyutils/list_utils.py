import re

def insert_sublist_between_markers(input_list, input_sublist, start_pattern, end_pattern):
    """
    Insert input_sublist into input_list between start_pattern and end_pattern.
    The final list will be resized accordingly.

    Args:
        input_list (list): The list to modify.
        input_sublist (list): The sublist to insert.
        start_pattern (str or Pattern): Pattern or regex to identify the start marker.
        end_pattern (str or Pattern): Pattern or regex to identify the end marker.

    Returns:
        list: A new list with the sublist inserted between markers.
    """
    start_index = None
    end_index = None

    for idx, line in enumerate(input_list):
        if start_index is None and re.search(start_pattern, line):
            start_index = idx
        if end_index is None and re.search(end_pattern, line):
            end_index = idx

    if start_index is None:
        raise ValueError(f'{start_pattern=} must match at least once')
    if end_index is None:
        raise ValueError(f'{end_pattern=} must match at least once')

    if start_index >= end_index:
        raise ValueError(f'{start_pattern} (index {start_index}) cannot be after {end_pattern} (index {end_index})')

    output_list = (
        input_list[:start_index + 1]
        + input_sublist
        + input_list[end_index:]
    )

    return output_list
