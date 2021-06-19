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
    Admintimeout: Optional[float]
    AdmintimeoutOverride: Optional[str]
    Authgrp: Optional[str]
    Comments: Optional[str]
    Ftviewgrp: Optional[str]
    Fwgrp: Optional[str]
    Id: Optional[str]
    Loggrp: Optional[str]
    Name: Optional[str]
    Netgrp: Optional[str]
    Scope: Optional[str]
    Secfabgrp: Optional[str]
    Sysgrp: Optional[str]
    SystemDiagnostics: Optional[str]
    Utmgrp: Optional[str]
    Vdomparam: Optional[str]
    Vpngrp: Optional[str]
    Wanoptgrp: Optional[str]
    Wifi: Optional[str]
    FwgrpPermission: Optional[Sequence["_FwgrpPermissionDefinition"]]
    LoggrpPermission: Optional[Sequence["_LoggrpPermissionDefinition"]]
    NetgrpPermission: Optional[Sequence["_NetgrpPermissionDefinition"]]
    SysgrpPermission: Optional[Sequence["_SysgrpPermissionDefinition"]]
    UtmgrpPermission: Optional[Sequence["_UtmgrpPermissionDefinition"]]

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
            Admintimeout=json_data.get("Admintimeout"),
            AdmintimeoutOverride=json_data.get("AdmintimeoutOverride"),
            Authgrp=json_data.get("Authgrp"),
            Comments=json_data.get("Comments"),
            Ftviewgrp=json_data.get("Ftviewgrp"),
            Fwgrp=json_data.get("Fwgrp"),
            Id=json_data.get("Id"),
            Loggrp=json_data.get("Loggrp"),
            Name=json_data.get("Name"),
            Netgrp=json_data.get("Netgrp"),
            Scope=json_data.get("Scope"),
            Secfabgrp=json_data.get("Secfabgrp"),
            Sysgrp=json_data.get("Sysgrp"),
            SystemDiagnostics=json_data.get("SystemDiagnostics"),
            Utmgrp=json_data.get("Utmgrp"),
            Vdomparam=json_data.get("Vdomparam"),
            Vpngrp=json_data.get("Vpngrp"),
            Wanoptgrp=json_data.get("Wanoptgrp"),
            Wifi=json_data.get("Wifi"),
            FwgrpPermission=deserialize_list(json_data.get("FwgrpPermission"), FwgrpPermissionDefinition),
            LoggrpPermission=deserialize_list(json_data.get("LoggrpPermission"), LoggrpPermissionDefinition),
            NetgrpPermission=deserialize_list(json_data.get("NetgrpPermission"), NetgrpPermissionDefinition),
            SysgrpPermission=deserialize_list(json_data.get("SysgrpPermission"), SysgrpPermissionDefinition),
            UtmgrpPermission=deserialize_list(json_data.get("UtmgrpPermission"), UtmgrpPermissionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FwgrpPermissionDefinition(BaseModel):
    Address: Optional[str]
    Policy: Optional[str]
    Schedule: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FwgrpPermissionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FwgrpPermissionDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Policy=json_data.get("Policy"),
            Schedule=json_data.get("Schedule"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FwgrpPermissionDefinition = FwgrpPermissionDefinition


@dataclass
class LoggrpPermissionDefinition(BaseModel):
    Config: Optional[str]
    DataAccess: Optional[str]
    ReportAccess: Optional[str]
    ThreatWeight: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggrpPermissionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggrpPermissionDefinition"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            DataAccess=json_data.get("DataAccess"),
            ReportAccess=json_data.get("ReportAccess"),
            ThreatWeight=json_data.get("ThreatWeight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggrpPermissionDefinition = LoggrpPermissionDefinition


@dataclass
class NetgrpPermissionDefinition(BaseModel):
    Cfg: Optional[str]
    PacketCapture: Optional[str]
    RouteCfg: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetgrpPermissionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetgrpPermissionDefinition"]:
        if not json_data:
            return None
        return cls(
            Cfg=json_data.get("Cfg"),
            PacketCapture=json_data.get("PacketCapture"),
            RouteCfg=json_data.get("RouteCfg"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetgrpPermissionDefinition = NetgrpPermissionDefinition


@dataclass
class SysgrpPermissionDefinition(BaseModel):
    Admin: Optional[str]
    Cfg: Optional[str]
    Mnt: Optional[str]
    Upd: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SysgrpPermissionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysgrpPermissionDefinition"]:
        if not json_data:
            return None
        return cls(
            Admin=json_data.get("Admin"),
            Cfg=json_data.get("Cfg"),
            Mnt=json_data.get("Mnt"),
            Upd=json_data.get("Upd"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysgrpPermissionDefinition = SysgrpPermissionDefinition


@dataclass
class UtmgrpPermissionDefinition(BaseModel):
    Antivirus: Optional[str]
    ApplicationControl: Optional[str]
    DataLossPrevention: Optional[str]
    Dnsfilter: Optional[str]
    Emailfilter: Optional[str]
    EndpointControl: Optional[str]
    FileFilter: Optional[str]
    Icap: Optional[str]
    Ips: Optional[str]
    Spamfilter: Optional[str]
    Voip: Optional[str]
    Waf: Optional[str]
    Webfilter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UtmgrpPermissionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UtmgrpPermissionDefinition"]:
        if not json_data:
            return None
        return cls(
            Antivirus=json_data.get("Antivirus"),
            ApplicationControl=json_data.get("ApplicationControl"),
            DataLossPrevention=json_data.get("DataLossPrevention"),
            Dnsfilter=json_data.get("Dnsfilter"),
            Emailfilter=json_data.get("Emailfilter"),
            EndpointControl=json_data.get("EndpointControl"),
            FileFilter=json_data.get("FileFilter"),
            Icap=json_data.get("Icap"),
            Ips=json_data.get("Ips"),
            Spamfilter=json_data.get("Spamfilter"),
            Voip=json_data.get("Voip"),
            Waf=json_data.get("Waf"),
            Webfilter=json_data.get("Webfilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UtmgrpPermissionDefinition = UtmgrpPermissionDefinition


