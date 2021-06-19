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
    Id: Optional[str]
    Connections: Optional[Sequence["_ConnectionsDefinition"]]
    Cpu: Optional[Sequence["_CpuDefinition"]]
    Disks: Optional[Sequence["_DisksDefinition"]]
    Gc: Optional[Sequence["_GcDefinition"]]
    Java: Optional[Sequence["_JavaDefinition"]]
    Memory: Optional[Sequence["_MemoryDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]

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
            Id=json_data.get("Id"),
            Connections=deserialize_list(json_data.get("Connections"), ConnectionsDefinition),
            Cpu=deserialize_list(json_data.get("Cpu"), CpuDefinition),
            Disks=deserialize_list(json_data.get("Disks"), DisksDefinition),
            Gc=deserialize_list(json_data.get("Gc"), GcDefinition),
            Java=deserialize_list(json_data.get("Java"), JavaDefinition),
            Memory=deserialize_list(json_data.get("Memory"), MemoryDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionsDefinition(BaseModel):
    Enabled: Optional[bool]
    EnabledOnGracefulShutdowns: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            EnabledOnGracefulShutdowns=json_data.get("EnabledOnGracefulShutdowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionsDefinition = ConnectionsDefinition


@dataclass
class CpuDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CpuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CpuDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CpuDefinition = CpuDefinition


@dataclass
class ThresholdsDefinition(BaseModel):
    Utilization: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThresholdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThresholdsDefinition"]:
        if not json_data:
            return None
        return cls(
            Utilization=json_data.get("Utilization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThresholdsDefinition = ThresholdsDefinition


@dataclass
class DisksDefinition(BaseModel):
    Inodes: Optional[Sequence["_InodesDefinition"]]
    Space: Optional[Sequence["_SpaceDefinition"]]
    Speed: Optional[Sequence["_SpeedDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DisksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisksDefinition"]:
        if not json_data:
            return None
        return cls(
            Inodes=deserialize_list(json_data.get("Inodes"), InodesDefinition),
            Space=deserialize_list(json_data.get("Space"), SpaceDefinition),
            Speed=deserialize_list(json_data.get("Speed"), SpeedDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisksDefinition = DisksDefinition


@dataclass
class InodesDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InodesDefinition = InodesDefinition


@dataclass
class SpaceDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpaceDefinition = SpaceDefinition


@dataclass
class SpeedDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpeedDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpeedDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpeedDefinition = SpeedDefinition


@dataclass
class GcDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcDefinition = GcDefinition


@dataclass
class JavaDefinition(BaseModel):
    OutOfMemory: Optional[Sequence["_OutOfMemoryDefinition"]]
    OutOfThreads: Optional[Sequence["_OutOfThreadsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_JavaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JavaDefinition"]:
        if not json_data:
            return None
        return cls(
            OutOfMemory=deserialize_list(json_data.get("OutOfMemory"), OutOfMemoryDefinition),
            OutOfThreads=deserialize_list(json_data.get("OutOfThreads"), OutOfThreadsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_JavaDefinition = JavaDefinition


@dataclass
class OutOfMemoryDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutOfMemoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutOfMemoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutOfMemoryDefinition = OutOfMemoryDefinition


@dataclass
class OutOfThreadsDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutOfThreadsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutOfThreadsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutOfThreadsDefinition = OutOfThreadsDefinition


@dataclass
class MemoryDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MemoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemoryDefinition = MemoryDefinition


@dataclass
class NetworkDefinition(BaseModel):
    Connectivity: Optional[Sequence["_ConnectivityDefinition"]]
    DroppedPackets: Optional[Sequence["_DroppedPacketsDefinition"]]
    Errors: Optional[Sequence["_ErrorsDefinition"]]
    Retransmission: Optional[Sequence["_RetransmissionDefinition"]]
    Utilization: Optional[Sequence["_UtilizationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Connectivity=deserialize_list(json_data.get("Connectivity"), ConnectivityDefinition),
            DroppedPackets=deserialize_list(json_data.get("DroppedPackets"), DroppedPacketsDefinition),
            Errors=deserialize_list(json_data.get("Errors"), ErrorsDefinition),
            Retransmission=deserialize_list(json_data.get("Retransmission"), RetransmissionDefinition),
            Utilization=deserialize_list(json_data.get("Utilization"), UtilizationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class ConnectivityDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectivityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectivityDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectivityDefinition = ConnectivityDefinition


@dataclass
class DroppedPacketsDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DroppedPacketsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DroppedPacketsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DroppedPacketsDefinition = DroppedPacketsDefinition


@dataclass
class ErrorsDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ErrorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ErrorsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ErrorsDefinition = ErrorsDefinition


@dataclass
class RetransmissionDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RetransmissionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetransmissionDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetransmissionDefinition = RetransmissionDefinition


@dataclass
class UtilizationDefinition(BaseModel):
    Enabled: Optional[bool]
    Thresholds: Optional[Sequence["_ThresholdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UtilizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UtilizationDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Thresholds=deserialize_list(json_data.get("Thresholds"), ThresholdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UtilizationDefinition = UtilizationDefinition


