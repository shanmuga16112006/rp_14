path = r'D:\tt_o-main\Time-Table\src\scheduler.js'
with open(path, encoding='utf-8') as f:
    s = f.read()
old = "const manualSubjectKind = subject => String(subject?.manualKind || subject?.kind || '').toLowerCase();"
new = '''const manualSubjectKind = subject => {
  const k = String(subject?.manualKind || subject?.kind || '').toLowerCase();
  if (k === 'sdc' || 'skill development' in k) return 'placement';
  return k;
};'''
if old in s:
    s = s.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(s)
    print('ok')
else:
    print('no')