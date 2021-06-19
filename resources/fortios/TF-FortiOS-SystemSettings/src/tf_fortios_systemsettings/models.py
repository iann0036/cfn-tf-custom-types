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
    AllowLinkdownPath: Optional[str]
    AllowSubnetOverlap: Optional[str]
    Asymroute: Optional[str]
    Asymroute6: Optional[str]
    Asymroute6Icmp: Optional[str]
    AsymrouteIcmp: Optional[str]
    AuxiliarySession: Optional[str]
    Bfd: Optional[str]
    BfdDesiredMinTx: Optional[float]
    BfdDetectMult: Optional[float]
    BfdDontEnforceSrcPort: Optional[str]
    BfdRequiredMinRx: Optional[float]
    BlockLandAttack: Optional[str]
    CentralNat: Optional[str]
    Comments: Optional[str]
    ComplianceCheck: Optional[str]
    ConsolidatedFirewallMode: Optional[str]
    DefaultVoipAlgMode: Optional[str]
    DenyTcpWithIcmp: Optional[str]
    Device: Optional[str]
    Dhcp6ServerIp: Optional[str]
    DhcpProxy: Optional[str]
    DhcpProxyInterface: Optional[str]
    DhcpProxyInterfaceSelectMethod: Optional[str]
    DhcpServerIp: Optional[str]
    DiscoveredDeviceTimeout: Optional[float]
    DynamicSortSubtable: Optional[str]
    EcmpMaxPaths: Optional[float]
    EmailPortalCheckDns: Optional[str]
    FirewallSessionDirty: Optional[str]
    FwSessionHairpin: Optional[str]
    Gateway: Optional[str]
    Gateway6: Optional[str]
    GuiAdvancedPolicy: Optional[str]
    GuiAllowUnnamedPolicy: Optional[str]
    GuiAntivirus: Optional[str]
    GuiApProfile: Optional[str]
    GuiApplicationControl: Optional[str]
    GuiDhcpAdvanced: Optional[str]
    GuiDlp: Optional[str]
    GuiDnsDatabase: Optional[str]
    GuiDnsfilter: Optional[str]
    GuiDomainIpReputation: Optional[str]
    GuiDosPolicy: Optional[str]
    GuiDynamicProfileDisplay: Optional[str]
    GuiDynamicRouting: Optional[str]
    GuiEmailCollection: Optional[str]
    GuiEndpointControl: Optional[str]
    GuiEndpointControlAdvanced: Optional[str]
    GuiExplicitProxy: Optional[str]
    GuiFileFilter: Optional[str]
    GuiFortiapSplitTunneling: Optional[str]
    GuiFortiextenderController: Optional[str]
    GuiIcap: Optional[str]
    GuiImplicitPolicy: Optional[str]
    GuiIps: Optional[str]
    GuiLoadBalance: Optional[str]
    GuiLocalInPolicy: Optional[str]
    GuiLocalReports: Optional[str]
    GuiMulticastPolicy: Optional[str]
    GuiMultipleInterfacePolicy: Optional[str]
    GuiMultipleUtmProfiles: Optional[str]
    GuiNat4664: Optional[str]
    GuiObjectColors: Optional[str]
    GuiPerPolicyDisclaimer: Optional[str]
    GuiPolicyBasedIpsec: Optional[str]
    GuiPolicyDisclaimer: Optional[str]
    GuiPolicyLearning: Optional[str]
    GuiReplacementMessageGroups: Optional[str]
    GuiSecurityProfileGroup: Optional[str]
    GuiSpamfilter: Optional[str]
    GuiSslvpnPersonalBookmarks: Optional[str]
    GuiSslvpnRealms: Optional[str]
    GuiSwitchController: Optional[str]
    GuiThreatWeight: Optional[str]
    GuiTrafficShaping: Optional[str]
    GuiVoipProfile: Optional[str]
    GuiVpn: Optional[str]
    GuiWafProfile: Optional[str]
    GuiWanLoadBalancing: Optional[str]
    GuiWanoptCache: Optional[str]
    GuiWebfilter: Optional[str]
    GuiWebfilterAdvanced: Optional[str]
    GuiWirelessController: Optional[str]
    HttpExternalDest: Optional[str]
    Id: Optional[str]
    IkeDnFormat: Optional[str]
    IkeNattPort: Optional[float]
    IkePort: Optional[float]
    IkeQuickCrashDetect: Optional[str]
    IkeSessionResume: Optional[str]
    ImplicitAllowDns: Optional[str]
    InspectionMode: Optional[str]
    Ip: Optional[str]
    Ip6: Optional[str]
    LinkDownAccess: Optional[str]
    LldpReception: Optional[str]
    LldpTransmission: Optional[str]
    MacTtl: Optional[float]
    Manageip: Optional[str]
    Manageip6: Optional[str]
    MulticastForward: Optional[str]
    MulticastSkipPolicy: Optional[str]
    MulticastTtlNotchange: Optional[str]
    NgfwMode: Optional[str]
    Opmode: Optional[str]
    PrpTrailerAction: Optional[str]
    SccpPort: Optional[float]
    SctpSessionWithoutInit: Optional[str]
    SesDeniedTraffic: Optional[str]
    SipExpectation: Optional[str]
    SipHelper: Optional[str]
    SipNatTrace: Optional[str]
    SipSslPort: Optional[float]
    SipTcpPort: Optional[float]
    SipUdpPort: Optional[float]
    SnatHairpinTraffic: Optional[str]
    SslSshProfile: Optional[str]
    Status: Optional[str]
    StrictSrcCheck: Optional[str]
    TcpSessionWithoutSyn: Optional[str]
    Utf8SpamTagging: Optional[str]
    V4EcmpMode: Optional[str]
    Vdomparam: Optional[str]
    VpnStatsLog: Optional[str]
    VpnStatsPeriod: Optional[float]
    WccpCacheEngine: Optional[str]
    GuiDefaultPolicyColumns: Optional[Sequence["_GuiDefaultPolicyColumnsDefinition"]]

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
            AllowLinkdownPath=json_data.get("AllowLinkdownPath"),
            AllowSubnetOverlap=json_data.get("AllowSubnetOverlap"),
            Asymroute=json_data.get("Asymroute"),
            Asymroute6=json_data.get("Asymroute6"),
            Asymroute6Icmp=json_data.get("Asymroute6Icmp"),
            AsymrouteIcmp=json_data.get("AsymrouteIcmp"),
            AuxiliarySession=json_data.get("AuxiliarySession"),
            Bfd=json_data.get("Bfd"),
            BfdDesiredMinTx=json_data.get("BfdDesiredMinTx"),
            BfdDetectMult=json_data.get("BfdDetectMult"),
            BfdDontEnforceSrcPort=json_data.get("BfdDontEnforceSrcPort"),
            BfdRequiredMinRx=json_data.get("BfdRequiredMinRx"),
            BlockLandAttack=json_data.get("BlockLandAttack"),
            CentralNat=json_data.get("CentralNat"),
            Comments=json_data.get("Comments"),
            ComplianceCheck=json_data.get("ComplianceCheck"),
            ConsolidatedFirewallMode=json_data.get("ConsolidatedFirewallMode"),
            DefaultVoipAlgMode=json_data.get("DefaultVoipAlgMode"),
            DenyTcpWithIcmp=json_data.get("DenyTcpWithIcmp"),
            Device=json_data.get("Device"),
            Dhcp6ServerIp=json_data.get("Dhcp6ServerIp"),
            DhcpProxy=json_data.get("DhcpProxy"),
            DhcpProxyInterface=json_data.get("DhcpProxyInterface"),
            DhcpProxyInterfaceSelectMethod=json_data.get("DhcpProxyInterfaceSelectMethod"),
            DhcpServerIp=json_data.get("DhcpServerIp"),
            DiscoveredDeviceTimeout=json_data.get("DiscoveredDeviceTimeout"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EcmpMaxPaths=json_data.get("EcmpMaxPaths"),
            EmailPortalCheckDns=json_data.get("EmailPortalCheckDns"),
            FirewallSessionDirty=json_data.get("FirewallSessionDirty"),
            FwSessionHairpin=json_data.get("FwSessionHairpin"),
            Gateway=json_data.get("Gateway"),
            Gateway6=json_data.get("Gateway6"),
            GuiAdvancedPolicy=json_data.get("GuiAdvancedPolicy"),
            GuiAllowUnnamedPolicy=json_data.get("GuiAllowUnnamedPolicy"),
            GuiAntivirus=json_data.get("GuiAntivirus"),
            GuiApProfile=json_data.get("GuiApProfile"),
            GuiApplicationControl=json_data.get("GuiApplicationControl"),
            GuiDhcpAdvanced=json_data.get("GuiDhcpAdvanced"),
            GuiDlp=json_data.get("GuiDlp"),
            GuiDnsDatabase=json_data.get("GuiDnsDatabase"),
            GuiDnsfilter=json_data.get("GuiDnsfilter"),
            GuiDomainIpReputation=json_data.get("GuiDomainIpReputation"),
            GuiDosPolicy=json_data.get("GuiDosPolicy"),
            GuiDynamicProfileDisplay=json_data.get("GuiDynamicProfileDisplay"),
            GuiDynamicRouting=json_data.get("GuiDynamicRouting"),
            GuiEmailCollection=json_data.get("GuiEmailCollection"),
            GuiEndpointControl=json_data.get("GuiEndpointControl"),
            GuiEndpointControlAdvanced=json_data.get("GuiEndpointControlAdvanced"),
            GuiExplicitProxy=json_data.get("GuiExplicitProxy"),
            GuiFileFilter=json_data.get("GuiFileFilter"),
            GuiFortiapSplitTunneling=json_data.get("GuiFortiapSplitTunneling"),
            GuiFortiextenderController=json_data.get("GuiFortiextenderController"),
            GuiIcap=json_data.get("GuiIcap"),
            GuiImplicitPolicy=json_data.get("GuiImplicitPolicy"),
            GuiIps=json_data.get("GuiIps"),
            GuiLoadBalance=json_data.get("GuiLoadBalance"),
            GuiLocalInPolicy=json_data.get("GuiLocalInPolicy"),
            GuiLocalReports=json_data.get("GuiLocalReports"),
            GuiMulticastPolicy=json_data.get("GuiMulticastPolicy"),
            GuiMultipleInterfacePolicy=json_data.get("GuiMultipleInterfacePolicy"),
            GuiMultipleUtmProfiles=json_data.get("GuiMultipleUtmProfiles"),
            GuiNat4664=json_data.get("GuiNat4664"),
            GuiObjectColors=json_data.get("GuiObjectColors"),
            GuiPerPolicyDisclaimer=json_data.get("GuiPerPolicyDisclaimer"),
            GuiPolicyBasedIpsec=json_data.get("GuiPolicyBasedIpsec"),
            GuiPolicyDisclaimer=json_data.get("GuiPolicyDisclaimer"),
            GuiPolicyLearning=json_data.get("GuiPolicyLearning"),
            GuiReplacementMessageGroups=json_data.get("GuiReplacementMessageGroups"),
            GuiSecurityProfileGroup=json_data.get("GuiSecurityProfileGroup"),
            GuiSpamfilter=json_data.get("GuiSpamfilter"),
            GuiSslvpnPersonalBookmarks=json_data.get("GuiSslvpnPersonalBookmarks"),
            GuiSslvpnRealms=json_data.get("GuiSslvpnRealms"),
            GuiSwitchController=json_data.get("GuiSwitchController"),
            GuiThreatWeight=json_data.get("GuiThreatWeight"),
            GuiTrafficShaping=json_data.get("GuiTrafficShaping"),
            GuiVoipProfile=json_data.get("GuiVoipProfile"),
            GuiVpn=json_data.get("GuiVpn"),
            GuiWafProfile=json_data.get("GuiWafProfile"),
            GuiWanLoadBalancing=json_data.get("GuiWanLoadBalancing"),
            GuiWanoptCache=json_data.get("GuiWanoptCache"),
            GuiWebfilter=json_data.get("GuiWebfilter"),
            GuiWebfilterAdvanced=json_data.get("GuiWebfilterAdvanced"),
            GuiWirelessController=json_data.get("GuiWirelessController"),
            HttpExternalDest=json_data.get("HttpExternalDest"),
            Id=json_data.get("Id"),
            IkeDnFormat=json_data.get("IkeDnFormat"),
            IkeNattPort=json_data.get("IkeNattPort"),
            IkePort=json_data.get("IkePort"),
            IkeQuickCrashDetect=json_data.get("IkeQuickCrashDetect"),
            IkeSessionResume=json_data.get("IkeSessionResume"),
            ImplicitAllowDns=json_data.get("ImplicitAllowDns"),
            InspectionMode=json_data.get("InspectionMode"),
            Ip=json_data.get("Ip"),
            Ip6=json_data.get("Ip6"),
            LinkDownAccess=json_data.get("LinkDownAccess"),
            LldpReception=json_data.get("LldpReception"),
            LldpTransmission=json_data.get("LldpTransmission"),
            MacTtl=json_data.get("MacTtl"),
            Manageip=json_data.get("Manageip"),
            Manageip6=json_data.get("Manageip6"),
            MulticastForward=json_data.get("MulticastForward"),
            MulticastSkipPolicy=json_data.get("MulticastSkipPolicy"),
            MulticastTtlNotchange=json_data.get("MulticastTtlNotchange"),
            NgfwMode=json_data.get("NgfwMode"),
            Opmode=json_data.get("Opmode"),
            PrpTrailerAction=json_data.get("PrpTrailerAction"),
            SccpPort=json_data.get("SccpPort"),
            SctpSessionWithoutInit=json_data.get("SctpSessionWithoutInit"),
            SesDeniedTraffic=json_data.get("SesDeniedTraffic"),
            SipExpectation=json_data.get("SipExpectation"),
            SipHelper=json_data.get("SipHelper"),
            SipNatTrace=json_data.get("SipNatTrace"),
            SipSslPort=json_data.get("SipSslPort"),
            SipTcpPort=json_data.get("SipTcpPort"),
            SipUdpPort=json_data.get("SipUdpPort"),
            SnatHairpinTraffic=json_data.get("SnatHairpinTraffic"),
            SslSshProfile=json_data.get("SslSshProfile"),
            Status=json_data.get("Status"),
            StrictSrcCheck=json_data.get("StrictSrcCheck"),
            TcpSessionWithoutSyn=json_data.get("TcpSessionWithoutSyn"),
            Utf8SpamTagging=json_data.get("Utf8SpamTagging"),
            V4EcmpMode=json_data.get("V4EcmpMode"),
            Vdomparam=json_data.get("Vdomparam"),
            VpnStatsLog=json_data.get("VpnStatsLog"),
            VpnStatsPeriod=json_data.get("VpnStatsPeriod"),
            WccpCacheEngine=json_data.get("WccpCacheEngine"),
            GuiDefaultPolicyColumns=deserialize_list(json_data.get("GuiDefaultPolicyColumns"), GuiDefaultPolicyColumnsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GuiDefaultPolicyColumnsDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuiDefaultPolicyColumnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuiDefaultPolicyColumnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuiDefaultPolicyColumnsDefinition = GuiDefaultPolicyColumnsDefinition


