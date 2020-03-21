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
    AvailabilityDomain: Optional[str]
    CidrBlock: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DhcpOptionsId: Optional[str]
    DisplayName: Optional[str]
    DnsLabel: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    Ipv6cidrBlock: Optional[str]
    Ipv6publicCidrBlock: Optional[str]
    Ipv6virtualRouterIp: Optional[str]
    ProhibitPublicIpOnVnic: Optional[bool]
    RouteTableId: Optional[str]
    SecurityListIds: Optional[Sequence[str]]
    State: Optional[str]
    SubnetDomainName: Optional[str]
    TimeCreated: Optional[str]
    VcnId: Optional[str]
    VirtualRouterIp: Optional[str]
    VirtualRouterMac: Optional[str]
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
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            CidrBlock=json_data.get("CidrBlock"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DhcpOptionsId=json_data.get("DhcpOptionsId"),
            DisplayName=json_data.get("DisplayName"),
            DnsLabel=json_data.get("DnsLabel"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            Ipv6cidrBlock=json_data.get("Ipv6cidrBlock"),
            Ipv6publicCidrBlock=json_data.get("Ipv6publicCidrBlock"),
            Ipv6virtualRouterIp=json_data.get("Ipv6virtualRouterIp"),
            ProhibitPublicIpOnVnic=json_data.get("ProhibitPublicIpOnVnic"),
            RouteTableId=json_data.get("RouteTableId"),
            SecurityListIds=json_data.get("SecurityListIds"),
            State=json_data.get("State"),
            SubnetDomainName=json_data.get("SubnetDomainName"),
            TimeCreated=json_data.get("TimeCreated"),
            VcnId=json_data.get("VcnId"),
            VirtualRouterIp=json_data.get("VirtualRouterIp"),
            VirtualRouterMac=json_data.get("VirtualRouterMac"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


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


