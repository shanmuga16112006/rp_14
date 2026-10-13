path = 'D:\\tt_o-main\\Time-Table\\src\\app.js'
with open(path, encoding='utf-8') as f:
    s = f.read()
# replace with improved
old = '  const required = Number(subject.labPeriods || subject.placementPeriods || subject.libraryPeriods || subject.theoryPeriods || 0);'
new = '''  const sName = ((subject.name || '') + ' ' + (subject.code || '') + ' ' + (subject.acronym || '')).toLowerCase();
  const required = Number(subject.labPeriods || subject.placementPeriods || subject.libraryPeriods || subject.theoryPeriods || (sName.includes('sdc') || sName.includes('skill development') ? (subject.theoryPeriods || subject.periods || 0) : 0) || 0);'''
if old in s:
    s = s.replace(old, new)
with open(path, 'w', encoding='utf-8') as f:
    f.write(s)
print('ok')