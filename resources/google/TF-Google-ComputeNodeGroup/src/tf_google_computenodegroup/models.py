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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    InitialSize: Optional[float]
    MaintenancePolicy: Optional[str]
    Name: Optional[str]
    NodeTemplate: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    Size: Optional[float]
    Zone: Optional[str]
    AutoscalingPolicy: Optional[Sequence["_AutoscalingPolicyDefinition"]]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindowDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            InitialSize=json_data.get("InitialSize"),
            MaintenancePolicy=json_data.get("MaintenancePolicy"),
            Name=json_data.get("Name"),
            NodeTemplate=json_data.get("NodeTemplate"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Size=json_data.get("Size"),
            Zone=json_data.get("Zone"),
            AutoscalingPolicy=deserialize_list(json_data.get("AutoscalingPolicy"), AutoscalingPolicyDefinition),
            MaintenanceWindow=deserialize_list(json_data.get("MaintenanceWindow"), MaintenanceWindowDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AutoscalingPolicyDefinition(BaseModel):
    MaxNodes: Optional[float]
    MinNodes: Optional[float]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoscalingPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoscalingPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxNodes=json_data.get("MaxNodes"),
            MinNodes=json_data.get("MinNodes"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoscalingPolicyDefinition = AutoscalingPolicyDefinition


@dataclass
class MaintenanceWindowDefinition(BaseModel):
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition = MaintenanceWindowDefinition


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


