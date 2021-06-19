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
    AggregationType: Optional[str]
    Description: Optional[str]
    DisabledReason: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    MetricId: Optional[str]
    Name: Optional[str]
    PrimaryDimensionKey: Optional[str]
    Severity: Optional[str]
    Unknowns: Optional[str]
    WarningReason: Optional[str]
    Dimensions: Optional[Sequence["_DimensionsDefinition"]]
    Scopes: Optional[Sequence["_ScopesDefinition"]]
    Strategy: Optional[Sequence["_StrategyDefinition"]]

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
            AggregationType=json_data.get("AggregationType"),
            Description=json_data.get("Description"),
            DisabledReason=json_data.get("DisabledReason"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            MetricId=json_data.get("MetricId"),
            Name=json_data.get("Name"),
            PrimaryDimensionKey=json_data.get("PrimaryDimensionKey"),
            Severity=json_data.get("Severity"),
            Unknowns=json_data.get("Unknowns"),
            WarningReason=json_data.get("WarningReason"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), DimensionsDefinition),
            Scopes=deserialize_list(json_data.get("Scopes"), ScopesDefinition),
            Strategy=deserialize_list(json_data.get("Strategy"), StrategyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DimensionsDefinition(BaseModel):
    Dimension: Optional[Sequence["_DimensionDefinition"]]
    Entity: Optional[Sequence["_EntityDefinition"]]
    String: Optional[Sequence["_StringDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimension=deserialize_list(json_data.get("Dimension"), DimensionDefinition),
            Entity=deserialize_list(json_data.get("Entity"), EntityDefinition),
            String=deserialize_list(json_data.get("String"), StringDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionsDefinition = DimensionsDefinition


@dataclass
class DimensionDefinition(BaseModel):
    Key: Optional[str]
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionDefinition = DimensionDefinition


@dataclass
class EntityDefinition(BaseModel):
    Id: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityDefinition = EntityDefinition


@dataclass
class StringDefinition(BaseModel):
    Key: Optional[str]
    Unknowns: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Unknowns=json_data.get("Unknowns"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringDefinition = StringDefinition


@dataclass
class FilterDefinition(BaseModel):
    Context: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


@dataclass
class ScopesDefinition(BaseModel):
    CustomDeviceGroupName: Optional[Sequence["_CustomDeviceGroupNameDefinition"]]
    Entity: Optional[Sequence["_EntityDefinition"]]
    HostGroupName: Optional[Sequence["_HostGroupNameDefinition"]]
    HostName: Optional[Sequence["_HostNameDefinition"]]
    ManagementZone: Optional[Sequence["_ManagementZoneDefinition"]]
    Name: Optional[Sequence["_NameDefinition"]]
    ProcessGroupId: Optional[Sequence["_ProcessGroupIdDefinition"]]
    ProcessGroupName: Optional[Sequence["_ProcessGroupNameDefinition"]]
    Scope: Optional[Sequence["_ScopeDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScopesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopesDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomDeviceGroupName=deserialize_list(json_data.get("CustomDeviceGroupName"), CustomDeviceGroupNameDefinition),
            Entity=deserialize_list(json_data.get("Entity"), EntityDefinition),
            HostGroupName=deserialize_list(json_data.get("HostGroupName"), HostGroupNameDefinition),
            HostName=deserialize_list(json_data.get("HostName"), HostNameDefinition),
            ManagementZone=deserialize_list(json_data.get("ManagementZone"), ManagementZoneDefinition),
            Name=deserialize_list(json_data.get("Name"), NameDefinition),
            ProcessGroupId=deserialize_list(json_data.get("ProcessGroupId"), ProcessGroupIdDefinition),
            ProcessGroupName=deserialize_list(json_data.get("ProcessGroupName"), ProcessGroupNameDefinition),
            Scope=deserialize_list(json_data.get("Scope"), ScopeDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopesDefinition = ScopesDefinition


@dataclass
class CustomDeviceGroupNameDefinition(BaseModel):
    Unknowns: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDeviceGroupNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDeviceGroupNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Unknowns=json_data.get("Unknowns"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDeviceGroupNameDefinition = CustomDeviceGroupNameDefinition


@dataclass
class HostGroupNameDefinition(BaseModel):
    Unknowns: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostGroupNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostGroupNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Unknowns=json_data.get("Unknowns"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostGroupNameDefinition = HostGroupNameDefinition


@dataclass
class HostNameDefinition(BaseModel):
    Unknowns: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Unknowns=json_data.get("Unknowns"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostNameDefinition = HostNameDefinition


@dataclass
class ManagementZoneDefinition(BaseModel):
    Id: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementZoneDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementZoneDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementZoneDefinition = ManagementZoneDefinition


@dataclass
class NameDefinition(BaseModel):
    Unknowns: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NameDefinition"]:
        if not json_data:
            return None
        return cls(
            Unknowns=json_data.get("Unknowns"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NameDefinition = NameDefinition


@dataclass
class ProcessGroupIdDefinition(BaseModel):
    Id: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessGroupIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessGroupIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessGroupIdDefinition = ProcessGroupIdDefinition


@dataclass
class ProcessGroupNameDefinition(BaseModel):
    Unknowns: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessGroupNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessGroupNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Unknowns=json_data.get("Unknowns"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessGroupNameDefinition = ProcessGroupNameDefinition


@dataclass
class ScopeDefinition(BaseModel):
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopeDefinition = ScopeDefinition


@dataclass
class TagDefinition(BaseModel):
    Unknowns: Optional[str]
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Unknowns=json_data.get("Unknowns"),
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class StrategyDefinition(BaseModel):
    Auto: Optional[Sequence["_AutoDefinition"]]
    Generic: Optional[Sequence["_GenericDefinition"]]
    Static: Optional[Sequence["_StaticDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StrategyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrategyDefinition"]:
        if not json_data:
            return None
        return cls(
            Auto=deserialize_list(json_data.get("Auto"), AutoDefinition),
            Generic=deserialize_list(json_data.get("Generic"), GenericDefinition),
            Static=deserialize_list(json_data.get("Static"), StaticDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrategyDefinition = StrategyDefinition


@dataclass
class AutoDefinition(BaseModel):
    AlertCondition: Optional[str]
    AlertingOnMissingData: Optional[bool]
    DealertingSamples: Optional[float]
    Samples: Optional[float]
    SignalFluctuations: Optional[float]
    Unknowns: Optional[str]
    ViolatingSamples: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertCondition=json_data.get("AlertCondition"),
            AlertingOnMissingData=json_data.get("AlertingOnMissingData"),
            DealertingSamples=json_data.get("DealertingSamples"),
            Samples=json_data.get("Samples"),
            SignalFluctuations=json_data.get("SignalFluctuations"),
            Unknowns=json_data.get("Unknowns"),
            ViolatingSamples=json_data.get("ViolatingSamples"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoDefinition = AutoDefinition


@dataclass
class GenericDefinition(BaseModel):
    Type: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GenericDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GenericDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GenericDefinition = GenericDefinition


@dataclass
class StaticDefinition(BaseModel):
    AlertCondition: Optional[str]
    AlertingOnMissingData: Optional[bool]
    DealertingSamples: Optional[float]
    Samples: Optional[float]
    Threshold: Optional[float]
    Unit: Optional[str]
    Unknowns: Optional[str]
    ViolatingSamples: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StaticDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticDefinition"]:
        if not json_data:
            return None
        return cls(
            AlertCondition=json_data.get("AlertCondition"),
            AlertingOnMissingData=json_data.get("AlertingOnMissingData"),
            DealertingSamples=json_data.get("DealertingSamples"),
            Samples=json_data.get("Samples"),
            Threshold=json_data.get("Threshold"),
            Unit=json_data.get("Unit"),
            Unknowns=json_data.get("Unknowns"),
            ViolatingSamples=json_data.get("ViolatingSamples"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticDefinition = StaticDefinition


