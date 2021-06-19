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
    Column: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Parent: Optional[str]
    Template: Optional[str]
    TemplateDisplayname: Optional[str]
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
            Column=json_data.get("Column"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Parent=json_data.get("Parent"),
            Template=json_data.get("Template"),
            TemplateDisplayname=json_data.get("TemplateDisplayname"),
            Fields=deserialize_list(json_data.get("Fields"), FieldsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FieldsDefinition(BaseModel):
    BoolValue: Optional[bool]
    DoubleValue: Optional[float]
    EnumValue: Optional[str]
    FieldName: Optional[str]
    StringValue: Optional[str]
    TimestampValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            BoolValue=json_data.get("BoolValue"),
            DoubleValue=json_data.get("DoubleValue"),
            EnumValue=json_data.get("EnumValue"),
            FieldName=json_data.get("FieldName"),
            StringValue=json_data.get("StringValue"),
            TimestampValue=json_data.get("TimestampValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldsDefinition = FieldsDefinition


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


