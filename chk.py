path = 'D:\\tt_o-main\\Time-Table\\src\\data-model.js'
with open(path, encoding='utf-8') as f:
    s = f.read()
# ensure dist also has? but build copies src->dist/src; so we need to rebuild
# but build just copies; so we should run build again - it already ran? let us check
print('rebuild needed')