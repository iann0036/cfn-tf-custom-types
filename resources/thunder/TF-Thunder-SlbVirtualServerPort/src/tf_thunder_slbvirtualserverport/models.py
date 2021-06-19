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
    Action: Optional[str]
    AltProtocol1: Optional[str]
    AltProtocol2: Optional[str]
    AlternatePort: Optional[float]
    AlternatePortNumber: Optional[float]
    Auto: Optional[float]
    ClientipStickyNat: Optional[float]
    ConnLimit: Optional[float]
    CpuCompute: Optional[float]
    DefSelectionIfPrefFailed: Optional[str]
    EnablePlayeridCheck: Optional[float]
    EthFwd: Optional[float]
    EthRev: Optional[float]
    Expand: Optional[float]
    ExtendedStats: Optional[float]
    ForceRoutingMode: Optional[float]
    GslbEnable: Optional[float]
    GtpSessionLb: Optional[float]
    HaConnMirror: Optional[float]
    Id: Optional[str]
    IgnoreGlobal: Optional[float]
    IpMapList: Optional[str]
    Ipinip: Optional[float]
    L7HardwareAssist: Optional[float]
    MemoryCompute: Optional[float]
    MessageSwitching: Optional[float]
    Name: Optional[str]
    NoAutoUpOnAflex: Optional[float]
    NoDestNat: Optional[float]
    NoLogging: Optional[float]
    OnSyn: Optional[float]
    OptimizationLevel: Optional[str]
    PTemplateSipShared: Optional[float]
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
    SharedPartitionDblbTemplate: Optional[float]
    SharedPartitionDiameterTemplate: Optional[float]
    SharedPartitionDnsTemplate: Optional[float]
    SharedPartitionDohTemplate: Optional[float]
    SharedPartitionDynamicServiceTemplate: Optional[float]
    SharedPartitionExternalServiceTemplate: Optional[float]
    SharedPartitionFixTemplate: Optional[float]
    SharedPartitionHttpPolicyTemplate: Optional[float]
    SharedPartitionHttpTemplate: Optional[float]
    SharedPartitionImapPop3Template: Optional[float]
    SharedPartitionPersistCookieTemplate: Optional[float]
    SharedPartitionPersistDestinationIpTemplate: Optional[float]
    SharedPartitionPersistSourceIpTemplate: Optional[float]
    SharedPartitionPersistSslSidTemplate: Optional[float]
    SharedPartitionPolicyTemplate: Optional[float]
    SharedPartitionPool: Optional[float]
    SharedPartitionServerSslTemplate: Optional[float]
    SharedPartitionSmppTemplate: Optional[float]
    SharedPartitionSmtpTemplate: Optional[float]
    SharedPartitionTcp: Optional[float]
    SharedPartitionTcpProxyTemplate: Optional[float]
    SharedPartitionUdp: Optional[float]
    SharedPartitionVirtualPortTemplate: Optional[float]
    SkipRevHash: Optional[float]
    SnatOnVip: Optional[float]
    StatsDataAction: Optional[str]
    SubstituteSourceMac: Optional[float]
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
    TemplateDblbShared: Optional[str]
    TemplateDiameter: Optional[str]
    TemplateDiameterShared: Optional[str]
    TemplateDns: Optional[str]
    TemplateDnsShared: Optional[str]
    TemplateDoh: Optional[str]
    TemplateDohShared: Optional[str]
    TemplateDynamicService: Optional[str]
    TemplateDynamicServiceShared: Optional[str]
    TemplateExternalService: Optional[str]
    TemplateExternalServiceShared: Optional[str]
    TemplateFileInspection: Optional[str]
    TemplateFix: Optional[str]
    TemplateFixShared: Optional[str]
    TemplateFtp: Optional[str]
    TemplateHttp: Optional[str]
    TemplateHttpPolicy: Optional[str]
    TemplateHttpPolicyShared: Optional[str]
    TemplateHttpShared: Optional[str]
    TemplateImapPop3: Optional[str]
    TemplateImapPop3Shared: Optional[str]
    TemplateMqtt: Optional[str]
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
    TemplateSipShared: Optional[str]
    TemplateSmpp: Optional[str]
    TemplateSmppShared: Optional[str]
    TemplateSmtp: Optional[str]
    TemplateSmtpShared: Optional[str]
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
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Action=json_data.get("Action"),
            AltProtocol1=json_data.get("AltProtocol1"),
            AltProtocol2=json_data.get("AltProtocol2"),
            AlternatePort=json_data.get("AlternatePort"),
            AlternatePortNumber=json_data.get("AlternatePortNumber"),
            Auto=json_data.get("Auto"),
            ClientipStickyNat=json_data.get("ClientipStickyNat"),
            ConnLimit=json_data.get("ConnLimit"),
            CpuCompute=json_data.get("CpuCompute"),
            DefSelectionIfPrefFailed=json_data.get("DefSelectionIfPrefFailed"),
            EnablePlayeridCheck=json_data.get("EnablePlayeridCheck"),
            EthFwd=json_data.get("EthFwd"),
            EthRev=json_data.get("EthRev"),
            Expand=json_data.get("Expand"),
            ExtendedStats=json_data.get("ExtendedStats"),
            ForceRoutingMode=json_data.get("ForceRoutingMode"),
            GslbEnable=json_data.get("GslbEnable"),
            GtpSessionLb=json_data.get("GtpSessionLb"),
            HaConnMirror=json_data.get("HaConnMirror"),
            Id=json_data.get("Id"),
            IgnoreGlobal=json_data.get("IgnoreGlobal"),
            IpMapList=json_data.get("IpMapList"),
            Ipinip=json_data.get("Ipinip"),
            L7HardwareAssist=json_data.get("L7HardwareAssist"),
            MemoryCompute=json_data.get("MemoryCompute"),
            MessageSwitching=json_data.get("MessageSwitching"),
            Name=json_data.get("Name"),
            NoAutoUpOnAflex=json_data.get("NoAutoUpOnAflex"),
            NoDestNat=json_data.get("NoDestNat"),
            NoLogging=json_data.get("NoLogging"),
            OnSyn=json_data.get("OnSyn"),
            OptimizationLevel=json_data.get("OptimizationLevel"),
            PTemplateSipShared=json_data.get("PTemplateSipShared"),
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
            SharedPartitionDblbTemplate=json_data.get("SharedPartitionDblbTemplate"),
            SharedPartitionDiameterTemplate=json_data.get("SharedPartitionDiameterTemplate"),
            SharedPartitionDnsTemplate=json_data.get("SharedPartitionDnsTemplate"),
            SharedPartitionDohTemplate=json_data.get("SharedPartitionDohTemplate"),
            SharedPartitionDynamicServiceTemplate=json_data.get("SharedPartitionDynamicServiceTemplate"),
            SharedPartitionExternalServiceTemplate=json_data.get("SharedPartitionExternalServiceTemplate"),
            SharedPartitionFixTemplate=json_data.get("SharedPartitionFixTemplate"),
            SharedPartitionHttpPolicyTemplate=json_data.get("SharedPartitionHttpPolicyTemplate"),
            SharedPartitionHttpTemplate=json_data.get("SharedPartitionHttpTemplate"),
            SharedPartitionImapPop3Template=json_data.get("SharedPartitionImapPop3Template"),
            SharedPartitionPersistCookieTemplate=json_data.get("SharedPartitionPersistCookieTemplate"),
            SharedPartitionPersistDestinationIpTemplate=json_data.get("SharedPartitionPersistDestinationIpTemplate"),
            SharedPartitionPersistSourceIpTemplate=json_data.get("SharedPartitionPersistSourceIpTemplate"),
            SharedPartitionPersistSslSidTemplate=json_data.get("SharedPartitionPersistSslSidTemplate"),
            SharedPartitionPolicyTemplate=json_data.get("SharedPartitionPolicyTemplate"),
            SharedPartitionPool=json_data.get("SharedPartitionPool"),
            SharedPartitionServerSslTemplate=json_data.get("SharedPartitionServerSslTemplate"),
            SharedPartitionSmppTemplate=json_data.get("SharedPartitionSmppTemplate"),
            SharedPartitionSmtpTemplate=json_data.get("SharedPartitionSmtpTemplate"),
            SharedPartitionTcp=json_data.get("SharedPartitionTcp"),
            SharedPartitionTcpProxyTemplate=json_data.get("SharedPartitionTcpProxyTemplate"),
            SharedPartitionUdp=json_data.get("SharedPartitionUdp"),
            SharedPartitionVirtualPortTemplate=json_data.get("SharedPartitionVirtualPortTemplate"),
            SkipRevHash=json_data.get("SkipRevHash"),
            SnatOnVip=json_data.get("SnatOnVip"),
            StatsDataAction=json_data.get("StatsDataAction"),
            SubstituteSourceMac=json_data.get("SubstituteSourceMac"),
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
            TemplateDblbShared=json_data.get("TemplateDblbShared"),
            TemplateDiameter=json_data.get("TemplateDiameter"),
            TemplateDiameterShared=json_data.get("TemplateDiameterShared"),
            TemplateDns=json_data.get("TemplateDns"),
            TemplateDnsShared=json_data.get("TemplateDnsShared"),
            TemplateDoh=json_data.get("TemplateDoh"),
            TemplateDohShared=json_data.get("TemplateDohShared"),
            TemplateDynamicService=json_data.get("TemplateDynamicService"),
            TemplateDynamicServiceShared=json_data.get("TemplateDynamicServiceShared"),
            TemplateExternalService=json_data.get("TemplateExternalService"),
            TemplateExternalServiceShared=json_data.get("TemplateExternalServiceShared"),
            TemplateFileInspection=json_data.get("TemplateFileInspection"),
            TemplateFix=json_data.get("TemplateFix"),
            TemplateFixShared=json_data.get("TemplateFixShared"),
            TemplateFtp=json_data.get("TemplateFtp"),
            TemplateHttp=json_data.get("TemplateHttp"),
            TemplateHttpPolicy=json_data.get("TemplateHttpPolicy"),
            TemplateHttpPolicyShared=json_data.get("TemplateHttpPolicyShared"),
            TemplateHttpShared=json_data.get("TemplateHttpShared"),
            TemplateImapPop3=json_data.get("TemplateImapPop3"),
            TemplateImapPop3Shared=json_data.get("TemplateImapPop3Shared"),
            TemplateMqtt=json_data.get("TemplateMqtt"),
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
            TemplateSipShared=json_data.get("TemplateSipShared"),
            TemplateSmpp=json_data.get("TemplateSmpp"),
            TemplateSmppShared=json_data.get("TemplateSmppShared"),
            TemplateSmtp=json_data.get("TemplateSmtp"),
            TemplateSmtpShared=json_data.get("TemplateSmtpShared"),
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
_ResourceModel = ResourceModel


