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
    ApplicationObject: Optional[str]
    Comment: Optional[str]
    DeviceGroup: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrderedMatch: Optional[bool]
    Scope: Optional[str]
    AndCondition: Optional[Sequence["_AndCondition"]]
    OrCondition: Optional[Sequence["_OrCondition"]]
    EqualTo: Optional[Sequence["_EqualTo"]]
    GreaterThan: Optional[Sequence["_GreaterThan"]]
    LessThan: Optional[Sequence["_LessThan"]]
    PatternMatch: Optional[Sequence["_PatternMatch"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApplicationObject=json_data.get("ApplicationObject"),
            Comment=json_data.get("Comment"),
            DeviceGroup=json_data.get("DeviceGroup"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrderedMatch=json_data.get("OrderedMatch"),
            Scope=json_data.get("Scope"),
            AndCondition=json_data.get("AndCondition"),
            OrCondition=json_data.get("OrCondition"),
            EqualTo=json_data.get("EqualTo"),
            GreaterThan=json_data.get("GreaterThan"),
            LessThan=json_data.get("LessThan"),
            PatternMatch=json_data.get("PatternMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AndCondition:
    OrCondition: Optional[Sequence["_OrCondition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AndCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AndCondition"]:
        if not json_data:
            return None
        return cls(
            OrCondition=json_data.get("OrCondition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AndCondition = AndCondition


@dataclass
class OrCondition:
    EqualTo: Optional[Sequence["_EqualTo"]]
    GreaterThan: Optional[Sequence["_GreaterThan"]]
    LessThan: Optional[Sequence["_LessThan"]]
    PatternMatch: Optional[Sequence["_PatternMatch"]]

    @classmethod
    def _deserialize(
        cls: Type["_OrCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrCondition"]:
        if not json_data:
            return None
        return cls(
            EqualTo=json_data.get("EqualTo"),
            GreaterThan=json_data.get("GreaterThan"),
            LessThan=json_data.get("LessThan"),
            PatternMatch=json_data.get("PatternMatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrCondition = OrCondition


@dataclass
class EqualTo:
    Context: Optional[str]
    Mask: Optional[str]
    Position: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EqualTo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EqualTo"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Mask=json_data.get("Mask"),
            Position=json_data.get("Position"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EqualTo = EqualTo


@dataclass
class GreaterThan:
    Context: Optional[str]
    Qualifiers: Optional[Sequence["_Qualifiers"]]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GreaterThan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GreaterThan"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Qualifiers=json_data.get("Qualifiers"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GreaterThan = GreaterThan


@dataclass
class Qualifiers:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Qualifiers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Qualifiers"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Qualifiers = Qualifiers


@dataclass
class LessThan:
    Context: Optional[str]
    Qualifiers: Optional[Sequence["_Qualifiers2"]]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LessThan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LessThan"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Qualifiers=json_data.get("Qualifiers"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LessThan = LessThan


@dataclass
class Qualifiers2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Qualifiers2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Qualifiers2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Qualifiers2 = Qualifiers2


@dataclass
class PatternMatch:
    Context: Optional[str]
    Pattern: Optional[str]
    Qualifiers: Optional[Sequence["_Qualifiers3"]]

    @classmethod
    def _deserialize(
        cls: Type["_PatternMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatternMatch"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            Pattern=json_data.get("Pattern"),
            Qualifiers=json_data.get("Qualifiers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatternMatch = PatternMatch


@dataclass
class Qualifiers3:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Qualifiers3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Qualifiers3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Qualifiers3 = Qualifiers3


