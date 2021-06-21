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
    Arn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SizeConstraints: Optional[Sequence["_SizeConstraintsDefinition"]]

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
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SizeConstraints=deserialize_list(json_data.get("SizeConstraints"), SizeConstraintsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SizeConstraintsDefinition(BaseModel):
    ComparisonOperator: Optional[str]
    Size: Optional[float]
    TextTransformation: Optional[str]
    FieldToMatch: Optional[Sequence["_FieldToMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SizeConstraintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SizeConstraintsDefinition"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Size=json_data.get("Size"),
            TextTransformation=json_data.get("TextTransformation"),
            FieldToMatch=deserialize_list(json_data.get("FieldToMatch"), FieldToMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SizeConstraintsDefinition = SizeConstraintsDefinition


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

