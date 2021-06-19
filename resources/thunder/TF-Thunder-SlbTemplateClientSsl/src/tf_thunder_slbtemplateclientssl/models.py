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
    AdGroupList: Optional[str]
    AlertType: Optional[str]
    AuthSg: Optional[str]
    AuthSgDn: Optional[float]
    AuthSgFilter: Optional[str]
    AuthUsername: Optional[str]
    AuthUsernameAttribute: Optional[str]
    AuthenName: Optional[str]
    Authorization: Optional[float]
    BypassCertIssuerClassListName: Optional[str]
    BypassCertSanClassListName: Optional[str]
    BypassCertSubjectClassListName: Optional[str]
    CachePersistenceListName: Optional[str]
    CaseInsensitive: Optional[float]
    Cert: Optional[str]
    CertAltPartitionShared: Optional[float]
    CertAlternate: Optional[str]
    CertRevokeAction: Optional[str]
    CertSharedStr: Optional[str]
    CertUnknownAction: Optional[str]
    ChainCert: Optional[str]
    ChainCertSharedStr: Optional[str]
    ClassListName: Optional[str]
    ClientAuthCaseInsensitive: Optional[float]
    ClientAuthClassList: Optional[str]
    ClientCertificate: Optional[str]
    CloseNotify: Optional[float]
    Dgversion: Optional[float]
    DhType: Optional[str]
    DirectClientServerAuth: Optional[float]
    DisableSslv3: Optional[float]
    EarlyData: Optional[float]
    EnableTlsAlertLogging: Optional[float]
    ExceptionAdGroupList: Optional[str]
    ExceptionCertificateIssuerClName: Optional[str]
    ExceptionCertificateSanClName: Optional[str]
    ExceptionCertificateSubjectClName: Optional[str]
    ExceptionSniClName: Optional[str]
    ExceptionUserNameList: Optional[str]
    ExpireHours: Optional[float]
    ForwardEncrypted: Optional[str]
    ForwardPassphrase: Optional[str]
    ForwardProxyAltSign: Optional[float]
    ForwardProxyBlockMessage: Optional[str]
    ForwardProxyCaCert: Optional[str]
    ForwardProxyCaKey: Optional[str]
    ForwardProxyCertCacheLimit: Optional[float]
    ForwardProxyCertCacheTimeout: Optional[float]
    ForwardProxyCertExpiry: Optional[float]
    ForwardProxyCertNotReadyAction: Optional[str]
    ForwardProxyCertRevokeAction: Optional[float]
    ForwardProxyCertUnknownAction: Optional[float]
    ForwardProxyCrlDisable: Optional[float]
    ForwardProxyDecryptedDscp: Optional[float]
    ForwardProxyDecryptedDscpBypass: Optional[float]
    ForwardProxyEnable: Optional[float]
    ForwardProxyFailsafeDisable: Optional[float]
    ForwardProxyLogDisable: Optional[float]
    ForwardProxyNoSharedCipherAction: Optional[float]
    ForwardProxyNoSniAction: Optional[str]
    ForwardProxyOcspDisable: Optional[float]
    ForwardProxyRequireSniCertMatched: Optional[str]
    ForwardProxySelfsignRedir: Optional[float]
    ForwardProxySslVersion: Optional[float]
    ForwardProxyVerifyCertFailAction: Optional[float]
    FpAltCert: Optional[str]
    FpAltEncrypted: Optional[str]
    FpAltKey: Optional[str]
    FpAltPassphrase: Optional[str]
    FpAltShared: Optional[float]
    FpCaKeyShared: Optional[float]
    FpCaShared: Optional[float]
    FpCertExtAiaCaIssuers: Optional[str]
    FpCertExtAiaOcsp: Optional[str]
    FpCertExtCrldp: Optional[str]
    FpCertFetchAutonat: Optional[str]
    FpCertFetchAutonatPrecedence: Optional[float]
    FpCertFetchNatpoolName: Optional[str]
    FpCertFetchNatpoolNameShared: Optional[str]
    FpCertFetchNatpoolPrecedence: Optional[float]
    HandshakeLoggingEnable: Optional[float]
    HsmType: Optional[str]
    Id: Optional[str]
    InspectCertificateIssuerClName: Optional[str]
    InspectCertificateSanClName: Optional[str]
    InspectCertificateSubjectClName: Optional[str]
    InspectListName: Optional[str]
    Key: Optional[str]
    KeyAltEncrypted: Optional[str]
    KeyAltPartitionShared: Optional[float]
    KeyAltPassphrase: Optional[str]
    KeyAlternate: Optional[str]
    KeyEncrypted: Optional[str]
    KeyPassphrase: Optional[str]
    KeySharedEncrypted: Optional[str]
    KeySharedPassphrase: Optional[str]
    KeySharedStr: Optional[str]
    LdapBaseDnFromCert: Optional[float]
    LdapSearchFilter: Optional[str]
    LocalLogging: Optional[float]
    Name: Optional[str]
    NoAntiReplay: Optional[float]
    NoSharedCipherAction: Optional[str]
    NonSslBypassL4session: Optional[float]
    NonSslBypassServiceGroup: Optional[str]
    Notafter: Optional[float]
    Notafterday: Optional[float]
    Notaftermonth: Optional[float]
    Notafteryear: Optional[float]
    Notbefore: Optional[float]
    Notbeforeday: Optional[float]
    Notbeforemonth: Optional[float]
    Notbeforeyear: Optional[float]
    OcspStapling: Optional[float]
    OcspstCaCert: Optional[str]
    OcspstOcsp: Optional[float]
    OcspstSg: Optional[str]
    OcspstSgDays: Optional[float]
    OcspstSgHours: Optional[float]
    OcspstSgMinutes: Optional[float]
    OcspstSgTimeout: Optional[float]
    OcspstSrvr: Optional[str]
    OcspstSrvrDays: Optional[float]
    OcspstSrvrHours: Optional[float]
    OcspstSrvrMinutes: Optional[float]
    OcspstSrvrTimeout: Optional[float]
    RenegotiationDisable: Optional[float]
    RequireWebCategory: Optional[float]
    ServerNameAutoMap: Optional[float]
    SessionCacheSize: Optional[float]
    SessionCacheTimeout: Optional[float]
    SessionTicketDisable: Optional[float]
    SessionTicketLifetime: Optional[float]
    SharedPartitionCipherTemplate: Optional[float]
    SharedPartitionPool: Optional[float]
    SniEnableLog: Optional[float]
    SslFalseStartDisable: Optional[float]
    SsliLogging: Optional[float]
    Sslilogging: Optional[str]
    Sslv2BypassServiceGroup: Optional[str]
    TemplateCipher: Optional[str]
    TemplateCipherShared: Optional[str]
    TemplateHsm: Optional[str]
    UserNameList: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    VerifyCertFailAction: Optional[str]
    Version: Optional[float]
    BypassCertIssuerMultiClassList: Optional[Sequence["_BypassCertIssuerMultiClassListDefinition"]]
    BypassCertSanMultiClassList: Optional[Sequence["_BypassCertSanMultiClassListDefinition"]]
    BypassCertSubjectMultiClassList: Optional[Sequence["_BypassCertSubjectMultiClassListDefinition"]]
    CaCerts: Optional[Sequence["_CaCertsDefinition"]]
    CertificateIssuerContainsList: Optional[Sequence["_CertificateIssuerContainsListDefinition"]]
    CertificateIssuerEndsWithList: Optional[Sequence["_CertificateIssuerEndsWithListDefinition"]]
    CertificateIssuerEqualsList: Optional[Sequence["_CertificateIssuerEqualsListDefinition"]]
    CertificateIssuerStartsWithList: Optional[Sequence["_CertificateIssuerStartsWithListDefinition"]]
    CertificateList: Optional[Sequence["_CertificateListDefinition"]]
    CertificateSanContainsList: Optional[Sequence["_CertificateSanContainsListDefinition"]]
    CertificateSanEndsWithList: Optional[Sequence["_CertificateSanEndsWithListDefinition"]]
    CertificateSanEqualsList: Optional[Sequence["_CertificateSanEqualsListDefinition"]]
    CertificateSanStartsWithList: Optional[Sequence["_CertificateSanStartsWithListDefinition"]]
    CertificateSubjectContainsList: Optional[Sequence["_CertificateSubjectContainsListDefinition"]]
    CertificateSubjectEndsWithList: Optional[Sequence["_CertificateSubjectEndsWithListDefinition"]]
    CertificateSubjectEqualsList: Optional[Sequence["_CertificateSubjectEqualsListDefinition"]]
    CertificateSubjectStartsWithList: Optional[Sequence["_CertificateSubjectStartsWithListDefinition"]]
    CipherWithoutPrioList: Optional[Sequence["_CipherWithoutPrioListDefinition"]]
    ClientAuthContainsList: Optional[Sequence["_ClientAuthContainsListDefinition"]]
    ClientAuthEndsWithList: Optional[Sequence["_ClientAuthEndsWithListDefinition"]]
    ClientAuthEqualsList: Optional[Sequence["_ClientAuthEqualsListDefinition"]]
    ClientAuthStartsWithList: Optional[Sequence["_ClientAuthStartsWithListDefinition"]]
    ContainsList: Optional[Sequence["_ContainsListDefinition"]]
    CrlCerts: Optional[Sequence["_CrlCertsDefinition"]]
    EcList: Optional[Sequence["_EcListDefinition"]]
    EndsWithList: Optional[Sequence["_EndsWithListDefinition"]]
    EqualsList: Optional[Sequence["_EqualsListDefinition"]]
    ExceptionWebCategory: Optional[Sequence["_ExceptionWebCategoryDefinition"]]
    ExceptionWebReputation: Optional[Sequence["_ExceptionWebReputationDefinition"]]
    ForwardProxyTrustedCaLists: Optional[Sequence["_ForwardProxyTrustedCaListsDefinition"]]
    MultiClassList: Optional[Sequence["_MultiClassListDefinition"]]
    ReqCaLists: Optional[Sequence["_ReqCaListsDefinition"]]
    ServerNameList: Optional[Sequence["_ServerNameListDefinition"]]
    StartsWithList: Optional[Sequence["_StartsWithListDefinition"]]
    WebCategory: Optional[Sequence["_WebCategoryDefinition"]]
    WebReputation: Optional[Sequence["_WebReputationDefinition"]]

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
            AdGroupList=json_data.get("AdGroupList"),
            AlertType=json_data.get("AlertType"),
            AuthSg=json_data.get("AuthSg"),
            AuthSgDn=json_data.get("AuthSgDn"),
            AuthSgFilter=json_data.get("AuthSgFilter"),
            AuthUsername=json_data.get("AuthUsername"),
            AuthUsernameAttribute=json_data.get("AuthUsernameAttribute"),
            AuthenName=json_data.get("AuthenName"),
            Authorization=json_data.get("Authorization"),
            BypassCertIssuerClassListName=json_data.get("BypassCertIssuerClassListName"),
            BypassCertSanClassListName=json_data.get("BypassCertSanClassListName"),
            BypassCertSubjectClassListName=json_data.get("BypassCertSubjectClassListName"),
            CachePersistenceListName=json_data.get("CachePersistenceListName"),
            CaseInsensitive=json_data.get("CaseInsensitive"),
            Cert=json_data.get("Cert"),
            CertAltPartitionShared=json_data.get("CertAltPartitionShared"),
            CertAlternate=json_data.get("CertAlternate"),
            CertRevokeAction=json_data.get("CertRevokeAction"),
            CertSharedStr=json_data.get("CertSharedStr"),
            CertUnknownAction=json_data.get("CertUnknownAction"),
            ChainCert=json_data.get("ChainCert"),
            ChainCertSharedStr=json_data.get("ChainCertSharedStr"),
            ClassListName=json_data.get("ClassListName"),
            ClientAuthCaseInsensitive=json_data.get("ClientAuthCaseInsensitive"),
            ClientAuthClassList=json_data.get("ClientAuthClassList"),
            ClientCertificate=json_data.get("ClientCertificate"),
            CloseNotify=json_data.get("CloseNotify"),
            Dgversion=json_data.get("Dgversion"),
            DhType=json_data.get("DhType"),
            DirectClientServerAuth=json_data.get("DirectClientServerAuth"),
            DisableSslv3=json_data.get("DisableSslv3"),
            EarlyData=json_data.get("EarlyData"),
            EnableTlsAlertLogging=json_data.get("EnableTlsAlertLogging"),
            ExceptionAdGroupList=json_data.get("ExceptionAdGroupList"),
            ExceptionCertificateIssuerClName=json_data.get("ExceptionCertificateIssuerClName"),
            ExceptionCertificateSanClName=json_data.get("ExceptionCertificateSanClName"),
            ExceptionCertificateSubjectClName=json_data.get("ExceptionCertificateSubjectClName"),
            ExceptionSniClName=json_data.get("ExceptionSniClName"),
            ExceptionUserNameList=json_data.get("ExceptionUserNameList"),
            ExpireHours=json_data.get("ExpireHours"),
            ForwardEncrypted=json_data.get("ForwardEncrypted"),
            ForwardPassphrase=json_data.get("ForwardPassphrase"),
            ForwardProxyAltSign=json_data.get("ForwardProxyAltSign"),
            ForwardProxyBlockMessage=json_data.get("ForwardProxyBlockMessage"),
            ForwardProxyCaCert=json_data.get("ForwardProxyCaCert"),
            ForwardProxyCaKey=json_data.get("ForwardProxyCaKey"),
            ForwardProxyCertCacheLimit=json_data.get("ForwardProxyCertCacheLimit"),
            ForwardProxyCertCacheTimeout=json_data.get("ForwardProxyCertCacheTimeout"),
            ForwardProxyCertExpiry=json_data.get("ForwardProxyCertExpiry"),
            ForwardProxyCertNotReadyAction=json_data.get("ForwardProxyCertNotReadyAction"),
            ForwardProxyCertRevokeAction=json_data.get("ForwardProxyCertRevokeAction"),
            ForwardProxyCertUnknownAction=json_data.get("ForwardProxyCertUnknownAction"),
            ForwardProxyCrlDisable=json_data.get("ForwardProxyCrlDisable"),
            ForwardProxyDecryptedDscp=json_data.get("ForwardProxyDecryptedDscp"),
            ForwardProxyDecryptedDscpBypass=json_data.get("ForwardProxyDecryptedDscpBypass"),
            ForwardProxyEnable=json_data.get("ForwardProxyEnable"),
            ForwardProxyFailsafeDisable=json_data.get("ForwardProxyFailsafeDisable"),
            ForwardProxyLogDisable=json_data.get("ForwardProxyLogDisable"),
            ForwardProxyNoSharedCipherAction=json_data.get("ForwardProxyNoSharedCipherAction"),
            ForwardProxyNoSniAction=json_data.get("ForwardProxyNoSniAction"),
            ForwardProxyOcspDisable=json_data.get("ForwardProxyOcspDisable"),
            ForwardProxyRequireSniCertMatched=json_data.get("ForwardProxyRequireSniCertMatched"),
            ForwardProxySelfsignRedir=json_data.get("ForwardProxySelfsignRedir"),
            ForwardProxySslVersion=json_data.get("ForwardProxySslVersion"),
            ForwardProxyVerifyCertFailAction=json_data.get("ForwardProxyVerifyCertFailAction"),
            FpAltCert=json_data.get("FpAltCert"),
            FpAltEncrypted=json_data.get("FpAltEncrypted"),
            FpAltKey=json_data.get("FpAltKey"),
            FpAltPassphrase=json_data.get("FpAltPassphrase"),
            FpAltShared=json_data.get("FpAltShared"),
            FpCaKeyShared=json_data.get("FpCaKeyShared"),
            FpCaShared=json_data.get("FpCaShared"),
            FpCertExtAiaCaIssuers=json_data.get("FpCertExtAiaCaIssuers"),
            FpCertExtAiaOcsp=json_data.get("FpCertExtAiaOcsp"),
            FpCertExtCrldp=json_data.get("FpCertExtCrldp"),
            FpCertFetchAutonat=json_data.get("FpCertFetchAutonat"),
            FpCertFetchAutonatPrecedence=json_data.get("FpCertFetchAutonatPrecedence"),
            FpCertFetchNatpoolName=json_data.get("FpCertFetchNatpoolName"),
            FpCertFetchNatpoolNameShared=json_data.get("FpCertFetchNatpoolNameShared"),
            FpCertFetchNatpoolPrecedence=json_data.get("FpCertFetchNatpoolPrecedence"),
            HandshakeLoggingEnable=json_data.get("HandshakeLoggingEnable"),
            HsmType=json_data.get("HsmType"),
            Id=json_data.get("Id"),
            InspectCertificateIssuerClName=json_data.get("InspectCertificateIssuerClName"),
            InspectCertificateSanClName=json_data.get("InspectCertificateSanClName"),
            InspectCertificateSubjectClName=json_data.get("InspectCertificateSubjectClName"),
            InspectListName=json_data.get("InspectListName"),
            Key=json_data.get("Key"),
            KeyAltEncrypted=json_data.get("KeyAltEncrypted"),
            KeyAltPartitionShared=json_data.get("KeyAltPartitionShared"),
            KeyAltPassphrase=json_data.get("KeyAltPassphrase"),
            KeyAlternate=json_data.get("KeyAlternate"),
            KeyEncrypted=json_data.get("KeyEncrypted"),
            KeyPassphrase=json_data.get("KeyPassphrase"),
            KeySharedEncrypted=json_data.get("KeySharedEncrypted"),
            KeySharedPassphrase=json_data.get("KeySharedPassphrase"),
            KeySharedStr=json_data.get("KeySharedStr"),
            LdapBaseDnFromCert=json_data.get("LdapBaseDnFromCert"),
            LdapSearchFilter=json_data.get("LdapSearchFilter"),
            LocalLogging=json_data.get("LocalLogging"),
            Name=json_data.get("Name"),
            NoAntiReplay=json_data.get("NoAntiReplay"),
            NoSharedCipherAction=json_data.get("NoSharedCipherAction"),
            NonSslBypassL4session=json_data.get("NonSslBypassL4session"),
            NonSslBypassServiceGroup=json_data.get("NonSslBypassServiceGroup"),
            Notafter=json_data.get("Notafter"),
            Notafterday=json_data.get("Notafterday"),
            Notaftermonth=json_data.get("Notaftermonth"),
            Notafteryear=json_data.get("Notafteryear"),
            Notbefore=json_data.get("Notbefore"),
            Notbeforeday=json_data.get("Notbeforeday"),
            Notbeforemonth=json_data.get("Notbeforemonth"),
            Notbeforeyear=json_data.get("Notbeforeyear"),
            OcspStapling=json_data.get("OcspStapling"),
            OcspstCaCert=json_data.get("OcspstCaCert"),
            OcspstOcsp=json_data.get("OcspstOcsp"),
            OcspstSg=json_data.get("OcspstSg"),
            OcspstSgDays=json_data.get("OcspstSgDays"),
            OcspstSgHours=json_data.get("OcspstSgHours"),
            OcspstSgMinutes=json_data.get("OcspstSgMinutes"),
            OcspstSgTimeout=json_data.get("OcspstSgTimeout"),
            OcspstSrvr=json_data.get("OcspstSrvr"),
            OcspstSrvrDays=json_data.get("OcspstSrvrDays"),
            OcspstSrvrHours=json_data.get("OcspstSrvrHours"),
            OcspstSrvrMinutes=json_data.get("OcspstSrvrMinutes"),
            OcspstSrvrTimeout=json_data.get("OcspstSrvrTimeout"),
            RenegotiationDisable=json_data.get("RenegotiationDisable"),
            RequireWebCategory=json_data.get("RequireWebCategory"),
            ServerNameAutoMap=json_data.get("ServerNameAutoMap"),
            SessionCacheSize=json_data.get("SessionCacheSize"),
            SessionCacheTimeout=json_data.get("SessionCacheTimeout"),
            SessionTicketDisable=json_data.get("SessionTicketDisable"),
            SessionTicketLifetime=json_data.get("SessionTicketLifetime"),
            SharedPartitionCipherTemplate=json_data.get("SharedPartitionCipherTemplate"),
            SharedPartitionPool=json_data.get("SharedPartitionPool"),
            SniEnableLog=json_data.get("SniEnableLog"),
            SslFalseStartDisable=json_data.get("SslFalseStartDisable"),
            SsliLogging=json_data.get("SsliLogging"),
            Sslilogging=json_data.get("Sslilogging"),
            Sslv2BypassServiceGroup=json_data.get("Sslv2BypassServiceGroup"),
            TemplateCipher=json_data.get("TemplateCipher"),
            TemplateCipherShared=json_data.get("TemplateCipherShared"),
            TemplateHsm=json_data.get("TemplateHsm"),
            UserNameList=json_data.get("UserNameList"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            VerifyCertFailAction=json_data.get("VerifyCertFailAction"),
            Version=json_data.get("Version"),
            BypassCertIssuerMultiClassList=deserialize_list(json_data.get("BypassCertIssuerMultiClassList"), BypassCertIssuerMultiClassListDefinition),
            BypassCertSanMultiClassList=deserialize_list(json_data.get("BypassCertSanMultiClassList"), BypassCertSanMultiClassListDefinition),
            BypassCertSubjectMultiClassList=deserialize_list(json_data.get("BypassCertSubjectMultiClassList"), BypassCertSubjectMultiClassListDefinition),
            CaCerts=deserialize_list(json_data.get("CaCerts"), CaCertsDefinition),
            CertificateIssuerContainsList=deserialize_list(json_data.get("CertificateIssuerContainsList"), CertificateIssuerContainsListDefinition),
            CertificateIssuerEndsWithList=deserialize_list(json_data.get("CertificateIssuerEndsWithList"), CertificateIssuerEndsWithListDefinition),
            CertificateIssuerEqualsList=deserialize_list(json_data.get("CertificateIssuerEqualsList"), CertificateIssuerEqualsListDefinition),
            CertificateIssuerStartsWithList=deserialize_list(json_data.get("CertificateIssuerStartsWithList"), CertificateIssuerStartsWithListDefinition),
            CertificateList=deserialize_list(json_data.get("CertificateList"), CertificateListDefinition),
            CertificateSanContainsList=deserialize_list(json_data.get("CertificateSanContainsList"), CertificateSanContainsListDefinition),
            CertificateSanEndsWithList=deserialize_list(json_data.get("CertificateSanEndsWithList"), CertificateSanEndsWithListDefinition),
            CertificateSanEqualsList=deserialize_list(json_data.get("CertificateSanEqualsList"), CertificateSanEqualsListDefinition),
            CertificateSanStartsWithList=deserialize_list(json_data.get("CertificateSanStartsWithList"), CertificateSanStartsWithListDefinition),
            CertificateSubjectContainsList=deserialize_list(json_data.get("CertificateSubjectContainsList"), CertificateSubjectContainsListDefinition),
            CertificateSubjectEndsWithList=deserialize_list(json_data.get("CertificateSubjectEndsWithList"), CertificateSubjectEndsWithListDefinition),
            CertificateSubjectEqualsList=deserialize_list(json_data.get("CertificateSubjectEqualsList"), CertificateSubjectEqualsListDefinition),
            CertificateSubjectStartsWithList=deserialize_list(json_data.get("CertificateSubjectStartsWithList"), CertificateSubjectStartsWithListDefinition),
            CipherWithoutPrioList=deserialize_list(json_data.get("CipherWithoutPrioList"), CipherWithoutPrioListDefinition),
            ClientAuthContainsList=deserialize_list(json_data.get("ClientAuthContainsList"), ClientAuthContainsListDefinition),
            ClientAuthEndsWithList=deserialize_list(json_data.get("ClientAuthEndsWithList"), ClientAuthEndsWithListDefinition),
            ClientAuthEqualsList=deserialize_list(json_data.get("ClientAuthEqualsList"), ClientAuthEqualsListDefinition),
            ClientAuthStartsWithList=deserialize_list(json_data.get("ClientAuthStartsWithList"), ClientAuthStartsWithListDefinition),
            ContainsList=deserialize_list(json_data.get("ContainsList"), ContainsListDefinition),
            CrlCerts=deserialize_list(json_data.get("CrlCerts"), CrlCertsDefinition),
            EcList=deserialize_list(json_data.get("EcList"), EcListDefinition),
            EndsWithList=deserialize_list(json_data.get("EndsWithList"), EndsWithListDefinition),
            EqualsList=deserialize_list(json_data.get("EqualsList"), EqualsListDefinition),
            ExceptionWebCategory=deserialize_list(json_data.get("ExceptionWebCategory"), ExceptionWebCategoryDefinition),
            ExceptionWebReputation=deserialize_list(json_data.get("ExceptionWebReputation"), ExceptionWebReputationDefinition),
            ForwardProxyTrustedCaLists=deserialize_list(json_data.get("ForwardProxyTrustedCaLists"), ForwardProxyTrustedCaListsDefinition),
            MultiClassList=deserialize_list(json_data.get("MultiClassList"), MultiClassListDefinition),
            ReqCaLists=deserialize_list(json_data.get("ReqCaLists"), ReqCaListsDefinition),
            ServerNameList=deserialize_list(json_data.get("ServerNameList"), ServerNameListDefinition),
            StartsWithList=deserialize_list(json_data.get("StartsWithList"), StartsWithListDefinition),
            WebCategory=deserialize_list(json_data.get("WebCategory"), WebCategoryDefinition),
            WebReputation=deserialize_list(json_data.get("WebReputation"), WebReputationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BypassCertIssuerMultiClassListDefinition(BaseModel):
    BypassCertIssuerMultiClassListName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BypassCertIssuerMultiClassListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BypassCertIssuerMultiClassListDefinition"]:
        if not json_data:
            return None
        return cls(
            BypassCertIssuerMultiClassListName=json_data.get("BypassCertIssuerMultiClassListName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BypassCertIssuerMultiClassListDefinition = BypassCertIssuerMultiClassListDefinition


@dataclass
class BypassCertSanMultiClassListDefinition(BaseModel):
    BypassCertSanMultiClassListName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BypassCertSanMultiClassListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BypassCertSanMultiClassListDefinition"]:
        if not json_data:
            return None
        return cls(
            BypassCertSanMultiClassListName=json_data.get("BypassCertSanMultiClassListName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BypassCertSanMultiClassListDefinition = BypassCertSanMultiClassListDefinition


@dataclass
class BypassCertSubjectMultiClassListDefinition(BaseModel):
    BypassCertSubjectMultiClassListName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BypassCertSubjectMultiClassListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BypassCertSubjectMultiClassListDefinition"]:
        if not json_data:
            return None
        return cls(
            BypassCertSubjectMultiClassListName=json_data.get("BypassCertSubjectMultiClassListName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BypassCertSubjectMultiClassListDefinition = BypassCertSubjectMultiClassListDefinition


@dataclass
class CaCertsDefinition(BaseModel):
    CaCert: Optional[str]
    CaShared: Optional[float]
    ClientOcsp: Optional[float]
    ClientOcspSg: Optional[str]
    ClientOcspSrvr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaCertsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaCertsDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCert=json_data.get("CaCert"),
            CaShared=json_data.get("CaShared"),
            ClientOcsp=json_data.get("ClientOcsp"),
            ClientOcspSg=json_data.get("ClientOcspSg"),
            ClientOcspSrvr=json_data.get("ClientOcspSrvr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaCertsDefinition = CaCertsDefinition


@dataclass
class CertificateIssuerContainsListDefinition(BaseModel):
    CertificateIssuerContains: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateIssuerContainsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateIssuerContainsListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateIssuerContains=json_data.get("CertificateIssuerContains"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateIssuerContainsListDefinition = CertificateIssuerContainsListDefinition


@dataclass
class CertificateIssuerEndsWithListDefinition(BaseModel):
    CertificateIssuerEndsWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateIssuerEndsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateIssuerEndsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateIssuerEndsWith=json_data.get("CertificateIssuerEndsWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateIssuerEndsWithListDefinition = CertificateIssuerEndsWithListDefinition


@dataclass
class CertificateIssuerEqualsListDefinition(BaseModel):
    CertificateIssuerEquals: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateIssuerEqualsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateIssuerEqualsListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateIssuerEquals=json_data.get("CertificateIssuerEquals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateIssuerEqualsListDefinition = CertificateIssuerEqualsListDefinition


@dataclass
class CertificateIssuerStartsWithListDefinition(BaseModel):
    CertificateIssuerStarts: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateIssuerStartsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateIssuerStartsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateIssuerStarts=json_data.get("CertificateIssuerStarts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateIssuerStartsWithListDefinition = CertificateIssuerStartsWithListDefinition


@dataclass
class CertificateListDefinition(BaseModel):
    Cert: Optional[str]
    ChainCert: Optional[str]
    Key: Optional[str]
    KeyEncrypted: Optional[str]
    Passphrase: Optional[str]
    Shared: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateListDefinition"]:
        if not json_data:
            return None
        return cls(
            Cert=json_data.get("Cert"),
            ChainCert=json_data.get("ChainCert"),
            Key=json_data.get("Key"),
            KeyEncrypted=json_data.get("KeyEncrypted"),
            Passphrase=json_data.get("Passphrase"),
            Shared=json_data.get("Shared"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateListDefinition = CertificateListDefinition


@dataclass
class CertificateSanContainsListDefinition(BaseModel):
    CertificateSanContains: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateSanContainsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateSanContainsListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSanContains=json_data.get("CertificateSanContains"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateSanContainsListDefinition = CertificateSanContainsListDefinition


@dataclass
class CertificateSanEndsWithListDefinition(BaseModel):
    CertificateSanEndsWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateSanEndsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateSanEndsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSanEndsWith=json_data.get("CertificateSanEndsWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateSanEndsWithListDefinition = CertificateSanEndsWithListDefinition


@dataclass
class CertificateSanEqualsListDefinition(BaseModel):
    CertificateSanEquals: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateSanEqualsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateSanEqualsListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSanEquals=json_data.get("CertificateSanEquals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateSanEqualsListDefinition = CertificateSanEqualsListDefinition


@dataclass
class CertificateSanStartsWithListDefinition(BaseModel):
    CertificateSanStarts: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateSanStartsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateSanStartsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSanStarts=json_data.get("CertificateSanStarts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateSanStartsWithListDefinition = CertificateSanStartsWithListDefinition


@dataclass
class CertificateSubjectContainsListDefinition(BaseModel):
    CertificateSubjectContains: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateSubjectContainsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateSubjectContainsListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSubjectContains=json_data.get("CertificateSubjectContains"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateSubjectContainsListDefinition = CertificateSubjectContainsListDefinition


@dataclass
class CertificateSubjectEndsWithListDefinition(BaseModel):
    CertificateSubjectEndsWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateSubjectEndsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateSubjectEndsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSubjectEndsWith=json_data.get("CertificateSubjectEndsWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateSubjectEndsWithListDefinition = CertificateSubjectEndsWithListDefinition


@dataclass
class CertificateSubjectEqualsListDefinition(BaseModel):
    CertificateSubjectEquals: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateSubjectEqualsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateSubjectEqualsListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSubjectEquals=json_data.get("CertificateSubjectEquals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateSubjectEqualsListDefinition = CertificateSubjectEqualsListDefinition


@dataclass
class CertificateSubjectStartsWithListDefinition(BaseModel):
    CertificateSubjectStarts: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateSubjectStartsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateSubjectStartsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateSubjectStarts=json_data.get("CertificateSubjectStarts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateSubjectStartsWithListDefinition = CertificateSubjectStartsWithListDefinition


@dataclass
class CipherWithoutPrioListDefinition(BaseModel):
    CipherWoPrio: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CipherWithoutPrioListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CipherWithoutPrioListDefinition"]:
        if not json_data:
            return None
        return cls(
            CipherWoPrio=json_data.get("CipherWoPrio"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CipherWithoutPrioListDefinition = CipherWithoutPrioListDefinition


@dataclass
class ClientAuthContainsListDefinition(BaseModel):
    ClientAuthContains: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthContainsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthContainsListDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientAuthContains=json_data.get("ClientAuthContains"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthContainsListDefinition = ClientAuthContainsListDefinition


@dataclass
class ClientAuthEndsWithListDefinition(BaseModel):
    ClientAuthEndsWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthEndsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthEndsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientAuthEndsWith=json_data.get("ClientAuthEndsWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthEndsWithListDefinition = ClientAuthEndsWithListDefinition


@dataclass
class ClientAuthEqualsListDefinition(BaseModel):
    ClientAuthEquals: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthEqualsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthEqualsListDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientAuthEquals=json_data.get("ClientAuthEquals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthEqualsListDefinition = ClientAuthEqualsListDefinition


@dataclass
class ClientAuthStartsWithListDefinition(BaseModel):
    ClientAuthStartsWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthStartsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthStartsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientAuthStartsWith=json_data.get("ClientAuthStartsWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthStartsWithListDefinition = ClientAuthStartsWithListDefinition


@dataclass
class ContainsListDefinition(BaseModel):
    Contains: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainsListDefinition"]:
        if not json_data:
            return None
        return cls(
            Contains=json_data.get("Contains"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainsListDefinition = ContainsListDefinition


@dataclass
class CrlCertsDefinition(BaseModel):
    Crl: Optional[str]
    CrlShared: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CrlCertsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrlCertsDefinition"]:
        if not json_data:
            return None
        return cls(
            Crl=json_data.get("Crl"),
            CrlShared=json_data.get("CrlShared"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrlCertsDefinition = CrlCertsDefinition


@dataclass
class EcListDefinition(BaseModel):
    Ec: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ec=json_data.get("Ec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcListDefinition = EcListDefinition


@dataclass
class EndsWithListDefinition(BaseModel):
    EndsWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            EndsWith=json_data.get("EndsWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndsWithListDefinition = EndsWithListDefinition


@dataclass
class EqualsListDefinition(BaseModel):
    Equals: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EqualsListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EqualsListDefinition"]:
        if not json_data:
            return None
        return cls(
            Equals=json_data.get("Equals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EqualsListDefinition = EqualsListDefinition


@dataclass
class ExceptionWebCategoryDefinition(BaseModel):
    ExceptionAbortion: Optional[float]
    ExceptionAdultAndPornography: Optional[float]
    ExceptionAlcoholAndTobacco: Optional[float]
    ExceptionAuctions: Optional[float]
    ExceptionBotNets: Optional[float]
    ExceptionBusinessAndEconomy: Optional[float]
    ExceptionCdns: Optional[float]
    ExceptionCheating: Optional[float]
    ExceptionComputerAndInternetInfo: Optional[float]
    ExceptionComputerAndInternetSecurity: Optional[float]
    ExceptionConfirmedSpamSources: Optional[float]
    ExceptionCultAndOccult: Optional[float]
    ExceptionDating: Optional[float]
    ExceptionDeadSites: Optional[float]
    ExceptionDrugs: Optional[float]
    ExceptionDynamicComment: Optional[float]
    ExceptionEducationalInstitutions: Optional[float]
    ExceptionEntertainmentAndArts: Optional[float]
    ExceptionFashionAndBeauty: Optional[float]
    ExceptionFinancialServices: Optional[float]
    ExceptionFoodAndDining: Optional[float]
    ExceptionGambling: Optional[float]
    ExceptionGames: Optional[float]
    ExceptionGovernment: Optional[float]
    ExceptionGross: Optional[float]
    ExceptionHacking: Optional[float]
    ExceptionHateAndRacism: Optional[float]
    ExceptionHealthAndMedicine: Optional[float]
    ExceptionHomeAndGarden: Optional[float]
    ExceptionHuntingAndFishing: Optional[float]
    ExceptionIllegal: Optional[float]
    ExceptionImageAndVideoSearch: Optional[float]
    ExceptionInternetCommunications: Optional[float]
    ExceptionInternetPortals: Optional[float]
    ExceptionJobSearch: Optional[float]
    ExceptionKeyloggersAndMonitoring: Optional[float]
    ExceptionKids: Optional[float]
    ExceptionLegal: Optional[float]
    ExceptionLocalInformation: Optional[float]
    ExceptionMalwareSites: Optional[float]
    ExceptionMarijuana: Optional[float]
    ExceptionMilitary: Optional[float]
    ExceptionMotorVehicles: Optional[float]
    ExceptionMusic: Optional[float]
    ExceptionNewsAndMedia: Optional[float]
    ExceptionNudity: Optional[float]
    ExceptionOnlineGreetingCards: Optional[float]
    ExceptionOpenHttpProxies: Optional[float]
    ExceptionParkedDomains: Optional[float]
    ExceptionPayToSurf: Optional[float]
    ExceptionPeerToPeer: Optional[float]
    ExceptionPersonalSitesAndBlogs: Optional[float]
    ExceptionPersonalStorage: Optional[float]
    ExceptionPhilosophyAndPolitics: Optional[float]
    ExceptionPhishingAndOtherFraud: Optional[float]
    ExceptionPrivateIpAddresses: Optional[float]
    ExceptionProxyAvoidAndAnonymizers: Optional[float]
    ExceptionQuestionable: Optional[float]
    ExceptionRealEstate: Optional[float]
    ExceptionRecreationAndHobbies: Optional[float]
    ExceptionReferenceAndResearch: Optional[float]
    ExceptionReligion: Optional[float]
    ExceptionSearchEngines: Optional[float]
    ExceptionSexEducation: Optional[float]
    ExceptionSharewareAndFreeware: Optional[float]
    ExceptionShopping: Optional[float]
    ExceptionSocialNetwork: Optional[float]
    ExceptionSociety: Optional[float]
    ExceptionSpamUrls: Optional[float]
    ExceptionSports: Optional[float]
    ExceptionSpywareAndAdware: Optional[float]
    ExceptionStockAdviceAndTools: Optional[float]
    ExceptionStreamingMedia: Optional[float]
    ExceptionSwimsuitsAndIntimateApparel: Optional[float]
    ExceptionTrainingAndTools: Optional[float]
    ExceptionTranslation: Optional[float]
    ExceptionTravel: Optional[float]
    ExceptionUncategorized: Optional[float]
    ExceptionUnconfirmedSpamSources: Optional[float]
    ExceptionViolence: Optional[float]
    ExceptionWeapons: Optional[float]
    ExceptionWebAdvertisements: Optional[float]
    ExceptionWebBasedEmail: Optional[float]
    ExceptionWebHostingSites: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExceptionWebCategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExceptionWebCategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            ExceptionAbortion=json_data.get("ExceptionAbortion"),
            ExceptionAdultAndPornography=json_data.get("ExceptionAdultAndPornography"),
            ExceptionAlcoholAndTobacco=json_data.get("ExceptionAlcoholAndTobacco"),
            ExceptionAuctions=json_data.get("ExceptionAuctions"),
            ExceptionBotNets=json_data.get("ExceptionBotNets"),
            ExceptionBusinessAndEconomy=json_data.get("ExceptionBusinessAndEconomy"),
            ExceptionCdns=json_data.get("ExceptionCdns"),
            ExceptionCheating=json_data.get("ExceptionCheating"),
            ExceptionComputerAndInternetInfo=json_data.get("ExceptionComputerAndInternetInfo"),
            ExceptionComputerAndInternetSecurity=json_data.get("ExceptionComputerAndInternetSecurity"),
            ExceptionConfirmedSpamSources=json_data.get("ExceptionConfirmedSpamSources"),
            ExceptionCultAndOccult=json_data.get("ExceptionCultAndOccult"),
            ExceptionDating=json_data.get("ExceptionDating"),
            ExceptionDeadSites=json_data.get("ExceptionDeadSites"),
            ExceptionDrugs=json_data.get("ExceptionDrugs"),
            ExceptionDynamicComment=json_data.get("ExceptionDynamicComment"),
            ExceptionEducationalInstitutions=json_data.get("ExceptionEducationalInstitutions"),
            ExceptionEntertainmentAndArts=json_data.get("ExceptionEntertainmentAndArts"),
            ExceptionFashionAndBeauty=json_data.get("ExceptionFashionAndBeauty"),
            ExceptionFinancialServices=json_data.get("ExceptionFinancialServices"),
            ExceptionFoodAndDining=json_data.get("ExceptionFoodAndDining"),
            ExceptionGambling=json_data.get("ExceptionGambling"),
            ExceptionGames=json_data.get("ExceptionGames"),
            ExceptionGovernment=json_data.get("ExceptionGovernment"),
            ExceptionGross=json_data.get("ExceptionGross"),
            ExceptionHacking=json_data.get("ExceptionHacking"),
            ExceptionHateAndRacism=json_data.get("ExceptionHateAndRacism"),
            ExceptionHealthAndMedicine=json_data.get("ExceptionHealthAndMedicine"),
            ExceptionHomeAndGarden=json_data.get("ExceptionHomeAndGarden"),
            ExceptionHuntingAndFishing=json_data.get("ExceptionHuntingAndFishing"),
            ExceptionIllegal=json_data.get("ExceptionIllegal"),
            ExceptionImageAndVideoSearch=json_data.get("ExceptionImageAndVideoSearch"),
            ExceptionInternetCommunications=json_data.get("ExceptionInternetCommunications"),
            ExceptionInternetPortals=json_data.get("ExceptionInternetPortals"),
            ExceptionJobSearch=json_data.get("ExceptionJobSearch"),
            ExceptionKeyloggersAndMonitoring=json_data.get("ExceptionKeyloggersAndMonitoring"),
            ExceptionKids=json_data.get("ExceptionKids"),
            ExceptionLegal=json_data.get("ExceptionLegal"),
            ExceptionLocalInformation=json_data.get("ExceptionLocalInformation"),
            ExceptionMalwareSites=json_data.get("ExceptionMalwareSites"),
            ExceptionMarijuana=json_data.get("ExceptionMarijuana"),
            ExceptionMilitary=json_data.get("ExceptionMilitary"),
            ExceptionMotorVehicles=json_data.get("ExceptionMotorVehicles"),
            ExceptionMusic=json_data.get("ExceptionMusic"),
            ExceptionNewsAndMedia=json_data.get("ExceptionNewsAndMedia"),
            ExceptionNudity=json_data.get("ExceptionNudity"),
            ExceptionOnlineGreetingCards=json_data.get("ExceptionOnlineGreetingCards"),
            ExceptionOpenHttpProxies=json_data.get("ExceptionOpenHttpProxies"),
            ExceptionParkedDomains=json_data.get("ExceptionParkedDomains"),
            ExceptionPayToSurf=json_data.get("ExceptionPayToSurf"),
            ExceptionPeerToPeer=json_data.get("ExceptionPeerToPeer"),
            ExceptionPersonalSitesAndBlogs=json_data.get("ExceptionPersonalSitesAndBlogs"),
            ExceptionPersonalStorage=json_data.get("ExceptionPersonalStorage"),
            ExceptionPhilosophyAndPolitics=json_data.get("ExceptionPhilosophyAndPolitics"),
            ExceptionPhishingAndOtherFraud=json_data.get("ExceptionPhishingAndOtherFraud"),
            ExceptionPrivateIpAddresses=json_data.get("ExceptionPrivateIpAddresses"),
            ExceptionProxyAvoidAndAnonymizers=json_data.get("ExceptionProxyAvoidAndAnonymizers"),
            ExceptionQuestionable=json_data.get("ExceptionQuestionable"),
            ExceptionRealEstate=json_data.get("ExceptionRealEstate"),
            ExceptionRecreationAndHobbies=json_data.get("ExceptionRecreationAndHobbies"),
            ExceptionReferenceAndResearch=json_data.get("ExceptionReferenceAndResearch"),
            ExceptionReligion=json_data.get("ExceptionReligion"),
            ExceptionSearchEngines=json_data.get("ExceptionSearchEngines"),
            ExceptionSexEducation=json_data.get("ExceptionSexEducation"),
            ExceptionSharewareAndFreeware=json_data.get("ExceptionSharewareAndFreeware"),
            ExceptionShopping=json_data.get("ExceptionShopping"),
            ExceptionSocialNetwork=json_data.get("ExceptionSocialNetwork"),
            ExceptionSociety=json_data.get("ExceptionSociety"),
            ExceptionSpamUrls=json_data.get("ExceptionSpamUrls"),
            ExceptionSports=json_data.get("ExceptionSports"),
            ExceptionSpywareAndAdware=json_data.get("ExceptionSpywareAndAdware"),
            ExceptionStockAdviceAndTools=json_data.get("ExceptionStockAdviceAndTools"),
            ExceptionStreamingMedia=json_data.get("ExceptionStreamingMedia"),
            ExceptionSwimsuitsAndIntimateApparel=json_data.get("ExceptionSwimsuitsAndIntimateApparel"),
            ExceptionTrainingAndTools=json_data.get("ExceptionTrainingAndTools"),
            ExceptionTranslation=json_data.get("ExceptionTranslation"),
            ExceptionTravel=json_data.get("ExceptionTravel"),
            ExceptionUncategorized=json_data.get("ExceptionUncategorized"),
            ExceptionUnconfirmedSpamSources=json_data.get("ExceptionUnconfirmedSpamSources"),
            ExceptionViolence=json_data.get("ExceptionViolence"),
            ExceptionWeapons=json_data.get("ExceptionWeapons"),
            ExceptionWebAdvertisements=json_data.get("ExceptionWebAdvertisements"),
            ExceptionWebBasedEmail=json_data.get("ExceptionWebBasedEmail"),
            ExceptionWebHostingSites=json_data.get("ExceptionWebHostingSites"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExceptionWebCategoryDefinition = ExceptionWebCategoryDefinition


@dataclass
class ExceptionWebReputationDefinition(BaseModel):
    ExceptionLowRisk: Optional[float]
    ExceptionMalicious: Optional[float]
    ExceptionModerateRisk: Optional[float]
    ExceptionSuspicious: Optional[float]
    ExceptionThreshold: Optional[float]
    ExceptionTrustworthy: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExceptionWebReputationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExceptionWebReputationDefinition"]:
        if not json_data:
            return None
        return cls(
            ExceptionLowRisk=json_data.get("ExceptionLowRisk"),
            ExceptionMalicious=json_data.get("ExceptionMalicious"),
            ExceptionModerateRisk=json_data.get("ExceptionModerateRisk"),
            ExceptionSuspicious=json_data.get("ExceptionSuspicious"),
            ExceptionThreshold=json_data.get("ExceptionThreshold"),
            ExceptionTrustworthy=json_data.get("ExceptionTrustworthy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExceptionWebReputationDefinition = ExceptionWebReputationDefinition


@dataclass
class ForwardProxyTrustedCaListsDefinition(BaseModel):
    ForwardProxyTrustedCa: Optional[str]
    FpTrustedCaShared: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardProxyTrustedCaListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardProxyTrustedCaListsDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardProxyTrustedCa=json_data.get("ForwardProxyTrustedCa"),
            FpTrustedCaShared=json_data.get("FpTrustedCaShared"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardProxyTrustedCaListsDefinition = ForwardProxyTrustedCaListsDefinition


@dataclass
class MultiClassListDefinition(BaseModel):
    MultiClistName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MultiClassListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiClassListDefinition"]:
        if not json_data:
            return None
        return cls(
            MultiClistName=json_data.get("MultiClistName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiClassListDefinition = MultiClassListDefinition


@dataclass
class ReqCaListsDefinition(BaseModel):
    ClientCertReqCaShared: Optional[float]
    ClientCertificateRequestCa: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReqCaListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReqCaListsDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientCertReqCaShared=json_data.get("ClientCertReqCaShared"),
            ClientCertificateRequestCa=json_data.get("ClientCertificateRequestCa"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReqCaListsDefinition = ReqCaListsDefinition


@dataclass
class ServerNameListDefinition(BaseModel):
    ServerCert: Optional[str]
    ServerCertRegex: Optional[str]
    ServerChain: Optional[str]
    ServerChainRegex: Optional[str]
    ServerEncrypted: Optional[str]
    ServerEncryptedRegex: Optional[str]
    ServerKey: Optional[str]
    ServerKeyRegex: Optional[str]
    ServerName: Optional[str]
    ServerNameAlternate: Optional[float]
    ServerNameRegex: Optional[str]
    ServerNameRegexAlternate: Optional[float]
    ServerPassphrase: Optional[str]
    ServerPassphraseRegex: Optional[str]
    ServerShared: Optional[float]
    ServerSharedRegex: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServerNameListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerNameListDefinition"]:
        if not json_data:
            return None
        return cls(
            ServerCert=json_data.get("ServerCert"),
            ServerCertRegex=json_data.get("ServerCertRegex"),
            ServerChain=json_data.get("ServerChain"),
            ServerChainRegex=json_data.get("ServerChainRegex"),
            ServerEncrypted=json_data.get("ServerEncrypted"),
            ServerEncryptedRegex=json_data.get("ServerEncryptedRegex"),
            ServerKey=json_data.get("ServerKey"),
            ServerKeyRegex=json_data.get("ServerKeyRegex"),
            ServerName=json_data.get("ServerName"),
            ServerNameAlternate=json_data.get("ServerNameAlternate"),
            ServerNameRegex=json_data.get("ServerNameRegex"),
            ServerNameRegexAlternate=json_data.get("ServerNameRegexAlternate"),
            ServerPassphrase=json_data.get("ServerPassphrase"),
            ServerPassphraseRegex=json_data.get("ServerPassphraseRegex"),
            ServerShared=json_data.get("ServerShared"),
            ServerSharedRegex=json_data.get("ServerSharedRegex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerNameListDefinition = ServerNameListDefinition


@dataclass
class StartsWithListDefinition(BaseModel):
    StartsWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StartsWithListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StartsWithListDefinition"]:
        if not json_data:
            return None
        return cls(
            StartsWith=json_data.get("StartsWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StartsWithListDefinition = StartsWithListDefinition


@dataclass
class WebCategoryDefinition(BaseModel):
    Abortion: Optional[float]
    AdultAndPornography: Optional[float]
    AlcoholAndTobacco: Optional[float]
    Auctions: Optional[float]
    BotNets: Optional[float]
    BusinessAndEconomy: Optional[float]
    Cdns: Optional[float]
    Cheating: Optional[float]
    ComputerAndInternetInfo: Optional[float]
    ComputerAndInternetSecurity: Optional[float]
    ConfirmedSpamSources: Optional[float]
    CultAndOccult: Optional[float]
    Dating: Optional[float]
    DeadSites: Optional[float]
    Drugs: Optional[float]
    DynamicComment: Optional[float]
    EducationalInstitutions: Optional[float]
    EntertainmentAndArts: Optional[float]
    FashionAndBeauty: Optional[float]
    FinancialServices: Optional[float]
    FoodAndDining: Optional[float]
    Gambling: Optional[float]
    Games: Optional[float]
    Government: Optional[float]
    Gross: Optional[float]
    Hacking: Optional[float]
    HateAndRacism: Optional[float]
    HealthAndMedicine: Optional[float]
    HomeAndGarden: Optional[float]
    HuntingAndFishing: Optional[float]
    Illegal: Optional[float]
    ImageAndVideoSearch: Optional[float]
    InternetCommunications: Optional[float]
    InternetPortals: Optional[float]
    JobSearch: Optional[float]
    KeyloggersAndMonitoring: Optional[float]
    Kids: Optional[float]
    Legal: Optional[float]
    LocalInformation: Optional[float]
    MalwareSites: Optional[float]
    Marijuana: Optional[float]
    Military: Optional[float]
    MotorVehicles: Optional[float]
    Music: Optional[float]
    NewsAndMedia: Optional[float]
    Nudity: Optional[float]
    OnlineGreetingCards: Optional[float]
    OpenHttpProxies: Optional[float]
    ParkedDomains: Optional[float]
    PayToSurf: Optional[float]
    PeerToPeer: Optional[float]
    PersonalSitesAndBlogs: Optional[float]
    PersonalStorage: Optional[float]
    PhilosophyAndPolitics: Optional[float]
    PhishingAndOtherFraud: Optional[float]
    PrivateIpAddresses: Optional[float]
    ProxyAvoidAndAnonymizers: Optional[float]
    Questionable: Optional[float]
    RealEstate: Optional[float]
    RecreationAndHobbies: Optional[float]
    ReferenceAndResearch: Optional[float]
    Religion: Optional[float]
    SearchEngines: Optional[float]
    SexEducation: Optional[float]
    SharewareAndFreeware: Optional[float]
    Shopping: Optional[float]
    SocialNetwork: Optional[float]
    Society: Optional[float]
    SpamUrls: Optional[float]
    Sports: Optional[float]
    SpywareAndAdware: Optional[float]
    StockAdviceAndTools: Optional[float]
    StreamingMedia: Optional[float]
    SwimsuitsAndIntimateApparel: Optional[float]
    TrainingAndTools: Optional[float]
    Translation: Optional[float]
    Travel: Optional[float]
    Uncategorized: Optional[float]
    UnconfirmedSpamSources: Optional[float]
    Violence: Optional[float]
    Weapons: Optional[float]
    WebAdvertisements: Optional[float]
    WebBasedEmail: Optional[float]
    WebHostingSites: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WebCategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebCategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Abortion=json_data.get("Abortion"),
            AdultAndPornography=json_data.get("AdultAndPornography"),
            AlcoholAndTobacco=json_data.get("AlcoholAndTobacco"),
            Auctions=json_data.get("Auctions"),
            BotNets=json_data.get("BotNets"),
            BusinessAndEconomy=json_data.get("BusinessAndEconomy"),
            Cdns=json_data.get("Cdns"),
            Cheating=json_data.get("Cheating"),
            ComputerAndInternetInfo=json_data.get("ComputerAndInternetInfo"),
            ComputerAndInternetSecurity=json_data.get("ComputerAndInternetSecurity"),
            ConfirmedSpamSources=json_data.get("ConfirmedSpamSources"),
            CultAndOccult=json_data.get("CultAndOccult"),
            Dating=json_data.get("Dating"),
            DeadSites=json_data.get("DeadSites"),
            Drugs=json_data.get("Drugs"),
            DynamicComment=json_data.get("DynamicComment"),
            EducationalInstitutions=json_data.get("EducationalInstitutions"),
            EntertainmentAndArts=json_data.get("EntertainmentAndArts"),
            FashionAndBeauty=json_data.get("FashionAndBeauty"),
            FinancialServices=json_data.get("FinancialServices"),
            FoodAndDining=json_data.get("FoodAndDining"),
            Gambling=json_data.get("Gambling"),
            Games=json_data.get("Games"),
            Government=json_data.get("Government"),
            Gross=json_data.get("Gross"),
            Hacking=json_data.get("Hacking"),
            HateAndRacism=json_data.get("HateAndRacism"),
            HealthAndMedicine=json_data.get("HealthAndMedicine"),
            HomeAndGarden=json_data.get("HomeAndGarden"),
            HuntingAndFishing=json_data.get("HuntingAndFishing"),
            Illegal=json_data.get("Illegal"),
            ImageAndVideoSearch=json_data.get("ImageAndVideoSearch"),
            InternetCommunications=json_data.get("InternetCommunications"),
            InternetPortals=json_data.get("InternetPortals"),
            JobSearch=json_data.get("JobSearch"),
            KeyloggersAndMonitoring=json_data.get("KeyloggersAndMonitoring"),
            Kids=json_data.get("Kids"),
            Legal=json_data.get("Legal"),
            LocalInformation=json_data.get("LocalInformation"),
            MalwareSites=json_data.get("MalwareSites"),
            Marijuana=json_data.get("Marijuana"),
            Military=json_data.get("Military"),
            MotorVehicles=json_data.get("MotorVehicles"),
            Music=json_data.get("Music"),
            NewsAndMedia=json_data.get("NewsAndMedia"),
            Nudity=json_data.get("Nudity"),
            OnlineGreetingCards=json_data.get("OnlineGreetingCards"),
            OpenHttpProxies=json_data.get("OpenHttpProxies"),
            ParkedDomains=json_data.get("ParkedDomains"),
            PayToSurf=json_data.get("PayToSurf"),
            PeerToPeer=json_data.get("PeerToPeer"),
            PersonalSitesAndBlogs=json_data.get("PersonalSitesAndBlogs"),
            PersonalStorage=json_data.get("PersonalStorage"),
            PhilosophyAndPolitics=json_data.get("PhilosophyAndPolitics"),
            PhishingAndOtherFraud=json_data.get("PhishingAndOtherFraud"),
            PrivateIpAddresses=json_data.get("PrivateIpAddresses"),
            ProxyAvoidAndAnonymizers=json_data.get("ProxyAvoidAndAnonymizers"),
            Questionable=json_data.get("Questionable"),
            RealEstate=json_data.get("RealEstate"),
            RecreationAndHobbies=json_data.get("RecreationAndHobbies"),
            ReferenceAndResearch=json_data.get("ReferenceAndResearch"),
            Religion=json_data.get("Religion"),
            SearchEngines=json_data.get("SearchEngines"),
            SexEducation=json_data.get("SexEducation"),
            SharewareAndFreeware=json_data.get("SharewareAndFreeware"),
            Shopping=json_data.get("Shopping"),
            SocialNetwork=json_data.get("SocialNetwork"),
            Society=json_data.get("Society"),
            SpamUrls=json_data.get("SpamUrls"),
            Sports=json_data.get("Sports"),
            SpywareAndAdware=json_data.get("SpywareAndAdware"),
            StockAdviceAndTools=json_data.get("StockAdviceAndTools"),
            StreamingMedia=json_data.get("StreamingMedia"),
            SwimsuitsAndIntimateApparel=json_data.get("SwimsuitsAndIntimateApparel"),
            TrainingAndTools=json_data.get("TrainingAndTools"),
            Translation=json_data.get("Translation"),
            Travel=json_data.get("Travel"),
            Uncategorized=json_data.get("Uncategorized"),
            UnconfirmedSpamSources=json_data.get("UnconfirmedSpamSources"),
            Violence=json_data.get("Violence"),
            Weapons=json_data.get("Weapons"),
            WebAdvertisements=json_data.get("WebAdvertisements"),
            WebBasedEmail=json_data.get("WebBasedEmail"),
            WebHostingSites=json_data.get("WebHostingSites"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebCategoryDefinition = WebCategoryDefinition


@dataclass
class WebReputationDefinition(BaseModel):
    BypassLowRisk: Optional[float]
    BypassMalicious: Optional[float]
    BypassModerateRisk: Optional[float]
    BypassSuspicious: Optional[float]
    BypassThreshold: Optional[float]
    BypassTrustworthy: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WebReputationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebReputationDefinition"]:
        if not json_data:
            return None
        return cls(
            BypassLowRisk=json_data.get("BypassLowRisk"),
            BypassMalicious=json_data.get("BypassMalicious"),
            BypassModerateRisk=json_data.get("BypassModerateRisk"),
            BypassSuspicious=json_data.get("BypassSuspicious"),
            BypassThreshold=json_data.get("BypassThreshold"),
            BypassTrustworthy=json_data.get("BypassTrustworthy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebReputationDefinition = WebReputationDefinition


