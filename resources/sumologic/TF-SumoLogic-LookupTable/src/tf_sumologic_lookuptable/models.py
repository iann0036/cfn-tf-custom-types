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
    Id: Optional[str]
    Name: Optional[str]
    ParentFolderId: Optional[str]
    PrimaryKeys: Optional[Sequence[str]]
    SizeLimitAction: Optional[str]
    Ttl: Optional[float]
    Fields: Optional[Sequence["_FieldsDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ParentFolderId=json_data.get("ParentFolderId"),
            PrimaryKeys=json_data.get("PrimaryKeys"),
            SizeLimitAction=json_data.get("SizeLimitAction"),
            Ttl=json_data.get("Ttl"),
            Fields=deserialize_list(json_data.get("Fields"), FieldsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FieldsDefinition(BaseModel):
    FieldName: Optional[str]
    FieldType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            FieldName=json_data.get("FieldName"),
            FieldType=json_data.get("FieldType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldsDefinition = FieldsDefinition


