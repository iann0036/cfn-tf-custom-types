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
    AllowClaim: Optional[bool]
    DisallowPublicIpAddress: Optional[bool]
    Fqdn: Optional[str]
    Id: Optional[str]
    LabName: Optional[str]
    LabSubnetName: Optional[str]
    LabVirtualNetworkId: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    Notes: Optional[str]
    Password: Optional[str]
    ResourceGroupName: Optional[str]
    Size: Optional[str]
    StorageType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UniqueIdentifier: Optional[str]
    Username: Optional[str]
    GalleryImageReference: Optional[Sequence["_GalleryImageReferenceDefinition"]]
    InboundNatRule: Optional[Sequence["_InboundNatRuleDefinition"]]
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
            AllowClaim=json_data.get("AllowClaim"),
            DisallowPublicIpAddress=json_data.get("DisallowPublicIpAddress"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            LabName=json_data.get("LabName"),
            LabSubnetName=json_data.get("LabSubnetName"),
            LabVirtualNetworkId=json_data.get("LabVirtualNetworkId"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Password=json_data.get("Password"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Size=json_data.get("Size"),
            StorageType=json_data.get("StorageType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UniqueIdentifier=json_data.get("UniqueIdentifier"),
            Username=json_data.get("Username"),
            GalleryImageReference=deserialize_list(json_data.get("GalleryImageReference"), GalleryImageReferenceDefinition),
            InboundNatRule=deserialize_list(json_data.get("InboundNatRule"), InboundNatRuleDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class GalleryImageReferenceDefinition(BaseModel):
    Offer: Optional[str]
    Publisher: Optional[str]
    Sku: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GalleryImageReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GalleryImageReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Offer=json_data.get("Offer"),
            Publisher=json_data.get("Publisher"),
            Sku=json_data.get("Sku"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GalleryImageReferenceDefinition = GalleryImageReferenceDefinition


@dataclass
class InboundNatRuleDefinition(BaseModel):
    BackendPort: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InboundNatRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundNatRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendPort=json_data.get("BackendPort"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundNatRuleDefinition = InboundNatRuleDefinition


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


