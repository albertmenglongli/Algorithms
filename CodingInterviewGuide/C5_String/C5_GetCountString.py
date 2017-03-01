def get_count_string(s):
    if s:
        eles = list(s)
        new_eles = list()
        pre = ''
        cur_cnt = 0
        for idx, c in enumerate(eles):
            if c != pre:
                if cur_cnt != 0:
                    new_eles.append(cur_cnt)
                cur_cnt = 1
                new_eles.append(c)
            else:
                cur_cnt += 1
            pre = c
        new_eles.append(cur_cnt)
        return '_'.join([str(v) for v in new_eles])
    else:
        return ''


print get_count_string('aaabbadddffc')
