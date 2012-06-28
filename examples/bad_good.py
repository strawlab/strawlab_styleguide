import svg_stack as ss

doc0 = ss.Document()

layout0 = ss.HBoxLayout()
layout0.addSVG('scatter_bad.svg',
               xml=('<g>'
                    '<text font-family="Arial" font-size="14" dy="10" dx="5" style="font-weight:bold">simple matplotlib:</text>'
                    '</g>'))
layout0.addSVG('panel_scatter.svg',
               xml=('<g>'
                    '<text font-family="Arial" font-size="14" dy="10" dx="5" style="font-weight:bold">better style:</text>'
                    '</g>'))

#layout0.setSpacing(10)
doc0.setLayout(layout0)

doc0.save('bad_good.svg')
