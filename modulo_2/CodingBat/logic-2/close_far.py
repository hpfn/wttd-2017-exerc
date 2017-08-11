# coding=utf-8
def close_far(a, b, c):
    a_b_diff = abs(a - b)
    b_c_diff = abs(b - c)
    a_c_diff = abs(a - c)

    ab_ac_diff_sum = a_b_diff + a_c_diff
    bc_ab_diff_sum = b_c_diff + a_b_diff
    ac_bc_diff_sum = a_c_diff + b_c_diff

    return (
        (ab_ac_diff_sum >= 4 or bc_ab_diff_sum >= 4 or ac_bc_diff_sum >= 4)
        and
        (b_c_diff < 2 or a_c_diff < 2 or a_b_diff < 2)
    )


    # result False
    # if ab_ac_diff_sum >= 4 and b_c_diff < 2:
    #    result = True
    # elif bc_ab_diff_sum >= 4 and a_c_diff < 2:
    #    result = True
    # elif ac_bc_diff_sum >= 4 and a_b_diff < 2:
    #    result = True

    # return result
