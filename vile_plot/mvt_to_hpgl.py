import vector_tile_base

def mvt_to_hpgl(mvt_buffer):
    hpgl = ['IN;SC;PU;VS5;PU;']
    # TODO: scale plotter coordinates to tile coordinates
    # Make sure to handle negative tile coordinates
    tile = vector_tile_base.VectorTile(mvt_buffer)
    for layer in tile.layers:
        for feature in layer.features:
            # Supports only points
            if feature.type != 'point':
                continue
            geometry = feature.get_geometry()
            hpgl.append('PU{},{};PD;'.format(geometry[0][0], geometry[0][1]))
    hpgl.append('PU;')
    return ''.join(hpgl)


def convert_mvt_file(mvt_filename, hpgl_filename):
    with open(mvt_filename, 'rb') as f_mvt:
        mvt_buffer = f_mvt.read()
        hpgl = mvt_to_hpgl(mvt_buffer)
    with open(hpgl_filename, 'w+') as f_hpgl:
        f_hpgl.write(hpgl)