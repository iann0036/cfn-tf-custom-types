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
    App: Optional[str]
    Blob: Optional[Sequence["_Blob"]]
    BuildpackProvidedDescription: Optional[str]
    Checksum: Optional[str]
    Commit: Optional[str]
    CommitDescription: Optional[str]
    FilePath: Optional[str]
    FileUrl: Optional[str]
    Id: Optional[str]
    ProcessTypes: Optional[Sequence["_ProcessTypes"]]
    Size: Optional[float]
    Stack: Optional[str]
    StackId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            App=json_data.get("App"),
            Blob=json_data.get("Blob"),
            BuildpackProvidedDescription=json_data.get("BuildpackProvidedDescription"),
            Checksum=json_data.get("Checksum"),
            Commit=json_data.get("Commit"),
            CommitDescription=json_data.get("CommitDescription"),
            FilePath=json_data.get("FilePath"),
            FileUrl=json_data.get("FileUrl"),
            Id=json_data.get("Id"),
            ProcessTypes=json_data.get("ProcessTypes"),
            Size=json_data.get("Size"),
            Stack=json_data.get("Stack"),
            StackId=json_data.get("StackId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Blob:
    Method: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Blob"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Blob"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Blob = Blob


@dataclass
class ProcessTypes:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessTypes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessTypes"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessTypes = ProcessTypes


