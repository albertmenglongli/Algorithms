def dfs(s, start,step,ip,result):
    if len(s) == start and step == 4:
        result.append(ip[:-1])
        return
    if start+4-step<= len(s) <= start+(4-step)*3 :
        num = 0
        for i in range(start, start+3):
            if i > len(s) - 1 : return
            num = int(s[i]) + num * 10
            if num <= 255:
                ip += s[i]
                dfs(s, i+1, step+1, ip+'.', result)
            if num == 0:
                break

def main():
    s = '25525511135';
    result = list()
    ip = ''
    dfs(s, 0, 0, ip, result)
    for r in result:
        print r


if __name__=="__main__":
    main()
