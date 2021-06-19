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
    Description: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    IpProtocol: Optional[str]
    IpVersion: Optional[str]
    LabelFingerprint: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LoadBalancingScheme: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    PortRange: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    Target: Optional[str]
    MetadataFilters: Optional[Sequence["_MetadataFiltersDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            IpProtocol=json_data.get("IpProtocol"),
            IpVersion=json_data.get("IpVersion"),
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LoadBalancingScheme=json_data.get("LoadBalancingScheme"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            PortRange=json_data.get("PortRange"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Target=json_data.get("Target"),
            MetadataFilters=deserialize_list(json_data.get("MetadataFilters"), MetadataFiltersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class MetadataFiltersDefinition(BaseModel):
    FilterMatchCriteria: Optional[str]
    FilterLabels: Optional[Sequence["_FilterLabelsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataFiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            FilterMatchCriteria=json_data.get("FilterMatchCriteria"),
            FilterLabels=deserialize_list(json_data.get("FilterLabels"), FilterLabelsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataFiltersDefinition = MetadataFiltersDefinition


@dataclass
class FilterLabelsDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterLabelsDefinition = FilterLabelsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


