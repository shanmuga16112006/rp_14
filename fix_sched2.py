path = 'D:\\tt_o-main\\Time-Table\\src\\scheduler.js'
with open(path, encoding='utf-8') as f:
    s = f.read()
# fix 'skill development' in k (k is string)
s = s.replace("'skill development' in k", 'k.includes(\"skill development\")')
with open(path, 'w', encoding='utf-8') as f:
    f.write(s)
print('ok')