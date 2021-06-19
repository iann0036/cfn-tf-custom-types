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
    Action: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Position: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    FindingCriteria: Optional[Sequence["_FindingCriteriaDefinition"]]

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
            Action=json_data.get("Action"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Position=json_data.get("Position"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            FindingCriteria=deserialize_list(json_data.get("FindingCriteria"), FindingCriteriaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class FindingCriteriaDefinition(BaseModel):
    Criterion: Optional[Sequence["_CriterionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FindingCriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingCriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            Criterion=deserialize_list(json_data.get("Criterion"), CriterionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingCriteriaDefinition = FindingCriteriaDefinition


@dataclass
class CriterionDefinition(BaseModel):
    Eq: Optional[Sequence[str]]
    EqExactMatch: Optional[Sequence[str]]
    Field: Optional[str]
    Gt: Optional[str]
    Gte: Optional[str]
    Lt: Optional[str]
    Lte: Optional[str]
    Neq: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CriterionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriterionDefinition"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            EqExactMatch=json_data.get("EqExactMatch"),
            Field=json_data.get("Field"),
            Gt=json_data.get("Gt"),
            Gte=json_data.get("Gte"),
            Lt=json_data.get("Lt"),
            Lte=json_data.get("Lte"),
            Neq=json_data.get("Neq"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriterionDefinition = CriterionDefinition


