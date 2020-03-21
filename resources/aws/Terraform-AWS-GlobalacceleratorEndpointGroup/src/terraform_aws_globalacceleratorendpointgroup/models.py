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
    EndpointGroupRegion: Optional[str]
    HealthCheckIntervalSeconds: Optional[float]
    HealthCheckPath: Optional[str]
    HealthCheckPort: Optional[float]
    HealthCheckProtocol: Optional[str]
    Id: Optional[str]
    ListenerArn: Optional[str]
    ThresholdCount: Optional[float]
    TrafficDialPercentage: Optional[float]
    EndpointConfiguration: Optional[Sequence["_EndpointConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EndpointGroupRegion=json_data.get("EndpointGroupRegion"),
            HealthCheckIntervalSeconds=json_data.get("HealthCheckIntervalSeconds"),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            HealthCheckPort=json_data.get("HealthCheckPort"),
            HealthCheckProtocol=json_data.get("HealthCheckProtocol"),
            Id=json_data.get("Id"),
            ListenerArn=json_data.get("ListenerArn"),
            ThresholdCount=json_data.get("ThresholdCount"),
            TrafficDialPercentage=json_data.get("TrafficDialPercentage"),
            EndpointConfiguration=json_data.get("EndpointConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointConfiguration:
    EndpointId: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfiguration"]:
        if not json_data:
            return None
        return cls(
            EndpointId=json_data.get("EndpointId"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfiguration = EndpointConfiguration


