def rep_char(c, n):
    return c * n
    
def draw_line_string(s):
    nstr = len(s)
    line1 = rep_char('-', nstr + 2)
    line2 = s 
    line3 = rep_char('-', nstr + 2)

    print(line1)
    print(line2)
    print(line3)

name: input("Input his/her name:")

msg1 = 'Hello'+name
msg2= 'Welcome to Seoul.'
nstr=len(msg1) if (len(msg1) > len(msg2)) else len(msg2)

draw_line_string(rep_char(' ',nstr))
draw_line_string(msg1)
draw_line_string(msg2)
draw_line_string(rep_char(' '),nstr)