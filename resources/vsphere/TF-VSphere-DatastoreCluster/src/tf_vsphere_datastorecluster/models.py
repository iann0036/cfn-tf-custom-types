# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttributesDefinition"]]
    DatacenterId: Optional[str]
    Folder: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SdrsAdvancedOptions: Optional[Sequence["_SdrsAdvancedOptionsDefinition"]]
    SdrsAutomationLevel: Optional[str]
    SdrsDefaultIntraVmAffinity: Optional[bool]
    SdrsEnabled: Optional[bool]
    SdrsFreeSpaceThreshold: Optional[float]
    SdrsFreeSpaceThresholdMode: Optional[str]
    SdrsFreeSpaceUtilizationDifference: Optional[float]
    SdrsIoBalanceAutomationLevel: Optional[str]
    SdrsIoLatencyThreshold: Optional[float]
    SdrsIoLoadBalanceEnabled: Optional[bool]
    SdrsIoLoadImbalanceThreshold: Optional[float]
    SdrsIoReservableIopsThreshold: Optional[float]
    SdrsIoReservablePercentThreshold: Optional[float]
    SdrsIoReservableThresholdMode: Optional[str]
    SdrsLoadBalanceInterval: Optional[float]
    SdrsPolicyEnforcementAutomationLevel: Optional[str]
    SdrsRuleEnforcementAutomationLevel: Optional[str]
    SdrsSpaceBalanceAutomationLevel: Optional[str]
    SdrsSpaceUtilizationThreshold: Optional[float]
    SdrsVmEvacuationAutomationLevel: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CustomAttributes=deserialize_list(json_data.get("CustomAttributes"), CustomAttributesDefinition),
            DatacenterId=json_data.get("DatacenterId"),
            Folder=json_data.get("Folder"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SdrsAdvancedOptions=deserialize_list(json_data.get("SdrsAdvancedOptions"), SdrsAdvancedOptionsDefinition),
            SdrsAutomationLevel=json_data.get("SdrsAutomationLevel"),
            SdrsDefaultIntraVmAffinity=json_data.get("SdrsDefaultIntraVmAffinity"),
            SdrsEnabled=json_data.get("SdrsEnabled"),
            SdrsFreeSpaceThreshold=json_data.get("SdrsFreeSpaceThreshold"),
            SdrsFreeSpaceThresholdMode=json_data.get("SdrsFreeSpaceThresholdMode"),
            SdrsFreeSpaceUtilizationDifference=json_data.get("SdrsFreeSpaceUtilizationDifference"),
            SdrsIoBalanceAutomationLevel=json_data.get("SdrsIoBalanceAutomationLevel"),
            SdrsIoLatencyThreshold=json_data.get("SdrsIoLatencyThreshold"),
            SdrsIoLoadBalanceEnabled=json_data.get("SdrsIoLoadBalanceEnabled"),
            SdrsIoLoadImbalanceThreshold=json_data.get("SdrsIoLoadImbalanceThreshold"),
            SdrsIoReservableIopsThreshold=json_data.get("SdrsIoReservableIopsThreshold"),
            SdrsIoReservablePercentThreshold=json_data.get("SdrsIoReservablePercentThreshold"),
            SdrsIoReservableThresholdMode=json_data.get("SdrsIoReservableThresholdMode"),
            SdrsLoadBalanceInterval=json_data.get("SdrsLoadBalanceInterval"),
            SdrsPolicyEnforcementAutomationLevel=json_data.get("SdrsPolicyEnforcementAutomationLevel"),
            SdrsRuleEnforcementAutomationLevel=json_data.get("SdrsRuleEnforcementAutomationLevel"),
            SdrsSpaceBalanceAutomationLevel=json_data.get("SdrsSpaceBalanceAutomationLevel"),
            SdrsSpaceUtilizationThreshold=json_data.get("SdrsSpaceUtilizationThreshold"),
            SdrsVmEvacuationAutomationLevel=json_data.get("SdrsVmEvacuationAutomationLevel"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributesDefinition = CustomAttributesDefinition


@dataclass
class SdrsAdvancedOptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SdrsAdvancedOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdrsAdvancedOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdrsAdvancedOptionsDefinition = SdrsAdvancedOptionsDefinition


