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
    Buildpacks: Optional[Sequence[str]]
    Id: Optional[str]
    LocalChecksum: Optional[str]
    OutputStreamUrl: Optional[str]
    ReleaseId: Optional[str]
    SlugId: Optional[str]
    Stack: Optional[str]
    Status: Optional[str]
    User: Optional[Sequence["_UserDefinition"]]
    Uuid: Optional[str]
    Source: Optional[Sequence["_SourceDefinition"]]

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
            Buildpacks=json_data.get("Buildpacks"),
            Id=json_data.get("Id"),
            LocalChecksum=json_data.get("LocalChecksum"),
            OutputStreamUrl=json_data.get("OutputStreamUrl"),
            ReleaseId=json_data.get("ReleaseId"),
            SlugId=json_data.get("SlugId"),
            Stack=json_data.get("Stack"),
            Status=json_data.get("Status"),
            User=deserialize_list(json_data.get("User"), UserDefinition),
            Uuid=json_data.get("Uuid"),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UserDefinition(BaseModel):
    Email: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinition = UserDefinition


@dataclass
class SourceDefinition(BaseModel):
    Checksum: Optional[str]
    Path: Optional[str]
    Url: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Checksum=json_data.get("Checksum"),
            Path=json_data.get("Path"),
            Url=json_data.get("Url"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


