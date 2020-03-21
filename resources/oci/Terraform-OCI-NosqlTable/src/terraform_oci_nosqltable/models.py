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
    CompartmentId: Optional[str]
    DdlStatement: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    LifecycleDetails: Optional[str]
    Name: Optional[str]
    Schema: Optional[Sequence["_Schema"]]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    TableLimits: Optional[Sequence["_TableLimits"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DdlStatement=json_data.get("DdlStatement"),
            DefinedTags=json_data.get("DefinedTags"),
            FreeformTags=json_data.get("FreeformTags"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Name=json_data.get("Name"),
            Schema=json_data.get("Schema"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            TableLimits=json_data.get("TableLimits"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class Schema:
    Columns: Optional[Sequence["_Columns"]]
    PrimaryKey: Optional[Sequence[str]]
    ShardKey: Optional[Sequence[str]]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Schema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schema"]:
        if not json_data:
            return None
        return cls(
            Columns=json_data.get("Columns"),
            PrimaryKey=json_data.get("PrimaryKey"),
            ShardKey=json_data.get("ShardKey"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schema = Schema


@dataclass
class Columns:
    DefaultValue: Optional[str]
    IsNullable: Optional[bool]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Columns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Columns"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            IsNullable=json_data.get("IsNullable"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Columns = Columns


@dataclass
class TableLimits:
    MaxReadUnits: Optional[float]
    MaxStorageInGbs: Optional[float]
    MaxWriteUnits: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TableLimits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableLimits"]:
        if not json_data:
            return None
        return cls(
            MaxReadUnits=json_data.get("MaxReadUnits"),
            MaxStorageInGbs=json_data.get("MaxStorageInGbs"),
            MaxWriteUnits=json_data.get("MaxWriteUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableLimits = TableLimits


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


