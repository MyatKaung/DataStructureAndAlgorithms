def singleline_diff(line1,line2):
    min_len = min(len(line1),len(line2))
    for i in range(min_len):
        if line1[1] != line2[i]:
            return i
        
    if len(line1) == len(line2):
        return -1
    else:
        return min_len
    

def singleline_diff_format(line1, line2, idx):
    if '\n' in line1 or '\r' in line1 or '\n' in line2 or '\r' in line2:
        return ''
    if idx<0 or idx > min(len(line1),len(line2)):
        return ''
    separator = '=' * idx + '^'
    return line1 + '\n' + separator + '\n' + line2 + '\n'


line1 = 'abcdef'
line2 = 'abcef'
idx = 3

result = singleline_diff_format(line1, line2, idx)

print(result)