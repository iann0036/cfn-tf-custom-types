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
    AccountHost: Optional[str]
    AccountName: Optional[str]
    Global: Optional[Sequence[str]]
    Id: Optional[str]
    MysqlId: Optional[str]
    Column: Optional[Sequence["_ColumnDefinition"]]
    Database: Optional[Sequence["_DatabaseDefinition"]]
    Table: Optional[Sequence["_TableDefinition"]]

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
            AccountHost=json_data.get("AccountHost"),
            AccountName=json_data.get("AccountName"),
            Global=json_data.get("Global"),
            Id=json_data.get("Id"),
            MysqlId=json_data.get("MysqlId"),
            Column=deserialize_list(json_data.get("Column"), ColumnDefinition),
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
            Table=deserialize_list(json_data.get("Table"), TableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ColumnDefinition(BaseModel):
    ColumnName: Optional[str]
    DatabaseName: Optional[str]
    Privileges: Optional[Sequence[str]]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnDefinition"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            DatabaseName=json_data.get("DatabaseName"),
            Privileges=json_data.get("Privileges"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnDefinition = ColumnDefinition


@dataclass
class DatabaseDefinition(BaseModel):
    DatabaseName: Optional[str]
    Privileges: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            Privileges=json_data.get("Privileges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDefinition = DatabaseDefinition


@dataclass
class TableDefinition(BaseModel):
    DatabaseName: Optional[str]
    Privileges: Optional[Sequence[str]]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            Privileges=json_data.get("Privileges"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableDefinition = TableDefinition


