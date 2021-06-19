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
    Logstore: Optional[str]
    Project: Optional[str]
    FieldSearch: Optional[Sequence["_FieldSearchDefinition"]]
    FullText: Optional[Sequence["_FullTextDefinition"]]

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
            Logstore=json_data.get("Logstore"),
            Project=json_data.get("Project"),
            FieldSearch=deserialize_list(json_data.get("FieldSearch"), FieldSearchDefinition),
            FullText=deserialize_list(json_data.get("FullText"), FullTextDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FieldSearchDefinition(BaseModel):
    Alias: Optional[str]
    CaseSensitive: Optional[bool]
    EnableAnalytics: Optional[bool]
    IncludeChinese: Optional[bool]
    Name: Optional[str]
    Token: Optional[str]
    Type: Optional[str]
    JsonKeys: Optional[Sequence["_JsonKeysDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FieldSearchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldSearchDefinition"]:
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
            JsonKeys=deserialize_list(json_data.get("JsonKeys"), JsonKeysDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldSearchDefinition = FieldSearchDefinition


@dataclass
class JsonKeysDefinition(BaseModel):
    Alias: Optional[str]
    DocValue: Optional[bool]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            DocValue=json_data.get("DocValue"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonKeysDefinition = JsonKeysDefinition


@dataclass
class FullTextDefinition(BaseModel):
    CaseSensitive: Optional[bool]
    IncludeChinese: Optional[bool]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FullTextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FullTextDefinition"]:
        if not json_data:
            return None
        return cls(
            CaseSensitive=json_data.get("CaseSensitive"),
            IncludeChinese=json_data.get("IncludeChinese"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FullTextDefinition = FullTextDefinition


