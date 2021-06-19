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
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    GroupType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    Admin: Optional[Sequence["_AdminDefinition"]]
    Alertmail: Optional[Sequence["_AlertmailDefinition"]]
    Auth: Optional[Sequence["_AuthDefinition"]]
    Automation: Optional[Sequence["_AutomationDefinition"]]
    CustomMessage: Optional[Sequence["_CustomMessageDefinition"]]
    DeviceDetectionPortal: Optional[Sequence["_DeviceDetectionPortalDefinition"]]
    Ec: Optional[Sequence["_EcDefinition"]]
    FortiguardWf: Optional[Sequence["_FortiguardWfDefinition"]]
    Ftp: Optional[Sequence["_FtpDefinition"]]
    Http: Optional[Sequence["_HttpDefinition"]]
    Icap: Optional[Sequence["_IcapDefinition"]]
    Mail: Optional[Sequence["_MailDefinition"]]
    NacQuar: Optional[Sequence["_NacQuarDefinition"]]
    Nntp: Optional[Sequence["_NntpDefinition"]]
    Spam: Optional[Sequence["_SpamDefinition"]]
    Sslvpn: Optional[Sequence["_SslvpnDefinition"]]
    TrafficQuota: Optional[Sequence["_TrafficQuotaDefinition"]]
    Utm: Optional[Sequence["_UtmDefinition"]]
    Webproxy: Optional[Sequence["_WebproxyDefinition"]]

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
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            GroupType=json_data.get("GroupType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Admin=deserialize_list(json_data.get("Admin"), AdminDefinition),
            Alertmail=deserialize_list(json_data.get("Alertmail"), AlertmailDefinition),
            Auth=deserialize_list(json_data.get("Auth"), AuthDefinition),
            Automation=deserialize_list(json_data.get("Automation"), AutomationDefinition),
            CustomMessage=deserialize_list(json_data.get("CustomMessage"), CustomMessageDefinition),
            DeviceDetectionPortal=deserialize_list(json_data.get("DeviceDetectionPortal"), DeviceDetectionPortalDefinition),
            Ec=deserialize_list(json_data.get("Ec"), EcDefinition),
            FortiguardWf=deserialize_list(json_data.get("FortiguardWf"), FortiguardWfDefinition),
            Ftp=deserialize_list(json_data.get("Ftp"), FtpDefinition),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
            Icap=deserialize_list(json_data.get("Icap"), IcapDefinition),
            Mail=deserialize_list(json_data.get("Mail"), MailDefinition),
            NacQuar=deserialize_list(json_data.get("NacQuar"), NacQuarDefinition),
            Nntp=deserialize_list(json_data.get("Nntp"), NntpDefinition),
            Spam=deserialize_list(json_data.get("Spam"), SpamDefinition),
            Sslvpn=deserialize_list(json_data.get("Sslvpn"), SslvpnDefinition),
            TrafficQuota=deserialize_list(json_data.get("TrafficQuota"), TrafficQuotaDefinition),
            Utm=deserialize_list(json_data.get("Utm"), UtmDefinition),
            Webproxy=deserialize_list(json_data.get("Webproxy"), WebproxyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdminDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdminDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminDefinition = AdminDefinition


@dataclass
class AlertmailDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlertmailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertmailDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertmailDefinition = AlertmailDefinition


@dataclass
class AuthDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthDefinition = AuthDefinition


@dataclass
class AutomationDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutomationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomationDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomationDefinition = AutomationDefinition


@dataclass
class CustomMessageDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomMessageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomMessageDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomMessageDefinition = CustomMessageDefinition


@dataclass
class DeviceDetectionPortalDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceDetectionPortalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceDetectionPortalDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceDetectionPortalDefinition = DeviceDetectionPortalDefinition


@dataclass
class EcDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcDefinition = EcDefinition


@dataclass
class FortiguardWfDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FortiguardWfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FortiguardWfDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FortiguardWfDefinition = FortiguardWfDefinition


@dataclass
class FtpDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FtpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FtpDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FtpDefinition = FtpDefinition


@dataclass
class HttpDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class IcapDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IcapDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcapDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcapDefinition = IcapDefinition


@dataclass
class MailDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MailDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MailDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MailDefinition = MailDefinition


@dataclass
class NacQuarDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NacQuarDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NacQuarDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NacQuarDefinition = NacQuarDefinition


@dataclass
class NntpDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NntpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NntpDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NntpDefinition = NntpDefinition


@dataclass
class SpamDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpamDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpamDefinition = SpamDefinition


@dataclass
class SslvpnDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslvpnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslvpnDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslvpnDefinition = SslvpnDefinition


@dataclass
class TrafficQuotaDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficQuotaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficQuotaDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficQuotaDefinition = TrafficQuotaDefinition


@dataclass
class UtmDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UtmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UtmDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UtmDefinition = UtmDefinition


@dataclass
class WebproxyDefinition(BaseModel):
    Buffer: Optional[str]
    Format: Optional[str]
    Header: Optional[str]
    MsgType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebproxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebproxyDefinition"]:
        if not json_data:
            return None
        return cls(
            Buffer=json_data.get("Buffer"),
            Format=json_data.get("Format"),
            Header=json_data.get("Header"),
            MsgType=json_data.get("MsgType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebproxyDefinition = WebproxyDefinition


