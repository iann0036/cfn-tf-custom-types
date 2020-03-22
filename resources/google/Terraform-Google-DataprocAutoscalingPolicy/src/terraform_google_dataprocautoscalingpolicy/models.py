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
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[str]
    Project: Optional[str]
    BasicAlgorithm: Optional[Sequence["_BasicAlgorithm"]]
    SecondaryWorkerConfig: Optional[Sequence["_SecondaryWorkerConfig"]]
    Timeouts: Optional["_Timeouts"]
    WorkerConfig: Optional[Sequence["_WorkerConfig"]]
    YarnConfig: Optional[Sequence["_YarnConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            Project=json_data.get("Project"),
            BasicAlgorithm=json_data.get("BasicAlgorithm"),
            SecondaryWorkerConfig=json_data.get("SecondaryWorkerConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            WorkerConfig=json_data.get("WorkerConfig"),
            YarnConfig=json_data.get("YarnConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BasicAlgorithm:
    CooldownPeriod: Optional[str]
    YarnConfig: Optional[Sequence["_YarnConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_BasicAlgorithm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicAlgorithm"]:
        if not json_data:
            return None
        return cls(
            CooldownPeriod=json_data.get("CooldownPeriod"),
            YarnConfig=json_data.get("YarnConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicAlgorithm = BasicAlgorithm


@dataclass
class YarnConfig:
    GracefulDecommissionTimeout: Optional[str]
    ScaleDownFactor: Optional[float]
    ScaleDownMinWorkerFraction: Optional[float]
    ScaleUpFactor: Optional[float]
    ScaleUpMinWorkerFraction: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_YarnConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_YarnConfig"]:
        if not json_data:
            return None
        return cls(
            GracefulDecommissionTimeout=json_data.get("GracefulDecommissionTimeout"),
            ScaleDownFactor=json_data.get("ScaleDownFactor"),
            ScaleDownMinWorkerFraction=json_data.get("ScaleDownMinWorkerFraction"),
            ScaleUpFactor=json_data.get("ScaleUpFactor"),
            ScaleUpMinWorkerFraction=json_data.get("ScaleUpMinWorkerFraction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_YarnConfig = YarnConfig


@dataclass
class SecondaryWorkerConfig:
    MaxInstances: Optional[float]
    MinInstances: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryWorkerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryWorkerConfig"]:
        if not json_data:
            return None
        return cls(
            MaxInstances=json_data.get("MaxInstances"),
            MinInstances=json_data.get("MinInstances"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryWorkerConfig = SecondaryWorkerConfig


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class WorkerConfig:
    MaxInstances: Optional[float]
    MinInstances: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfig"]:
        if not json_data:
            return None
        return cls(
            MaxInstances=json_data.get("MaxInstances"),
            MinInstances=json_data.get("MinInstances"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfig = WorkerConfig


