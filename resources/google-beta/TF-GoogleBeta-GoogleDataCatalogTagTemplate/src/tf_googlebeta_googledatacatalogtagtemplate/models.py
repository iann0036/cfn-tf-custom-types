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
    DisplayName: Optional[str]
    ForceDelete: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    TagTemplateId: Optional[str]
    Fields: Optional[Sequence["_FieldsDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            DisplayName=json_data.get("DisplayName"),
            ForceDelete=json_data.get("ForceDelete"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            TagTemplateId=json_data.get("TagTemplateId"),
            Fields=deserialize_list(json_data.get("Fields"), FieldsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FieldsDefinition(BaseModel):
    Description: Optional[str]
    DisplayName: Optional[str]
    FieldId: Optional[str]
    IsRequired: Optional[bool]
    Order: Optional[float]
    Type: Optional[Sequence["_TypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FieldId=json_data.get("FieldId"),
            IsRequired=json_data.get("IsRequired"),
            Order=json_data.get("Order"),
            Type=deserialize_list(json_data.get("Type"), TypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldsDefinition = FieldsDefinition


@dataclass
class TypeDefinition(BaseModel):
    PrimitiveType: Optional[str]
    EnumType: Optional[Sequence["_EnumTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeDefinition"]:
        if not json_data:
            return None
        return cls(
            PrimitiveType=json_data.get("PrimitiveType"),
            EnumType=deserialize_list(json_data.get("EnumType"), EnumTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TypeDefinition = TypeDefinition


@dataclass
class EnumTypeDefinition(BaseModel):
    AllowedValues: Optional[Sequence["_AllowedValuesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnumTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnumTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedValues=deserialize_list(json_data.get("AllowedValues"), AllowedValuesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnumTypeDefinition = EnumTypeDefinition


@dataclass
class AllowedValuesDefinition(BaseModel):
    DisplayName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedValuesDefinition = AllowedValuesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


