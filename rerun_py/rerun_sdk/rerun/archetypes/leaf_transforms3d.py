# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/archetypes/leaf_transforms3d.fbs".

# You can extend this class by creating a "LeafTransforms3DExt" class in "leaf_transforms3d_ext.py".

from __future__ import annotations

from typing import Any

from attrs import define, field

from .. import components, datatypes
from .._baseclasses import (
    Archetype,
)
from ..error_utils import catch_and_log_exceptions

__all__ = ["LeafTransforms3D"]


@define(str=False, repr=False, init=False)
class LeafTransforms3D(Archetype):
    """
    **Archetype**: One or more transforms between the parent and the current entity which are *not* propagated in the transform hierarchy.

    For transforms that are propagated in the transform hierarchy, see [`archetypes.Transform3D`][rerun.archetypes.Transform3D].

    If both [`archetypes.LeafTransforms3D`][rerun.archetypes.LeafTransforms3D] and [`archetypes.Transform3D`][rerun.archetypes.Transform3D] are present,
    first the tree propagating [`archetypes.Transform3D`][rerun.archetypes.Transform3D] is applied, then [`archetypes.LeafTransforms3D`][rerun.archetypes.LeafTransforms3D].

    Currently, most visualizers support only a single leaf transform per entity.
    Check archetype documentations for details - if not otherwise specified, only the first leaf transform is applied.

    From the point of view of the entity's coordinate system,
    all components are applied in the inverse order they are listed here.
    E.g. if both a translation and a max3x3 transform are present,
    the 3x3 matrix is applied first, followed by the translation.

    Example
    -------
    ### Regular & leaf transform in tandom:
    ```python
    import numpy as np
    import rerun as rr

    rr.init("rerun_example_leaf_transform3d_combined", spawn=True)

    rr.set_time_sequence("frame", 0)

    # Log a box and points further down in the hierarchy.
    rr.log("world/box", rr.Boxes3D(half_sizes=[[1.0, 1.0, 1.0]]))
    rr.log("world/box/points", rr.Points3D(np.vstack([xyz.ravel() for xyz in np.mgrid[3 * [slice(-10, 10, 10j)]]]).T))

    for i in range(0, 180):
        rr.set_time_sequence("frame", i)

        # Log a regular transform which affects both the box and the points.
        rr.log("world/box", rr.Transform3D(rotation_axis_angle=rr.RotationAxisAngle([0, 0, 1], angle=rr.Angle(deg=i * 2))))

        # Log an leaf transform which affects only the box.
        rr.log("world/box", rr.LeafTransforms3D(translations=[0, 0, abs(i * 0.1 - 5.0) - 5.0]))
    ```
    <center>
    <picture>
      <source media="(max-width: 480px)" srcset="https://static.rerun.io/leaf_transform3d/41674f0082d6de489f8a1cd1583f60f6b5820ddf/480w.png">
      <source media="(max-width: 768px)" srcset="https://static.rerun.io/leaf_transform3d/41674f0082d6de489f8a1cd1583f60f6b5820ddf/768w.png">
      <source media="(max-width: 1024px)" srcset="https://static.rerun.io/leaf_transform3d/41674f0082d6de489f8a1cd1583f60f6b5820ddf/1024w.png">
      <source media="(max-width: 1200px)" srcset="https://static.rerun.io/leaf_transform3d/41674f0082d6de489f8a1cd1583f60f6b5820ddf/1200w.png">
      <img src="https://static.rerun.io/leaf_transform3d/41674f0082d6de489f8a1cd1583f60f6b5820ddf/full.png" width="640">
    </picture>
    </center>

    """

    def __init__(
        self: Any,
        *,
        translations: datatypes.Vec3DArrayLike | None = None,
        rotation_axis_angles: datatypes.RotationAxisAngleArrayLike | None = None,
        quaternions: datatypes.QuaternionArrayLike | None = None,
        scales: datatypes.Vec3DArrayLike | None = None,
        mat3x3: datatypes.Mat3x3ArrayLike | None = None,
    ):
        """
        Create a new instance of the LeafTransforms3D archetype.

        Parameters
        ----------
        translations:
            Translation vectors.
        rotation_axis_angles:
            Rotations via axis + angle.
        quaternions:
            Rotations via quaternion.
        scales:
            Scaling factors.
        mat3x3:
            3x3 transformation matrices.

        """

        # You can define your own __init__ function as a member of LeafTransforms3DExt in leaf_transforms3d_ext.py
        with catch_and_log_exceptions(context=self.__class__.__name__):
            self.__attrs_init__(
                translations=translations,
                rotation_axis_angles=rotation_axis_angles,
                quaternions=quaternions,
                scales=scales,
                mat3x3=mat3x3,
            )
            return
        self.__attrs_clear__()

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            translations=None,  # type: ignore[arg-type]
            rotation_axis_angles=None,  # type: ignore[arg-type]
            quaternions=None,  # type: ignore[arg-type]
            scales=None,  # type: ignore[arg-type]
            mat3x3=None,  # type: ignore[arg-type]
        )

    @classmethod
    def _clear(cls) -> LeafTransforms3D:
        """Produce an empty LeafTransforms3D, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    translations: components.LeafTranslation3DBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.LeafTranslation3DBatch._optional,  # type: ignore[misc]
    )
    # Translation vectors.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    rotation_axis_angles: components.LeafRotationAxisAngleBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.LeafRotationAxisAngleBatch._optional,  # type: ignore[misc]
    )
    # Rotations via axis + angle.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    quaternions: components.LeafRotationQuatBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.LeafRotationQuatBatch._optional,  # type: ignore[misc]
    )
    # Rotations via quaternion.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    scales: components.LeafScale3DBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.LeafScale3DBatch._optional,  # type: ignore[misc]
    )
    # Scaling factors.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    mat3x3: components.LeafTransformMat3x3Batch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.LeafTransformMat3x3Batch._optional,  # type: ignore[misc]
    )
    # 3x3 transformation matrices.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
