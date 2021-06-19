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
    Content: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    KvNamespaceBinding: Optional[Sequence["_KvNamespaceBindingDefinition"]]
    PlainTextBinding: Optional[Sequence["_PlainTextBindingDefinition"]]
    SecretTextBinding: Optional[Sequence["_SecretTextBindingDefinition"]]
    WebassemblyBinding: Optional[Sequence["_WebassemblyBindingDefinition"]]

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
            Content=json_data.get("Content"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            KvNamespaceBinding=deserialize_list(json_data.get("KvNamespaceBinding"), KvNamespaceBindingDefinition),
            PlainTextBinding=deserialize_list(json_data.get("PlainTextBinding"), PlainTextBindingDefinition),
            SecretTextBinding=deserialize_list(json_data.get("SecretTextBinding"), SecretTextBindingDefinition),
            WebassemblyBinding=deserialize_list(json_data.get("WebassemblyBinding"), WebassemblyBindingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KvNamespaceBindingDefinition(BaseModel):
    Name: Optional[str]
    NamespaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KvNamespaceBindingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KvNamespaceBindingDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            NamespaceId=json_data.get("NamespaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KvNamespaceBindingDefinition = KvNamespaceBindingDefinition


@dataclass
class PlainTextBindingDefinition(BaseModel):
    Name: Optional[str]
    Text: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlainTextBindingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlainTextBindingDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Text=json_data.get("Text"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlainTextBindingDefinition = PlainTextBindingDefinition


@dataclass
class SecretTextBindingDefinition(BaseModel):
    Name: Optional[str]
    Text: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretTextBindingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretTextBindingDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Text=json_data.get("Text"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretTextBindingDefinition = SecretTextBindingDefinition


@dataclass
class WebassemblyBindingDefinition(BaseModel):
    Module: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebassemblyBindingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebassemblyBindingDefinition"]:
        if not json_data:
            return None
        return cls(
            Module=json_data.get("Module"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebassemblyBindingDefinition = WebassemblyBindingDefinition


