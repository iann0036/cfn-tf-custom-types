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
    Location: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[str]
    Project: Optional[str]
    BasicAlgorithm: Optional[Sequence["_BasicAlgorithmDefinition"]]
    SecondaryWorkerConfig: Optional[Sequence["_SecondaryWorkerConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WorkerConfig: Optional[Sequence["_WorkerConfigDefinition"]]

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
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            Project=json_data.get("Project"),
            BasicAlgorithm=deserialize_list(json_data.get("BasicAlgorithm"), BasicAlgorithmDefinition),
            SecondaryWorkerConfig=deserialize_list(json_data.get("SecondaryWorkerConfig"), SecondaryWorkerConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WorkerConfig=deserialize_list(json_data.get("WorkerConfig"), WorkerConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BasicAlgorithmDefinition(BaseModel):
    CooldownPeriod: Optional[str]
    YarnConfig: Optional[Sequence["_YarnConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BasicAlgorithmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicAlgorithmDefinition"]:
        if not json_data:
            return None
        return cls(
            CooldownPeriod=json_data.get("CooldownPeriod"),
            YarnConfig=deserialize_list(json_data.get("YarnConfig"), YarnConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicAlgorithmDefinition = BasicAlgorithmDefinition


@dataclass
class YarnConfigDefinition(BaseModel):
    GracefulDecommissionTimeout: Optional[str]
    ScaleDownFactor: Optional[float]
    ScaleDownMinWorkerFraction: Optional[float]
    ScaleUpFactor: Optional[float]
    ScaleUpMinWorkerFraction: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_YarnConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_YarnConfigDefinition"]:
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
_YarnConfigDefinition = YarnConfigDefinition


@dataclass
class SecondaryWorkerConfigDefinition(BaseModel):
    MaxInstances: Optional[float]
    MinInstances: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryWorkerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryWorkerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxInstances=json_data.get("MaxInstances"),
            MinInstances=json_data.get("MinInstances"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryWorkerConfigDefinition = SecondaryWorkerConfigDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class WorkerConfigDefinition(BaseModel):
    MaxInstances: Optional[float]
    MinInstances: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxInstances=json_data.get("MaxInstances"),
            MinInstances=json_data.get("MinInstances"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfigDefinition = WorkerConfigDefinition


