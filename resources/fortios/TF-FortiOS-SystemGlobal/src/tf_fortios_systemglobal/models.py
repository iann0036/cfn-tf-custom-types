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
    AdminConcurrent: Optional[str]
    AdminConsoleTimeout: Optional[float]
    AdminHstsMaxAge: Optional[float]
    AdminHttpsPkiRequired: Optional[str]
    AdminHttpsRedirect: Optional[str]
    AdminHttpsSslVersions: Optional[str]
    AdminLockoutDuration: Optional[float]
    AdminLockoutThreshold: Optional[float]
    AdminLoginMax: Optional[float]
    AdminMaintainer: Optional[str]
    AdminPort: Optional[float]
    AdminRestrictLocal: Optional[str]
    AdminScp: Optional[str]
    AdminServerCert: Optional[str]
    AdminSport: Optional[float]
    AdminSshGraceTime: Optional[float]
    AdminSshPassword: Optional[str]
    AdminSshPort: Optional[float]
    AdminSshV1: Optional[str]
    AdminTelnet: Optional[str]
    AdminTelnetPort: Optional[float]
    Admintimeout: Optional[float]
    Alias: Optional[str]
    AllowTrafficRedirect: Optional[str]
    AntiReplay: Optional[str]
    ArpMaxEntry: Optional[float]
    Asymroute: Optional[str]
    AuthCert: Optional[str]
    AuthHttpPort: Optional[float]
    AuthHttpsPort: Optional[float]
    AuthKeepalive: Optional[str]
    AuthSessionLimit: Optional[str]
    AutoAuthExtensionDevice: Optional[str]
    AutorunLogFsck: Optional[str]
    AvAffinity: Optional[str]
    AvFailopen: Optional[str]
    AvFailopenSession: Optional[str]
    BatchCmdb: Optional[str]
    BlockSessionTimer: Optional[float]
    BrFdbMaxEntry: Optional[float]
    CertChainMax: Optional[float]
    CfgRevertTimeout: Optional[float]
    CfgSave: Optional[str]
    CheckProtocolHeader: Optional[str]
    CheckResetRange: Optional[str]
    CliAuditLog: Optional[str]
    CloudCommunication: Optional[str]
    CltCertReq: Optional[str]
    ComplianceCheck: Optional[str]
    ComplianceCheckTime: Optional[str]
    CpuUseThreshold: Optional[float]
    CsrCaAttribute: Optional[str]
    DailyRestart: Optional[str]
    DefaultServiceSourcePort: Optional[str]
    DeviceIdentificationActiveScanDelay: Optional[float]
    DeviceIdleTimeout: Optional[float]
    DhParams: Optional[str]
    DnsproxyWorkerCount: Optional[float]
    Dst: Optional[str]
    EndpointControlFdsAccess: Optional[str]
    EndpointControlPortalPort: Optional[float]
    Failtime: Optional[float]
    FazDiskBufferSize: Optional[float]
    FdsStatistics: Optional[str]
    FdsStatisticsPeriod: Optional[float]
    FecPort: Optional[float]
    FgdAlertSubscription: Optional[str]
    Fortiextender: Optional[str]
    FortiextenderDataPort: Optional[float]
    FortiextenderVlanMode: Optional[str]
    FortiipamIntegration: Optional[str]
    FortiservicePort: Optional[float]
    FortitokenCloud: Optional[str]
    GuiAllowDefaultHostname: Optional[str]
    GuiCertificates: Optional[str]
    GuiCustomLanguage: Optional[str]
    GuiDateFormat: Optional[str]
    GuiDateTimeSource: Optional[str]
    GuiDeviceLatitude: Optional[str]
    GuiDeviceLongitude: Optional[str]
    GuiDisplayHostname: Optional[str]
    GuiFirmwareUpgradeSetupWarning: Optional[str]
    GuiFirmwareUpgradeWarning: Optional[str]
    GuiForticareRegistrationSetupWarning: Optional[str]
    GuiFortigateCloudSandbox: Optional[str]
    GuiFortisandboxCloud: Optional[str]
    GuiIpv6: Optional[str]
    GuiLinesPerPage: Optional[float]
    GuiTheme: Optional[str]
    GuiWirelessOpensecurity: Optional[str]
    HonorDf: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    IgmpStateLimit: Optional[float]
    IkeEmbryonicLimit: Optional[float]
    Interval: Optional[float]
    IpSrcPortRange: Optional[str]
    IpsAffinity: Optional[str]
    IpsecAsicOffload: Optional[str]
    IpsecHmacOffload: Optional[str]
    IpsecSoftDecAsync: Optional[str]
    Ipv6AcceptDad: Optional[float]
    Ipv6AllowAnycastProbe: Optional[str]
    Ipv6AllowTrafficRedirect: Optional[str]
    IrqTimeAccounting: Optional[str]
    Language: Optional[str]
    Ldapconntimeout: Optional[float]
    LldpReception: Optional[str]
    LldpTransmission: Optional[str]
    LogSslConnection: Optional[str]
    LogUuidAddress: Optional[str]
    LogUuidPolicy: Optional[str]
    LoginTimestamp: Optional[str]
    LongVdomName: Optional[str]
    ManagementVdom: Optional[str]
    MaxDlpstatMemory: Optional[float]
    MaxRouteCacheSize: Optional[float]
    McTtlNotchange: Optional[str]
    MemoryUseThresholdExtreme: Optional[float]
    MemoryUseThresholdGreen: Optional[float]
    MemoryUseThresholdRed: Optional[float]
    MiglogAffinity: Optional[str]
    MiglogdChildren: Optional[float]
    MultiFactorAuthentication: Optional[str]
    MulticastForward: Optional[str]
    NdpMaxEntry: Optional[float]
    PerUserBal: Optional[str]
    PerUserBwl: Optional[str]
    PolicyAuthConcurrent: Optional[float]
    PostLoginBanner: Optional[str]
    PreLoginBanner: Optional[str]
    PrivateDataEncryption: Optional[str]
    ProxyAuthLifetime: Optional[str]
    ProxyAuthLifetimeTimeout: Optional[float]
    ProxyAuthTimeout: Optional[float]
    ProxyCipherHardwareAcceleration: Optional[str]
    ProxyKxpHardwareAcceleration: Optional[str]
    ProxyReAuthenticationMode: Optional[str]
    ProxyWorkerCount: Optional[float]
    RadiusPort: Optional[float]
    RebootUponConfigRestore: Optional[str]
    Refresh: Optional[float]
    Remoteauthtimeout: Optional[float]
    ResetSessionlessTcp: Optional[str]
    RestartTime: Optional[str]
    RevisionBackupOnLogout: Optional[str]
    RevisionImageAutoBackup: Optional[str]
    ScanunitCount: Optional[float]
    SecurityRatingResultSubmission: Optional[str]
    SecurityRatingRunOnSchedule: Optional[str]
    SendPmtuIcmp: Optional[str]
    SnatRouteChange: Optional[str]
    SpecialFile23Support: Optional[str]
    SsdTrimDate: Optional[float]
    SsdTrimFreq: Optional[str]
    SsdTrimHour: Optional[float]
    SsdTrimMin: Optional[float]
    SsdTrimWeekday: Optional[str]
    SshCbcCipher: Optional[str]
    SshHmacMd5: Optional[str]
    SshKexSha1: Optional[str]
    SshMacWeak: Optional[str]
    SslMinProtoVersion: Optional[str]
    SslStaticKeyCiphers: Optional[str]
    SslvpnCipherHardwareAcceleration: Optional[str]
    SslvpnEmsSnCheck: Optional[str]
    SslvpnKxpHardwareAcceleration: Optional[str]
    SslvpnMaxWorkerCount: Optional[float]
    SslvpnPluginVersionCheck: Optional[str]
    StrictDirtySessionCheck: Optional[str]
    StrongCrypto: Optional[str]
    SwitchController: Optional[str]
    SwitchControllerReservedNetwork: Optional[str]
    SysPerfLogInterval: Optional[float]
    TcpHalfcloseTimer: Optional[float]
    TcpHalfopenTimer: Optional[float]
    TcpOption: Optional[str]
    TcpTimewaitTimer: Optional[float]
    Tftp: Optional[str]
    Timezone: Optional[str]
    TpMcSkipPolicy: Optional[str]
    TrafficPriority: Optional[str]
    TrafficPriorityLevel: Optional[str]
    TwoFactorEmailExpiry: Optional[float]
    TwoFactorFacExpiry: Optional[float]
    TwoFactorFtkExpiry: Optional[float]
    TwoFactorFtmExpiry: Optional[float]
    TwoFactorSmsExpiry: Optional[float]
    UdpIdleTimer: Optional[float]
    UrlFilterAffinity: Optional[str]
    UrlFilterCount: Optional[float]
    UserDeviceStoreMaxDevices: Optional[float]
    UserDeviceStoreMaxUsers: Optional[float]
    UserServerCert: Optional[str]
    VdomAdmin: Optional[str]
    VdomMode: Optional[str]
    Vdomparam: Optional[str]
    VipArpRange: Optional[str]
    VirtualServerCount: Optional[float]
    VirtualServerHardwareAcceleration: Optional[str]
    WadAffinity: Optional[str]
    WadCsvcCsCount: Optional[float]
    WadCsvcDbCount: Optional[float]
    WadMemoryChangeGranularity: Optional[float]
    WadSourceAffinity: Optional[str]
    WadWorkerCount: Optional[float]
    WifiCaCertificate: Optional[str]
    WifiCertificate: Optional[str]
    Wimax4gUsb: Optional[str]
    WirelessController: Optional[str]
    WirelessControllerPort: Optional[float]

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
            AdminConcurrent=json_data.get("AdminConcurrent"),
            AdminConsoleTimeout=json_data.get("AdminConsoleTimeout"),
            AdminHstsMaxAge=json_data.get("AdminHstsMaxAge"),
            AdminHttpsPkiRequired=json_data.get("AdminHttpsPkiRequired"),
            AdminHttpsRedirect=json_data.get("AdminHttpsRedirect"),
            AdminHttpsSslVersions=json_data.get("AdminHttpsSslVersions"),
            AdminLockoutDuration=json_data.get("AdminLockoutDuration"),
            AdminLockoutThreshold=json_data.get("AdminLockoutThreshold"),
            AdminLoginMax=json_data.get("AdminLoginMax"),
            AdminMaintainer=json_data.get("AdminMaintainer"),
            AdminPort=json_data.get("AdminPort"),
            AdminRestrictLocal=json_data.get("AdminRestrictLocal"),
            AdminScp=json_data.get("AdminScp"),
            AdminServerCert=json_data.get("AdminServerCert"),
            AdminSport=json_data.get("AdminSport"),
            AdminSshGraceTime=json_data.get("AdminSshGraceTime"),
            AdminSshPassword=json_data.get("AdminSshPassword"),
            AdminSshPort=json_data.get("AdminSshPort"),
            AdminSshV1=json_data.get("AdminSshV1"),
            AdminTelnet=json_data.get("AdminTelnet"),
            AdminTelnetPort=json_data.get("AdminTelnetPort"),
            Admintimeout=json_data.get("Admintimeout"),
            Alias=json_data.get("Alias"),
            AllowTrafficRedirect=json_data.get("AllowTrafficRedirect"),
            AntiReplay=json_data.get("AntiReplay"),
            ArpMaxEntry=json_data.get("ArpMaxEntry"),
            Asymroute=json_data.get("Asymroute"),
            AuthCert=json_data.get("AuthCert"),
            AuthHttpPort=json_data.get("AuthHttpPort"),
            AuthHttpsPort=json_data.get("AuthHttpsPort"),
            AuthKeepalive=json_data.get("AuthKeepalive"),
            AuthSessionLimit=json_data.get("AuthSessionLimit"),
            AutoAuthExtensionDevice=json_data.get("AutoAuthExtensionDevice"),
            AutorunLogFsck=json_data.get("AutorunLogFsck"),
            AvAffinity=json_data.get("AvAffinity"),
            AvFailopen=json_data.get("AvFailopen"),
            AvFailopenSession=json_data.get("AvFailopenSession"),
            BatchCmdb=json_data.get("BatchCmdb"),
            BlockSessionTimer=json_data.get("BlockSessionTimer"),
            BrFdbMaxEntry=json_data.get("BrFdbMaxEntry"),
            CertChainMax=json_data.get("CertChainMax"),
            CfgRevertTimeout=json_data.get("CfgRevertTimeout"),
            CfgSave=json_data.get("CfgSave"),
            CheckProtocolHeader=json_data.get("CheckProtocolHeader"),
            CheckResetRange=json_data.get("CheckResetRange"),
            CliAuditLog=json_data.get("CliAuditLog"),
            CloudCommunication=json_data.get("CloudCommunication"),
            CltCertReq=json_data.get("CltCertReq"),
            ComplianceCheck=json_data.get("ComplianceCheck"),
            ComplianceCheckTime=json_data.get("ComplianceCheckTime"),
            CpuUseThreshold=json_data.get("CpuUseThreshold"),
            CsrCaAttribute=json_data.get("CsrCaAttribute"),
            DailyRestart=json_data.get("DailyRestart"),
            DefaultServiceSourcePort=json_data.get("DefaultServiceSourcePort"),
            DeviceIdentificationActiveScanDelay=json_data.get("DeviceIdentificationActiveScanDelay"),
            DeviceIdleTimeout=json_data.get("DeviceIdleTimeout"),
            DhParams=json_data.get("DhParams"),
            DnsproxyWorkerCount=json_data.get("DnsproxyWorkerCount"),
            Dst=json_data.get("Dst"),
            EndpointControlFdsAccess=json_data.get("EndpointControlFdsAccess"),
            EndpointControlPortalPort=json_data.get("EndpointControlPortalPort"),
            Failtime=json_data.get("Failtime"),
            FazDiskBufferSize=json_data.get("FazDiskBufferSize"),
            FdsStatistics=json_data.get("FdsStatistics"),
            FdsStatisticsPeriod=json_data.get("FdsStatisticsPeriod"),
            FecPort=json_data.get("FecPort"),
            FgdAlertSubscription=json_data.get("FgdAlertSubscription"),
            Fortiextender=json_data.get("Fortiextender"),
            FortiextenderDataPort=json_data.get("FortiextenderDataPort"),
            FortiextenderVlanMode=json_data.get("FortiextenderVlanMode"),
            FortiipamIntegration=json_data.get("FortiipamIntegration"),
            FortiservicePort=json_data.get("FortiservicePort"),
            FortitokenCloud=json_data.get("FortitokenCloud"),
            GuiAllowDefaultHostname=json_data.get("GuiAllowDefaultHostname"),
            GuiCertificates=json_data.get("GuiCertificates"),
            GuiCustomLanguage=json_data.get("GuiCustomLanguage"),
            GuiDateFormat=json_data.get("GuiDateFormat"),
            GuiDateTimeSource=json_data.get("GuiDateTimeSource"),
            GuiDeviceLatitude=json_data.get("GuiDeviceLatitude"),
            GuiDeviceLongitude=json_data.get("GuiDeviceLongitude"),
            GuiDisplayHostname=json_data.get("GuiDisplayHostname"),
            GuiFirmwareUpgradeSetupWarning=json_data.get("GuiFirmwareUpgradeSetupWarning"),
            GuiFirmwareUpgradeWarning=json_data.get("GuiFirmwareUpgradeWarning"),
            GuiForticareRegistrationSetupWarning=json_data.get("GuiForticareRegistrationSetupWarning"),
            GuiFortigateCloudSandbox=json_data.get("GuiFortigateCloudSandbox"),
            GuiFortisandboxCloud=json_data.get("GuiFortisandboxCloud"),
            GuiIpv6=json_data.get("GuiIpv6"),
            GuiLinesPerPage=json_data.get("GuiLinesPerPage"),
            GuiTheme=json_data.get("GuiTheme"),
            GuiWirelessOpensecurity=json_data.get("GuiWirelessOpensecurity"),
            HonorDf=json_data.get("HonorDf"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IgmpStateLimit=json_data.get("IgmpStateLimit"),
            IkeEmbryonicLimit=json_data.get("IkeEmbryonicLimit"),
            Interval=json_data.get("Interval"),
            IpSrcPortRange=json_data.get("IpSrcPortRange"),
            IpsAffinity=json_data.get("IpsAffinity"),
            IpsecAsicOffload=json_data.get("IpsecAsicOffload"),
            IpsecHmacOffload=json_data.get("IpsecHmacOffload"),
            IpsecSoftDecAsync=json_data.get("IpsecSoftDecAsync"),
            Ipv6AcceptDad=json_data.get("Ipv6AcceptDad"),
            Ipv6AllowAnycastProbe=json_data.get("Ipv6AllowAnycastProbe"),
            Ipv6AllowTrafficRedirect=json_data.get("Ipv6AllowTrafficRedirect"),
            IrqTimeAccounting=json_data.get("IrqTimeAccounting"),
            Language=json_data.get("Language"),
            Ldapconntimeout=json_data.get("Ldapconntimeout"),
            LldpReception=json_data.get("LldpReception"),
            LldpTransmission=json_data.get("LldpTransmission"),
            LogSslConnection=json_data.get("LogSslConnection"),
            LogUuidAddress=json_data.get("LogUuidAddress"),
            LogUuidPolicy=json_data.get("LogUuidPolicy"),
            LoginTimestamp=json_data.get("LoginTimestamp"),
            LongVdomName=json_data.get("LongVdomName"),
            ManagementVdom=json_data.get("ManagementVdom"),
            MaxDlpstatMemory=json_data.get("MaxDlpstatMemory"),
            MaxRouteCacheSize=json_data.get("MaxRouteCacheSize"),
            McTtlNotchange=json_data.get("McTtlNotchange"),
            MemoryUseThresholdExtreme=json_data.get("MemoryUseThresholdExtreme"),
            MemoryUseThresholdGreen=json_data.get("MemoryUseThresholdGreen"),
            MemoryUseThresholdRed=json_data.get("MemoryUseThresholdRed"),
            MiglogAffinity=json_data.get("MiglogAffinity"),
            MiglogdChildren=json_data.get("MiglogdChildren"),
            MultiFactorAuthentication=json_data.get("MultiFactorAuthentication"),
            MulticastForward=json_data.get("MulticastForward"),
            NdpMaxEntry=json_data.get("NdpMaxEntry"),
            PerUserBal=json_data.get("PerUserBal"),
            PerUserBwl=json_data.get("PerUserBwl"),
            PolicyAuthConcurrent=json_data.get("PolicyAuthConcurrent"),
            PostLoginBanner=json_data.get("PostLoginBanner"),
            PreLoginBanner=json_data.get("PreLoginBanner"),
            PrivateDataEncryption=json_data.get("PrivateDataEncryption"),
            ProxyAuthLifetime=json_data.get("ProxyAuthLifetime"),
            ProxyAuthLifetimeTimeout=json_data.get("ProxyAuthLifetimeTimeout"),
            ProxyAuthTimeout=json_data.get("ProxyAuthTimeout"),
            ProxyCipherHardwareAcceleration=json_data.get("ProxyCipherHardwareAcceleration"),
            ProxyKxpHardwareAcceleration=json_data.get("ProxyKxpHardwareAcceleration"),
            ProxyReAuthenticationMode=json_data.get("ProxyReAuthenticationMode"),
            ProxyWorkerCount=json_data.get("ProxyWorkerCount"),
            RadiusPort=json_data.get("RadiusPort"),
            RebootUponConfigRestore=json_data.get("RebootUponConfigRestore"),
            Refresh=json_data.get("Refresh"),
            Remoteauthtimeout=json_data.get("Remoteauthtimeout"),
            ResetSessionlessTcp=json_data.get("ResetSessionlessTcp"),
            RestartTime=json_data.get("RestartTime"),
            RevisionBackupOnLogout=json_data.get("RevisionBackupOnLogout"),
            RevisionImageAutoBackup=json_data.get("RevisionImageAutoBackup"),
            ScanunitCount=json_data.get("ScanunitCount"),
            SecurityRatingResultSubmission=json_data.get("SecurityRatingResultSubmission"),
            SecurityRatingRunOnSchedule=json_data.get("SecurityRatingRunOnSchedule"),
            SendPmtuIcmp=json_data.get("SendPmtuIcmp"),
            SnatRouteChange=json_data.get("SnatRouteChange"),
            SpecialFile23Support=json_data.get("SpecialFile23Support"),
            SsdTrimDate=json_data.get("SsdTrimDate"),
            SsdTrimFreq=json_data.get("SsdTrimFreq"),
            SsdTrimHour=json_data.get("SsdTrimHour"),
            SsdTrimMin=json_data.get("SsdTrimMin"),
            SsdTrimWeekday=json_data.get("SsdTrimWeekday"),
            SshCbcCipher=json_data.get("SshCbcCipher"),
            SshHmacMd5=json_data.get("SshHmacMd5"),
            SshKexSha1=json_data.get("SshKexSha1"),
            SshMacWeak=json_data.get("SshMacWeak"),
            SslMinProtoVersion=json_data.get("SslMinProtoVersion"),
            SslStaticKeyCiphers=json_data.get("SslStaticKeyCiphers"),
            SslvpnCipherHardwareAcceleration=json_data.get("SslvpnCipherHardwareAcceleration"),
            SslvpnEmsSnCheck=json_data.get("SslvpnEmsSnCheck"),
            SslvpnKxpHardwareAcceleration=json_data.get("SslvpnKxpHardwareAcceleration"),
            SslvpnMaxWorkerCount=json_data.get("SslvpnMaxWorkerCount"),
            SslvpnPluginVersionCheck=json_data.get("SslvpnPluginVersionCheck"),
            StrictDirtySessionCheck=json_data.get("StrictDirtySessionCheck"),
            StrongCrypto=json_data.get("StrongCrypto"),
            SwitchController=json_data.get("SwitchController"),
            SwitchControllerReservedNetwork=json_data.get("SwitchControllerReservedNetwork"),
            SysPerfLogInterval=json_data.get("SysPerfLogInterval"),
            TcpHalfcloseTimer=json_data.get("TcpHalfcloseTimer"),
            TcpHalfopenTimer=json_data.get("TcpHalfopenTimer"),
            TcpOption=json_data.get("TcpOption"),
            TcpTimewaitTimer=json_data.get("TcpTimewaitTimer"),
            Tftp=json_data.get("Tftp"),
            Timezone=json_data.get("Timezone"),
            TpMcSkipPolicy=json_data.get("TpMcSkipPolicy"),
            TrafficPriority=json_data.get("TrafficPriority"),
            TrafficPriorityLevel=json_data.get("TrafficPriorityLevel"),
            TwoFactorEmailExpiry=json_data.get("TwoFactorEmailExpiry"),
            TwoFactorFacExpiry=json_data.get("TwoFactorFacExpiry"),
            TwoFactorFtkExpiry=json_data.get("TwoFactorFtkExpiry"),
            TwoFactorFtmExpiry=json_data.get("TwoFactorFtmExpiry"),
            TwoFactorSmsExpiry=json_data.get("TwoFactorSmsExpiry"),
            UdpIdleTimer=json_data.get("UdpIdleTimer"),
            UrlFilterAffinity=json_data.get("UrlFilterAffinity"),
            UrlFilterCount=json_data.get("UrlFilterCount"),
            UserDeviceStoreMaxDevices=json_data.get("UserDeviceStoreMaxDevices"),
            UserDeviceStoreMaxUsers=json_data.get("UserDeviceStoreMaxUsers"),
            UserServerCert=json_data.get("UserServerCert"),
            VdomAdmin=json_data.get("VdomAdmin"),
            VdomMode=json_data.get("VdomMode"),
            Vdomparam=json_data.get("Vdomparam"),
            VipArpRange=json_data.get("VipArpRange"),
            VirtualServerCount=json_data.get("VirtualServerCount"),
            VirtualServerHardwareAcceleration=json_data.get("VirtualServerHardwareAcceleration"),
            WadAffinity=json_data.get("WadAffinity"),
            WadCsvcCsCount=json_data.get("WadCsvcCsCount"),
            WadCsvcDbCount=json_data.get("WadCsvcDbCount"),
            WadMemoryChangeGranularity=json_data.get("WadMemoryChangeGranularity"),
            WadSourceAffinity=json_data.get("WadSourceAffinity"),
            WadWorkerCount=json_data.get("WadWorkerCount"),
            WifiCaCertificate=json_data.get("WifiCaCertificate"),
            WifiCertificate=json_data.get("WifiCertificate"),
            Wimax4gUsb=json_data.get("Wimax4gUsb"),
            WirelessController=json_data.get("WirelessController"),
            WirelessControllerPort=json_data.get("WirelessControllerPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


