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
    Description: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    ProfileName: Optional[str]
    ReplacemsgOverrideGroup: Optional[str]
    Vdomparam: Optional[str]
    DeviceGroups: Optional[Sequence["_DeviceGroupsDefinition"]]
    ForticlientAndroidSettings: Optional[Sequence["_ForticlientAndroidSettingsDefinition"]]
    ForticlientIosSettings: Optional[Sequence["_ForticlientIosSettingsDefinition"]]
    ForticlientWinmacSettings: Optional[Sequence["_ForticlientWinmacSettingsDefinition"]]
    OnNetAddr: Optional[Sequence["_OnNetAddrDefinition"]]
    SrcAddr: Optional[Sequence["_SrcAddrDefinition"]]
    UserGroups: Optional[Sequence["_UserGroupsDefinition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

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
            Description=json_data.get("Description"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            ProfileName=json_data.get("ProfileName"),
            ReplacemsgOverrideGroup=json_data.get("ReplacemsgOverrideGroup"),
            Vdomparam=json_data.get("Vdomparam"),
            DeviceGroups=deserialize_list(json_data.get("DeviceGroups"), DeviceGroupsDefinition),
            ForticlientAndroidSettings=deserialize_list(json_data.get("ForticlientAndroidSettings"), ForticlientAndroidSettingsDefinition),
            ForticlientIosSettings=deserialize_list(json_data.get("ForticlientIosSettings"), ForticlientIosSettingsDefinition),
            ForticlientWinmacSettings=deserialize_list(json_data.get("ForticlientWinmacSettings"), ForticlientWinmacSettingsDefinition),
            OnNetAddr=deserialize_list(json_data.get("OnNetAddr"), OnNetAddrDefinition),
            SrcAddr=deserialize_list(json_data.get("SrcAddr"), SrcAddrDefinition),
            UserGroups=deserialize_list(json_data.get("UserGroups"), UserGroupsDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeviceGroupsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceGroupsDefinition = DeviceGroupsDefinition


@dataclass
class ForticlientAndroidSettingsDefinition(BaseModel):
    DisableWfWhenProtected: Optional[str]
    ForticlientAdvancedVpn: Optional[str]
    ForticlientAdvancedVpnBuffer: Optional[str]
    ForticlientVpnProvisioning: Optional[str]
    ForticlientWf: Optional[str]
    ForticlientWfProfile: Optional[str]
    ForticlientVpnSettings: Optional[Sequence["_ForticlientVpnSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientAndroidSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientAndroidSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableWfWhenProtected=json_data.get("DisableWfWhenProtected"),
            ForticlientAdvancedVpn=json_data.get("ForticlientAdvancedVpn"),
            ForticlientAdvancedVpnBuffer=json_data.get("ForticlientAdvancedVpnBuffer"),
            ForticlientVpnProvisioning=json_data.get("ForticlientVpnProvisioning"),
            ForticlientWf=json_data.get("ForticlientWf"),
            ForticlientWfProfile=json_data.get("ForticlientWfProfile"),
            ForticlientVpnSettings=deserialize_list(json_data.get("ForticlientVpnSettings"), ForticlientVpnSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientAndroidSettingsDefinition = ForticlientAndroidSettingsDefinition


@dataclass
class ForticlientVpnSettingsDefinition(BaseModel):
    AuthMethod: Optional[str]
    Name: Optional[str]
    PresharedKey: Optional[str]
    RemoteGw: Optional[str]
    SslvpnAccessPort: Optional[float]
    SslvpnRequireCertificate: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientVpnSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientVpnSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthMethod=json_data.get("AuthMethod"),
            Name=json_data.get("Name"),
            PresharedKey=json_data.get("PresharedKey"),
            RemoteGw=json_data.get("RemoteGw"),
            SslvpnAccessPort=json_data.get("SslvpnAccessPort"),
            SslvpnRequireCertificate=json_data.get("SslvpnRequireCertificate"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientVpnSettingsDefinition = ForticlientVpnSettingsDefinition


@dataclass
class ForticlientIosSettingsDefinition(BaseModel):
    ClientVpnProvisioning: Optional[str]
    ConfigurationContent: Optional[str]
    ConfigurationName: Optional[str]
    DisableWfWhenProtected: Optional[str]
    DistributeConfigurationProfile: Optional[str]
    ForticlientWf: Optional[str]
    ForticlientWfProfile: Optional[str]
    ClientVpnSettings: Optional[Sequence["_ClientVpnSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientIosSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientIosSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientVpnProvisioning=json_data.get("ClientVpnProvisioning"),
            ConfigurationContent=json_data.get("ConfigurationContent"),
            ConfigurationName=json_data.get("ConfigurationName"),
            DisableWfWhenProtected=json_data.get("DisableWfWhenProtected"),
            DistributeConfigurationProfile=json_data.get("DistributeConfigurationProfile"),
            ForticlientWf=json_data.get("ForticlientWf"),
            ForticlientWfProfile=json_data.get("ForticlientWfProfile"),
            ClientVpnSettings=deserialize_list(json_data.get("ClientVpnSettings"), ClientVpnSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientIosSettingsDefinition = ForticlientIosSettingsDefinition


@dataclass
class ClientVpnSettingsDefinition(BaseModel):
    AuthMethod: Optional[str]
    Name: Optional[str]
    PresharedKey: Optional[str]
    RemoteGw: Optional[str]
    SslvpnAccessPort: Optional[float]
    SslvpnRequireCertificate: Optional[str]
    Type: Optional[str]
    VpnConfigurationContent: Optional[str]
    VpnConfigurationName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientVpnSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientVpnSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthMethod=json_data.get("AuthMethod"),
            Name=json_data.get("Name"),
            PresharedKey=json_data.get("PresharedKey"),
            RemoteGw=json_data.get("RemoteGw"),
            SslvpnAccessPort=json_data.get("SslvpnAccessPort"),
            SslvpnRequireCertificate=json_data.get("SslvpnRequireCertificate"),
            Type=json_data.get("Type"),
            VpnConfigurationContent=json_data.get("VpnConfigurationContent"),
            VpnConfigurationName=json_data.get("VpnConfigurationName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientVpnSettingsDefinition = ClientVpnSettingsDefinition


@dataclass
class ForticlientWinmacSettingsDefinition(BaseModel):
    AvRealtimeProtection: Optional[str]
    AvSignatureUpToDate: Optional[str]
    ForticlientApplicationFirewall: Optional[str]
    ForticlientApplicationFirewallList: Optional[str]
    ForticlientAv: Optional[str]
    ForticlientEmsCompliance: Optional[str]
    ForticlientEmsComplianceAction: Optional[str]
    ForticlientLinuxVer: Optional[str]
    ForticlientLogUpload: Optional[str]
    ForticlientLogUploadLevel: Optional[str]
    ForticlientLogUploadServer: Optional[str]
    ForticlientMacVer: Optional[str]
    ForticlientMinimumSoftwareVersion: Optional[str]
    ForticlientRegistrationComplianceAction: Optional[str]
    ForticlientSecurityPosture: Optional[str]
    ForticlientSecurityPostureComplianceAction: Optional[str]
    ForticlientSystemCompliance: Optional[str]
    ForticlientSystemComplianceAction: Optional[str]
    ForticlientVulnScan: Optional[str]
    ForticlientVulnScanComplianceAction: Optional[str]
    ForticlientVulnScanEnforce: Optional[str]
    ForticlientVulnScanEnforceGrace: Optional[float]
    ForticlientVulnScanExempt: Optional[str]
    ForticlientWf: Optional[str]
    ForticlientWfProfile: Optional[str]
    ForticlientWinVer: Optional[str]
    OsAvSoftwareInstalled: Optional[str]
    SandboxAddress: Optional[str]
    SandboxAnalysis: Optional[str]
    ForticlientEmsEntries: Optional[Sequence["_ForticlientEmsEntriesDefinition"]]
    ForticlientOperatingSystem: Optional[Sequence["_ForticlientOperatingSystemDefinition"]]
    ForticlientOwnFile: Optional[Sequence["_ForticlientOwnFileDefinition"]]
    ForticlientRegistryEntry: Optional[Sequence["_ForticlientRegistryEntryDefinition"]]
    ForticlientRunningApp: Optional[Sequence["_ForticlientRunningAppDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientWinmacSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientWinmacSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AvRealtimeProtection=json_data.get("AvRealtimeProtection"),
            AvSignatureUpToDate=json_data.get("AvSignatureUpToDate"),
            ForticlientApplicationFirewall=json_data.get("ForticlientApplicationFirewall"),
            ForticlientApplicationFirewallList=json_data.get("ForticlientApplicationFirewallList"),
            ForticlientAv=json_data.get("ForticlientAv"),
            ForticlientEmsCompliance=json_data.get("ForticlientEmsCompliance"),
            ForticlientEmsComplianceAction=json_data.get("ForticlientEmsComplianceAction"),
            ForticlientLinuxVer=json_data.get("ForticlientLinuxVer"),
            ForticlientLogUpload=json_data.get("ForticlientLogUpload"),
            ForticlientLogUploadLevel=json_data.get("ForticlientLogUploadLevel"),
            ForticlientLogUploadServer=json_data.get("ForticlientLogUploadServer"),
            ForticlientMacVer=json_data.get("ForticlientMacVer"),
            ForticlientMinimumSoftwareVersion=json_data.get("ForticlientMinimumSoftwareVersion"),
            ForticlientRegistrationComplianceAction=json_data.get("ForticlientRegistrationComplianceAction"),
            ForticlientSecurityPosture=json_data.get("ForticlientSecurityPosture"),
            ForticlientSecurityPostureComplianceAction=json_data.get("ForticlientSecurityPostureComplianceAction"),
            ForticlientSystemCompliance=json_data.get("ForticlientSystemCompliance"),
            ForticlientSystemComplianceAction=json_data.get("ForticlientSystemComplianceAction"),
            ForticlientVulnScan=json_data.get("ForticlientVulnScan"),
            ForticlientVulnScanComplianceAction=json_data.get("ForticlientVulnScanComplianceAction"),
            ForticlientVulnScanEnforce=json_data.get("ForticlientVulnScanEnforce"),
            ForticlientVulnScanEnforceGrace=json_data.get("ForticlientVulnScanEnforceGrace"),
            ForticlientVulnScanExempt=json_data.get("ForticlientVulnScanExempt"),
            ForticlientWf=json_data.get("ForticlientWf"),
            ForticlientWfProfile=json_data.get("ForticlientWfProfile"),
            ForticlientWinVer=json_data.get("ForticlientWinVer"),
            OsAvSoftwareInstalled=json_data.get("OsAvSoftwareInstalled"),
            SandboxAddress=json_data.get("SandboxAddress"),
            SandboxAnalysis=json_data.get("SandboxAnalysis"),
            ForticlientEmsEntries=deserialize_list(json_data.get("ForticlientEmsEntries"), ForticlientEmsEntriesDefinition),
            ForticlientOperatingSystem=deserialize_list(json_data.get("ForticlientOperatingSystem"), ForticlientOperatingSystemDefinition),
            ForticlientOwnFile=deserialize_list(json_data.get("ForticlientOwnFile"), ForticlientOwnFileDefinition),
            ForticlientRegistryEntry=deserialize_list(json_data.get("ForticlientRegistryEntry"), ForticlientRegistryEntryDefinition),
            ForticlientRunningApp=deserialize_list(json_data.get("ForticlientRunningApp"), ForticlientRunningAppDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientWinmacSettingsDefinition = ForticlientWinmacSettingsDefinition


@dataclass
class ForticlientEmsEntriesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientEmsEntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientEmsEntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientEmsEntriesDefinition = ForticlientEmsEntriesDefinition


@dataclass
class ForticlientOperatingSystemDefinition(BaseModel):
    Id: Optional[float]
    OsName: Optional[str]
    OsType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientOperatingSystemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientOperatingSystemDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            OsName=json_data.get("OsName"),
            OsType=json_data.get("OsType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientOperatingSystemDefinition = ForticlientOperatingSystemDefinition


@dataclass
class ForticlientOwnFileDefinition(BaseModel):
    File: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientOwnFileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientOwnFileDefinition"]:
        if not json_data:
            return None
        return cls(
            File=json_data.get("File"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientOwnFileDefinition = ForticlientOwnFileDefinition


@dataclass
class ForticlientRegistryEntryDefinition(BaseModel):
    Id: Optional[float]
    RegistryEntry: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientRegistryEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientRegistryEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            RegistryEntry=json_data.get("RegistryEntry"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientRegistryEntryDefinition = ForticlientRegistryEntryDefinition


@dataclass
class ForticlientRunningAppDefinition(BaseModel):
    AppName: Optional[str]
    AppSha256Signature: Optional[str]
    AppSha256Signature2: Optional[str]
    AppSha256Signature3: Optional[str]
    AppSha256Signature4: Optional[str]
    ApplicationCheckRule: Optional[str]
    Id: Optional[float]
    ProcessName: Optional[str]
    ProcessName2: Optional[str]
    ProcessName3: Optional[str]
    ProcessName4: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForticlientRunningAppDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForticlientRunningAppDefinition"]:
        if not json_data:
            return None
        return cls(
            AppName=json_data.get("AppName"),
            AppSha256Signature=json_data.get("AppSha256Signature"),
            AppSha256Signature2=json_data.get("AppSha256Signature2"),
            AppSha256Signature3=json_data.get("AppSha256Signature3"),
            AppSha256Signature4=json_data.get("AppSha256Signature4"),
            ApplicationCheckRule=json_data.get("ApplicationCheckRule"),
            Id=json_data.get("Id"),
            ProcessName=json_data.get("ProcessName"),
            ProcessName2=json_data.get("ProcessName2"),
            ProcessName3=json_data.get("ProcessName3"),
            ProcessName4=json_data.get("ProcessName4"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForticlientRunningAppDefinition = ForticlientRunningAppDefinition


@dataclass
class OnNetAddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnNetAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnNetAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnNetAddrDefinition = OnNetAddrDefinition


@dataclass
class SrcAddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcAddrDefinition = SrcAddrDefinition


@dataclass
class UserGroupsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserGroupsDefinition = UserGroupsDefinition


@dataclass
class UsersDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition


