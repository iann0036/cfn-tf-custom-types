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
    CatalogId: Optional[str]
    CatalogResource: Optional[bool]
    Id: Optional[str]
    Permissions: Optional[Sequence[str]]
    PermissionsWithGrantOption: Optional[Sequence[str]]
    Principal: Optional[str]
    DataLocation: Optional[Sequence["_DataLocationDefinition"]]
    Database: Optional[Sequence["_DatabaseDefinition"]]
    Table: Optional[Sequence["_TableDefinition"]]
    TableWithColumns: Optional[Sequence["_TableWithColumnsDefinition"]]

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
            CatalogId=json_data.get("CatalogId"),
            CatalogResource=json_data.get("CatalogResource"),
            Id=json_data.get("Id"),
            Permissions=json_data.get("Permissions"),
            PermissionsWithGrantOption=json_data.get("PermissionsWithGrantOption"),
            Principal=json_data.get("Principal"),
            DataLocation=deserialize_list(json_data.get("DataLocation"), DataLocationDefinition),
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
            Table=deserialize_list(json_data.get("Table"), TableDefinition),
            TableWithColumns=deserialize_list(json_data.get("TableWithColumns"), TableWithColumnsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DataLocationDefinition(BaseModel):
    Arn: Optional[str]
    CatalogId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            CatalogId=json_data.get("CatalogId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataLocationDefinition = DataLocationDefinition


@dataclass
class DatabaseDefinition(BaseModel):
    CatalogId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDefinition = DatabaseDefinition


@dataclass
class TableDefinition(BaseModel):
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    Name: Optional[str]
    Wildcard: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableDefinition"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            Name=json_data.get("Name"),
            Wildcard=json_data.get("Wildcard"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableDefinition = TableDefinition


@dataclass
class TableWithColumnsDefinition(BaseModel):
    CatalogId: Optional[str]
    ColumnNames: Optional[Sequence[str]]
    DatabaseName: Optional[str]
    ExcludedColumnNames: Optional[Sequence[str]]
    Name: Optional[str]
    Wildcard: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TableWithColumnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableWithColumnsDefinition"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            ColumnNames=json_data.get("ColumnNames"),
            DatabaseName=json_data.get("DatabaseName"),
            ExcludedColumnNames=json_data.get("ExcludedColumnNames"),
            Name=json_data.get("Name"),
            Wildcard=json_data.get("Wildcard"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableWithColumnsDefinition = TableWithColumnsDefinition


