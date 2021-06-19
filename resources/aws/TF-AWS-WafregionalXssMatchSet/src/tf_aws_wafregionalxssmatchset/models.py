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
    Id: Optional[str]
    Name: Optional[str]
    XssMatchTuple: Optional[Sequence["_XssMatchTupleDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            XssMatchTuple=deserialize_list(json_data.get("XssMatchTuple"), XssMatchTupleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class XssMatchTupleDefinition(BaseModel):
    TextTransformation: Optional[str]
    FieldToMatch: Optional[Sequence["_FieldToMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_XssMatchTupleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XssMatchTupleDefinition"]:
        if not json_data:
            return None
        return cls(
            TextTransformation=json_data.get("TextTransformation"),
            FieldToMatch=deserialize_list(json_data.get("FieldToMatch"), FieldToMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_XssMatchTupleDefinition = XssMatchTupleDefinition


@dataclass
class FieldToMatchDefinition(BaseModel):
    Data: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldToMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldToMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldToMatchDefinition = FieldToMatchDefinition


