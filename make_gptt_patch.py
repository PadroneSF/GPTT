fout = []

fin = open('GPTT_yonge.cfg', 'r')
outf = open('zzzGPTT_base_parts.cfg', 'w')

parts = ''
start = True
tech = ''
sp = False

for line in fin:
    if ('id = ') in line:
        if start:
            start = False
        else:
            if len(parts) > 1:
                newline = '@PART['
                newline += parts
                outf.writelines([
                    newline[:-1] + ']:LAST[zzGPTT]\n',
                    '{\n',
                    '   @TechRequired = ' + tech,
                    '}\n',
                    ])
            tech = ''
            parts = ''
        ch = ''
        for c in line:
            if 'id = ' in ch:
                tech += c
            else:
                ch += c
        print(tech)
    elif ('	part = ') in line:
        ch = ''
        part = ''
        sp = False
        for c in line:
            if 'part = ' in ch:
                if c == '/':
                    part += c
                    break
                elif c == ' ':
                    sp = True
                else:
                    if sp:
                        part += '?'
                        sp = False
                    part += c
            else:
                ch += c
        parts+=part[:-1]+'|'

if len(parts) > 1:
    newline = '@PART['
    newline += parts
    outf.writelines([
        newline[:-1] + ']:LAST[zzGPTT]\n',
        '{\n',
        '   @TechRequired = ' + tech,
        '}\n',
        ])

outf.close()

