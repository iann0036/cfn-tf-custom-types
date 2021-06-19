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
    BatchSize: Optional[float]
    BisectBatchOnFunctionError: Optional[bool]
    Enabled: Optional[bool]
    EventSourceArn: Optional[str]
    FunctionArn: Optional[str]
    FunctionName: Optional[str]
    FunctionResponseTypes: Optional[Sequence[str]]
    Id: Optional[str]
    LastModified: Optional[str]
    LastProcessingResult: Optional[str]
    MaximumBatchingWindowInSeconds: Optional[float]
    MaximumRecordAgeInSeconds: Optional[float]
    MaximumRetryAttempts: Optional[float]
    ParallelizationFactor: Optional[float]
    Queues: Optional[Sequence[str]]
    StartingPosition: Optional[str]
    StartingPositionTimestamp: Optional[str]
    State: Optional[str]
    StateTransitionReason: Optional[str]
    Topics: Optional[Sequence[str]]
    TumblingWindowInSeconds: Optional[float]
    Uuid: Optional[str]
    DestinationConfig: Optional[Sequence["_DestinationConfigDefinition"]]
    SelfManagedEventSource: Optional[Sequence["_SelfManagedEventSourceDefinition"]]
    SourceAccessConfiguration: Optional[Sequence["_SourceAccessConfigurationDefinition"]]

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
            BatchSize=json_data.get("BatchSize"),
            BisectBatchOnFunctionError=json_data.get("BisectBatchOnFunctionError"),
            Enabled=json_data.get("Enabled"),
            EventSourceArn=json_data.get("EventSourceArn"),
            FunctionArn=json_data.get("FunctionArn"),
            FunctionName=json_data.get("FunctionName"),
            FunctionResponseTypes=json_data.get("FunctionResponseTypes"),
            Id=json_data.get("Id"),
            LastModified=json_data.get("LastModified"),
            LastProcessingResult=json_data.get("LastProcessingResult"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
            MaximumRecordAgeInSeconds=json_data.get("MaximumRecordAgeInSeconds"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
            ParallelizationFactor=json_data.get("ParallelizationFactor"),
            Queues=json_data.get("Queues"),
            StartingPosition=json_data.get("StartingPosition"),
            StartingPositionTimestamp=json_data.get("StartingPositionTimestamp"),
            State=json_data.get("State"),
            StateTransitionReason=json_data.get("StateTransitionReason"),
            Topics=json_data.get("Topics"),
            TumblingWindowInSeconds=json_data.get("TumblingWindowInSeconds"),
            Uuid=json_data.get("Uuid"),
            DestinationConfig=deserialize_list(json_data.get("DestinationConfig"), DestinationConfigDefinition),
            SelfManagedEventSource=deserialize_list(json_data.get("SelfManagedEventSource"), SelfManagedEventSourceDefinition),
            SourceAccessConfiguration=deserialize_list(json_data.get("SourceAccessConfiguration"), SourceAccessConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DestinationConfigDefinition(BaseModel):
    OnFailure: Optional[Sequence["_OnFailureDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            OnFailure=deserialize_list(json_data.get("OnFailure"), OnFailureDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationConfigDefinition = DestinationConfigDefinition


@dataclass
class OnFailureDefinition(BaseModel):
    DestinationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnFailureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnFailureDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnFailureDefinition = OnFailureDefinition


@dataclass
class SelfManagedEventSourceDefinition(BaseModel):
    Endpoints: Optional[Sequence["_EndpointsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SelfManagedEventSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfManagedEventSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Endpoints=deserialize_list(json_data.get("Endpoints"), EndpointsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelfManagedEventSourceDefinition = SelfManagedEventSourceDefinition


@dataclass
class EndpointsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointsDefinition = EndpointsDefinition


@dataclass
class SourceAccessConfigurationDefinition(BaseModel):
    Type: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceAccessConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceAccessConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceAccessConfigurationDefinition = SourceAccessConfigurationDefinition


