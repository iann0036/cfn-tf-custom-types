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
    AclId: Optional[float]
    AclIdShared: Optional[float]
    AclName: Optional[str]
    AclNameShared: Optional[str]
    ArpDisable: Optional[float]
    Description: Optional[str]
    DisableVipAdv: Optional[float]
    EnableDisableAction: Optional[str]
    Ethernet: Optional[float]
    ExtendedStats: Optional[float]
    HaDynamic: Optional[float]
    Id: Optional[str]
    IpAddress: Optional[str]
    Ipv6Acl: Optional[str]
    Ipv6AclShared: Optional[str]
    Name: Optional[str]
    Netmask: Optional[str]
    RedistributeRouteMap: Optional[str]
    RedistributionFlagged: Optional[float]
    SharedPartitionPolicyTemplate: Optional[float]
    StatsDataAction: Optional[str]
    TemplateLogging: Optional[str]
    TemplatePolicy: Optional[str]
    TemplatePolicyAcl: Optional[str]
    TemplatePolicyAclShared: Optional[str]
    TemplatePolicyAddress: Optional[str]
    TemplatePolicyShared: Optional[str]
    TemplateScaleout: Optional[str]
    TemplateVirtualServer: Optional[str]
    UseIfIp: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    Vrid: Optional[float]
    MigrateVip: Optional[Sequence["_MigrateVipDefinition"]]
    PortList: Optional[Sequence["_PortListDefinition"]]

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
            AclId=json_data.get("AclId"),
            AclIdShared=json_data.get("AclIdShared"),
            AclName=json_data.get("AclName"),
            AclNameShared=json_data.get("AclNameShared"),
            ArpDisable=json_data.get("ArpDisable"),
            Description=json_data.get("Description"),
            DisableVipAdv=json_data.get("DisableVipAdv"),
            EnableDisableAction=json_data.get("EnableDisableAction"),
            Ethernet=json_data.get("Ethernet"),
            ExtendedStats=json_data.get("ExtendedStats"),
            HaDynamic=json_data.get("HaDynamic"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            Ipv6Acl=json_data.get("Ipv6Acl"),
            Ipv6AclShared=json_data.get("Ipv6AclShared"),
            Name=json_data.get("Name"),
            Netmask=json_data.get("Netmask"),
            RedistributeRouteMap=json_data.get("RedistributeRouteMap"),
            RedistributionFlagged=json_data.get("RedistributionFlagged"),
            SharedPartitionPolicyTemplate=json_data.get("SharedPartitionPolicyTemplate"),
            StatsDataAction=json_data.get("StatsDataAction"),
            TemplateLogging=json_data.get("TemplateLogging"),
            TemplatePolicy=json_data.get("TemplatePolicy"),
            TemplatePolicyAcl=json_data.get("TemplatePolicyAcl"),
            TemplatePolicyAclShared=json_data.get("TemplatePolicyAclShared"),
            TemplatePolicyAddress=json_data.get("TemplatePolicyAddress"),
            TemplatePolicyShared=json_data.get("TemplatePolicyShared"),
            TemplateScaleout=json_data.get("TemplateScaleout"),
            TemplateVirtualServer=json_data.get("TemplateVirtualServer"),
            UseIfIp=json_data.get("UseIfIp"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Vrid=json_data.get("Vrid"),
            MigrateVip=deserialize_list(json_data.get("MigrateVip"), MigrateVipDefinition),
            PortList=deserialize_list(json_data.get("PortList"), PortListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MigrateVipDefinition(BaseModel):
    CancelMigration: Optional[float]
    FinishMigration: Optional[float]
    TargetDataCpu: Optional[float]
    TargetFloatingIpv4: Optional[str]
    TargetFloatingTemplatePolicy: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MigrateVipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MigrateVipDefinition"]:
        if not json_data:
            return None
        return cls(
            CancelMigration=json_data.get("CancelMigration"),
            FinishMigration=json_data.get("FinishMigration"),
            TargetDataCpu=json_data.get("TargetDataCpu"),
            TargetFloatingIpv4=json_data.get("TargetFloatingIpv4"),
            TargetFloatingTemplatePolicy=json_data.get("TargetFloatingTemplatePolicy"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MigrateVipDefinition = MigrateVipDefinition


@dataclass
class PortListDefinition(BaseModel):
    Action: Optional[str]
    AltProtocol1: Optional[str]
    AltProtocol2: Optional[str]
    AlternatePort: Optional[float]
    AlternatePortNumber: Optional[float]
    Auto: Optional[float]
    ClientipStickyNat: Optional[float]
    ConnLimit: Optional[float]
    DefSelectionIfPrefFailed: Optional[str]
    EnablePlayeridCheck: Optional[float]
    EthFwd: Optional[float]
    EthRev: Optional[float]
    Expand: Optional[float]
    ExtendedStats: Optional[float]
    ForceRoutingMode: Optional[float]
    GslbEnable: Optional[float]
    HaConnMirror: Optional[float]
    IpMapList: Optional[str]
    Ipinip: Optional[float]
    Ipv6Acl: Optional[str]
    L7HardwareAssist: Optional[float]
    MessageSwitching: Optional[float]
    Name: Optional[str]
    NoAutoUpOnAflex: Optional[float]
    NoDestNat: Optional[float]
    NoLogging: Optional[float]
    OnSyn: Optional[float]
    OptimizationLevel: Optional[str]
    PersistType: Optional[str]
    Pool: Optional[str]
    PoolShared: Optional[str]
    PortNumber: Optional[float]
    PortTranslation: Optional[float]
    Precedence: Optional[float]
    Protocol: Optional[str]
    Range: Optional[float]
    Rate: Optional[float]
    RedirectToHttps: Optional[float]
    ReqFail: Optional[float]
    Reset: Optional[float]
    ResetOnServerSelectionFail: Optional[float]
    RtpSipCallIdMatch: Optional[float]
    ScaleoutBucketCount: Optional[float]
    ScaleoutDeviceGroup: Optional[float]
    Secs: Optional[float]
    ServSelFail: Optional[float]
    ServiceGroup: Optional[str]
    SharedPartitionCacheTemplate: Optional[float]
    SharedPartitionClientSslTemplate: Optional[float]
    SharedPartitionConnectionReuseTemplate: Optional[float]
    SharedPartitionDiameterTemplate: Optional[float]
    SharedPartitionDnsTemplate: Optional[float]
    SharedPartitionDynamicServiceTemplate: Optional[float]
    SharedPartitionExternalServiceTemplate: Optional[float]
    SharedPartitionHttpPolicyTemplate: Optional[float]
    SharedPartitionHttpTemplate: Optional[float]
    SharedPartitionPersistCookieTemplate: Optional[float]
    SharedPartitionPersistDestinationIpTemplate: Optional[float]
    SharedPartitionPersistSourceIpTemplate: Optional[float]
    SharedPartitionPersistSslSidTemplate: Optional[float]
    SharedPartitionPolicyTemplate: Optional[float]
    SharedPartitionPool: Optional[float]
    SharedPartitionServerSslTemplate: Optional[float]
    SharedPartitionTcp: Optional[float]
    SharedPartitionTcpProxyTemplate: Optional[float]
    SharedPartitionUdp: Optional[float]
    SharedPartitionVirtualPortTemplate: Optional[float]
    SkipRevHash: Optional[float]
    SnatOnVip: Optional[float]
    StatsDataAction: Optional[str]
    SupportHttp2: Optional[float]
    SynCookie: Optional[float]
    TemplateCache: Optional[str]
    TemplateCacheShared: Optional[str]
    TemplateClientSsh: Optional[str]
    TemplateClientSsl: Optional[str]
    TemplateClientSslShared: Optional[str]
    TemplateConnectionReuse: Optional[str]
    TemplateConnectionReuseShared: Optional[str]
    TemplateDblb: Optional[str]
    TemplateDiameter: Optional[str]
    TemplateDiameterShared: Optional[str]
    TemplateDns: Optional[str]
    TemplateDnsShared: Optional[str]
    TemplateDynamicService: Optional[str]
    TemplateDynamicServiceShared: Optional[str]
    TemplateExternalService: Optional[str]
    TemplateExternalServiceShared: Optional[str]
    TemplateFileInspection: Optional[str]
    TemplateFix: Optional[str]
    TemplateFtp: Optional[str]
    TemplateHttp: Optional[str]
    TemplateHttpPolicy: Optional[str]
    TemplateHttpPolicyShared: Optional[str]
    TemplateHttpShared: Optional[str]
    TemplateImapPop3: Optional[str]
    TemplatePersistCookie: Optional[str]
    TemplatePersistCookieShared: Optional[str]
    TemplatePersistDestinationIp: Optional[str]
    TemplatePersistDestinationIpShared: Optional[str]
    TemplatePersistSourceIp: Optional[str]
    TemplatePersistSourceIpShared: Optional[str]
    TemplatePersistSslSid: Optional[str]
    TemplatePersistSslSidShared: Optional[str]
    TemplatePolicy: Optional[str]
    TemplatePolicyShared: Optional[str]
    TemplateReqmodIcap: Optional[str]
    TemplateRespmodIcap: Optional[str]
    TemplateScaleout: Optional[str]
    TemplateServerSsh: Optional[str]
    TemplateServerSsl: Optional[str]
    TemplateServerSslShared: Optional[str]
    TemplateSip: Optional[str]
    TemplateSmpp: Optional[str]
    TemplateSmtp: Optional[str]
    TemplateSsli: Optional[str]
    TemplateTcp: Optional[str]
    TemplateTcpProxy: Optional[str]
    TemplateTcpProxyClient: Optional[str]
    TemplateTcpProxyServer: Optional[str]
    TemplateTcpProxyShared: Optional[str]
    TemplateTcpShared: Optional[str]
    TemplateUdp: Optional[str]
    TemplateUdpShared: Optional[str]
    TemplateVirtualPort: Optional[str]
    TemplateVirtualPortShared: Optional[str]
    TrunkFwd: Optional[float]
    TrunkRev: Optional[float]
    UseAlternatePort: Optional[float]
    UseCgnv6: Optional[float]
    UseDefaultIfNoServer: Optional[float]
    UseRcvHopForResp: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    View: Optional[float]
    WafTemplate: Optional[str]
    WhenDown: Optional[float]
    WhenDownProtocol2: Optional[float]
    AclIdList: Optional[Sequence["_AclIdListDefinition"]]
    AclNameList: Optional[Sequence["_AclNameListDefinition"]]
    AflexScripts: Optional[Sequence["_AflexScriptsDefinition"]]
    AuthCfg: Optional[Sequence["_AuthCfgDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PortListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AltProtocol1=json_data.get("AltProtocol1"),
            AltProtocol2=json_data.get("AltProtocol2"),
            AlternatePort=json_data.get("AlternatePort"),
            AlternatePortNumber=json_data.get("AlternatePortNumber"),
            Auto=json_data.get("Auto"),
            ClientipStickyNat=json_data.get("ClientipStickyNat"),
            ConnLimit=json_data.get("ConnLimit"),
            DefSelectionIfPrefFailed=json_data.get("DefSelectionIfPrefFailed"),
            EnablePlayeridCheck=json_data.get("EnablePlayeridCheck"),
            EthFwd=json_data.get("EthFwd"),
            EthRev=json_data.get("EthRev"),
            Expand=json_data.get("Expand"),
            ExtendedStats=json_data.get("ExtendedStats"),
            ForceRoutingMode=json_data.get("ForceRoutingMode"),
            GslbEnable=json_data.get("GslbEnable"),
            HaConnMirror=json_data.get("HaConnMirror"),
            IpMapList=json_data.get("IpMapList"),
            Ipinip=json_data.get("Ipinip"),
            Ipv6Acl=json_data.get("Ipv6Acl"),
            L7HardwareAssist=json_data.get("L7HardwareAssist"),
            MessageSwitching=json_data.get("MessageSwitching"),
            Name=json_data.get("Name"),
            NoAutoUpOnAflex=json_data.get("NoAutoUpOnAflex"),
            NoDestNat=json_data.get("NoDestNat"),
            NoLogging=json_data.get("NoLogging"),
            OnSyn=json_data.get("OnSyn"),
            OptimizationLevel=json_data.get("OptimizationLevel"),
            PersistType=json_data.get("PersistType"),
            Pool=json_data.get("Pool"),
            PoolShared=json_data.get("PoolShared"),
            PortNumber=json_data.get("PortNumber"),
            PortTranslation=json_data.get("PortTranslation"),
            Precedence=json_data.get("Precedence"),
            Protocol=json_data.get("Protocol"),
            Range=json_data.get("Range"),
            Rate=json_data.get("Rate"),
            RedirectToHttps=json_data.get("RedirectToHttps"),
            ReqFail=json_data.get("ReqFail"),
            Reset=json_data.get("Reset"),
            ResetOnServerSelectionFail=json_data.get("ResetOnServerSelectionFail"),
            RtpSipCallIdMatch=json_data.get("RtpSipCallIdMatch"),
            ScaleoutBucketCount=json_data.get("ScaleoutBucketCount"),
            ScaleoutDeviceGroup=json_data.get("ScaleoutDeviceGroup"),
            Secs=json_data.get("Secs"),
            ServSelFail=json_data.get("ServSelFail"),
            ServiceGroup=json_data.get("ServiceGroup"),
            SharedPartitionCacheTemplate=json_data.get("SharedPartitionCacheTemplate"),
            SharedPartitionClientSslTemplate=json_data.get("SharedPartitionClientSslTemplate"),
            SharedPartitionConnectionReuseTemplate=json_data.get("SharedPartitionConnectionReuseTemplate"),
            SharedPartitionDiameterTemplate=json_data.get("SharedPartitionDiameterTemplate"),
            SharedPartitionDnsTemplate=json_data.get("SharedPartitionDnsTemplate"),
            SharedPartitionDynamicServiceTemplate=json_data.get("SharedPartitionDynamicServiceTemplate"),
            SharedPartitionExternalServiceTemplate=json_data.get("SharedPartitionExternalServiceTemplate"),
            SharedPartitionHttpPolicyTemplate=json_data.get("SharedPartitionHttpPolicyTemplate"),
            SharedPartitionHttpTemplate=json_data.get("SharedPartitionHttpTemplate"),
            SharedPartitionPersistCookieTemplate=json_data.get("SharedPartitionPersistCookieTemplate"),
            SharedPartitionPersistDestinationIpTemplate=json_data.get("SharedPartitionPersistDestinationIpTemplate"),
            SharedPartitionPersistSourceIpTemplate=json_data.get("SharedPartitionPersistSourceIpTemplate"),
            SharedPartitionPersistSslSidTemplate=json_data.get("SharedPartitionPersistSslSidTemplate"),
            SharedPartitionPolicyTemplate=json_data.get("SharedPartitionPolicyTemplate"),
            SharedPartitionPool=json_data.get("SharedPartitionPool"),
            SharedPartitionServerSslTemplate=json_data.get("SharedPartitionServerSslTemplate"),
            SharedPartitionTcp=json_data.get("SharedPartitionTcp"),
            SharedPartitionTcpProxyTemplate=json_data.get("SharedPartitionTcpProxyTemplate"),
            SharedPartitionUdp=json_data.get("SharedPartitionUdp"),
            SharedPartitionVirtualPortTemplate=json_data.get("SharedPartitionVirtualPortTemplate"),
            SkipRevHash=json_data.get("SkipRevHash"),
            SnatOnVip=json_data.get("SnatOnVip"),
            StatsDataAction=json_data.get("StatsDataAction"),
            SupportHttp2=json_data.get("SupportHttp2"),
            SynCookie=json_data.get("SynCookie"),
            TemplateCache=json_data.get("TemplateCache"),
            TemplateCacheShared=json_data.get("TemplateCacheShared"),
            TemplateClientSsh=json_data.get("TemplateClientSsh"),
            TemplateClientSsl=json_data.get("TemplateClientSsl"),
            TemplateClientSslShared=json_data.get("TemplateClientSslShared"),
            TemplateConnectionReuse=json_data.get("TemplateConnectionReuse"),
            TemplateConnectionReuseShared=json_data.get("TemplateConnectionReuseShared"),
            TemplateDblb=json_data.get("TemplateDblb"),
            TemplateDiameter=json_data.get("TemplateDiameter"),
            TemplateDiameterShared=json_data.get("TemplateDiameterShared"),
            TemplateDns=json_data.get("TemplateDns"),
            TemplateDnsShared=json_data.get("TemplateDnsShared"),
            TemplateDynamicService=json_data.get("TemplateDynamicService"),
            TemplateDynamicServiceShared=json_data.get("TemplateDynamicServiceShared"),
            TemplateExternalService=json_data.get("TemplateExternalService"),
            TemplateExternalServiceShared=json_data.get("TemplateExternalServiceShared"),
            TemplateFileInspection=json_data.get("TemplateFileInspection"),
            TemplateFix=json_data.get("TemplateFix"),
            TemplateFtp=json_data.get("TemplateFtp"),
            TemplateHttp=json_data.get("TemplateHttp"),
            TemplateHttpPolicy=json_data.get("TemplateHttpPolicy"),
            TemplateHttpPolicyShared=json_data.get("TemplateHttpPolicyShared"),
            TemplateHttpShared=json_data.get("TemplateHttpShared"),
            TemplateImapPop3=json_data.get("TemplateImapPop3"),
            TemplatePersistCookie=json_data.get("TemplatePersistCookie"),
            TemplatePersistCookieShared=json_data.get("TemplatePersistCookieShared"),
            TemplatePersistDestinationIp=json_data.get("TemplatePersistDestinationIp"),
            TemplatePersistDestinationIpShared=json_data.get("TemplatePersistDestinationIpShared"),
            TemplatePersistSourceIp=json_data.get("TemplatePersistSourceIp"),
            TemplatePersistSourceIpShared=json_data.get("TemplatePersistSourceIpShared"),
            TemplatePersistSslSid=json_data.get("TemplatePersistSslSid"),
            TemplatePersistSslSidShared=json_data.get("TemplatePersistSslSidShared"),
            TemplatePolicy=json_data.get("TemplatePolicy"),
            TemplatePolicyShared=json_data.get("TemplatePolicyShared"),
            TemplateReqmodIcap=json_data.get("TemplateReqmodIcap"),
            TemplateRespmodIcap=json_data.get("TemplateRespmodIcap"),
            TemplateScaleout=json_data.get("TemplateScaleout"),
            TemplateServerSsh=json_data.get("TemplateServerSsh"),
            TemplateServerSsl=json_data.get("TemplateServerSsl"),
            TemplateServerSslShared=json_data.get("TemplateServerSslShared"),
            TemplateSip=json_data.get("TemplateSip"),
            TemplateSmpp=json_data.get("TemplateSmpp"),
            TemplateSmtp=json_data.get("TemplateSmtp"),
            TemplateSsli=json_data.get("TemplateSsli"),
            TemplateTcp=json_data.get("TemplateTcp"),
            TemplateTcpProxy=json_data.get("TemplateTcpProxy"),
            TemplateTcpProxyClient=json_data.get("TemplateTcpProxyClient"),
            TemplateTcpProxyServer=json_data.get("TemplateTcpProxyServer"),
            TemplateTcpProxyShared=json_data.get("TemplateTcpProxyShared"),
            TemplateTcpShared=json_data.get("TemplateTcpShared"),
            TemplateUdp=json_data.get("TemplateUdp"),
            TemplateUdpShared=json_data.get("TemplateUdpShared"),
            TemplateVirtualPort=json_data.get("TemplateVirtualPort"),
            TemplateVirtualPortShared=json_data.get("TemplateVirtualPortShared"),
            TrunkFwd=json_data.get("TrunkFwd"),
            TrunkRev=json_data.get("TrunkRev"),
            UseAlternatePort=json_data.get("UseAlternatePort"),
            UseCgnv6=json_data.get("UseCgnv6"),
            UseDefaultIfNoServer=json_data.get("UseDefaultIfNoServer"),
            UseRcvHopForResp=json_data.get("UseRcvHopForResp"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            View=json_data.get("View"),
            WafTemplate=json_data.get("WafTemplate"),
            WhenDown=json_data.get("WhenDown"),
            WhenDownProtocol2=json_data.get("WhenDownProtocol2"),
            AclIdList=deserialize_list(json_data.get("AclIdList"), AclIdListDefinition),
            AclNameList=deserialize_list(json_data.get("AclNameList"), AclNameListDefinition),
            AflexScripts=deserialize_list(json_data.get("AflexScripts"), AflexScriptsDefinition),
            AuthCfg=deserialize_list(json_data.get("AuthCfg"), AuthCfgDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortListDefinition = PortListDefinition


@dataclass
class AclIdListDefinition(BaseModel):
    AclId: Optional[float]
    AclIdSeqNum: Optional[float]
    AclIdSeqNumShared: Optional[float]
    AclIdSrcNatPool: Optional[str]
    AclIdSrcNatPoolShared: Optional[str]
    SharedPartitionPoolId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AclIdListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AclIdListDefinition"]:
        if not json_data:
            return None
        return cls(
            AclId=json_data.get("AclId"),
            AclIdSeqNum=json_data.get("AclIdSeqNum"),
            AclIdSeqNumShared=json_data.get("AclIdSeqNumShared"),
            AclIdSrcNatPool=json_data.get("AclIdSrcNatPool"),
            AclIdSrcNatPoolShared=json_data.get("AclIdSrcNatPoolShared"),
            SharedPartitionPoolId=json_data.get("SharedPartitionPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclIdListDefinition = AclIdListDefinition


@dataclass
class AclNameListDefinition(BaseModel):
    AclName: Optional[str]
    AclNameSeqNum: Optional[float]
    AclNameSeqNumShared: Optional[float]
    AclNameSrcNatPool: Optional[str]
    AclNameSrcNatPoolShared: Optional[str]
    SharedPartitionPoolName: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AclNameListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AclNameListDefinition"]:
        if not json_data:
            return None
        return cls(
            AclName=json_data.get("AclName"),
            AclNameSeqNum=json_data.get("AclNameSeqNum"),
            AclNameSeqNumShared=json_data.get("AclNameSeqNumShared"),
            AclNameSrcNatPool=json_data.get("AclNameSrcNatPool"),
            AclNameSrcNatPoolShared=json_data.get("AclNameSrcNatPoolShared"),
            SharedPartitionPoolName=json_data.get("SharedPartitionPoolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclNameListDefinition = AclNameListDefinition


@dataclass
class AflexScriptsDefinition(BaseModel):
    Aflex: Optional[str]
    AflexShared: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AflexScriptsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AflexScriptsDefinition"]:
        if not json_data:
            return None
        return cls(
            Aflex=json_data.get("Aflex"),
            AflexShared=json_data.get("AflexShared"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AflexScriptsDefinition = AflexScriptsDefinition


@dataclass
class AuthCfgDefinition(BaseModel):
    AaaPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            AaaPolicy=json_data.get("AaaPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthCfgDefinition = AuthCfgDefinition


@dataclass
class SamplingEnableDefinition(BaseModel):
    Counters1: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingEnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingEnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Counters1=json_data.get("Counters1"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingEnableDefinition = SamplingEnableDefinition


