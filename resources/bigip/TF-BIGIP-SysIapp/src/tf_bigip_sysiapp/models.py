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
    Description: Optional[str]
    Devicegroup: Optional[str]
    ExecuteAction: Optional[str]
    Id: Optional[str]
    InheritedDevicegroup: Optional[str]
    InheritedTrafficGroup: Optional[str]
    Jsonfile: Optional[str]
    Name: Optional[str]
    Partition: Optional[str]
    StrictUpdates: Optional[str]
    Template: Optional[str]
    TemplateModified: Optional[str]
    TemplatePrerequisiteErrors: Optional[str]
    TrafficGroup: Optional[str]
    Lists: Optional[Sequence["_ListsDefinition"]]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Tables: Optional[Sequence["_TablesDefinition"]]
    Variables: Optional[Sequence["_VariablesDefinition"]]

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
            Description=json_data.get("Description"),
            Devicegroup=json_data.get("Devicegroup"),
            ExecuteAction=json_data.get("ExecuteAction"),
            Id=json_data.get("Id"),
            InheritedDevicegroup=json_data.get("InheritedDevicegroup"),
            InheritedTrafficGroup=json_data.get("InheritedTrafficGroup"),
            Jsonfile=json_data.get("Jsonfile"),
            Name=json_data.get("Name"),
            Partition=json_data.get("Partition"),
            StrictUpdates=json_data.get("StrictUpdates"),
            Template=json_data.get("Template"),
            TemplateModified=json_data.get("TemplateModified"),
            TemplatePrerequisiteErrors=json_data.get("TemplatePrerequisiteErrors"),
            TrafficGroup=json_data.get("TrafficGroup"),
            Lists=deserialize_list(json_data.get("Lists"), ListsDefinition),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Tables=deserialize_list(json_data.get("Tables"), TablesDefinition),
            Variables=deserialize_list(json_data.get("Variables"), VariablesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ListsDefinition(BaseModel):
    Encrypted: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListsDefinition"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListsDefinition = ListsDefinition


@dataclass
class MetadataDefinition(BaseModel):
    Persists: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Persists=json_data.get("Persists"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class TablesDefinition(BaseModel):
    ColumnNames: Optional[Sequence[str]]
    EncryptedColumns: Optional[str]
    Name: Optional[str]
    Rows: Optional[Sequence["_RowsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TablesDefinition"]:
        if not json_data:
            return None
        return cls(
            ColumnNames=json_data.get("ColumnNames"),
            EncryptedColumns=json_data.get("EncryptedColumns"),
            Name=json_data.get("Name"),
            Rows=deserialize_list(json_data.get("Rows"), RowsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TablesDefinition = TablesDefinition


@dataclass
class RowsDefinition(BaseModel):
    Row: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RowsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RowsDefinition"]:
        if not json_data:
            return None
        return cls(
            Row=json_data.get("Row"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RowsDefinition = RowsDefinition


@dataclass
class VariablesDefinition(BaseModel):
    Encrypted: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariablesDefinition = VariablesDefinition


