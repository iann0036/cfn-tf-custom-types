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
    DomainController: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ServerCredentialType: Optional[str]
    Vdomparam: Optional[str]
    FileFilter: Optional[Sequence["_FileFilterDefinition"]]
    ServerKeytab: Optional[Sequence["_ServerKeytabDefinition"]]

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
            DomainController=json_data.get("DomainController"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ServerCredentialType=json_data.get("ServerCredentialType"),
            Vdomparam=json_data.get("Vdomparam"),
            FileFilter=deserialize_list(json_data.get("FileFilter"), FileFilterDefinition),
            ServerKeytab=deserialize_list(json_data.get("ServerKeytab"), ServerKeytabDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FileFilterDefinition(BaseModel):
    Log: Optional[str]
    Status: Optional[str]
    Entries: Optional[Sequence["_EntriesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FileFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Log=json_data.get("Log"),
            Status=json_data.get("Status"),
            Entries=deserialize_list(json_data.get("Entries"), EntriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileFilterDefinition = FileFilterDefinition


@dataclass
class EntriesDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    Direction: Optional[str]
    Filter: Optional[str]
    FileType: Optional[Sequence["_FileTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            Direction=json_data.get("Direction"),
            Filter=json_data.get("Filter"),
            FileType=deserialize_list(json_data.get("FileType"), FileTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntriesDefinition = EntriesDefinition


@dataclass
class FileTypeDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileTypeDefinition = FileTypeDefinition


@dataclass
class ServerKeytabDefinition(BaseModel):
    Keytab: Optional[str]
    Principal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerKeytabDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerKeytabDefinition"]:
        if not json_data:
            return None
        return cls(
            Keytab=json_data.get("Keytab"),
            Principal=json_data.get("Principal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerKeytabDefinition = ServerKeytabDefinition


