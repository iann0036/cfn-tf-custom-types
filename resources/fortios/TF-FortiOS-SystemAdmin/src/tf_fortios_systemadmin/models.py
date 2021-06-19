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
    Accprofile: Optional[str]
    AccprofileOverride: Optional[str]
    AllowRemoveAdminSession: Optional[str]
    Comments: Optional[str]
    DynamicSortSubtable: Optional[str]
    EmailTo: Optional[str]
    ForcePasswordChange: Optional[str]
    Fortitoken: Optional[str]
    GuestAuth: Optional[str]
    GuestLang: Optional[str]
    Hidden: Optional[float]
    History0: Optional[str]
    History1: Optional[str]
    Id: Optional[str]
    Ip6Trusthost1: Optional[str]
    Ip6Trusthost10: Optional[str]
    Ip6Trusthost2: Optional[str]
    Ip6Trusthost3: Optional[str]
    Ip6Trusthost4: Optional[str]
    Ip6Trusthost5: Optional[str]
    Ip6Trusthost6: Optional[str]
    Ip6Trusthost7: Optional[str]
    Ip6Trusthost8: Optional[str]
    Ip6Trusthost9: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    PasswordExpire: Optional[str]
    PeerAuth: Optional[str]
    PeerGroup: Optional[str]
    RadiusVdomOverride: Optional[str]
    RemoteAuth: Optional[str]
    RemoteGroup: Optional[str]
    Schedule: Optional[str]
    SmsCustomServer: Optional[str]
    SmsPhone: Optional[str]
    SmsServer: Optional[str]
    SshCertificate: Optional[str]
    SshPublicKey1: Optional[str]
    SshPublicKey2: Optional[str]
    SshPublicKey3: Optional[str]
    Trusthost1: Optional[str]
    Trusthost10: Optional[str]
    Trusthost2: Optional[str]
    Trusthost3: Optional[str]
    Trusthost4: Optional[str]
    Trusthost5: Optional[str]
    Trusthost6: Optional[str]
    Trusthost7: Optional[str]
    Trusthost8: Optional[str]
    Trusthost9: Optional[str]
    TwoFactor: Optional[str]
    TwoFactorAuthentication: Optional[str]
    TwoFactorNotification: Optional[str]
    Vdomparam: Optional[str]
    Wildcard: Optional[str]
    GuestUsergroups: Optional[Sequence["_GuestUsergroupsDefinition"]]
    GuiDashboard: Optional[Sequence["_GuiDashboardDefinition"]]
    GuiGlobalMenuFavorites: Optional[Sequence["_GuiGlobalMenuFavoritesDefinition"]]
    GuiNewFeatureAcknowledge: Optional[Sequence["_GuiNewFeatureAcknowledgeDefinition"]]
    GuiVdomMenuFavorites: Optional[Sequence["_GuiVdomMenuFavoritesDefinition"]]
    LoginTime: Optional[Sequence["_LoginTimeDefinition"]]
    Vdom: Optional[Sequence["_VdomDefinition"]]

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
            Accprofile=json_data.get("Accprofile"),
            AccprofileOverride=json_data.get("AccprofileOverride"),
            AllowRemoveAdminSession=json_data.get("AllowRemoveAdminSession"),
            Comments=json_data.get("Comments"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmailTo=json_data.get("EmailTo"),
            ForcePasswordChange=json_data.get("ForcePasswordChange"),
            Fortitoken=json_data.get("Fortitoken"),
            GuestAuth=json_data.get("GuestAuth"),
            GuestLang=json_data.get("GuestLang"),
            Hidden=json_data.get("Hidden"),
            History0=json_data.get("History0"),
            History1=json_data.get("History1"),
            Id=json_data.get("Id"),
            Ip6Trusthost1=json_data.get("Ip6Trusthost1"),
            Ip6Trusthost10=json_data.get("Ip6Trusthost10"),
            Ip6Trusthost2=json_data.get("Ip6Trusthost2"),
            Ip6Trusthost3=json_data.get("Ip6Trusthost3"),
            Ip6Trusthost4=json_data.get("Ip6Trusthost4"),
            Ip6Trusthost5=json_data.get("Ip6Trusthost5"),
            Ip6Trusthost6=json_data.get("Ip6Trusthost6"),
            Ip6Trusthost7=json_data.get("Ip6Trusthost7"),
            Ip6Trusthost8=json_data.get("Ip6Trusthost8"),
            Ip6Trusthost9=json_data.get("Ip6Trusthost9"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PasswordExpire=json_data.get("PasswordExpire"),
            PeerAuth=json_data.get("PeerAuth"),
            PeerGroup=json_data.get("PeerGroup"),
            RadiusVdomOverride=json_data.get("RadiusVdomOverride"),
            RemoteAuth=json_data.get("RemoteAuth"),
            RemoteGroup=json_data.get("RemoteGroup"),
            Schedule=json_data.get("Schedule"),
            SmsCustomServer=json_data.get("SmsCustomServer"),
            SmsPhone=json_data.get("SmsPhone"),
            SmsServer=json_data.get("SmsServer"),
            SshCertificate=json_data.get("SshCertificate"),
            SshPublicKey1=json_data.get("SshPublicKey1"),
            SshPublicKey2=json_data.get("SshPublicKey2"),
            SshPublicKey3=json_data.get("SshPublicKey3"),
            Trusthost1=json_data.get("Trusthost1"),
            Trusthost10=json_data.get("Trusthost10"),
            Trusthost2=json_data.get("Trusthost2"),
            Trusthost3=json_data.get("Trusthost3"),
            Trusthost4=json_data.get("Trusthost4"),
            Trusthost5=json_data.get("Trusthost5"),
            Trusthost6=json_data.get("Trusthost6"),
            Trusthost7=json_data.get("Trusthost7"),
            Trusthost8=json_data.get("Trusthost8"),
            Trusthost9=json_data.get("Trusthost9"),
            TwoFactor=json_data.get("TwoFactor"),
            TwoFactorAuthentication=json_data.get("TwoFactorAuthentication"),
            TwoFactorNotification=json_data.get("TwoFactorNotification"),
            Vdomparam=json_data.get("Vdomparam"),
            Wildcard=json_data.get("Wildcard"),
            GuestUsergroups=deserialize_list(json_data.get("GuestUsergroups"), GuestUsergroupsDefinition),
            GuiDashboard=deserialize_list(json_data.get("GuiDashboard"), GuiDashboardDefinition),
            GuiGlobalMenuFavorites=deserialize_list(json_data.get("GuiGlobalMenuFavorites"), GuiGlobalMenuFavoritesDefinition),
            GuiNewFeatureAcknowledge=deserialize_list(json_data.get("GuiNewFeatureAcknowledge"), GuiNewFeatureAcknowledgeDefinition),
            GuiVdomMenuFavorites=deserialize_list(json_data.get("GuiVdomMenuFavorites"), GuiVdomMenuFavoritesDefinition),
            LoginTime=deserialize_list(json_data.get("LoginTime"), LoginTimeDefinition),
            Vdom=deserialize_list(json_data.get("Vdom"), VdomDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GuestUsergroupsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestUsergroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestUsergroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestUsergroupsDefinition = GuestUsergroupsDefinition


@dataclass
class GuiDashboardDefinition(BaseModel):
    Columns: Optional[float]
    Id: Optional[float]
    LayoutType: Optional[str]
    Name: Optional[str]
    Scope: Optional[str]
    Widget: Optional[Sequence["_WidgetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GuiDashboardDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuiDashboardDefinition"]:
        if not json_data:
            return None
        return cls(
            Columns=json_data.get("Columns"),
            Id=json_data.get("Id"),
            LayoutType=json_data.get("LayoutType"),
            Name=json_data.get("Name"),
            Scope=json_data.get("Scope"),
            Widget=deserialize_list(json_data.get("Widget"), WidgetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuiDashboardDefinition = GuiDashboardDefinition


@dataclass
class WidgetDefinition(BaseModel):
    FabricDevice: Optional[str]
    Height: Optional[float]
    Id: Optional[float]
    Industry: Optional[str]
    Interface: Optional[str]
    Region: Optional[str]
    ReportBy: Optional[str]
    SortBy: Optional[str]
    Timeframe: Optional[str]
    Title: Optional[str]
    Type: Optional[str]
    Visualization: Optional[str]
    Width: Optional[float]
    XPos: Optional[float]
    YPos: Optional[float]
    Filters: Optional[Sequence["_FiltersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WidgetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WidgetDefinition"]:
        if not json_data:
            return None
        return cls(
            FabricDevice=json_data.get("FabricDevice"),
            Height=json_data.get("Height"),
            Id=json_data.get("Id"),
            Industry=json_data.get("Industry"),
            Interface=json_data.get("Interface"),
            Region=json_data.get("Region"),
            ReportBy=json_data.get("ReportBy"),
            SortBy=json_data.get("SortBy"),
            Timeframe=json_data.get("Timeframe"),
            Title=json_data.get("Title"),
            Type=json_data.get("Type"),
            Visualization=json_data.get("Visualization"),
            Width=json_data.get("Width"),
            XPos=json_data.get("XPos"),
            YPos=json_data.get("YPos"),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WidgetDefinition = WidgetDefinition


@dataclass
class FiltersDefinition(BaseModel):
    Id: Optional[float]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


@dataclass
class GuiGlobalMenuFavoritesDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuiGlobalMenuFavoritesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuiGlobalMenuFavoritesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuiGlobalMenuFavoritesDefinition = GuiGlobalMenuFavoritesDefinition


@dataclass
class GuiNewFeatureAcknowledgeDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuiNewFeatureAcknowledgeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuiNewFeatureAcknowledgeDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuiNewFeatureAcknowledgeDefinition = GuiNewFeatureAcknowledgeDefinition


@dataclass
class GuiVdomMenuFavoritesDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuiVdomMenuFavoritesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuiVdomMenuFavoritesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuiVdomMenuFavoritesDefinition = GuiVdomMenuFavoritesDefinition


@dataclass
class LoginTimeDefinition(BaseModel):
    LastFailedLogin: Optional[str]
    LastLogin: Optional[str]
    UsrName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoginTimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoginTimeDefinition"]:
        if not json_data:
            return None
        return cls(
            LastFailedLogin=json_data.get("LastFailedLogin"),
            LastLogin=json_data.get("LastLogin"),
            UsrName=json_data.get("UsrName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoginTimeDefinition = LoginTimeDefinition


@dataclass
class VdomDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VdomDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VdomDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VdomDefinition = VdomDefinition


