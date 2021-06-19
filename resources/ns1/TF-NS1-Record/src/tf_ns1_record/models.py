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
    Domain: Optional[str]
    Id: Optional[str]
    Link: Optional[str]
    Meta: Optional[Sequence["_MetaDefinition"]]
    ShortAnswers: Optional[Sequence[str]]
    Ttl: Optional[float]
    Type: Optional[str]
    UseClientSubnet: Optional[bool]
    Zone: Optional[str]
    Answers: Optional[Sequence["_AnswersDefinition"]]
    Filters: Optional[Sequence["_FiltersDefinition"]]
    Regions: Optional[Sequence["_RegionsDefinition"]]

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
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            Link=json_data.get("Link"),
            Meta=deserialize_list(json_data.get("Meta"), MetaDefinition),
            ShortAnswers=json_data.get("ShortAnswers"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            UseClientSubnet=json_data.get("UseClientSubnet"),
            Zone=json_data.get("Zone"),
            Answers=deserialize_list(json_data.get("Answers"), AnswersDefinition),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
            Regions=deserialize_list(json_data.get("Regions"), RegionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetaDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetaDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetaDefinition = MetaDefinition


@dataclass
class AnswersDefinition(BaseModel):
    Answer: Optional[str]
    Meta: Optional[Sequence["_MetaDefinition2"]]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnswersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnswersDefinition"]:
        if not json_data:
            return None
        return cls(
            Answer=json_data.get("Answer"),
            Meta=deserialize_list(json_data.get("Meta"), MetaDefinition2),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnswersDefinition = AnswersDefinition


@dataclass
class MetaDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetaDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetaDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetaDefinition2 = MetaDefinition2


@dataclass
class FiltersDefinition(BaseModel):
    Config: Optional[Sequence["_ConfigDefinition"]]
    Disabled: Optional[bool]
    Filter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Disabled=json_data.get("Disabled"),
            Filter=json_data.get("Filter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


@dataclass
class ConfigDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class RegionsDefinition(BaseModel):
    Meta: Optional[Sequence["_MetaDefinition3"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Meta=deserialize_list(json_data.get("Meta"), MetaDefinition3),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionsDefinition = RegionsDefinition


@dataclass
class MetaDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetaDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetaDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetaDefinition3 = MetaDefinition3


