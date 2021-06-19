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
    AppServiceType: Optional[str]
    Category: Optional[str]
    CheckResetRange: Optional[str]
    Color: Optional[float]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Fqdn: Optional[str]
    Helper: Optional[str]
    Icmpcode: Optional[float]
    Icmptype: Optional[float]
    Id: Optional[str]
    Iprange: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    ProtocolNumber: Optional[float]
    Proxy: Optional[str]
    SctpPortrange: Optional[str]
    SessionTtl: Optional[float]
    TcpHalfcloseTimer: Optional[float]
    TcpHalfopenTimer: Optional[float]
    TcpPortrange: Optional[str]
    TcpTimewaitTimer: Optional[float]
    UdpIdleTimer: Optional[float]
    UdpPortrange: Optional[str]
    Vdomparam: Optional[str]
    Visibility: Optional[str]
    AppCategory: Optional[Sequence["_AppCategoryDefinition"]]
    Application: Optional[Sequence["_ApplicationDefinition"]]

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
            AppServiceType=json_data.get("AppServiceType"),
            Category=json_data.get("Category"),
            CheckResetRange=json_data.get("CheckResetRange"),
            Color=json_data.get("Color"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Fqdn=json_data.get("Fqdn"),
            Helper=json_data.get("Helper"),
            Icmpcode=json_data.get("Icmpcode"),
            Icmptype=json_data.get("Icmptype"),
            Id=json_data.get("Id"),
            Iprange=json_data.get("Iprange"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            ProtocolNumber=json_data.get("ProtocolNumber"),
            Proxy=json_data.get("Proxy"),
            SctpPortrange=json_data.get("SctpPortrange"),
            SessionTtl=json_data.get("SessionTtl"),
            TcpHalfcloseTimer=json_data.get("TcpHalfcloseTimer"),
            TcpHalfopenTimer=json_data.get("TcpHalfopenTimer"),
            TcpPortrange=json_data.get("TcpPortrange"),
            TcpTimewaitTimer=json_data.get("TcpTimewaitTimer"),
            UdpIdleTimer=json_data.get("UdpIdleTimer"),
            UdpPortrange=json_data.get("UdpPortrange"),
            Vdomparam=json_data.get("Vdomparam"),
            Visibility=json_data.get("Visibility"),
            AppCategory=deserialize_list(json_data.get("AppCategory"), AppCategoryDefinition),
            Application=deserialize_list(json_data.get("Application"), ApplicationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppCategoryDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AppCategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppCategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppCategoryDefinition = AppCategoryDefinition


@dataclass
class ApplicationDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationDefinition = ApplicationDefinition


