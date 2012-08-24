all: fig1.svg fig1.png fig1.pdf bad_good.svg bad_good.png

fig1_panels = panel_timeseries.svg panel_timeseries.png panel_scatter.svg panel_scatter.png

bad_good_panels = scatter_bad.svg scatter_bad.png panel_scatter.svg panel_scatter.png

%.png: %.svg
	inkscape -f $< --export-dpi=90  --export-background=white --export-png=$@

%.pdf: %.svg
	inkscape -f $< --export-pdf=$@

panel_timeseries.svg: figpanel_timeseries.py
	python figpanel_timeseries.py

scatter_bad.svg panel_scatter.svg: figpanel_scatter.py
	python figpanel_scatter.py

fig1.svg: $(fig1_panels) fig1.py
	python fig1.py

bad_good.svg: $(bad_good_panels) bad_good.py
	python bad_good.py

.PHONY: clean
clean:
	rm -f *.svg *.png
