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
    DeregistrationDelay: Optional[float]
    Id: Optional[str]
    LambdaMultiValueHeadersEnabled: Optional[bool]
    LoadBalancingAlgorithmType: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Port: Optional[float]
    PreserveClientIp: Optional[str]
    Protocol: Optional[str]
    ProtocolVersion: Optional[str]
    ProxyProtocolV2: Optional[bool]
    SlowStart: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TargetType: Optional[str]
    VpcId: Optional[str]
    HealthCheck: Optional[Sequence["_HealthCheckDefinition"]]
    Stickiness: Optional[Sequence["_StickinessDefinition"]]

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
            DeregistrationDelay=json_data.get("DeregistrationDelay"),
            Id=json_data.get("Id"),
            LambdaMultiValueHeadersEnabled=json_data.get("LambdaMultiValueHeadersEnabled"),
            LoadBalancingAlgorithmType=json_data.get("LoadBalancingAlgorithmType"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Port=json_data.get("Port"),
            PreserveClientIp=json_data.get("PreserveClientIp"),
            Protocol=json_data.get("Protocol"),
            ProtocolVersion=json_data.get("ProtocolVersion"),
            ProxyProtocolV2=json_data.get("ProxyProtocolV2"),
            SlowStart=json_data.get("SlowStart"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TargetType=json_data.get("TargetType"),
            VpcId=json_data.get("VpcId"),
            HealthCheck=deserialize_list(json_data.get("HealthCheck"), HealthCheckDefinition),
            Stickiness=deserialize_list(json_data.get("Stickiness"), StickinessDefinition),
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
class HealthCheckDefinition(BaseModel):
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
        cls: Type["_HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckDefinition"]:
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
_HealthCheckDefinition = HealthCheckDefinition


@dataclass
class StickinessDefinition(BaseModel):
    CookieDuration: Optional[float]
    Enabled: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StickinessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StickinessDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieDuration=json_data.get("CookieDuration"),
            Enabled=json_data.get("Enabled"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StickinessDefinition = StickinessDefinition


