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
    AvailableMemoryMb: Optional[float]
    Description: Optional[str]
    EntryPoint: Optional[str]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariables"]]
    HttpsTriggerUrl: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
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
    EventTrigger: Optional[Sequence["_EventTrigger"]]
    SourceRepository: Optional[Sequence["_SourceRepository"]]
    Timeouts: Optional["_Timeouts"]
    FailurePolicy: Optional[Sequence["_FailurePolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailableMemoryMb=json_data.get("AvailableMemoryMb"),
            Description=json_data.get("Description"),
            EntryPoint=json_data.get("EntryPoint"),
            EnvironmentVariables=json_data.get("EnvironmentVariables"),
            HttpsTriggerUrl=json_data.get("HttpsTriggerUrl"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
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
            EventTrigger=json_data.get("EventTrigger"),
            SourceRepository=json_data.get("SourceRepository"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            FailurePolicy=json_data.get("FailurePolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvironmentVariables:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariables"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariables = EnvironmentVariables


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class EventTrigger:
    EventType: Optional[str]
    Resource: Optional[str]
    FailurePolicy: Optional[Sequence["_FailurePolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_EventTrigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventTrigger"]:
        if not json_data:
            return None
        return cls(
            EventType=json_data.get("EventType"),
            Resource=json_data.get("Resource"),
            FailurePolicy=json_data.get("FailurePolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventTrigger = EventTrigger


@dataclass
class FailurePolicy:
    Retry: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FailurePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailurePolicy"]:
        if not json_data:
            return None
        return cls(
            Retry=json_data.get("Retry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailurePolicy = FailurePolicy


@dataclass
class SourceRepository:
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceRepository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceRepository"]:
        if not json_data:
            return None
        return cls(
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceRepository = SourceRepository


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


