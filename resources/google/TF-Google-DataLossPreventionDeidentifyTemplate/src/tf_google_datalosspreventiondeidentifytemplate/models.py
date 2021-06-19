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
    DisplayName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Parent: Optional[str]
    DeidentifyConfig: Optional[Sequence["_DeidentifyConfigDefinition"]]
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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Parent=json_data.get("Parent"),
            DeidentifyConfig=deserialize_list(json_data.get("DeidentifyConfig"), DeidentifyConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeidentifyConfigDefinition(BaseModel):
    InfoTypeTransformations: Optional[Sequence["_InfoTypeTransformationsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeidentifyConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeidentifyConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            InfoTypeTransformations=deserialize_list(json_data.get("InfoTypeTransformations"), InfoTypeTransformationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeidentifyConfigDefinition = DeidentifyConfigDefinition


@dataclass
class InfoTypeTransformationsDefinition(BaseModel):
    Transformations: Optional[Sequence["_TransformationsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InfoTypeTransformationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfoTypeTransformationsDefinition"]:
        if not json_data:
            return None
        return cls(
            Transformations=deserialize_list(json_data.get("Transformations"), TransformationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfoTypeTransformationsDefinition = InfoTypeTransformationsDefinition


@dataclass
class TransformationsDefinition(BaseModel):
    InfoTypes: Optional[Sequence["_InfoTypesDefinition"]]
    PrimitiveTransformation: Optional[Sequence["_PrimitiveTransformationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TransformationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformationsDefinition"]:
        if not json_data:
            return None
        return cls(
            InfoTypes=deserialize_list(json_data.get("InfoTypes"), InfoTypesDefinition),
            PrimitiveTransformation=deserialize_list(json_data.get("PrimitiveTransformation"), PrimitiveTransformationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformationsDefinition = TransformationsDefinition


@dataclass
class InfoTypesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InfoTypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InfoTypesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InfoTypesDefinition = InfoTypesDefinition


@dataclass
class PrimitiveTransformationDefinition(BaseModel):
    CharacterMaskConfig: Optional[Sequence["_CharacterMaskConfigDefinition"]]
    ReplaceConfig: Optional[Sequence["_ReplaceConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrimitiveTransformationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrimitiveTransformationDefinition"]:
        if not json_data:
            return None
        return cls(
            CharacterMaskConfig=deserialize_list(json_data.get("CharacterMaskConfig"), CharacterMaskConfigDefinition),
            ReplaceConfig=deserialize_list(json_data.get("ReplaceConfig"), ReplaceConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrimitiveTransformationDefinition = PrimitiveTransformationDefinition


@dataclass
class CharacterMaskConfigDefinition(BaseModel):
    MaskingCharacter: Optional[str]
    NumberToMask: Optional[float]
    ReverseOrder: Optional[bool]
    CharactersToIgnore: Optional[Sequence["_CharactersToIgnoreDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CharacterMaskConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CharacterMaskConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MaskingCharacter=json_data.get("MaskingCharacter"),
            NumberToMask=json_data.get("NumberToMask"),
            ReverseOrder=json_data.get("ReverseOrder"),
            CharactersToIgnore=deserialize_list(json_data.get("CharactersToIgnore"), CharactersToIgnoreDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CharacterMaskConfigDefinition = CharacterMaskConfigDefinition


@dataclass
class CharactersToIgnoreDefinition(BaseModel):
    CharacterToSkip: Optional[str]
    CommonCharactersToIgnore: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CharactersToIgnoreDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CharactersToIgnoreDefinition"]:
        if not json_data:
            return None
        return cls(
            CharacterToSkip=json_data.get("CharacterToSkip"),
            CommonCharactersToIgnore=json_data.get("CommonCharactersToIgnore"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CharactersToIgnoreDefinition = CharactersToIgnoreDefinition


@dataclass
class ReplaceConfigDefinition(BaseModel):
    NewValue: Optional[Sequence["_NewValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplaceConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplaceConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            NewValue=deserialize_list(json_data.get("NewValue"), NewValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplaceConfigDefinition = ReplaceConfigDefinition


@dataclass
class NewValueDefinition(BaseModel):
    BooleanValue: Optional[bool]
    DayOfWeekValue: Optional[str]
    FloatValue: Optional[float]
    IntegerValue: Optional[float]
    StringValue: Optional[str]
    TimestampValue: Optional[str]
    DateValue: Optional[Sequence["_DateValueDefinition"]]
    TimeValue: Optional[Sequence["_TimeValueDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NewValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NewValueDefinition"]:
        if not json_data:
            return None
        return cls(
            BooleanValue=json_data.get("BooleanValue"),
            DayOfWeekValue=json_data.get("DayOfWeekValue"),
            FloatValue=json_data.get("FloatValue"),
            IntegerValue=json_data.get("IntegerValue"),
            StringValue=json_data.get("StringValue"),
            TimestampValue=json_data.get("TimestampValue"),
            DateValue=deserialize_list(json_data.get("DateValue"), DateValueDefinition),
            TimeValue=deserialize_list(json_data.get("TimeValue"), TimeValueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NewValueDefinition = NewValueDefinition


@dataclass
class DateValueDefinition(BaseModel):
    Day: Optional[float]
    Month: Optional[float]
    Year: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DateValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Month=json_data.get("Month"),
            Year=json_data.get("Year"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateValueDefinition = DateValueDefinition


@dataclass
class TimeValueDefinition(BaseModel):
    Hours: Optional[float]
    Minutes: Optional[float]
    Nanos: Optional[float]
    Seconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Hours=json_data.get("Hours"),
            Minutes=json_data.get("Minutes"),
            Nanos=json_data.get("Nanos"),
            Seconds=json_data.get("Seconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeValueDefinition = TimeValueDefinition


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


