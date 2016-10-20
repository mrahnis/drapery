# using dask for out of core processing on large rasters
# https://gist.github.com/lpinner/bd57b54a5c6903e4a6a2
import logging
from shapely.geometry import Point, LineString

def drape(raster, feature):
    """Convert a 2D feature to a 3D feature by sampling a raster

    Parameters:
        raster (rasterio): raster to provide the z coordinate
        feature (dict): fiona feature record to convert

    Returns:
        result (Point or Linestring): shapely Point or LineString of xyz coordinate triples

    """
    coords = feature['geometry']['coordinates']
    geom_type = feature['geometry']['type']

    if geom_type == 'Point':
        xyz = sample(raster, [coords])
        result = Point(xyz[0])
    elif geom_type == 'LineString':
        xyz = sample(raster, coords)
        points = [Point(x, y, z) for x, y, z in xyz]
        result = LineString(points)
    else:
        logging.error('drape not implemented for {}'.format(geom_type))

    return result

def sample(raster, coords):
    """Sample a raster at given coordinates

    Given a list of coordinates, return a list of x,y,z triples with z coordinates sampled from an input raster

    Parameters:
        raster (rasterio): raster dataset to sample
        coords: array of tuples containing coordinate pairs (x,y) or triples (x,y,z)

    Returns:
        result: array of tuples containing coordinate triples (x,y,z)
        
    """
    if len(coords[0]) == 3:
        logging.info('Input is a 3D geometry, z coordinate will be updated.')
        z = raster.sample([(x, y) for x, y, z in coords], indexes=raster.indexes)
    else:
        z = raster.sample(coords, indexes=raster.indexes)

    result = [(vert[0], vert[1], vert_z) for vert, vert_z in zip(coords, z)]

    return result
