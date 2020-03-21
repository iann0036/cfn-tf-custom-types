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
    Id: Optional[str]
    Name: Optional[str]
    CsvClassifier: Optional[Sequence["_CsvClassifier"]]
    GrokClassifier: Optional[Sequence["_GrokClassifier"]]
    JsonClassifier: Optional[Sequence["_JsonClassifier"]]
    XmlClassifier: Optional[Sequence["_XmlClassifier"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            CsvClassifier=json_data.get("CsvClassifier"),
            GrokClassifier=json_data.get("GrokClassifier"),
            JsonClassifier=json_data.get("JsonClassifier"),
            XmlClassifier=json_data.get("XmlClassifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CsvClassifier:
    AllowSingleColumn: Optional[bool]
    ContainsHeader: Optional[str]
    Delimiter: Optional[str]
    DisableValueTrimming: Optional[bool]
    Header: Optional[Sequence[str]]
    QuoteSymbol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CsvClassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvClassifier"]:
        if not json_data:
            return None
        return cls(
            AllowSingleColumn=json_data.get("AllowSingleColumn"),
            ContainsHeader=json_data.get("ContainsHeader"),
            Delimiter=json_data.get("Delimiter"),
            DisableValueTrimming=json_data.get("DisableValueTrimming"),
            Header=json_data.get("Header"),
            QuoteSymbol=json_data.get("QuoteSymbol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsvClassifier = CsvClassifier


@dataclass
class GrokClassifier:
    Classification: Optional[str]
    CustomPatterns: Optional[str]
    GrokPattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GrokClassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrokClassifier"]:
        if not json_data:
            return None
        return cls(
            Classification=json_data.get("Classification"),
            CustomPatterns=json_data.get("CustomPatterns"),
            GrokPattern=json_data.get("GrokPattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrokClassifier = GrokClassifier


@dataclass
class JsonClassifier:
    JsonPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonClassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonClassifier"]:
        if not json_data:
            return None
        return cls(
            JsonPath=json_data.get("JsonPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonClassifier = JsonClassifier


@dataclass
class XmlClassifier:
    Classification: Optional[str]
    RowTag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_XmlClassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XmlClassifier"]:
        if not json_data:
            return None
        return cls(
            Classification=json_data.get("Classification"),
            RowTag=json_data.get("RowTag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XmlClassifier = XmlClassifier


