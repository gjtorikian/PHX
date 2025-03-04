from pathlib import Path
import pytest
from PHX.from_HBJSON import read_HBJSON_file, create_project


@pytest.mark.parametrize(
    "filename,results",
    [
        ("Default_Model_Single_Zone.hbjson", None),
        ("Multi_Room_Complete.hbjson", None),
    ],
)
def test_convert_model_PhxProject(filename, results):
    file_path = Path("tests", "_source_hbjson", filename)

    # -- Build the HB-Model, convert to a PhxProject
    hb_json_dict = read_HBJSON_file.read_hb_json_from_file(file_path)
    hb_model = read_HBJSON_file.convert_hbjson_dict_to_hb_model(hb_json_dict)
    phx_project = create_project.convert_hb_model_to_PhxProject(
        hb_model, _group_components=True
    )

    assert phx_project
