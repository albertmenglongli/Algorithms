# s = '{track=lml, fullname=menglonglee}'[1:-1]
# d = {k.strip(): v for k, v in (x.split("=") for x in s.split(","))}

# exec('dd = dict(' + 'track="lml", fullname="menglonglee"'  + ')')
# print(dd)


def parse_raw(s):
    chars = list(s)
    stack = list()
    stack.append(chars[0])
    i = 1
    key = ''
    value = ''
    result = dict()

    while stack and i < len(chars):
        start = i
        while chars[i] not in ('{', '}', '=', ',') and i < len(chars):
            i += 1
        end = i
        words = ''.join(chars[start: end])
        if chars[i] == '=':
            i += 1
            key = words.lstrip()
            continue
        elif chars[i] == ',' or chars[i] == '}':
            if chars[i - 1] != '}':
                value = words
                result.update({key: value})
            if chars[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                i += 1
                continue
        elif chars[i] == '{':
            start = i
            inner_stack = list()
            while True:
                if chars[i] == '{':
                    inner_stack.append('{')
                if chars[i] == '}':
                    inner_stack.pop()
                if not inner_stack:
                    break
                i += 1
            end = i
            inner_string = ''.join(chars[start:end + 1])
            value = parse(inner_string)
            result.update({key: value})
            i += 1
            while chars[i] in (' ', ',') and i < len(chars) - 1:
                i += 1
            continue

    return result


def parse(s):
    if not s:
        return dict()
    assert s[0] == '{' and s[-1] == '}'
    if len(s) == 2:
        return dict()
    chars = list(s)
    stack = list()
    stack.append(chars[0])
    i = 1
    result = dict()

    while stack and i < len(chars):
        start = i
        while chars[i] not in ('{', '}', '=', ','):
            i += 1
        end = i
        words = ''.join(chars[start: end])
        if chars[i] == '=':
            i += 1
            key = words.lstrip()
        elif chars[i] == ',' or chars[i] == '}':
            if chars[i - 1] != '}':
                value = words
                result.update({key: value})
            if chars[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                i += 1
        elif chars[i] == '{':
            start = i
            inner_stack = list()
            while True:
                if chars[i] == '{':
                    inner_stack.append('{')
                if chars[i] == '}':
                    inner_stack.pop()
                if not inner_stack:
                    break
                i += 1
            end = i
            result.update({key: parse(''.join(chars[start:end + 1]))})
            i += 1
            while chars[i] in (' ', ','):
                i += 1

    return result

print('{track=lml, fullname=menglonglee} =>', parse('{track=lml, fullname=menglonglee}'))
print('{track={inside1=value1, inside2={inside3=value3}}, fullname=menglonglee} =>', parse('{track={inside1=value1, inside2={inside3=value3}}, fullname=menglonglee}'))
