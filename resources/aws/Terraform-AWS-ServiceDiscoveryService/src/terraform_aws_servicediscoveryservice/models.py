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
    Description: Optional[str]
    Name: Optional[str]
    NamespaceId: Optional[str]
    DnsConfig: Optional[Sequence["_DnsConfig"]]
    HealthCheckConfig: Optional[Sequence["_HealthCheckConfig"]]
    HealthCheckCustomConfig: Optional[Sequence["_HealthCheckCustomConfig"]]
    DnsRecords: Optional[Sequence["_DnsRecords"]]

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
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            NamespaceId=json_data.get("NamespaceId"),
            DnsConfig=json_data.get("DnsConfig"),
            HealthCheckConfig=json_data.get("HealthCheckConfig"),
            HealthCheckCustomConfig=json_data.get("HealthCheckCustomConfig"),
            DnsRecords=json_data.get("DnsRecords"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsConfig:
    NamespaceId: Optional[str]
    RoutingPolicy: Optional[str]
    DnsRecords: Optional[Sequence["_DnsRecords"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfig"]:
        if not json_data:
            return None
        return cls(
            NamespaceId=json_data.get("NamespaceId"),
            RoutingPolicy=json_data.get("RoutingPolicy"),
            DnsRecords=json_data.get("DnsRecords"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfig = DnsConfig


@dataclass
class DnsRecords:
    Ttl: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsRecords"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsRecords"]:
        if not json_data:
            return None
        return cls(
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsRecords = DnsRecords


@dataclass
class HealthCheckConfig:
    FailureThreshold: Optional[float]
    ResourcePath: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckConfig"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
            ResourcePath=json_data.get("ResourcePath"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckConfig = HealthCheckConfig


@dataclass
class HealthCheckCustomConfig:
    FailureThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckCustomConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckCustomConfig"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckCustomConfig = HealthCheckCustomConfig


