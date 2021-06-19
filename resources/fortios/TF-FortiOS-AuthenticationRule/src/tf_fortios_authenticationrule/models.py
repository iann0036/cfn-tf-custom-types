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
    ActiveAuthMethod: Optional[str]
    Comments: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    IpBased: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    SsoAuthMethod: Optional[str]
    Status: Optional[str]
    TransactionBased: Optional[str]
    Vdomparam: Optional[str]
    WebAuthCookie: Optional[str]
    WebPortal: Optional[str]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Srcaddr: Optional[Sequence["_SrcaddrDefinition"]]
    Srcaddr6: Optional[Sequence["_Srcaddr6Definition"]]
    Srcintf: Optional[Sequence["_SrcintfDefinition"]]

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
            ActiveAuthMethod=json_data.get("ActiveAuthMethod"),
            Comments=json_data.get("Comments"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            IpBased=json_data.get("IpBased"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            SsoAuthMethod=json_data.get("SsoAuthMethod"),
            Status=json_data.get("Status"),
            TransactionBased=json_data.get("TransactionBased"),
            Vdomparam=json_data.get("Vdomparam"),
            WebAuthCookie=json_data.get("WebAuthCookie"),
            WebPortal=json_data.get("WebPortal"),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
            Srcaddr6=deserialize_list(json_data.get("Srcaddr6"), Srcaddr6Definition),
            Srcintf=deserialize_list(json_data.get("Srcintf"), SrcintfDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class SrcaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcaddrDefinition = SrcaddrDefinition


@dataclass
class Srcaddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Srcaddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Srcaddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Srcaddr6Definition = Srcaddr6Definition


@dataclass
class SrcintfDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcintfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcintfDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcintfDefinition = SrcintfDefinition


