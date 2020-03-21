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
    ApplicationId: Optional[str]
    Arguments: Optional[Sequence[str]]
    Asynchronous: Optional[bool]
    ClassName: Optional[str]
    CompartmentId: Optional[str]
    Configuration: Optional[Sequence["_Configuration"]]
    DataReadInBytes: Optional[str]
    DataWrittenInBytes: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    DriverShape: Optional[str]
    ExecutorShape: Optional[str]
    FileUri: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Language: Optional[str]
    LifecycleDetails: Optional[str]
    LogsBucketUri: Optional[str]
    NumExecutors: Optional[float]
    OpcRequestId: Optional[str]
    OwnerPrincipalId: Optional[str]
    OwnerUserName: Optional[str]
    RunDurationInMilliseconds: Optional[str]
    SparkVersion: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    TotalOcpu: Optional[float]
    WarehouseBucketUri: Optional[str]
    Parameters: Optional[Sequence["_Parameters"]]
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
            ApplicationId=json_data.get("ApplicationId"),
            Arguments=json_data.get("Arguments"),
            Asynchronous=json_data.get("Asynchronous"),
            ClassName=json_data.get("ClassName"),
            CompartmentId=json_data.get("CompartmentId"),
            Configuration=json_data.get("Configuration"),
            DataReadInBytes=json_data.get("DataReadInBytes"),
            DataWrittenInBytes=json_data.get("DataWrittenInBytes"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            DriverShape=json_data.get("DriverShape"),
            ExecutorShape=json_data.get("ExecutorShape"),
            FileUri=json_data.get("FileUri"),
            FreeformTags=json_data.get("FreeformTags"),
            Language=json_data.get("Language"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            LogsBucketUri=json_data.get("LogsBucketUri"),
            NumExecutors=json_data.get("NumExecutors"),
            OpcRequestId=json_data.get("OpcRequestId"),
            OwnerPrincipalId=json_data.get("OwnerPrincipalId"),
            OwnerUserName=json_data.get("OwnerUserName"),
            RunDurationInMilliseconds=json_data.get("RunDurationInMilliseconds"),
            SparkVersion=json_data.get("SparkVersion"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            TotalOcpu=json_data.get("TotalOcpu"),
            WarehouseBucketUri=json_data.get("WarehouseBucketUri"),
            Parameters=json_data.get("Parameters"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Configuration:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configuration"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configuration = Configuration


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class Parameters:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


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


