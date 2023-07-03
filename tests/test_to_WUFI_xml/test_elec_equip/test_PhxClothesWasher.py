from PHX.model import elec_equip
from PHX.to_WUFI_XML.xml_builder import generate_WUFI_XML_from_object
from tests.test_to_WUFI_xml._utils import xml_string_to_list


def test_default_PhxDeviceClothesWasher(reset_class_counters):
    d1 = elec_equip.PhxDeviceClothesWasher()
    result = generate_WUFI_XML_from_object(d1, "", "_PhxElectricalDevice")
    assert xml_string_to_list(result) == [
        "<Comment></Comment>",
        "<ReferenceQuantity>1</ReferenceQuantity>",
        "<Quantity>1</Quantity>",
        "<InConditionedSpace>true</InConditionedSpace>",
        "<ReferenceEnergyDemandNorm>2</ReferenceEnergyDemandNorm>",
        "<EnergyDemandNorm>100.0</EnergyDemandNorm>",
        "<EnergyDemandNormUse>100.0</EnergyDemandNormUse>",
        "<CEF_CombinedEnergyFactor>0.0</CEF_CombinedEnergyFactor>",
        "<Type>2</Type>",
        "<Connection>1</Connection>",
        "<UtilizationFactor>1.0</UtilizationFactor>",
        "<CapacityClothesWasher>0.0814</CapacityClothesWasher>",
        "<MEF_ModifiedEnergyFactor>2.38</MEF_ModifiedEnergyFactor>",
    ]
