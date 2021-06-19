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
    AllocationMethod: Optional[str]
    AvailabilityZone: Optional[str]
    DomainNameLabel: Optional[str]
    Fqdn: Optional[str]
    Id: Optional[str]
    IdleTimeoutInMinutes: Optional[float]
    IpAddress: Optional[str]
    IpTags: Optional[Sequence["_IpTagsDefinition"]]
    IpVersion: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PublicIpPrefixId: Optional[str]
    ResourceGroupName: Optional[str]
    ReverseFqdn: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Zones: Optional[Sequence[str]]
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
            AllocationMethod=json_data.get("AllocationMethod"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            DomainNameLabel=json_data.get("DomainNameLabel"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            IdleTimeoutInMinutes=json_data.get("IdleTimeoutInMinutes"),
            IpAddress=json_data.get("IpAddress"),
            IpTags=deserialize_list(json_data.get("IpTags"), IpTagsDefinition),
            IpVersion=json_data.get("IpVersion"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PublicIpPrefixId=json_data.get("PublicIpPrefixId"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ReverseFqdn=json_data.get("ReverseFqdn"),
            Sku=json_data.get("Sku"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Zones=json_data.get("Zones"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpTagsDefinition = IpTagsDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


