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
    AccessUrl: Optional[str]
    Alias: Optional[str]
    Description: Optional[str]
    DnsIpAddresses: Optional[Sequence[str]]
    Edition: Optional[str]
    EnableSso: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    SecurityGroupId: Optional[str]
    ShortName: Optional[str]
    Size: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Type: Optional[str]
    ConnectSettings: Optional[Sequence["_ConnectSettingsDefinition"]]
    VpcSettings: Optional[Sequence["_VpcSettingsDefinition"]]

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
            AccessUrl=json_data.get("AccessUrl"),
            Alias=json_data.get("Alias"),
            Description=json_data.get("Description"),
            DnsIpAddresses=json_data.get("DnsIpAddresses"),
            Edition=json_data.get("Edition"),
            EnableSso=json_data.get("EnableSso"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            ShortName=json_data.get("ShortName"),
            Size=json_data.get("Size"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Type=json_data.get("Type"),
            ConnectSettings=deserialize_list(json_data.get("ConnectSettings"), ConnectSettingsDefinition),
            VpcSettings=deserialize_list(json_data.get("VpcSettings"), VpcSettingsDefinition),
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
class ConnectSettingsDefinition(BaseModel):
    CustomerDnsIps: Optional[Sequence[str]]
    CustomerUsername: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomerDnsIps=json_data.get("CustomerDnsIps"),
            CustomerUsername=json_data.get("CustomerUsername"),
            SubnetIds=json_data.get("SubnetIds"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectSettingsDefinition = ConnectSettingsDefinition


@dataclass
class VpcSettingsDefinition(BaseModel):
    SubnetIds: Optional[Sequence[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=json_data.get("SubnetIds"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcSettingsDefinition = VpcSettingsDefinition


