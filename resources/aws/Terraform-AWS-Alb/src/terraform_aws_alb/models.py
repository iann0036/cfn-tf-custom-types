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
    ArnSuffix: Optional[str]
    DnsName: Optional[str]
    DropInvalidHeaderFields: Optional[bool]
    EnableCrossZoneLoadBalancing: Optional[bool]
    EnableDeletionProtection: Optional[bool]
    EnableHttp2: Optional[bool]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    Internal: Optional[bool]
    IpAddressType: Optional[str]
    LoadBalancerType: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    VpcId: Optional[str]
    ZoneId: Optional[str]
    AccessLogs: Optional[Sequence["_AccessLogs"]]
    SubnetMapping: Optional[Sequence["_SubnetMapping"]]
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
            Arn=json_data.get("Arn"),
            ArnSuffix=json_data.get("ArnSuffix"),
            DnsName=json_data.get("DnsName"),
            DropInvalidHeaderFields=json_data.get("DropInvalidHeaderFields"),
            EnableCrossZoneLoadBalancing=json_data.get("EnableCrossZoneLoadBalancing"),
            EnableDeletionProtection=json_data.get("EnableDeletionProtection"),
            EnableHttp2=json_data.get("EnableHttp2"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Internal=json_data.get("Internal"),
            IpAddressType=json_data.get("IpAddressType"),
            LoadBalancerType=json_data.get("LoadBalancerType"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Subnets=json_data.get("Subnets"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            ZoneId=json_data.get("ZoneId"),
            AccessLogs=json_data.get("AccessLogs"),
            SubnetMapping=json_data.get("SubnetMapping"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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
class AccessLogs:
    Bucket: Optional[str]
    Enabled: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogs"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Enabled=json_data.get("Enabled"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogs = AccessLogs


@dataclass
class SubnetMapping:
    AllocationId: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetMapping"]:
        if not json_data:
            return None
        return cls(
            AllocationId=json_data.get("AllocationId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetMapping = SubnetMapping


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