@dataclass
class AclIdListDefinition(BaseModel):
    AclId: Optional[float]
    AclIdSeqNum: Optional[float]
    AclIdSeqNumShared: Optional[float]
    AclIdShared: Optional[float]
    AclIdSrcNatPool: Optional[str]
    AclIdSrcNatPoolShared: Optional[str]
    SharedPartitionPoolId: Optional[float]
    VAclIdSeqNum: Optional[float]
    VAclIdSeqNumShared: Optional[float]
    VAclIdSrcNatPool: Optional[str]
    VAclIdSrcNatPoolShared: Optional[str]
    VSharedPartitionPoolId: Optional[float]

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
            AclIdShared=json_data.get("AclIdShared"),
            AclIdSrcNatPool=json_data.get("AclIdSrcNatPool"),
            AclIdSrcNatPoolShared=json_data.get("AclIdSrcNatPoolShared"),
            SharedPartitionPoolId=json_data.get("SharedPartitionPoolId"),
            VAclIdSeqNum=json_data.get("VAclIdSeqNum"),
            VAclIdSeqNumShared=json_data.get("VAclIdSeqNumShared"),
            VAclIdSrcNatPool=json_data.get("VAclIdSrcNatPool"),
            VAclIdSrcNatPoolShared=json_data.get("VAclIdSrcNatPoolShared"),
            VSharedPartitionPoolId=json_data.get("VSharedPartitionPoolId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclIdListDefinition = AclIdListDefinition


@dataclass
class AclNameListDefinition(BaseModel):
    AclName: Optional[str]
    AclNameSeqNum: Optional[float]
    AclNameSeqNumShared: Optional[float]
    AclNameShared: Optional[str]
    AclNameSrcNatPool: Optional[str]
    AclNameSrcNatPoolShared: Optional[str]
    SharedPartitionPoolName: Optional[float]
    VAclNameSeqNum: Optional[float]
    VAclNameSeqNumShared: Optional[float]
    VAclNameSrcNatPool: Optional[str]
    VAclNameSrcNatPoolShared: Optional[str]
    VSharedPartitionPoolName: Optional[float]

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
            AclNameShared=json_data.get("AclNameShared"),
            AclNameSrcNatPool=json_data.get("AclNameSrcNatPool"),
            AclNameSrcNatPoolShared=json_data.get("AclNameSrcNatPoolShared"),
            SharedPartitionPoolName=json_data.get("SharedPartitionPoolName"),
            VAclNameSeqNum=json_data.get("VAclNameSeqNum"),
            VAclNameSeqNumShared=json_data.get("VAclNameSeqNumShared"),
            VAclNameSrcNatPool=json_data.get("VAclNameSrcNatPool"),
            VAclNameSrcNatPoolShared=json_data.get("VAclNameSrcNatPoolShared"),
            VSharedPartitionPoolName=json_data.get("VSharedPartitionPoolName"),
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


