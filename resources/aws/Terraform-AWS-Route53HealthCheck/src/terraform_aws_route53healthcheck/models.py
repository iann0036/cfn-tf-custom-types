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
    ChildHealthThreshold: Optional[float]
    ChildHealthchecks: Optional[Sequence[str]]
    CloudwatchAlarmName: Optional[str]
    CloudwatchAlarmRegion: Optional[str]
    EnableSni: Optional[bool]
    FailureThreshold: Optional[float]
    Fqdn: Optional[str]
    Id: Optional[str]
    InsufficientDataHealthStatus: Optional[str]
    InvertHealthcheck: Optional[bool]
    IpAddress: Optional[str]
    MeasureLatency: Optional[bool]
    Port: Optional[float]
    ReferenceName: Optional[str]
    Regions: Optional[Sequence[str]]
    RequestInterval: Optional[float]
    ResourcePath: Optional[str]
    SearchString: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ChildHealthThreshold=json_data.get("ChildHealthThreshold"),
            ChildHealthchecks=json_data.get("ChildHealthchecks"),
            CloudwatchAlarmName=json_data.get("CloudwatchAlarmName"),
            CloudwatchAlarmRegion=json_data.get("CloudwatchAlarmRegion"),
            EnableSni=json_data.get("EnableSni"),
            FailureThreshold=json_data.get("FailureThreshold"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            InsufficientDataHealthStatus=json_data.get("InsufficientDataHealthStatus"),
            InvertHealthcheck=json_data.get("InvertHealthcheck"),
            IpAddress=json_data.get("IpAddress"),
            MeasureLatency=json_data.get("MeasureLatency"),
            Port=json_data.get("Port"),
            ReferenceName=json_data.get("ReferenceName"),
            Regions=json_data.get("Regions"),
            RequestInterval=json_data.get("RequestInterval"),
            ResourcePath=json_data.get("ResourcePath"),
            SearchString=json_data.get("SearchString"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
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


