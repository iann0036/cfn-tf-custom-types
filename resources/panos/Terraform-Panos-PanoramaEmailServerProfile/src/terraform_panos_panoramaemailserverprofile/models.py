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
    AuthFormat: Optional[str]
    ConfigFormat: Optional[str]
    DataFormat: Optional[str]
    DeviceGroup: Optional[str]
    EscapeCharacter: Optional[str]
    EscapedCharacters: Optional[str]
    GtpFormat: Optional[str]
    HipMatchFormat: Optional[str]
    IptagFormat: Optional[str]
    Name: Optional[str]
    SctpFormat: Optional[str]
    SystemFormat: Optional[str]
    Template: Optional[str]
    TemplateStack: Optional[str]
    ThreatFormat: Optional[str]
    TrafficFormat: Optional[str]
    TunnelFormat: Optional[str]
    UrlFormat: Optional[str]
    UserIdFormat: Optional[str]
    Vsys: Optional[str]
    WildfireFormat: Optional[str]
    EmailServer: Optional[Sequence["_EmailServer"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AuthFormat=json_data.get("AuthFormat"),
            ConfigFormat=json_data.get("ConfigFormat"),
            DataFormat=json_data.get("DataFormat"),
            DeviceGroup=json_data.get("DeviceGroup"),
            EscapeCharacter=json_data.get("EscapeCharacter"),
            EscapedCharacters=json_data.get("EscapedCharacters"),
            GtpFormat=json_data.get("GtpFormat"),
            HipMatchFormat=json_data.get("HipMatchFormat"),
            IptagFormat=json_data.get("IptagFormat"),
            Name=json_data.get("Name"),
            SctpFormat=json_data.get("SctpFormat"),
            SystemFormat=json_data.get("SystemFormat"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            ThreatFormat=json_data.get("ThreatFormat"),
            TrafficFormat=json_data.get("TrafficFormat"),
            TunnelFormat=json_data.get("TunnelFormat"),
            UrlFormat=json_data.get("UrlFormat"),
            UserIdFormat=json_data.get("UserIdFormat"),
            Vsys=json_data.get("Vsys"),
            WildfireFormat=json_data.get("WildfireFormat"),
            EmailServer=json_data.get("EmailServer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EmailServer:
    AlsoToEmail: Optional[str]
    DisplayName: Optional[str]
    EmailGateway: Optional[str]
    FromEmail: Optional[str]
    Name: Optional[str]
    ToEmail: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailServer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailServer"]:
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
_EmailServer = EmailServer


