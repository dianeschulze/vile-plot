from vile_plot.mvt_to_hpgl import mvt_to_hpgl
import os

TEST_DIR = os.path.dirname(__file__)

def test_something():
    mvt_filename = '{}/fixtures/mvt_fixtures/real_world_sf_15_5237_12665.mvt'.format(TEST_DIR)
    with open(mvt_filename, 'rb') as f_mvt:
        mvt_buffer = f_mvt.read()
        hpgl = mvt_to_hpgl(mvt_buffer)
        assert isinstance(hpgl, str)
        