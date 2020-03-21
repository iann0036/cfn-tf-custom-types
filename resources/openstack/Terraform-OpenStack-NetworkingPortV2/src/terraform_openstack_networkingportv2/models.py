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
    AdminStateUp: Optional[bool]
    AllFixedIps: Optional[Sequence[str]]
    AllSecurityGroupIds: Optional[Sequence[str]]
    AllTags: Optional[Sequence[str]]
    Description: Optional[str]
    DeviceId: Optional[str]
    DeviceOwner: Optional[str]
    DnsAssignment: Optional[Sequence[Sequence["_DnsAssignment"]]]
    DnsName: Optional[str]
    Id: Optional[str]
    MacAddress: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    NoFixedIp: Optional[bool]
    NoSecurityGroups: Optional[bool]
    PortSecurityEnabled: Optional[bool]
    QosPolicyId: Optional[str]
    Region: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    Tags: Optional[Sequence[str]]
    TenantId: Optional[str]
    ValueSpecs: Optional[Sequence["_ValueSpecs"]]
    AllowedAddressPairs: Optional[Sequence["_AllowedAddressPairs"]]
    Binding: Optional[Sequence["_Binding"]]
    ExtraDhcpOption: Optional[Sequence["_ExtraDhcpOption"]]
    FixedIp: Optional[Sequence["_FixedIp"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminStateUp=json_data.get("AdminStateUp"),
            AllFixedIps=json_data.get("AllFixedIps"),
            AllSecurityGroupIds=json_data.get("AllSecurityGroupIds"),
            AllTags=json_data.get("AllTags"),
            Description=json_data.get("Description"),
            DeviceId=json_data.get("DeviceId"),
            DeviceOwner=json_data.get("DeviceOwner"),
            DnsAssignment=json_data.get("DnsAssignment"),
            DnsName=json_data.get("DnsName"),
            Id=json_data.get("Id"),
            MacAddress=json_data.get("MacAddress"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            NoFixedIp=json_data.get("NoFixedIp"),
            NoSecurityGroups=json_data.get("NoSecurityGroups"),
            PortSecurityEnabled=json_data.get("PortSecurityEnabled"),
            QosPolicyId=json_data.get("QosPolicyId"),
            Region=json_data.get("Region"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Tags=json_data.get("Tags"),
            TenantId=json_data.get("TenantId"),
            ValueSpecs=json_data.get("ValueSpecs"),
            AllowedAddressPairs=json_data.get("AllowedAddressPairs"),
            Binding=json_data.get("Binding"),
            ExtraDhcpOption=json_data.get("ExtraDhcpOption"),
            FixedIp=json_data.get("FixedIp"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsAssignment:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsAssignment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsAssignment"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsAssignment = DnsAssignment


@dataclass
class ValueSpecs:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValueSpecs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueSpecs"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueSpecs = ValueSpecs


@dataclass
class AllowedAddressPairs:
    IpAddress: Optional[str]
    MacAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedAddressPairs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedAddressPairs"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            MacAddress=json_data.get("MacAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedAddressPairs = AllowedAddressPairs


@dataclass
class Binding:
    HostId: Optional[str]
    Profile: Optional[str]
    VnicType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Binding"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Binding"]:
        if not json_data:
            return None
        return cls(
            HostId=json_data.get("HostId"),
            Profile=json_data.get("Profile"),
            VnicType=json_data.get("VnicType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Binding = Binding


@dataclass
class ExtraDhcpOption:
    IpVersion: Optional[float]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtraDhcpOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtraDhcpOption"]:
        if not json_data:
            return None
        return cls(
            IpVersion=json_data.get("IpVersion"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtraDhcpOption = ExtraDhcpOption


@dataclass
class FixedIp:
    IpAddress: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedIp"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedIp = FixedIp


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


