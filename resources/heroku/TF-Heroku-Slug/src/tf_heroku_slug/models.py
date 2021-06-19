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
    App: Optional[str]
    Blob: Optional[Sequence["_BlobDefinition"]]
    BuildpackProvidedDescription: Optional[str]
    Checksum: Optional[str]
    Commit: Optional[str]
    CommitDescription: Optional[str]
    FilePath: Optional[str]
    FileUrl: Optional[str]
    Id: Optional[str]
    ProcessTypes: Optional[Sequence["_ProcessTypesDefinition"]]
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
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            App=json_data.get("App"),
            Blob=deserialize_list(json_data.get("Blob"), BlobDefinition),
            BuildpackProvidedDescription=json_data.get("BuildpackProvidedDescription"),
            Checksum=json_data.get("Checksum"),
            Commit=json_data.get("Commit"),
            CommitDescription=json_data.get("CommitDescription"),
            FilePath=json_data.get("FilePath"),
            FileUrl=json_data.get("FileUrl"),
            Id=json_data.get("Id"),
            ProcessTypes=deserialize_list(json_data.get("ProcessTypes"), ProcessTypesDefinition),
            Size=json_data.get("Size"),
            Stack=json_data.get("Stack"),
            StackId=json_data.get("StackId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BlobDefinition(BaseModel):
    Method: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlobDefinition"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlobDefinition = BlobDefinition


@dataclass
class ProcessTypesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessTypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessTypesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessTypesDefinition = ProcessTypesDefinition


