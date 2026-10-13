path = 'D:\\tt_o-main\\Time-Table\\src\\scheduler.js'
with open(path, encoding='utf-8') as f:
    s = f.read()
old = "const isManualCategory = subject => ['placement', 'library'].includes(manualSubjectKind(subject));"
new = '''const isManualCategory = subject => {
  const k = manualSubjectKind(subject);
  const n = ((subject?.name||'') + ' ' + (subject?.code||'') + ' ' + (subject?.acronym||'')).toLowerCase();
  return ['placement', 'library'].includes(k) || n.includes('sdc') || n.includes('skill development');
};'''
s = s.replace(old, new)
with open(path, 'w', encoding='utf-8') as f:
    f.write(s)
print('ok')