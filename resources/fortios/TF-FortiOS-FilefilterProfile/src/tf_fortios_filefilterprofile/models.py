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
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    ExtendedLog: Optional[str]
    FeatureSet: Optional[str]
    Id: Optional[str]
    Log: Optional[str]
    Name: Optional[str]
    ReplacemsgGroup: Optional[str]
    ScanArchiveContents: Optional[str]
    Vdomparam: Optional[str]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            ExtendedLog=json_data.get("ExtendedLog"),
            FeatureSet=json_data.get("FeatureSet"),
            Id=json_data.get("Id"),
            Log=json_data.get("Log"),
            Name=json_data.get("Name"),
            ReplacemsgGroup=json_data.get("ReplacemsgGroup"),
            ScanArchiveContents=json_data.get("ScanArchiveContents"),
            Vdomparam=json_data.get("Vdomparam"),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RulesDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    Direction: Optional[str]
    Name: Optional[str]
    PasswordProtected: Optional[str]
    Protocol: Optional[str]
    FileType: Optional[Sequence["_FileTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            Direction=json_data.get("Direction"),
            Name=json_data.get("Name"),
            PasswordProtected=json_data.get("PasswordProtected"),
            Protocol=json_data.get("Protocol"),
            FileType=deserialize_list(json_data.get("FileType"), FileTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


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


