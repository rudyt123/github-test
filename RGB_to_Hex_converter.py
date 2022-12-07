def rgb(r, g, b):
    hex_vals = {
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'

    }
    list_get = [10,11,12,13,14,15]
    
    if r > 255:
        r = 255
    if r < 0:
        r = 0
    r_1 = r//16
    r_2 = r - (16*r_1)
    for r_val in list_get:
        if r_val == r_1:
            r_1 = hex_vals.get(r_val)
        if r_val == r_2:
            r_2 = hex_vals.get(r_val)
    r_rgb = ''
    r_rgb += str(r_1)
    r_rgb += str(r_2)
    print(r_rgb)

    if g > 255:
        g = 255
    if g < 0:
        g = 0
    g_1 = g//16
    g_2 = g - (16*g_1)
    for g_val in list_get:
        if g_val == g_1:
            g_1 = hex_vals.get(g_val)
        if g_val == g_2:
            g_2 = hex_vals.get(g_val)
    g_rgb = ''
    g_rgb += str(g_1)
    g_rgb += str(g_2)
    print(g_rgb)

    if b > 255:
        b = 255
    if b < 0:
        b = 0
    b_1 = b//16
    b_2 = b - (16*b_1)
    for b_val in list_get:
        if b_val == b_1:
            b_1 = hex_vals.get(b_val)
        if b_val == b_2:
            b_2 = hex_vals.get(b_val)
    b_rgb = ''
    b_rgb += str(b_1)
    b_rgb += str(b_2)
    print(b_rgb)
    


rgb(723,-99,3)
