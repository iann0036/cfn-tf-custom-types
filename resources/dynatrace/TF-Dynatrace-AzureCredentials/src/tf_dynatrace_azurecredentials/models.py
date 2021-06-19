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
    Active: Optional[bool]
    AppId: Optional[str]
    AutoTagging: Optional[bool]
    DirectoryId: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    Label: Optional[str]
    MonitorOnlyTaggedEntities: Optional[bool]
    Unknowns: Optional[str]
    MonitorOnlyTagPairs: Optional[Sequence["_MonitorOnlyTagPairsDefinition"]]
    SupportingServices: Optional[Sequence["_SupportingServicesDefinition"]]

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
            Active=json_data.get("Active"),
            AppId=json_data.get("AppId"),
            AutoTagging=json_data.get("AutoTagging"),
            DirectoryId=json_data.get("DirectoryId"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            Label=json_data.get("Label"),
            MonitorOnlyTaggedEntities=json_data.get("MonitorOnlyTaggedEntities"),
            Unknowns=json_data.get("Unknowns"),
            MonitorOnlyTagPairs=deserialize_list(json_data.get("MonitorOnlyTagPairs"), MonitorOnlyTagPairsDefinition),
            SupportingServices=deserialize_list(json_data.get("SupportingServices"), SupportingServicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MonitorOnlyTagPairsDefinition(BaseModel):
    Name: Optional[str]
    Unknowns: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorOnlyTagPairsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorOnlyTagPairsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Unknowns=json_data.get("Unknowns"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorOnlyTagPairsDefinition = MonitorOnlyTagPairsDefinition


@dataclass
class SupportingServicesDefinition(BaseModel):
    Name: Optional[str]
    Unknowns: Optional[str]
    MonitoredMetrics: Optional[Sequence["_MonitoredMetricsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SupportingServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportingServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Unknowns=json_data.get("Unknowns"),
            MonitoredMetrics=deserialize_list(json_data.get("MonitoredMetrics"), MonitoredMetricsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportingServicesDefinition = SupportingServicesDefinition


@dataclass
class MonitoredMetricsDefinition(BaseModel):
    Dimensions: Optional[Sequence[str]]
    Name: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoredMetricsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoredMetricsDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimensions=json_data.get("Dimensions"),
            Name=json_data.get("Name"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoredMetricsDefinition = MonitoredMetricsDefinition


