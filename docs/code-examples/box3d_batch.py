"""Log a batch of oriented bounding boxes."""
import rerun as rr
import rerun.experimental as rr2
from rerun.experimental import dt as rrd
from scipy.spatial.transform import Rotation

rr.init("rerun_example_box3d", spawn=True)

rr2.log(
    "/",
    rr2.AnnotationContext(
        [
            rrd.ClassDescription(info=(1, "red", (255, 0, 0))),
            rrd.ClassDescription(info=(2, "green", (0, 255, 0))),
        ]
    ),
)

rr.log_obbs(
    "batch",
    half_sizes=[[2.0, 2.0, 1.0], [1.0, 1.0, 0.5]],
    rotations_q=[
        Rotation.from_euler("xyz", [0, 0, 0]).as_quat(),
        Rotation.from_euler("xyz", [0, 0, 45]).as_quat(),
    ],
    positions=[[2, 0, 0], [-2, 0, 0]],
    stroke_widths=0.05,
    class_ids=[2, 1],
)
