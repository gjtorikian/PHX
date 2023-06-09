from PHX.model.hvac import cooling, _base, collection
from PHX.to_WUFI_XML.xml_builder import generate_WUFI_XML_from_object
from tests.test_to_WUFI_xml._utils import xml_string_to_list


def test_default_PhxCoolingVentilation(reset_class_counters):
    d1 = cooling.PhxCoolingVentilation()
    coll = collection.PhxMechanicalSystemCollection()
    coll.add_new_mech_device(d1.identifier, d1)
    result = generate_WUFI_XML_from_object(coll, _header="")
    assert xml_string_to_list(result) == [
        '<Systems count="1">',
        '<System index="0">',
        "<Name>Ideal Air System</Name>",
        '<Type choice="User defined (ideal system)">1</Type>',
        "<IdentNr>1</IdentNr>",
        '<ZonesCoverage count="1">',
        '<ZoneCoverage index="0">',
        "<IdentNrZone>1.0</IdentNrZone>",
        "<CoverageHeating>1.0</CoverageHeating>",
        "<CoverageCooling>1.0</CoverageCooling>",
        "<CoverageVentilation>1.0</CoverageVentilation>",
        "<CoverageHumidification>1.0</CoverageHumidification>",
        "<CoverageDehumidification>1.0</CoverageDehumidification>",
        "</ZoneCoverage>",
        "</ZonesCoverage>",
        '<Devices count="1">',
        '<Device index="0">',
        "<Name>_unnamed_equipment_</Name>",
        "<IdentNr>1</IdentNr>",
        "<SystemType>5</SystemType>",
        "<TypeDevice>5</TypeDevice>",
        "<UsedFor_Heating>false</UsedFor_Heating>",
        "<UsedFor_DHW>false</UsedFor_DHW>",
        "<UsedFor_Cooling>true</UsedFor_Cooling>",
        "<UsedFor_Ventilation>false</UsedFor_Ventilation>",
        "<UsedFor_Humidification>false</UsedFor_Humidification>",
        "<UsedFor_Dehumidification>false</UsedFor_Dehumidification>",
        "<PH_Parameters>",
        "<AuxiliaryEnergy>None</AuxiliaryEnergy>",
        "<AuxiliaryEnergyDHW>None</AuxiliaryEnergyDHW>",
        "<InConditionedSpace>true</InConditionedSpace>",
        "<AnnualCOP>4</AnnualCOP>",
        "<TotalSystemPerformanceRatioHeatGenerator>0.25</TotalSystemPerformanceRatioHeatGenerator>",
        "<HPType>3</HPType>",
        "</PH_Parameters>",
        "<DHW_Parameters>",
        "<CoverageWithinSystem>0.0</CoverageWithinSystem>",
        "<Unit>0.0</Unit>",
        "<Selection>1</Selection>",
        "</DHW_Parameters>",
        "<Heating_Parameters>",
        "<CoverageWithinSystem>0.0</CoverageWithinSystem>",
        "<Unit>0.0</Unit>",
        "<Selection>1</Selection>",
        "</Heating_Parameters>",
        "</Device>",
        "</Devices>",
        "<PHDistribution>",
        "<DistributionDHW>",
        "<CalculationMethodIndividualPipes>1</CalculationMethodIndividualPipes>",
        "<DemandRecirculation>true</DemandRecirculation>",
        "<SelectionhotWaterFixtureEff>1</SelectionhotWaterFixtureEff>",
        "<NumberOfBathrooms>1</NumberOfBathrooms>",
        "<AllPipesAreInsulated>true</AllPipesAreInsulated>",
        "<SelectionUnitsOrFloors>1</SelectionUnitsOrFloors>",
        "<PipeMaterialSimplifiedMethod>1</PipeMaterialSimplifiedMethod>",
        "<PipeDiameterSimplifiedMethod>1.0</PipeDiameterSimplifiedMethod>",
        "<TemperatureRoom_WR>20.0</TemperatureRoom_WR>",
        "<DesignFlowTemperature_WR>60.0</DesignFlowTemperature_WR>",
        "<DailyRunningHoursCirculation_WR>24</DailyRunningHoursCirculation_WR>",
        "<LengthCirculationPipes_WR>0</LengthCirculationPipes_WR>",
        "<HeatLossCoefficient_WR>None</HeatLossCoefficient_WR>",
        "<LengthIndividualPipes_WR>0</LengthIndividualPipes_WR>",
        "<ExteriorPipeDiameter_WR>None</ExteriorPipeDiameter_WR>",
        "</DistributionDHW>",
        "<DistributionCooling>",
        "<CoolingViaVentilationAir>true</CoolingViaVentilationAir>",
        "<SupplyAirCoolingOnOff>false</SupplyAirCoolingOnOff>",
        "<MaxSupplyAirCoolingPower>10</MaxSupplyAirCoolingPower>",
        "<MinTemperatureCoolingCoilSupplyAir>12</MinTemperatureCoolingCoilSupplyAir>",
        "<SupplyAirCoolinCOP>4</SupplyAirCoolinCOP>",
        "</DistributionCooling>",
        '<DistributionVentilation count="0"/>',
        "<UseDefaultValues>false</UseDefaultValues>",
        "<DeviceInConditionedSpace>true</DeviceInConditionedSpace>",
        '<SupportiveDevices count="0"/>',
        "</PHDistribution>",
        "</System>",
        "</Systems>",
    ]
