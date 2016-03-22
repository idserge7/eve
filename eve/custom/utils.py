""" Custom utils for eve framework
"""
NTH = {
    '$first': 0,
    '$second': 1,
    '$third': 2,
    '$fourth': 3,
    '$fifth': 4,
    '$sixth': 5,
    '$seventh': 6,
    '$eighth': 7,
    '$ninth': 8,
    '$tenth': 9,
}


def get_stage(stage_title):
    """Converts first_stage to 0, second_stage to 1 etc.
    """
    stage = stage_title.split('_')[0]
    return NTH.get(stage)


def user_aggregation_handler(pipeline, key, value):
    """Change pipeline stages using key and value
    """
    stage = get_stage(key)
    if stage is None:
        return

    pipeline[stage]['$match'] = value
