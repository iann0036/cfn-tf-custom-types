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
    BatchRolloverSizeInMbs: Optional[float]
    BatchRolloverTimeInSeconds: Optional[float]
    Bucket: Optional[str]
    Error: Optional[Sequence["_Error"]]
    StartPosition: Optional[str]
    State: Optional[str]
    StreamId: Optional[str]
    TimeCreated: Optional[str]
    UseExistingBucket: Optional[bool]
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
            BatchRolloverSizeInMbs=json_data.get("BatchRolloverSizeInMbs"),
            BatchRolloverTimeInSeconds=json_data.get("BatchRolloverTimeInSeconds"),
            Bucket=json_data.get("Bucket"),
            Error=json_data.get("Error"),
            StartPosition=json_data.get("StartPosition"),
            State=json_data.get("State"),
            StreamId=json_data.get("StreamId"),
            TimeCreated=json_data.get("TimeCreated"),
            UseExistingBucket=json_data.get("UseExistingBucket"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Error:
    Code: Optional[str]
    Message: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Error"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Error"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Message=json_data.get("Message"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Error = Error


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


