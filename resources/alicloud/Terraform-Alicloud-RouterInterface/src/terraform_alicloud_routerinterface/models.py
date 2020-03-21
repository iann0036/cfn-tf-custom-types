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
    AccessPointId: Optional[str]
    Description: Optional[str]
    HealthCheckSourceIp: Optional[str]
    HealthCheckTargetIp: Optional[str]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    Name: Optional[str]
    OppositeAccessPointId: Optional[str]
    OppositeInterfaceId: Optional[str]
    OppositeInterfaceOwnerId: Optional[str]
    OppositeRegion: Optional[str]
    OppositeRouterId: Optional[str]
    OppositeRouterType: Optional[str]
    Period: Optional[float]
    Role: Optional[str]
    RouterId: Optional[str]
    RouterType: Optional[str]
    Specification: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessPointId=json_data.get("AccessPointId"),
            Description=json_data.get("Description"),
            HealthCheckSourceIp=json_data.get("HealthCheckSourceIp"),
            HealthCheckTargetIp=json_data.get("HealthCheckTargetIp"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            Name=json_data.get("Name"),
            OppositeAccessPointId=json_data.get("OppositeAccessPointId"),
            OppositeInterfaceId=json_data.get("OppositeInterfaceId"),
            OppositeInterfaceOwnerId=json_data.get("OppositeInterfaceOwnerId"),
            OppositeRegion=json_data.get("OppositeRegion"),
            OppositeRouterId=json_data.get("OppositeRouterId"),
            OppositeRouterType=json_data.get("OppositeRouterType"),
            Period=json_data.get("Period"),
            Role=json_data.get("Role"),
            RouterId=json_data.get("RouterId"),
            RouterType=json_data.get("RouterType"),
            Specification=json_data.get("Specification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


