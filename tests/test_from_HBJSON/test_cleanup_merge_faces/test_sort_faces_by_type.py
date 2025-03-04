from math import radians
from honeybee.face import Face
from PHX.from_HBJSON.cleanup_merge_faces import (
    sort_hb_faces_by_type,
    _hb_face_type_unique_key,
)
from honeybee.facetype import Wall, RoofCeiling, Floor, AirBoundary, _FaceTypes


def faces_are_same(f1, f2):
    """Check if two faces are the same."""
    return (
        f1.geometry == f2.geometry
        and f1.type == f2.type
        and f1.display_name == f2.display_name
    )


def test_sort_faces_by_type():
    # Test case 1: Empty list of faces
    f1 = Face.from_vertices(
        "f1", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=Wall()
    )

    faces = [f1]
    sorted_faces = sort_hb_faces_by_type(faces)
    assert len(sorted_faces) == 1
    assert faces_are_same(sorted_faces[0][0], f1)


def test_sort_faces_by_type_all_same():
    # Test case 2: faces with the same type
    f1 = Face.from_vertices(
        "f1", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=Wall()
    )
    f2 = Face.from_vertices(
        "f2", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=Wall()
    )
    f3 = Face.from_vertices(
        "f3", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=Wall()
    )

    faces = [f1, f2, f3]
    sorted_faces = sort_hb_faces_by_type(faces)
    assert len(sorted_faces) == 1
    assert faces_are_same(sorted_faces[0][0], f1)
    assert faces_are_same(sorted_faces[0][1], f2)
    assert faces_are_same(sorted_faces[0][2], f3)


def test_sort_faces_by_type_all_different():
    # Test case 2: faces with the same type
    f1 = Face.from_vertices(
        "f1", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=Wall()
    )
    f2 = Face.from_vertices(
        "f2", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=Floor()
    )
    f3 = Face.from_vertices(
        "f3", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=RoofCeiling()
    )

    faces = [f1, f2, f3]
    sorted_faces = sort_hb_faces_by_type(faces)
    assert len(sorted_faces) == 3
    assert faces_are_same(sorted_faces[0][0], f1)
    assert faces_are_same(sorted_faces[1][0], f2)
    assert faces_are_same(sorted_faces[2][0], f3)


def test_sort_faces_by_type_mixed():
    # Test case 2: faces with the same type
    f1 = Face.from_vertices(
        "f1", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=Wall()
    )
    f2 = Face.from_vertices(
        "f2", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=Floor()
    )
    f3 = Face.from_vertices(
        "f3", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=RoofCeiling()
    )
    f4 = Face.from_vertices(
        "f4", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)], type=Wall()
    )

    faces = [f1, f2, f3, f4]
    sorted_faces = sort_hb_faces_by_type(faces)
    assert len(sorted_faces) == 3
    assert faces_are_same(sorted_faces[0][0], f1)
    assert faces_are_same(sorted_faces[0][1], f4)
    assert faces_are_same(sorted_faces[1][0], f2)
    assert faces_are_same(sorted_faces[2][0], f3)
