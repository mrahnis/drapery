import sys
import logging
import warnings

import click
import fiona
import rasterio
from shapely.geometry import mapping

import drapery

"""
See
https://github.com/mapbox/rasterio/blob/master/rasterio/rio/sample.py
"""
@click.command(options_metavar='<options>')
@click.argument('source_f', nargs=1, type=click.Path(exists=True), metavar='<source_file>')
@click.argument('raster_f', nargs=1, type=click.Path(exists=True), metavar='<raster_file>')
@click.option('-o', '--output', metavar='<output_file>', type=click.Path(), help="Output file path")
@click.option('-v', '--verbose', is_flag=True, help='Enables verbose mode')
def cli(source_f, raster_f, output, verbose):
    """
    Converts 2D geometries to 3D using GEOS sample through fiona.

    \b
    Example:
    drape point.shp elevation.tif -o point_z.shp

    """
    with fiona.open(source_f, 'r') as source:
        source_driver = source.driver
        source_crs = source.crs
        sink_schema = source.schema.copy()

        source_geom = source.schema['geometry']
        if source_geom == 'Point':
            sink_schema['geometry'] = '3D Point'
        elif source_geom == 'LineString':
            sink_schema['geometry'] = '3D LineString'
        elif source_geom == '3D Point' or source_geom == '3D LineString':
            pass
        else:
            click.BadParameter("Source geometry type {} not implemented".format(source_geom))

        with rasterio.open(raster_f) as raster:
            if source_crs != raster.crs:
                click.BadParameter("Features and raster have different CRS.")
            if raster.count > 1:
                warnings.warn("Found {0} bands in {1}, expected a single band raster".format(raster.bands, raster_f))
            supported = ['int16', 'int32', 'float32', 'float64']
            if raster.dtypes[0] not in supported:
                warnings.warn("Found {0} type in {1}, expected one of {2}".format(raster.dtypes[0]), raster_f, supported)
            with fiona.open(
                output, 'w',
                driver=source_driver,
                crs=source_crs,
                schema=sink_schema) as sink:

                for feature in source:
                    try:
                        feature_z = drapery.drape(raster, feature)
                        sink.write({
                            'geometry': mapping(feature_z),
                            'properties': feature['properties'],
                        })
                    except Exception:
                        logging.exception("Error processing feature %s:", feature['id'])
            #print(sink.closed)
        #print(raster.closed)
    #print(source.closed)
