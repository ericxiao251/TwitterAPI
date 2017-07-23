def flatten_dict(dic):
    flat_dict = {}

    def unpack(prefix, d):
        for key, value in d.items():
            if isinstance(value, dict):
                unpack(str(key + '_'), value)
            else:
                flat_dict[(prefix + key)] = value

    unpack('', dic)

    return flat_dict

def test_one_dimension_dict():
    sample_dict = {
        'key_1': 1,
        'key_2': 2,
    }
    expected = {
        'key_1': 1,
        'key_2': 2,
    }
    output = flatten_dict(sample_dict)

    print(output == expected)

def test_two_dimension_dict():
    sample_dict = {
        'key_1': 1,
        '2': {
            'key_2': 2,
            'key_3': 3,
        },
    }
    expected = {
        'key_1': 1,
        '2_key_2': 2,
        '2_key_3': 3,
    }
    output = flatten_dict(sample_dict)

    print(output == expected)


def test_fourth_dimension_dict():
    sample_dict = {
        'key_1': 1,
        '2': {
            'key_2': 2,
            '3': {
                'key_3': 3,
                '4': {
                    'key_4': 4,
                    'key_5': 5,
                },
            },
        },
    }
    expected = {
        'key_1': 1,
        '2_key_2': 2,
        '3_key_3': 3,
        '4_key_4': 4,
        '4_key_5': 5,
    }
    output = flatten_dict(sample_dict)

    print(output == expected)

def test_flatten_dict():
    sample_dict = {
        'key_1': 1,
        '2': {
            'key_2': 2,
            'key_3': 3,
        },
        'key_4': 4,
        '2.1': {
            'key_5': 5,
            'key_6': 6,
        },
    }
    expected = {
        'key_1': 1,
        '2_key_2': 2,
        '2_key_3': 3,
        'key_4': 4,
        '2.1_key_5': 5,
        '2.1_key_6': 6,
    }
    output = flatten_dict(sample_dict)

    print(output == expected)


if __name__ == '__main__':
    test_one_dimension_dict()
    test_two_dimension_dict()
    test_fourth_dimension_dict()
    test_flatten_dict()
