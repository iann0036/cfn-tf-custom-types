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
    ApplicationObject: Optional[str]
    Comment: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrderedMatch: Optional[bool]
    Scope: Optional[str]
    Vsys: Optional[str]
    AndCondition: Optional[Sequence["_AndConditionDefinition"]]

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
            ApplicationObject=json_data.get("ApplicationObject"),
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrderedMatch=json_data.get("OrderedMatch"),
            Scope=json_data.get("Scope"),
            Vsys=json_data.get("Vsys"),
            AndCondition=deserialize_list(json_data.get("AndCondition"), AndConditionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AndConditionDefinition(BaseModel):
    OrCondition: Optional[Sequence["_OrConditionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AndConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AndConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            OrCondition=deserialize_list(json_data.get("OrCondition"), OrConditionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AndConditionDefinition = AndConditionDefinition


@dataclass
class OrConditionDefinition(BaseModel):
    EqualTo: Optional[Sequence["_EqualToDefinition"]]
    GreaterThan: Optional[Sequence["_GreaterThanDefinition"]]
    LessThan: Optional[Sequence["_LessThanDefinition"]]
    PatternMatch: Optional[Sequence["_PatternMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OrConditionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrConditionDefinition"]:
        if not json_data:
            return None
        return cls(
            EqualTo=deserialize_list(json_data.get("EqualTo"), EqualToDefinition),
            GreaterThan=deserialize_list(json_data.get("GreaterThan"), GreaterThanDefinition),
            LessThan=deserialize_list(json_data.get("LessThan"), LessThanDefinition),
            PatternMatch=deserialize_list(json_data.get("PatternMatch"), PatternMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrConditionDefinition = OrConditionDefinition


@dataclass
class EqualToDefinition(BaseModel):
    Context: Optional[str]
    Mask: Optional[str]
    Position: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EqualToDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EqualToDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Mask=json_data.get("Mask"),
            Position=json_data.get("Position"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EqualToDefinition = EqualToDefinition


@dataclass
class GreaterThanDefinition(BaseModel):
    Context: Optional[str]
    Qualifiers: Optional[Sequence["_QualifiersDefinition"]]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GreaterThanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GreaterThanDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Qualifiers=deserialize_list(json_data.get("Qualifiers"), QualifiersDefinition),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GreaterThanDefinition = GreaterThanDefinition


@dataclass
class QualifiersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QualifiersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QualifiersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QualifiersDefinition = QualifiersDefinition


@dataclass
class LessThanDefinition(BaseModel):
    Context: Optional[str]
    Qualifiers: Optional[Sequence["_QualifiersDefinition2"]]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LessThanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LessThanDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Qualifiers=deserialize_list(json_data.get("Qualifiers"), QualifiersDefinition2),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LessThanDefinition = LessThanDefinition


@dataclass
class QualifiersDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QualifiersDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QualifiersDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QualifiersDefinition2 = QualifiersDefinition2


@dataclass
class PatternMatchDefinition(BaseModel):
    Context: Optional[str]
    Pattern: Optional[str]
    Qualifiers: Optional[Sequence["_QualifiersDefinition3"]]

    @classmethod
    def _deserialize(
        cls: Type["_PatternMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatternMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Pattern=json_data.get("Pattern"),
            Qualifiers=deserialize_list(json_data.get("Qualifiers"), QualifiersDefinition3),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatternMatchDefinition = PatternMatchDefinition


@dataclass
class QualifiersDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QualifiersDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QualifiersDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QualifiersDefinition3 = QualifiersDefinition3


