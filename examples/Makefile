all: fig1.svg fig1.png fig1.pdf bad_good.svg bad_good.png

fig1_panels = panel_timeseries.svg panel_timeseries.png panel_scatter.svg panel_scatter.png

bad_good_panels = scatter_bad.svg scatter_bad.png panel_scatter.svg panel_scatter.png

# A rule to convert any svg file to png with inkscape
%.png: %.svg
	inkscape -f $< --export-dpi=90  --export-background=white --export-png=$@

# A rule to convert any svg file to pdf with inkscape
%.pdf: %.svg
	inkscape -f $< --export-pdf=$@

# build our timeseries panel
panel_timeseries.svg: figpanel_timeseries.py
	python figpanel_timeseries.py

# build our scatterplot panels (two targets)
scatter_bad.svg panel_scatter.svg: figpanel_scatter.py
	python figpanel_scatter.py

# combine panels into a single whole-figure svg file
fig1.svg: $(fig1_panels) fig1.py
	python fig1.py

# another multi-panel figure
bad_good.svg: $(bad_good_panels) bad_good.py
	python bad_good.py

.PHONY: clean
clean:
	rm -f *.svg *.png
