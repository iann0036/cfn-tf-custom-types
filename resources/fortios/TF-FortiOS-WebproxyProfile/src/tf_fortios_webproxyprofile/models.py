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
    DynamicSortSubtable: Optional[str]
    HeaderClientIp: Optional[str]
    HeaderFrontEndHttps: Optional[str]
    HeaderViaRequest: Optional[str]
    HeaderViaResponse: Optional[str]
    HeaderXAuthenticatedGroups: Optional[str]
    HeaderXAuthenticatedUser: Optional[str]
    HeaderXForwardedFor: Optional[str]
    Id: Optional[str]
    LogHeaderChange: Optional[str]
    Name: Optional[str]
    StripEncoding: Optional[str]
    Vdomparam: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            HeaderClientIp=json_data.get("HeaderClientIp"),
            HeaderFrontEndHttps=json_data.get("HeaderFrontEndHttps"),
            HeaderViaRequest=json_data.get("HeaderViaRequest"),
            HeaderViaResponse=json_data.get("HeaderViaResponse"),
            HeaderXAuthenticatedGroups=json_data.get("HeaderXAuthenticatedGroups"),
            HeaderXAuthenticatedUser=json_data.get("HeaderXAuthenticatedUser"),
            HeaderXForwardedFor=json_data.get("HeaderXForwardedFor"),
            Id=json_data.get("Id"),
            LogHeaderChange=json_data.get("LogHeaderChange"),
            Name=json_data.get("Name"),
            StripEncoding=json_data.get("StripEncoding"),
            Vdomparam=json_data.get("Vdomparam"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HeadersDefinition(BaseModel):
    Action: Optional[str]
    AddOption: Optional[str]
    Base64Encoding: Optional[str]
    Content: Optional[str]
    Id: Optional[float]
    Name: Optional[str]
    Protocol: Optional[str]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Dstaddr6: Optional[Sequence["_Dstaddr6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AddOption=json_data.get("AddOption"),
            Base64Encoding=json_data.get("Base64Encoding"),
            Content=json_data.get("Content"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Dstaddr6=deserialize_list(json_data.get("Dstaddr6"), Dstaddr6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class DstaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstaddrDefinition = DstaddrDefinition


@dataclass
class Dstaddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dstaddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dstaddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dstaddr6Definition = Dstaddr6Definition


