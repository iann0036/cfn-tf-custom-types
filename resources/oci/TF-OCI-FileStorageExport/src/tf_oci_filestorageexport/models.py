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
    ExportSetId: Optional[str]
    FileSystemId: Optional[str]
    Id: Optional[str]
    Path: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    ExportOptions: Optional[Sequence["_ExportOptionsDefinition"]]
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
            ExportSetId=json_data.get("ExportSetId"),
            FileSystemId=json_data.get("FileSystemId"),
            Id=json_data.get("Id"),
            Path=json_data.get("Path"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            ExportOptions=deserialize_list(json_data.get("ExportOptions"), ExportOptionsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExportOptionsDefinition(BaseModel):
    Access: Optional[str]
    AnonymousGid: Optional[str]
    AnonymousUid: Optional[str]
    IdentitySquash: Optional[str]
    RequirePrivilegedSourcePort: Optional[bool]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExportOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Access=json_data.get("Access"),
            AnonymousGid=json_data.get("AnonymousGid"),
            AnonymousUid=json_data.get("AnonymousUid"),
            IdentitySquash=json_data.get("IdentitySquash"),
            RequirePrivilegedSourcePort=json_data.get("RequirePrivilegedSourcePort"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportOptionsDefinition = ExportOptionsDefinition


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


