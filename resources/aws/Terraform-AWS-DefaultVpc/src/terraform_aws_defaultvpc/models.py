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
    Arn: Optional[str]
    AssignGeneratedIpv6CidrBlock: Optional[bool]
    CidrBlock: Optional[str]
    DefaultNetworkAclId: Optional[str]
    DefaultRouteTableId: Optional[str]
    DefaultSecurityGroupId: Optional[str]
    DhcpOptionsId: Optional[str]
    EnableClassiclink: Optional[bool]
    EnableClassiclinkDnsSupport: Optional[bool]
    EnableDnsHostnames: Optional[bool]
    EnableDnsSupport: Optional[bool]
    InstanceTenancy: Optional[str]
    Ipv6AssociationId: Optional[str]
    Ipv6CidrBlock: Optional[str]
    MainRouteTableId: Optional[str]
    OwnerId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            AssignGeneratedIpv6CidrBlock=json_data.get("AssignGeneratedIpv6CidrBlock"),
            CidrBlock=json_data.get("CidrBlock"),
            DefaultNetworkAclId=json_data.get("DefaultNetworkAclId"),
            DefaultRouteTableId=json_data.get("DefaultRouteTableId"),
            DefaultSecurityGroupId=json_data.get("DefaultSecurityGroupId"),
            DhcpOptionsId=json_data.get("DhcpOptionsId"),
            EnableClassiclink=json_data.get("EnableClassiclink"),
            EnableClassiclinkDnsSupport=json_data.get("EnableClassiclinkDnsSupport"),
            EnableDnsHostnames=json_data.get("EnableDnsHostnames"),
            EnableDnsSupport=json_data.get("EnableDnsSupport"),
            InstanceTenancy=json_data.get("InstanceTenancy"),
            Ipv6AssociationId=json_data.get("Ipv6AssociationId"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            MainRouteTableId=json_data.get("MainRouteTableId"),
            OwnerId=json_data.get("OwnerId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


