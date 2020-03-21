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
    Domain: Optional[str]
    HealthCheckCode: Optional[float]
    HealthCheckHealthNum: Optional[float]
    HealthCheckInterval: Optional[float]
    HealthCheckMethod: Optional[str]
    HealthCheckPath: Optional[str]
    HealthCheckSwitch: Optional[bool]
    HealthCheckUnhealthNum: Optional[float]
    Name: Optional[str]
    Protocol: Optional[str]
    ResourceId: Optional[str]
    ResourceType: Optional[str]
    RuleId: Optional[str]
    SourceList: Optional[Sequence[str]]
    SourceType: Optional[float]
    SslId: Optional[str]
    Status: Optional[float]
    Switch: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Domain=json_data.get("Domain"),
            HealthCheckCode=json_data.get("HealthCheckCode"),
            HealthCheckHealthNum=json_data.get("HealthCheckHealthNum"),
            HealthCheckInterval=json_data.get("HealthCheckInterval"),
            HealthCheckMethod=json_data.get("HealthCheckMethod"),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            HealthCheckSwitch=json_data.get("HealthCheckSwitch"),
            HealthCheckUnhealthNum=json_data.get("HealthCheckUnhealthNum"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
            RuleId=json_data.get("RuleId"),
            SourceList=json_data.get("SourceList"),
            SourceType=json_data.get("SourceType"),
            SslId=json_data.get("SslId"),
            Status=json_data.get("Status"),
            Switch=json_data.get("Switch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


