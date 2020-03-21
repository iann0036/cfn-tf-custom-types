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
    DeregistrationDelay: Optional[float]
    LambdaMultiValueHeadersEnabled: Optional[bool]
    LoadBalancingAlgorithmType: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    ProxyProtocolV2: Optional[bool]
    SlowStart: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    TargetType: Optional[str]
    VpcId: Optional[str]
    HealthCheck: Optional[Sequence["_HealthCheck"]]
    Stickiness: Optional[Sequence["_Stickiness"]]

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
            DeregistrationDelay=json_data.get("DeregistrationDelay"),
            LambdaMultiValueHeadersEnabled=json_data.get("LambdaMultiValueHeadersEnabled"),
            LoadBalancingAlgorithmType=json_data.get("LoadBalancingAlgorithmType"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ProxyProtocolV2=json_data.get("ProxyProtocolV2"),
            SlowStart=json_data.get("SlowStart"),
            Tags=json_data.get("Tags"),
            TargetType=json_data.get("TargetType"),
            VpcId=json_data.get("VpcId"),
            HealthCheck=json_data.get("HealthCheck"),
            Stickiness=json_data.get("Stickiness"),
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
class HealthCheck:
    Enabled: Optional[bool]
    HealthyThreshold: Optional[float]
    Interval: Optional[float]
    Matcher: Optional[str]
    Path: Optional[str]
    Port: Optional[str]
    Protocol: Optional[str]
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
            Enabled=json_data.get("Enabled"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Interval=json_data.get("Interval"),
            Matcher=json_data.get("Matcher"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Timeout=json_data.get("Timeout"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheck = HealthCheck


@dataclass
class Stickiness:
    CookieDuration: Optional[float]
    Enabled: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Stickiness"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Stickiness"]:
        if not json_data:
            return None
        return cls(
            CookieDuration=json_data.get("CookieDuration"),
            Enabled=json_data.get("Enabled"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Stickiness = Stickiness


