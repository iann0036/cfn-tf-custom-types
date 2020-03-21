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
    BatchSize: Optional[float]
    BisectBatchOnFunctionError: Optional[bool]
    Enabled: Optional[bool]
    EventSourceArn: Optional[str]
    FunctionArn: Optional[str]
    FunctionName: Optional[str]
    LastModified: Optional[str]
    LastProcessingResult: Optional[str]
    MaximumBatchingWindowInSeconds: Optional[float]
    MaximumRecordAgeInSeconds: Optional[float]
    MaximumRetryAttempts: Optional[float]
    ParallelizationFactor: Optional[float]
    StartingPosition: Optional[str]
    StartingPositionTimestamp: Optional[str]
    State: Optional[str]
    StateTransitionReason: Optional[str]
    Uuid: Optional[str]
    DestinationConfig: Optional[Sequence["_DestinationConfig"]]
    OnFailure: Optional[Sequence["_OnFailure"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BatchSize=json_data.get("BatchSize"),
            BisectBatchOnFunctionError=json_data.get("BisectBatchOnFunctionError"),
            Enabled=json_data.get("Enabled"),
            EventSourceArn=json_data.get("EventSourceArn"),
            FunctionArn=json_data.get("FunctionArn"),
            FunctionName=json_data.get("FunctionName"),
            LastModified=json_data.get("LastModified"),
            LastProcessingResult=json_data.get("LastProcessingResult"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
            MaximumRecordAgeInSeconds=json_data.get("MaximumRecordAgeInSeconds"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
            ParallelizationFactor=json_data.get("ParallelizationFactor"),
            StartingPosition=json_data.get("StartingPosition"),
            StartingPositionTimestamp=json_data.get("StartingPositionTimestamp"),
            State=json_data.get("State"),
            StateTransitionReason=json_data.get("StateTransitionReason"),
            Uuid=json_data.get("Uuid"),
            DestinationConfig=json_data.get("DestinationConfig"),
            OnFailure=json_data.get("OnFailure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DestinationConfig:
    OnFailure: Optional[Sequence["_OnFailure"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationConfig"]:
        if not json_data:
            return None
        return cls(
            OnFailure=json_data.get("OnFailure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationConfig = DestinationConfig


@dataclass
class OnFailure:
    DestinationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnFailure"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnFailure"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnFailure = OnFailure


