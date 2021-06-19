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
    AppliedDnsServers: Optional[Sequence[str]]
    DnsServers: Optional[Sequence[str]]
    EnableIpForwarding: Optional[bool]
    Id: Optional[str]
    InternalDnsNameLabel: Optional[str]
    InternalFqdn: Optional[str]
    Location: Optional[str]
    MacAddress: Optional[str]
    Name: Optional[str]
    NetworkSecurityGroupId: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddresses: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VirtualMachineId: Optional[str]
    IpConfiguration: Optional[Sequence["_IpConfigurationDefinition"]]

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
            AppliedDnsServers=json_data.get("AppliedDnsServers"),
            DnsServers=json_data.get("DnsServers"),
            EnableIpForwarding=json_data.get("EnableIpForwarding"),
            Id=json_data.get("Id"),
            InternalDnsNameLabel=json_data.get("InternalDnsNameLabel"),
            InternalFqdn=json_data.get("InternalFqdn"),
            Location=json_data.get("Location"),
            MacAddress=json_data.get("MacAddress"),
            Name=json_data.get("Name"),
            NetworkSecurityGroupId=json_data.get("NetworkSecurityGroupId"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddresses=json_data.get("PrivateIpAddresses"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VirtualMachineId=json_data.get("VirtualMachineId"),
            IpConfiguration=deserialize_list(json_data.get("IpConfiguration"), IpConfigurationDefinition),
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
class IpConfigurationDefinition(BaseModel):
    ApplicationGatewayBackendAddressPoolsIds: Optional[Sequence[str]]
    ApplicationSecurityGroupIds: Optional[Sequence[str]]
    LoadBalancerBackendAddressPoolsIds: Optional[Sequence[str]]
    LoadBalancerInboundNatRulesIds: Optional[Sequence[str]]
    Name: Optional[str]
    Primary: Optional[bool]
    PrivateIpAddress: Optional[str]
    PrivateIpAddressAllocation: Optional[str]
    PublicIpAddressId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            ApplicationGatewayBackendAddressPoolsIds=json_data.get("ApplicationGatewayBackendAddressPoolsIds"),
            ApplicationSecurityGroupIds=json_data.get("ApplicationSecurityGroupIds"),
            LoadBalancerBackendAddressPoolsIds=json_data.get("LoadBalancerBackendAddressPoolsIds"),
            LoadBalancerInboundNatRulesIds=json_data.get("LoadBalancerInboundNatRulesIds"),
            Name=json_data.get("Name"),
            Primary=json_data.get("Primary"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddressAllocation=json_data.get("PrivateIpAddressAllocation"),
            PublicIpAddressId=json_data.get("PublicIpAddressId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpConfigurationDefinition = IpConfigurationDefinition


