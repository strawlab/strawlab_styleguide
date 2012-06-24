import svg_stack as ss

doc0 = ss.Document()

layout0 = ss.VBoxLayout()
layout0.addSVG('panel_timeseries.svg',stretch=1,alignment=ss.AlignCenter,
               xml=('<g>'
                    '<text font-family="Arial" font-size="12" style="font-weight:bold" dy="10" dx="5">A</text>'
                    '<text font-family="Arial" font-size="12" style="font-weight:bold" dy="280" dx="5">B</text>'
                    '</g>'))
layout0.addSVG('panel_scatter.svg',stretch=0,alignment=ss.AlignLeft,
               xml=('<g>'
                    '<text font-family="Arial" font-size="12" style="font-weight:bold" dy="10" dx="5">C</text>'
                    '</g>'))

layout0.setSpacing(10)
doc0.setLayout(layout0)

doc0.save('fig1.svg')
