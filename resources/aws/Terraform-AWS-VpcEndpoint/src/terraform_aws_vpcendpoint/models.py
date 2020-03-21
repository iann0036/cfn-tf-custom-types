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
    AutoAccept: Optional[bool]
    CidrBlocks: Optional[Sequence[str]]
    DnsEntry: Optional[Sequence["_DnsEntry"]]
    Id: Optional[str]
    NetworkInterfaceIds: Optional[Sequence[str]]
    OwnerId: Optional[str]
    Policy: Optional[str]
    PrefixListId: Optional[str]
    PrivateDnsEnabled: Optional[bool]
    RequesterManaged: Optional[bool]
    RouteTableIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    ServiceName: Optional[str]
    State: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    VpcEndpointType: Optional[str]
    VpcId: Optional[str]
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
            AutoAccept=json_data.get("AutoAccept"),
            CidrBlocks=json_data.get("CidrBlocks"),
            DnsEntry=json_data.get("DnsEntry"),
            Id=json_data.get("Id"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
            OwnerId=json_data.get("OwnerId"),
            Policy=json_data.get("Policy"),
            PrefixListId=json_data.get("PrefixListId"),
            PrivateDnsEnabled=json_data.get("PrivateDnsEnabled"),
            RequesterManaged=json_data.get("RequesterManaged"),
            RouteTableIds=json_data.get("RouteTableIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            ServiceName=json_data.get("ServiceName"),
            State=json_data.get("State"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            VpcEndpointType=json_data.get("VpcEndpointType"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsEntry:
    DnsName: Optional[str]
    HostedZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsEntry"]:
        if not json_data:
            return None
        return cls(
            DnsName=json_data.get("DnsName"),
            HostedZoneId=json_data.get("HostedZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsEntry = DnsEntry


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


