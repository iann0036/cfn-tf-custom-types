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
    AvailabilityZones: Optional[Sequence[str]]
    ConnectionDraining: Optional[bool]
    ConnectionDrainingTimeout: Optional[float]
    CrossZoneLoadBalancing: Optional[bool]
    DnsName: Optional[str]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    Instances: Optional[Sequence[str]]
    Internal: Optional[bool]
    Name: Optional[str]
    NamePrefix: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SourceSecurityGroup: Optional[str]
    SourceSecurityGroupId: Optional[str]
    Subnets: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ZoneId: Optional[str]
    AccessLogs: Optional[Sequence["_AccessLogsDefinition"]]
    HealthCheck: Optional[Sequence["_HealthCheckDefinition"]]
    Listener: Optional[Sequence["_ListenerDefinition"]]

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
            AvailabilityZones=json_data.get("AvailabilityZones"),
            ConnectionDraining=json_data.get("ConnectionDraining"),
            ConnectionDrainingTimeout=json_data.get("ConnectionDrainingTimeout"),
            CrossZoneLoadBalancing=json_data.get("CrossZoneLoadBalancing"),
            DnsName=json_data.get("DnsName"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Instances=json_data.get("Instances"),
            Internal=json_data.get("Internal"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SourceSecurityGroup=json_data.get("SourceSecurityGroup"),
            SourceSecurityGroupId=json_data.get("SourceSecurityGroupId"),
            Subnets=json_data.get("Subnets"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ZoneId=json_data.get("ZoneId"),
            AccessLogs=deserialize_list(json_data.get("AccessLogs"), AccessLogsDefinition),
            HealthCheck=deserialize_list(json_data.get("HealthCheck"), HealthCheckDefinition),
            Listener=deserialize_list(json_data.get("Listener"), ListenerDefinition),
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
    BucketPrefix: Optional[str]
    Enabled: Optional[bool]
    Interval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            BucketPrefix=json_data.get("BucketPrefix"),
            Enabled=json_data.get("Enabled"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogsDefinition = AccessLogsDefinition


@dataclass
class HealthCheckDefinition(BaseModel):
    HealthyThreshold: Optional[float]
    Interval: Optional[float]
    Target: Optional[str]
    Timeout: Optional[float]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Interval=json_data.get("Interval"),
            Target=json_data.get("Target"),
            Timeout=json_data.get("Timeout"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckDefinition = HealthCheckDefinition


@dataclass
class ListenerDefinition(BaseModel):
    InstancePort: Optional[float]
    InstanceProtocol: Optional[str]
    LbPort: Optional[float]
    LbProtocol: Optional[str]
    SslCertificateId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerDefinition"]:
        if not json_data:
            return None
        return cls(
            InstancePort=json_data.get("InstancePort"),
            InstanceProtocol=json_data.get("InstanceProtocol"),
            LbPort=json_data.get("LbPort"),
            LbProtocol=json_data.get("LbProtocol"),
            SslCertificateId=json_data.get("SslCertificateId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerDefinition = ListenerDefinition


