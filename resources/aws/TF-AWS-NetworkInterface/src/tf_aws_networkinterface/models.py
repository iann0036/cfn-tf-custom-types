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
    InterfaceType: Optional[str]
    Ipv6AddressCount: Optional[float]
    Ipv6Addresses: Optional[Sequence[str]]
    MacAddress: Optional[str]
    OutpostArn: Optional[str]
    PrivateDnsName: Optional[str]
    PrivateIp: Optional[str]
    PrivateIps: Optional[Sequence[str]]
    PrivateIpsCount: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    SourceDestCheck: Optional[bool]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Attachment: Optional[Sequence["_AttachmentDefinition"]]

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
            InterfaceType=json_data.get("InterfaceType"),
            Ipv6AddressCount=json_data.get("Ipv6AddressCount"),
            Ipv6Addresses=json_data.get("Ipv6Addresses"),
            MacAddress=json_data.get("MacAddress"),
            OutpostArn=json_data.get("OutpostArn"),
            PrivateDnsName=json_data.get("PrivateDnsName"),
            PrivateIp=json_data.get("PrivateIp"),
            PrivateIps=json_data.get("PrivateIps"),
            PrivateIpsCount=json_data.get("PrivateIpsCount"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SourceDestCheck=json_data.get("SourceDestCheck"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Attachment=deserialize_list(json_data.get("Attachment"), AttachmentDefinition),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class AttachmentDefinition(BaseModel):
    DeviceIndex: Optional[float]
    Instance: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceIndex=json_data.get("DeviceIndex"),
            Instance=json_data.get("Instance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentDefinition = AttachmentDefinition


