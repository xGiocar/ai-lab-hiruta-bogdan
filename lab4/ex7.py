a = [[1,2,3], [4,5,6], [[7,8], [9, 10]]]
deep_list_multi = [
    "L1_a", "L1_b",
    [  # Level 2
        "L2_a", "L2_b",
        [  # Level 3
            "L3_a", "L3_b",
            [  # Level 4
                "L4_a", "L4_b",
                [  # Level 5
                    "L5_a", "L5_b",
                    [  # Level 6
                        "L6_a", "L6_b",
                        [  # Level 7
                            "L7_a", "L7_b",
                            [  # Level 8
                                "L8_a", "L8_b",
                                [  # Level 9
                                    "L9_a", "L9_b",
                                    [  # Level 10
                                        "L10_a", "L10_b",
                                        [  # Level 11
                                            "L11_a", "L11_b", "L11_c"
                                        ],
                                        "L10_c"
                                    ],
                                    "L9_c"
                                ],
                                "L8_c"
                            ],
                            "L7_c"
                        ],
                        "L6_c"
                    ],
                    "L5_c"
                ],
                "L4_c"
            ],
            "L3_c"
        ],
        "L2_c"
    ],
    "L1_c"
]

def flatten(lst):
    result = []

    for elem in lst:
        if type(elem) == list:
            result.extend(flatten(elem))
        else:
            result.append(elem)

    return result

print(flatten(a))
print(flatten(deep_list_multi))