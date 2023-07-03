# -*- coding: utf-8 -*-
# -*- Python Version: 3.7 -*-

"""Functions for building PHX-Geometry from Ladybug / Honeybee Geometry."""

from typing import Union

from honeybee import aperture, face, shade
from ladybug_geometry.geometry3d.pointvector import Vector3D, Point3D
from ladybug_geometry.geometry3d.plane import Plane
from PHX.model import geometry


class InvalidRectangularFaceError(Exception):
    def __init__(self, _hb_face: Union[aperture.Aperture, face.Face, shade.Shade]):
        self.msg = (
            f"Error: Cannot create a PhxPolygonRectangular for the"
            f"Honeybee Face: {_hb_face.display_name}. Must have at least 4 vertices?"
            f"Only {len(_hb_face.vertices)} vertices found?"
        )
        super().__init__(self.msg)


# -----------------------------------------------------------------------------


def create_PhxVertix_from_lbt_Point3D(_lbt_Point3D: Point3D) -> geometry.PhxVertix:
    """Returns a new PhxVertix object with attributes based on an LBT-Point3D."""
    return geometry.PhxVertix(_lbt_Point3D.x, _lbt_Point3D.y, _lbt_Point3D.z)


def create_PhxVector_from_lbt_Vector3D(_lbt_vector3d: Vector3D) -> geometry.PhxVector:
    """Return a new PhxVector with attributes based on an LBT-Vector3D."""
    return geometry.PhxVector(
        _lbt_vector3d.x,
        _lbt_vector3d.y,
        _lbt_vector3d.z,
    )


def create_PhxPlane_from_lbt_Plane(_lbt_plane: Plane) -> geometry.PhxPlane:
    """Return a new PhxPlane with attributes based on an LBT-Plane"""
    return geometry.PhxPlane(
        create_PhxVector_from_lbt_Vector3D(_lbt_plane.n),
        create_PhxVertix_from_lbt_Point3D(_lbt_plane.o),
        create_PhxVector_from_lbt_Vector3D(_lbt_plane.x),
        create_PhxVector_from_lbt_Vector3D(_lbt_plane.y),
    )


def create_PhxPolygon_from_hb_Face(
    _hb_face: Union[aperture.Aperture, face.Face, shade.Shade]
) -> geometry.PhxPolygon:
    """Return a new PhxPolygon based on an input honeybee-Face.

    Arguments:
    ----------
        * _hb_face (Union[aperture.Aperture, face.Face, shade.Shade]): The Honeybee-Face
            to base the PhxPolygon on.

    Returns:
    --------
        * (geometry.PhxPolygon): The new PhxPolygon object.
    """
    phx_polygon = geometry.PhxPolygon(
        _hb_face.display_name,
        _hb_face.geometry.area,
        create_PhxVertix_from_lbt_Point3D(_hb_face.geometry.center),
        create_PhxVector_from_lbt_Vector3D(_hb_face.normal),
        create_PhxPlane_from_lbt_Plane(_hb_face.geometry.plane),
    )

    for v in _hb_face.vertices:
        phx_polygon.add_vertix(create_PhxVertix_from_lbt_Point3D(v))

    return phx_polygon


def create_PhxPolygonRectangular_from_hb_Face(
    _hb_face: Union[aperture.Aperture, face.Face, shade.Shade], _tolerance: float = 0.001
) -> geometry.PhxPolygonRectangular:
    """Return a new PhxPolygonRectangular based on an input honeybee-Face.

    Arguments:
    ----------
        * _hb_face (Union[aperture.Aperture, face.Face, shade.Shade]): The Honeybee-Face
            to base the PhxPolygon on.

    Returns:
    --------
        * (geometry.PhxPolygonRectangular): The new PhxPolygonRectangular object.
    """

    # -- Try and clean up the polygon geometry
    face_polygon = _hb_face.geometry
    face_polygon = face_polygon.remove_colinear_vertices(_tolerance)
    if len(face_polygon.vertices) != 4:
        raise InvalidRectangularFaceError(_hb_face)

    # -- Create a new PhxPolygonRectangular
    phx_polygon = geometry.PhxPolygonRectangular(
        _hb_face.display_name,
        _hb_face.geometry.area,
        _center=create_PhxVertix_from_lbt_Point3D(_hb_face.geometry.center),
        normal_vector=create_PhxVector_from_lbt_Vector3D(_hb_face.normal),
        plane=create_PhxPlane_from_lbt_Plane(_hb_face.geometry.plane),
    )

    # -- Set the vertices using the upper_left_counter_clockwise_vertices method.
    # -- Note: cannot use the 'lower_right_corner' property as it is not always
    # -- the lower right corner of the face. It shows the vertix of the bounding box
    # -- which is not aligned when the face has been rotated.
    vertices = face_polygon.upper_left_counter_clockwise_vertices
    phx_polygon.vertix_upper_left = create_PhxVertix_from_lbt_Point3D(vertices[0])
    phx_polygon.vertix_upper_right = create_PhxVertix_from_lbt_Point3D(vertices[1])
    phx_polygon.vertix_lower_right = create_PhxVertix_from_lbt_Point3D(vertices[2])
    phx_polygon.vertix_lower_left = create_PhxVertix_from_lbt_Point3D(vertices[3])

    return phx_polygon
