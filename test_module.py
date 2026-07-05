import unittest
import pandas as pd
from medical_data_visualizer import draw_cat_plot, draw_heat_map


class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = draw_cat_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_labels(self):
        actual = self.ax.get_xlabel()
        expected = "variable"
        self.assertEqual(
            actual, expected,
            "Expected line plot xlabel to be 'variable'"
        )
        actual = self.ax.get_ylabel()
        expected = "total"
        self.assertEqual(
            actual, expected,
            "Expected line plot ylabel to be 'total'"
        )
        actual = []
        for label in self.ax.get_xaxis().get_majorticklabels():
            actual.append(label.get_text())
        expected = [
            'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'
        ]
        self.assertEqual(
            actual, expected,
            "Expected bar plot legend labels to be 'active', 'alco', "
            "'cholesterol', 'gluc', 'overweight', 'smoke'"
        )

    def test_bar_plot_number_of_bars(self):
        actual = len(
            [rect for rect in self.ax.get_children()
             if isinstance(rect, __import__('matplotlib').patches.Rectangle)]
        )
        expected = 13
        self.assertGreaterEqual(
            actual, expected,
            "Expected a certain number of bars in the bar plot."
        )


class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = draw_heat_map()
        self.ax = self.fig.axes[0]

    def test_heat_map_labels(self):
        actual = []
        for label in self.ax.get_xticklabels():
            actual.append(label.get_text())
        expected = [
            'id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo',
            'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio',
            'overweight'
        ]
        self.assertEqual(
            actual, expected,
            "Expected heat map labels to be 'id', 'age', 'sex', 'height', "
            "'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', "
            "'alco', 'active', 'cardio', 'overweight'"
        )


if __name__ == "__main__":
    unittest.main()
