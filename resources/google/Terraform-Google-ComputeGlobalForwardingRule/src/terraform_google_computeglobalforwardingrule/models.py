# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    IpProtocol: Optional[str]
    IpVersion: Optional[str]
    LoadBalancingScheme: Optional[str]
    Name: Optional[str]
    PortRange: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    Target: Optional[str]
    MetadataFilters: Optional[Sequence["_MetadataFilters"]]
    Timeouts: Optional["_Timeouts"]
    FilterLabels: Optional[Sequence["_FilterLabels"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            IpProtocol=json_data.get("IpProtocol"),
            IpVersion=json_data.get("IpVersion"),
            LoadBalancingScheme=json_data.get("LoadBalancingScheme"),
            Name=json_data.get("Name"),
            PortRange=json_data.get("PortRange"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Target=json_data.get("Target"),
            MetadataFilters=json_data.get("MetadataFilters"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            FilterLabels=json_data.get("FilterLabels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataFilters:
    FilterMatchCriteria: Optional[str]
    FilterLabels: Optional[Sequence["_FilterLabels"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataFilters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataFilters"]:
        if not json_data:
            return None
        return cls(
            FilterMatchCriteria=json_data.get("FilterMatchCriteria"),
            FilterLabels=json_data.get("FilterLabels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataFilters = MetadataFilters


@dataclass
class FilterLabels:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterLabels"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterLabels = FilterLabels


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


