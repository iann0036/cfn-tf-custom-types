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
    HealthCheckType: Optional[str]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    ListenType: Optional[str]
    LoadBalancerId: Optional[str]
    Method: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    Persistence: Optional[str]
    PersistenceType: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    Status: Optional[str]

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
            HealthCheckType=json_data.get("HealthCheckType"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            ListenType=json_data.get("ListenType"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            Persistence=json_data.get("Persistence"),
            PersistenceType=json_data.get("PersistenceType"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


