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
    Lists: Optional[Sequence["_Lists"]]
    Metadata: Optional[Sequence["_Metadata"]]
    Tables: Optional[Sequence["_Tables"]]
    Variables: Optional[Sequence["_Variables"]]
    Rows: Optional[Sequence["_Rows"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            Lists=json_data.get("Lists"),
            Metadata=json_data.get("Metadata"),
            Tables=json_data.get("Tables"),
            Variables=json_data.get("Variables"),
            Rows=json_data.get("Rows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Lists:
    Encrypted: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Lists"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lists"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lists = Lists


@dataclass
class Metadata:
    Persists: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Persists=json_data.get("Persists"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Tables:
    ColumnNames: Optional[Sequence[str]]
    EncryptedColumns: Optional[str]
    Name: Optional[str]
    Rows: Optional[Sequence["_Rows"]]

    @classmethod
    def _deserialize(
        cls: Type["_Tables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tables"]:
        if not json_data:
            return None
        return cls(
            ColumnNames=json_data.get("ColumnNames"),
            EncryptedColumns=json_data.get("EncryptedColumns"),
            Name=json_data.get("Name"),
            Rows=json_data.get("Rows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tables = Tables


@dataclass
class Rows:
    Row: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Rows"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rows"]:
        if not json_data:
            return None
        return cls(
            Row=json_data.get("Row"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rows = Rows


@dataclass
class Variables:
    Encrypted: Optional[str]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Variables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Variables"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Variables = Variables


