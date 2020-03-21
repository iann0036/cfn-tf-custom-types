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
    AvailabilityZones: Optional[Sequence[str]]
    ConnectionDraining: Optional[bool]
    ConnectionDrainingTimeout: Optional[float]
    CrossZoneLoadBalancing: Optional[bool]
    DnsName: Optional[str]
    IdleTimeout: Optional[float]
    Instances: Optional[Sequence[str]]
    Internal: Optional[bool]
    Name: Optional[str]
    NamePrefix: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SourceSecurityGroup: Optional[str]
    SourceSecurityGroupId: Optional[str]
    Subnets: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    ZoneId: Optional[str]
    AccessLogs: Optional[Sequence["_AccessLogs"]]
    HealthCheck: Optional[Sequence["_HealthCheck"]]
    Listener: Optional[Sequence["_Listener"]]

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
            AvailabilityZones=json_data.get("AvailabilityZones"),
            ConnectionDraining=json_data.get("ConnectionDraining"),
            ConnectionDrainingTimeout=json_data.get("ConnectionDrainingTimeout"),
            CrossZoneLoadBalancing=json_data.get("CrossZoneLoadBalancing"),
            DnsName=json_data.get("DnsName"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Instances=json_data.get("Instances"),
            Internal=json_data.get("Internal"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SourceSecurityGroup=json_data.get("SourceSecurityGroup"),
            SourceSecurityGroupId=json_data.get("SourceSecurityGroupId"),
            Subnets=json_data.get("Subnets"),
            Tags=json_data.get("Tags"),
            ZoneId=json_data.get("ZoneId"),
            AccessLogs=json_data.get("AccessLogs"),
            HealthCheck=json_data.get("HealthCheck"),
            Listener=json_data.get("Listener"),
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


@dataclass
class AccessLogs:
    Bucket: Optional[str]
    BucketPrefix: Optional[str]
    Enabled: Optional[bool]
    Interval: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogs"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            BucketPrefix=json_data.get("BucketPrefix"),
            Enabled=json_data.get("Enabled"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogs = AccessLogs


@dataclass
class HealthCheck:
    HealthyThreshold: Optional[float]
    Interval: Optional[float]
    Target: Optional[str]
    Timeout: Optional[float]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheck"]:
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
_HealthCheck = HealthCheck


@dataclass
class Listener:
    InstancePort: Optional[float]
    InstanceProtocol: Optional[str]
    LbPort: Optional[float]
    LbProtocol: Optional[str]
    SslCertificateId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Listener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Listener"]:
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
_Listener = Listener


