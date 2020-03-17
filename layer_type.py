#'qgis._core.WkbType

#from qgis.core import QgsWkbTypes

layer=QgsMapLayerRegistry.instance().mapLayersByName('sx0005')[0]


def layer_type(layer):
    types={0:'WKBUnknown',1: 'WKBPoint',2:'WKBLineString', 3:'WKBPolygon', 4:'WKBMultiPoint',5:'WKBMultiLineString',6:'WKBMultiPolygon',7:'WKBNoGeometry',8:'WKBPoint25D',9: 'WKBLineString25D',10:'WKBPolygon25D',11:'WKBMultiPoint25D',12:'WKBMultiLineString25D',13:'WKBMultiPolygon25D'}
    t=layer.wkbType()
    if t in types:
        return types[t]

print layer_type(layer)

#print geometryDisplayString(layer.wkbType())
#print layer.geometryType()
#print layer.type()

#dict([(v, k) for k, v in QgsWkbTypes.__dict__.items() if isinstance(v, int)])