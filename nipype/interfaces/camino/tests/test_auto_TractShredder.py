# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.convert import TractShredder

def test_TractShredder_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bunchsize=dict(argstr='%d',
    position=2,
    units='NA',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='< %s',
    mandatory=True,
    position=-2,
    ),
    offset=dict(argstr='%d',
    position=1,
    units='NA',
    ),
    out_file=dict(argstr='> %s',
    genfile=True,
    position=-1,
    ),
    space=dict(argstr='%d',
    position=3,
    units='NA',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = TractShredder.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_TractShredder_outputs():
    output_map = dict(shredded=dict(),
    )
    outputs = TractShredder.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
