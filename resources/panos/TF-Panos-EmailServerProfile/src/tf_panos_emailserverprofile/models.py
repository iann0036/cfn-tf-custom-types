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
    AuthFormat: Optional[str]
    ConfigFormat: Optional[str]
    DataFormat: Optional[str]
    EscapeCharacter: Optional[str]
    EscapedCharacters: Optional[str]
    GtpFormat: Optional[str]
    HipMatchFormat: Optional[str]
    Id: Optional[str]
    IptagFormat: Optional[str]
    Name: Optional[str]
    SctpFormat: Optional[str]
    SystemFormat: Optional[str]
    ThreatFormat: Optional[str]
    TrafficFormat: Optional[str]
    TunnelFormat: Optional[str]
    UrlFormat: Optional[str]
    UserIdFormat: Optional[str]
    Vsys: Optional[str]
    WildfireFormat: Optional[str]
    EmailServer: Optional[Sequence["_EmailServerDefinition"]]

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
            AuthFormat=json_data.get("AuthFormat"),
            ConfigFormat=json_data.get("ConfigFormat"),
            DataFormat=json_data.get("DataFormat"),
            EscapeCharacter=json_data.get("EscapeCharacter"),
            EscapedCharacters=json_data.get("EscapedCharacters"),
            GtpFormat=json_data.get("GtpFormat"),
            HipMatchFormat=json_data.get("HipMatchFormat"),
            Id=json_data.get("Id"),
            IptagFormat=json_data.get("IptagFormat"),
            Name=json_data.get("Name"),
            SctpFormat=json_data.get("SctpFormat"),
            SystemFormat=json_data.get("SystemFormat"),
            ThreatFormat=json_data.get("ThreatFormat"),
            TrafficFormat=json_data.get("TrafficFormat"),
            TunnelFormat=json_data.get("TunnelFormat"),
            UrlFormat=json_data.get("UrlFormat"),
            UserIdFormat=json_data.get("UserIdFormat"),
            Vsys=json_data.get("Vsys"),
            WildfireFormat=json_data.get("WildfireFormat"),
            EmailServer=deserialize_list(json_data.get("EmailServer"), EmailServerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EmailServerDefinition(BaseModel):
    AlsoToEmail: Optional[str]
    DisplayName: Optional[str]
    EmailGateway: Optional[str]
    FromEmail: Optional[str]
    Name: Optional[str]
    ToEmail: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailServerDefinition"]:
        if not json_data:
            return None
        return cls(
            AlsoToEmail=json_data.get("AlsoToEmail"),
            DisplayName=json_data.get("DisplayName"),
            EmailGateway=json_data.get("EmailGateway"),
            FromEmail=json_data.get("FromEmail"),
            Name=json_data.get("Name"),
            ToEmail=json_data.get("ToEmail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailServerDefinition = EmailServerDefinition


