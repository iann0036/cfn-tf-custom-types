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
    AvailableMemoryMb: Optional[float]
    BuildEnvironmentVariables: Optional[Sequence["_BuildEnvironmentVariablesDefinition"]]
    Description: Optional[str]
    EntryPoint: Optional[str]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariablesDefinition"]]
    HttpsTriggerUrl: Optional[str]
    Id: Optional[str]
    IngressSettings: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MaxInstances: Optional[float]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    Runtime: Optional[str]
    ServiceAccountEmail: Optional[str]
    SourceArchiveBucket: Optional[str]
    SourceArchiveObject: Optional[str]
    Timeout: Optional[float]
    TriggerHttp: Optional[bool]
    VpcConnector: Optional[str]
    VpcConnectorEgressSettings: Optional[str]
    EventTrigger: Optional[Sequence["_EventTriggerDefinition"]]
    SourceRepository: Optional[Sequence["_SourceRepositoryDefinition"]]
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
            AvailableMemoryMb=json_data.get("AvailableMemoryMb"),
            BuildEnvironmentVariables=deserialize_list(json_data.get("BuildEnvironmentVariables"), BuildEnvironmentVariablesDefinition),
            Description=json_data.get("Description"),
            EntryPoint=json_data.get("EntryPoint"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariablesDefinition),
            HttpsTriggerUrl=json_data.get("HttpsTriggerUrl"),
            Id=json_data.get("Id"),
            IngressSettings=json_data.get("IngressSettings"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MaxInstances=json_data.get("MaxInstances"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Runtime=json_data.get("Runtime"),
            ServiceAccountEmail=json_data.get("ServiceAccountEmail"),
            SourceArchiveBucket=json_data.get("SourceArchiveBucket"),
            SourceArchiveObject=json_data.get("SourceArchiveObject"),
            Timeout=json_data.get("Timeout"),
            TriggerHttp=json_data.get("TriggerHttp"),
            VpcConnector=json_data.get("VpcConnector"),
            VpcConnectorEgressSettings=json_data.get("VpcConnectorEgressSettings"),
            EventTrigger=deserialize_list(json_data.get("EventTrigger"), EventTriggerDefinition),
            SourceRepository=deserialize_list(json_data.get("SourceRepository"), SourceRepositoryDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BuildEnvironmentVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BuildEnvironmentVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BuildEnvironmentVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BuildEnvironmentVariablesDefinition = BuildEnvironmentVariablesDefinition


@dataclass
class EnvironmentVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariablesDefinition = EnvironmentVariablesDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class EventTriggerDefinition(BaseModel):
    EventType: Optional[str]
    Resource: Optional[str]
    FailurePolicy: Optional[Sequence["_FailurePolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EventTriggerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventTriggerDefinition"]:
        if not json_data:
            return None
        return cls(
            EventType=json_data.get("EventType"),
            Resource=json_data.get("Resource"),
            FailurePolicy=deserialize_list(json_data.get("FailurePolicy"), FailurePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventTriggerDefinition = EventTriggerDefinition


@dataclass
class FailurePolicyDefinition(BaseModel):
    Retry: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FailurePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailurePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Retry=json_data.get("Retry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailurePolicyDefinition = FailurePolicyDefinition


@dataclass
class SourceRepositoryDefinition(BaseModel):
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceRepositoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceRepositoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceRepositoryDefinition = SourceRepositoryDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


