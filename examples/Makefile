all: fig1.svg

fig1_panels = panel_timeseries.svg panel_scatter.svg

panel_timeseries.svg: figpanel_timeseries.py
	python figpanel_timeseries.py

panel_scatter.svg: figpanel_scatter.py
	python figpanel_scatter.py

fig1.svg: $(fig1_panels) fig1.py
	python fig1.py

.PHONY: clean
clean:
	rm -f *.svg
