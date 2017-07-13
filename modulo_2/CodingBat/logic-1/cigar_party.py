# coding=utf-8
def cigar_party(cigars, is_weekend):
    if not is_weekend and (40 <= cigars <= 60):
        check_cond = True
    elif is_weekend and cigars >= 40:
        check_cond = True
    else:
        check_cond = False

    return check_cond
