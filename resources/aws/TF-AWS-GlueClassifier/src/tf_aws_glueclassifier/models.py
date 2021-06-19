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
    CsvClassifier: Optional[Sequence["_CsvClassifierDefinition"]]
    GrokClassifier: Optional[Sequence["_GrokClassifierDefinition"]]
    JsonClassifier: Optional[Sequence["_JsonClassifierDefinition"]]
    XmlClassifier: Optional[Sequence["_XmlClassifierDefinition"]]

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
            CsvClassifier=deserialize_list(json_data.get("CsvClassifier"), CsvClassifierDefinition),
            GrokClassifier=deserialize_list(json_data.get("GrokClassifier"), GrokClassifierDefinition),
            JsonClassifier=deserialize_list(json_data.get("JsonClassifier"), JsonClassifierDefinition),
            XmlClassifier=deserialize_list(json_data.get("XmlClassifier"), XmlClassifierDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CsvClassifierDefinition(BaseModel):
    AllowSingleColumn: Optional[bool]
    ContainsHeader: Optional[str]
    Delimiter: Optional[str]
    DisableValueTrimming: Optional[bool]
    Header: Optional[Sequence[str]]
    QuoteSymbol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CsvClassifierDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvClassifierDefinition"]:
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
_CsvClassifierDefinition = CsvClassifierDefinition


@dataclass
class GrokClassifierDefinition(BaseModel):
    Classification: Optional[str]
    CustomPatterns: Optional[str]
    GrokPattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GrokClassifierDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrokClassifierDefinition"]:
        if not json_data:
            return None
        return cls(
            Classification=json_data.get("Classification"),
            CustomPatterns=json_data.get("CustomPatterns"),
            GrokPattern=json_data.get("GrokPattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrokClassifierDefinition = GrokClassifierDefinition


@dataclass
class JsonClassifierDefinition(BaseModel):
    JsonPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonClassifierDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonClassifierDefinition"]:
        if not json_data:
            return None
        return cls(
            JsonPath=json_data.get("JsonPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonClassifierDefinition = JsonClassifierDefinition


@dataclass
class XmlClassifierDefinition(BaseModel):
    Classification: Optional[str]
    RowTag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_XmlClassifierDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XmlClassifierDefinition"]:
        if not json_data:
            return None
        return cls(
            Classification=json_data.get("Classification"),
            RowTag=json_data.get("RowTag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XmlClassifierDefinition = XmlClassifierDefinition


