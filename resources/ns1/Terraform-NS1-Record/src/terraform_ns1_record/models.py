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
    Domain: Optional[str]
    Id: Optional[str]
    Link: Optional[str]
    Meta: Optional[Sequence["_Meta"]]
    ShortAnswers: Optional[Sequence[str]]
    Ttl: Optional[float]
    Type: Optional[str]
    UseClientSubnet: Optional[bool]
    Zone: Optional[str]
    Answers: Optional[Sequence["_Answers"]]
    Filters: Optional[Sequence["_Filters"]]
    Regions: Optional[Sequence["_Regions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            Link=json_data.get("Link"),
            Meta=json_data.get("Meta"),
            ShortAnswers=json_data.get("ShortAnswers"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            UseClientSubnet=json_data.get("UseClientSubnet"),
            Zone=json_data.get("Zone"),
            Answers=json_data.get("Answers"),
            Filters=json_data.get("Filters"),
            Regions=json_data.get("Regions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Meta:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Meta"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Meta"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Meta = Meta


@dataclass
class Answers:
    Answer: Optional[str]
    Meta: Optional[Sequence["_Meta2"]]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Answers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Answers"]:
        if not json_data:
            return None
        return cls(
            Answer=json_data.get("Answer"),
            Meta=json_data.get("Meta"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Answers = Answers


@dataclass
class Meta2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Meta2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Meta2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Meta2 = Meta2


@dataclass
class Filters:
    Config: Optional[Sequence["_Config"]]
    Disabled: Optional[bool]
    Filter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filters"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Disabled=json_data.get("Disabled"),
            Filter=json_data.get("Filter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filters = Filters


@dataclass
class Config:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Config"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Config = Config


@dataclass
class Regions:
    Meta: Optional[Sequence["_Meta3"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Regions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Regions"]:
        if not json_data:
            return None
        return cls(
            Meta=json_data.get("Meta"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Regions = Regions


@dataclass
class Meta3:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Meta3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Meta3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Meta3 = Meta3


