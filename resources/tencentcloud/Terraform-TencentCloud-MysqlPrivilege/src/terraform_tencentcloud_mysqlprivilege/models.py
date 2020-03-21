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
    AccountName: Optional[str]
    Global: Optional[Sequence[str]]
    MysqlId: Optional[str]
    Column: Optional[Sequence["_Column"]]
    Database: Optional[Sequence["_Database"]]
    Table: Optional[Sequence["_Table"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountName=json_data.get("AccountName"),
            Global=json_data.get("Global"),
            MysqlId=json_data.get("MysqlId"),
            Column=json_data.get("Column"),
            Database=json_data.get("Database"),
            Table=json_data.get("Table"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Column:
    ColumnName: Optional[str]
    DatabaseName: Optional[str]
    Privileges: Optional[Sequence[str]]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Column"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Column"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            DatabaseName=json_data.get("DatabaseName"),
            Privileges=json_data.get("Privileges"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Column = Column


@dataclass
class Database:
    DatabaseName: Optional[str]
    Privileges: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Database"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Database"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            Privileges=json_data.get("Privileges"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Database = Database


@dataclass
class Table:
    DatabaseName: Optional[str]
    Privileges: Optional[Sequence[str]]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Table"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Table"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            Privileges=json_data.get("Privileges"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Table = Table


