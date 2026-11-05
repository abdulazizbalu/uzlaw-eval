import re
def lat2cyr(s):
    s=s.replace("ʻ","'").replace("’","'")
    out=[];i=0;n=len(s)
    def up(c,ref): return c.upper() if ref.isupper() else c
    while i<n:
        c=s[i]; lo=c.lower(); nx=s[i+1].lower() if i+1<n else ''
        prev=s[i-1] if i>0 else ' '
        if lo=='o' and nx=="'": out.append(up('ў',c)); i+=2; continue
        if lo=='g' and nx=="'": out.append(up('ғ',c)); i+=2; continue
        if lo=='s' and nx=='h': out.append(up('ш',c)); i+=2; continue
        if lo=='c' and nx=='h': out.append(up('ч',c)); i+=2; continue
        if lo=='t' and nx=='s' and s[i+2:i+4].lower() in ('iy','ia'): out.append(up('ц',c)); i+=2; continue
        if lo=='y' and nx in 'oua' and nx:
            out.append(up({'o':'ё','u':'ю','a':'я'}[nx],c)); i+=2; continue
        if lo=='y' and nx=='e': out.append(up('е',c)); i+=2; continue
        if lo=='e':
            out.append(up('э' if not prev.isalpha() else 'е',c)); i+=1; continue
        if c=="'": out.append('ъ'); i+=1; continue
        m={'a':'а','b':'б','d':'д','f':'ф','g':'г','h':'ҳ','i':'и','j':'ж','k':'к','l':'л','m':'м','n':'н','o':'о','p':'п','q':'қ','r':'р','s':'с','t':'т','u':'у','v':'в','x':'х','y':'й','z':'з','c':'с','w':'в'}
        out.append(up(m[lo],c) if lo in m else c); i+=1
    return ''.join(out)
