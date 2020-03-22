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
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    ConnectSettings: Optional[Sequence["_ConnectSettings"]]
    VpcSettings: Optional[Sequence["_VpcSettings"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            ConnectSettings=json_data.get("ConnectSettings"),
            VpcSettings=json_data.get("VpcSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class ConnectSettings:
    CustomerDnsIps: Optional[Sequence[str]]
    CustomerUsername: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectSettings"]:
        if not json_data:
            return None
        return cls(
            CustomerDnsIps=json_data.get("CustomerDnsIps"),
            CustomerUsername=json_data.get("CustomerUsername"),
            SubnetIds=json_data.get("SubnetIds"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectSettings = ConnectSettings


@dataclass
class VpcSettings:
    SubnetIds: Optional[Sequence[str]]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcSettings"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=json_data.get("SubnetIds"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcSettings = VpcSettings


