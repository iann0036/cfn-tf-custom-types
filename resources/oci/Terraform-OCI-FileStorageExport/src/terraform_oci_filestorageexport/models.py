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
    ExportSetId: Optional[str]
    FileSystemId: Optional[str]
    Path: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    ExportOptions: Optional[Sequence["_ExportOptions"]]
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
            ExportSetId=json_data.get("ExportSetId"),
            FileSystemId=json_data.get("FileSystemId"),
            Path=json_data.get("Path"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            ExportOptions=json_data.get("ExportOptions"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExportOptions:
    Access: Optional[str]
    AnonymousGid: Optional[str]
    AnonymousUid: Optional[str]
    IdentitySquash: Optional[str]
    RequirePrivilegedSourcePort: Optional[bool]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExportOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportOptions"]:
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
_ExportOptions = ExportOptions


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


