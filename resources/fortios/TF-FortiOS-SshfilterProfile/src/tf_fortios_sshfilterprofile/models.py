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
    Block: Optional[str]
    DefaultCommandLog: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Log: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    FileFilter: Optional[Sequence["_FileFilterDefinition"]]
    ShellCommands: Optional[Sequence["_ShellCommandsDefinition"]]

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
            Block=json_data.get("Block"),
            DefaultCommandLog=json_data.get("DefaultCommandLog"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Log=json_data.get("Log"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            FileFilter=deserialize_list(json_data.get("FileFilter"), FileFilterDefinition),
            ShellCommands=deserialize_list(json_data.get("ShellCommands"), ShellCommandsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FileFilterDefinition(BaseModel):
    Log: Optional[str]
    ScanArchiveContents: Optional[str]
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
            ScanArchiveContents=json_data.get("ScanArchiveContents"),
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
    PasswordProtected: Optional[str]
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
            PasswordProtected=json_data.get("PasswordProtected"),
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
class ShellCommandsDefinition(BaseModel):
    Action: Optional[str]
    Alert: Optional[str]
    Id: Optional[float]
    Log: Optional[str]
    Pattern: Optional[str]
    Severity: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ShellCommandsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShellCommandsDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Alert=json_data.get("Alert"),
            Id=json_data.get("Id"),
            Log=json_data.get("Log"),
            Pattern=json_data.get("Pattern"),
            Severity=json_data.get("Severity"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShellCommandsDefinition = ShellCommandsDefinition


