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
    Fqdn: Optional[str]
    Name: Optional[str]
    ProfileStatus: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TrafficRoutingMethod: Optional[str]
    DnsConfig: Optional[Sequence["_DnsConfig"]]
    MonitorConfig: Optional[Sequence["_MonitorConfig"]]
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
            Fqdn=json_data.get("Fqdn"),
            Name=json_data.get("Name"),
            ProfileStatus=json_data.get("ProfileStatus"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            TrafficRoutingMethod=json_data.get("TrafficRoutingMethod"),
            DnsConfig=json_data.get("DnsConfig"),
            MonitorConfig=json_data.get("MonitorConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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
class DnsConfig:
    RelativeName: Optional[str]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfig"]:
        if not json_data:
            return None
        return cls(
            RelativeName=json_data.get("RelativeName"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfig = DnsConfig


@dataclass
class MonitorConfig:
    ExpectedStatusCodeRanges: Optional[Sequence[str]]
    IntervalInSeconds: Optional[float]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    TimeoutInSeconds: Optional[float]
    ToleratedNumberOfFailures: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorConfig"]:
        if not json_data:
            return None
        return cls(
            ExpectedStatusCodeRanges=json_data.get("ExpectedStatusCodeRanges"),
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            ToleratedNumberOfFailures=json_data.get("ToleratedNumberOfFailures"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorConfig = MonitorConfig


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


