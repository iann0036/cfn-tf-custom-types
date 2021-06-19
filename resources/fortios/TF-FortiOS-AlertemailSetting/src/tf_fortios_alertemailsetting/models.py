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
    AdminLoginLogs: Optional[str]
    AlertInterval: Optional[float]
    AmcInterfaceBypassMode: Optional[str]
    AntivirusLogs: Optional[str]
    ConfigurationChangesLogs: Optional[str]
    CriticalInterval: Optional[float]
    DebugInterval: Optional[float]
    EmailInterval: Optional[float]
    EmergencyInterval: Optional[float]
    ErrorInterval: Optional[float]
    FdsLicenseExpiringDays: Optional[float]
    FdsLicenseExpiringWarning: Optional[str]
    FdsUpdateLogs: Optional[str]
    FilterMode: Optional[str]
    FipsCcErrors: Optional[str]
    FirewallAuthenticationFailureLogs: Optional[str]
    FortiguardLogQuotaWarning: Optional[str]
    FssoDisconnectLogs: Optional[str]
    HaLogs: Optional[str]
    Id: Optional[str]
    InformationInterval: Optional[float]
    IpsLogs: Optional[str]
    IpsecErrorsLogs: Optional[str]
    LocalDiskUsage: Optional[float]
    LogDiskUsageWarning: Optional[str]
    Mailto1: Optional[str]
    Mailto2: Optional[str]
    Mailto3: Optional[str]
    NotificationInterval: Optional[float]
    PppErrorsLogs: Optional[str]
    Severity: Optional[str]
    SshLogs: Optional[str]
    SslvpnAuthenticationErrorsLogs: Optional[str]
    Username: Optional[str]
    Vdomparam: Optional[str]
    ViolationTrafficLogs: Optional[str]
    WarningInterval: Optional[float]
    WebfilterLogs: Optional[str]

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
            AdminLoginLogs=json_data.get("AdminLoginLogs"),
            AlertInterval=json_data.get("AlertInterval"),
            AmcInterfaceBypassMode=json_data.get("AmcInterfaceBypassMode"),
            AntivirusLogs=json_data.get("AntivirusLogs"),
            ConfigurationChangesLogs=json_data.get("ConfigurationChangesLogs"),
            CriticalInterval=json_data.get("CriticalInterval"),
            DebugInterval=json_data.get("DebugInterval"),
            EmailInterval=json_data.get("EmailInterval"),
            EmergencyInterval=json_data.get("EmergencyInterval"),
            ErrorInterval=json_data.get("ErrorInterval"),
            FdsLicenseExpiringDays=json_data.get("FdsLicenseExpiringDays"),
            FdsLicenseExpiringWarning=json_data.get("FdsLicenseExpiringWarning"),
            FdsUpdateLogs=json_data.get("FdsUpdateLogs"),
            FilterMode=json_data.get("FilterMode"),
            FipsCcErrors=json_data.get("FipsCcErrors"),
            FirewallAuthenticationFailureLogs=json_data.get("FirewallAuthenticationFailureLogs"),
            FortiguardLogQuotaWarning=json_data.get("FortiguardLogQuotaWarning"),
            FssoDisconnectLogs=json_data.get("FssoDisconnectLogs"),
            HaLogs=json_data.get("HaLogs"),
            Id=json_data.get("Id"),
            InformationInterval=json_data.get("InformationInterval"),
            IpsLogs=json_data.get("IpsLogs"),
            IpsecErrorsLogs=json_data.get("IpsecErrorsLogs"),
            LocalDiskUsage=json_data.get("LocalDiskUsage"),
            LogDiskUsageWarning=json_data.get("LogDiskUsageWarning"),
            Mailto1=json_data.get("Mailto1"),
            Mailto2=json_data.get("Mailto2"),
            Mailto3=json_data.get("Mailto3"),
            NotificationInterval=json_data.get("NotificationInterval"),
            PppErrorsLogs=json_data.get("PppErrorsLogs"),
            Severity=json_data.get("Severity"),
            SshLogs=json_data.get("SshLogs"),
            SslvpnAuthenticationErrorsLogs=json_data.get("SslvpnAuthenticationErrorsLogs"),
            Username=json_data.get("Username"),
            Vdomparam=json_data.get("Vdomparam"),
            ViolationTrafficLogs=json_data.get("ViolationTrafficLogs"),
            WarningInterval=json_data.get("WarningInterval"),
            WebfilterLogs=json_data.get("WebfilterLogs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


