from PHX.model import building
from PHX.to_WUFI_XML.xml_builder import generate_WUFI_XML_from_object
from tests.test_to_WUFI_xml._utils import xml_string_to_list


def test_default_PhxProject(reset_class_counters):
    z1 = building.PhxZone()
    result = generate_WUFI_XML_from_object(z1, _header="")
    assert xml_string_to_list(result) == [
        "<Name></Name>",
        '<KindZone>1</KindZone>',
        '<KindAttachedZone>0</KindAttachedZone>',
        '<TemperatureReductionFactorUserDefined>1.0</TemperatureReductionFactorUserDefined>',
        "<IdentNr>1</IdentNr>",
        '<RoomsVentilation count="0"/>',
        '<LoadsPersonsPH count="0"/>',
        '<LoadsLightingsPH count="0"/>',
        "<GrossVolume_Selection>6</GrossVolume_Selection>",
        "<GrossVolume>0.0</GrossVolume>",
        "<NetVolume_Selection>6</NetVolume_Selection>",
        "<NetVolume>0.0</NetVolume>",
        "<FloorArea_Selection>6</FloorArea_Selection>",
        "<FloorArea>0.0</FloorArea>",
        "<ClearanceHeight_Selection>1</ClearanceHeight_Selection>",
        "<ClearanceHeight>2.5</ClearanceHeight>",
        "<SpecificHeatCapacity_Selection>1</SpecificHeatCapacity_Selection>",
        "<SpecificHeatCapacity>60</SpecificHeatCapacity>",
        "<IdentNrPH_Building>1</IdentNrPH_Building>",
        '<OccupantQuantityUserDef unit="-">0</OccupantQuantityUserDef>',
        '<NumberBedrooms unit="-">0</NumberBedrooms>',
        '<HomeDevice count="0"/>',
        '<ExhaustVents count="0"/>',
        '<ThermalBridges count="0"/>',
        '<SummerNaturalVentilationDay unit="1/hr">0</SummerNaturalVentilationDay>',
        '<SummerNaturalVentilationNight unit="1/hr">0</SummerNaturalVentilationNight>',
    ]
