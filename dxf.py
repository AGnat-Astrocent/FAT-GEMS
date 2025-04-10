import ezdxf

def create_doc():
    doc = ezdxf.new('R2010',units=ezdxf.units.MM)
    # Create model space
    msp = doc.modelspace()
    # Add a new layer
    layer_pattern = "Pattern"
    doc.layers.add(layer_pattern)
    layer_shape = "Shape"
    doc.layers.add(layer_shape)
    layer_hole = "Hole"
    doc.layers.add(layer_hole)
    layer_active = "Active"
    doc.layers.add(layer_active)
    return doc, msp

def dxf_circle(msp, center, radius, layer):
    msp.add_circle(center, radius, dxfattribs={"layer": layer})

def dxf_square(msp, corner, layer):
    points = [(-corner, -corner), (corner, -corner), (corner, corner), (-corner, corner), (-corner, -corner)]
    msp.add_lwpolyline(points, dxfattribs={"layer": layer})