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
    AvailableZones: Optional[Sequence[str]]
    CoolDownTime: Optional[float]
    DeleteInstances: Optional[str]
    DeletePublicip: Optional[bool]
    DesireInstanceNumber: Optional[float]
    HealthPeriodicAuditMethod: Optional[str]
    HealthPeriodicAuditTime: Optional[float]
    Id: Optional[str]
    InstanceTerminatePolicy: Optional[str]
    Instances: Optional[Sequence[str]]
    LbListenerId: Optional[str]
    MaxInstanceNumber: Optional[float]
    MinInstanceNumber: Optional[float]
    Notifications: Optional[Sequence[str]]
    Region: Optional[str]
    ScalingConfigurationId: Optional[str]
    ScalingGroupName: Optional[str]
    VpcId: Optional[str]
    LbaasListeners: Optional[Sequence["_LbaasListeners"]]
    Networks: Optional[Sequence["_Networks"]]
    SecurityGroups: Optional[Sequence["_SecurityGroups"]]
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
            AvailableZones=json_data.get("AvailableZones"),
            CoolDownTime=json_data.get("CoolDownTime"),
            DeleteInstances=json_data.get("DeleteInstances"),
            DeletePublicip=json_data.get("DeletePublicip"),
            DesireInstanceNumber=json_data.get("DesireInstanceNumber"),
            HealthPeriodicAuditMethod=json_data.get("HealthPeriodicAuditMethod"),
            HealthPeriodicAuditTime=json_data.get("HealthPeriodicAuditTime"),
            Id=json_data.get("Id"),
            InstanceTerminatePolicy=json_data.get("InstanceTerminatePolicy"),
            Instances=json_data.get("Instances"),
            LbListenerId=json_data.get("LbListenerId"),
            MaxInstanceNumber=json_data.get("MaxInstanceNumber"),
            MinInstanceNumber=json_data.get("MinInstanceNumber"),
            Notifications=json_data.get("Notifications"),
            Region=json_data.get("Region"),
            ScalingConfigurationId=json_data.get("ScalingConfigurationId"),
            ScalingGroupName=json_data.get("ScalingGroupName"),
            VpcId=json_data.get("VpcId"),
            LbaasListeners=json_data.get("LbaasListeners"),
            Networks=json_data.get("Networks"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LbaasListeners:
    PoolId: Optional[str]
    ProtocolPort: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LbaasListeners"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LbaasListeners"]:
        if not json_data:
            return None
        return cls(
            PoolId=json_data.get("PoolId"),
            ProtocolPort=json_data.get("ProtocolPort"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LbaasListeners = LbaasListeners


@dataclass
class Networks:
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Networks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Networks"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Networks = Networks


@dataclass
class SecurityGroups:
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityGroups"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityGroups = SecurityGroups


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


