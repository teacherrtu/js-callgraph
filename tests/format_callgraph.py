import re

# Regex for representing the call graph itself
call_func = r'\'(.*)\' \(([^@]*)@([0-9]*):[0-9]*-[0-9]*\)'
native = r'\'(.*)\' \(Native\)'

reg_func = re.compile(call_func + ' -> ' + call_func)
reg_native = re.compile(call_func + ' -> ' + native)

def format_func(out):
    m = reg_func.match(out)

    fn_name1 = m.group(1)
    file1 = m.group(2)
    line1 = m.group(3)

    fn_name2 = m.group(4)
    file2 = m.group(5)
    line2 = m.group(6)

    return '{0}:{1}:{2} -> {3}:{4}:{5}'.format(file1, fn_name1, line1, file2, fn_name2, line2)

def format_native(out):
    m = reg_native.match(out)

    fn_name1 = m.group(1)
    file1 = m.group(2)
    line1 = m.group(3)

    native_name = m.group(4)

    return '{0}:{1}:{2} -> Native'.format(file1, fn_name1, line1)

def format_output(out):
    # print(out)
    if 'Native' in out:
        return format_native(out)
    else:
        return format_func(out)