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
    Arn: Optional[str]
    ArnSuffix: Optional[str]
    CustomerOwnedIpv4Pool: Optional[str]
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
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    VpcId: Optional[str]
    ZoneId: Optional[str]
    AccessLogs: Optional[Sequence["_AccessLogsDefinition"]]
    SubnetMapping: Optional[Sequence["_SubnetMappingDefinition"]]
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
            Arn=json_data.get("Arn"),
            ArnSuffix=json_data.get("ArnSuffix"),
            CustomerOwnedIpv4Pool=json_data.get("CustomerOwnedIpv4Pool"),
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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            VpcId=json_data.get("VpcId"),
            ZoneId=json_data.get("ZoneId"),
            AccessLogs=deserialize_list(json_data.get("AccessLogs"), AccessLogsDefinition),
            SubnetMapping=deserialize_list(json_data.get("SubnetMapping"), SubnetMappingDefinition),
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
class AccessLogsDefinition(BaseModel):
    Bucket: Optional[str]
    Enabled: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Enabled=json_data.get("Enabled"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogsDefinition = AccessLogsDefinition


@dataclass
class SubnetMappingDefinition(BaseModel):
    AllocationId: Optional[str]
    Ipv6Address: Optional[str]
    PrivateIpv4Address: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            AllocationId=json_data.get("AllocationId"),
            Ipv6Address=json_data.get("Ipv6Address"),
            PrivateIpv4Address=json_data.get("PrivateIpv4Address"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetMappingDefinition = SubnetMappingDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


