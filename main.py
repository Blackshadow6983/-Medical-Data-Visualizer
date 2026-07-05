import medical_data_visualizer as mdv
import unittest

# Draw the plots and save them as catplot.png and heatmap.png
mdv.draw_cat_plot()
mdv.draw_heat_map()

# Run the unit tests automatically
unittest.main(module='test_module', exit=False)
