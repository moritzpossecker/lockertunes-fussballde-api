from fontTools.ttLib import TTFont

font = TTFont('font.woff')
cmap = font['cmap']
searched_glyph_name = 'hyphen'  # name of '-' symbol

for table in cmap.tables:
    for codepoint, glyph_name in table.cmap.items():
        if glyph_name == searched_glyph_name:
            print(f"Codepoint: {hex(codepoint)}, Glyph Name: {glyph_name}")