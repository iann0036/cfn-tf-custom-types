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
    Logstore: Optional[str]
    Project: Optional[str]
    FieldSearch: Optional[Sequence["_FieldSearch"]]
    FullText: Optional[Sequence["_FullText"]]
    JsonKeys: Optional[Sequence["_JsonKeys"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Logstore=json_data.get("Logstore"),
            Project=json_data.get("Project"),
            FieldSearch=json_data.get("FieldSearch"),
            FullText=json_data.get("FullText"),
            JsonKeys=json_data.get("JsonKeys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FieldSearch:
    Alias: Optional[str]
    CaseSensitive: Optional[bool]
    EnableAnalytics: Optional[bool]
    IncludeChinese: Optional[bool]
    Name: Optional[str]
    Token: Optional[str]
    Type: Optional[str]
    JsonKeys: Optional[Sequence["_JsonKeys"]]

    @classmethod
    def _deserialize(
        cls: Type["_FieldSearch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldSearch"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            CaseSensitive=json_data.get("CaseSensitive"),
            EnableAnalytics=json_data.get("EnableAnalytics"),
            IncludeChinese=json_data.get("IncludeChinese"),
            Name=json_data.get("Name"),
            Token=json_data.get("Token"),
            Type=json_data.get("Type"),
            JsonKeys=json_data.get("JsonKeys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldSearch = FieldSearch


@dataclass
class JsonKeys:
    Alias: Optional[str]
    DocValue: Optional[bool]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonKeys"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonKeys"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            DocValue=json_data.get("DocValue"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonKeys = JsonKeys


@dataclass
class FullText:
    CaseSensitive: Optional[bool]
    IncludeChinese: Optional[bool]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FullText"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FullText"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            IncludeChinese=json_data.get("IncludeChinese"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FullText = FullText


