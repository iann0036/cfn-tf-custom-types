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
    AcctVerify: Optional[str]
    AddGwRoute: Optional[str]
    AddRoute: Optional[str]
    AssignIp: Optional[str]
    AssignIpFrom: Optional[str]
    Authmethod: Optional[str]
    AuthmethodRemote: Optional[str]
    Authpasswd: Optional[str]
    Authusr: Optional[str]
    Authusrgrp: Optional[str]
    AutoNegotiate: Optional[str]
    Banner: Optional[str]
    CertIdValidation: Optional[str]
    ChildlessIke: Optional[str]
    ClientAutoNegotiate: Optional[str]
    ClientKeepAlive: Optional[str]
    Comments: Optional[str]
    Dhcp6RaLinkaddr: Optional[str]
    DhcpRaGiaddr: Optional[str]
    Dhgrp: Optional[str]
    DigitalSignatureAuth: Optional[str]
    Distance: Optional[float]
    DnsMode: Optional[str]
    Domain: Optional[str]
    Dpd: Optional[str]
    DpdRetrycount: Optional[float]
    DpdRetryinterval: Optional[str]
    DynamicSortSubtable: Optional[str]
    Eap: Optional[str]
    EapExcludePeergrp: Optional[str]
    EapIdentity: Optional[str]
    EnforceUniqueId: Optional[str]
    FecBase: Optional[float]
    FecCodec: Optional[float]
    FecEgress: Optional[str]
    FecIngress: Optional[str]
    FecReceiveTimeout: Optional[float]
    FecRedundant: Optional[float]
    FecSendTimeout: Optional[float]
    ForticlientEnforcement: Optional[str]
    Fragmentation: Optional[str]
    FragmentationMtu: Optional[float]
    GroupAuthentication: Optional[str]
    GroupAuthenticationSecret: Optional[str]
    HaSyncEspSeqno: Optional[str]
    Id: Optional[str]
    IdleTimeout: Optional[str]
    IdleTimeoutinterval: Optional[float]
    IkeVersion: Optional[str]
    IncludeLocalLan: Optional[str]
    Interface: Optional[str]
    Ipv4DnsServer1: Optional[str]
    Ipv4DnsServer2: Optional[str]
    Ipv4DnsServer3: Optional[str]
    Ipv4EndIp: Optional[str]
    Ipv4Name: Optional[str]
    Ipv4Netmask: Optional[str]
    Ipv4SplitExclude: Optional[str]
    Ipv4SplitInclude: Optional[str]
    Ipv4StartIp: Optional[str]
    Ipv4WinsServer1: Optional[str]
    Ipv4WinsServer2: Optional[str]
    Ipv6DnsServer1: Optional[str]
    Ipv6DnsServer2: Optional[str]
    Ipv6DnsServer3: Optional[str]
    Ipv6EndIp: Optional[str]
    Ipv6Name: Optional[str]
    Ipv6Prefix: Optional[float]
    Ipv6SplitExclude: Optional[str]
    Ipv6SplitInclude: Optional[str]
    Ipv6StartIp: Optional[str]
    Keepalive: Optional[float]
    Keylife: Optional[float]
    LocalGw: Optional[str]
    Localid: Optional[str]
    LocalidType: Optional[str]
    MeshSelectorType: Optional[str]
    Mode: Optional[str]
    ModeCfg: Optional[str]
    Name: Optional[str]
    Nattraversal: Optional[str]
    NegotiateTimeout: Optional[float]
    NetworkId: Optional[float]
    NetworkOverlay: Optional[str]
    Peer: Optional[str]
    Peergrp: Optional[str]
    Peerid: Optional[str]
    Peertype: Optional[str]
    Ppk: Optional[str]
    PpkIdentity: Optional[str]
    PpkSecret: Optional[str]
    Priority: Optional[float]
    Proposal: Optional[str]
    Psksecret: Optional[str]
    PsksecretRemote: Optional[str]
    Reauth: Optional[str]
    Rekey: Optional[str]
    RemoteGw: Optional[str]
    RemotegwDdns: Optional[str]
    RsaSignatureFormat: Optional[str]
    SavePassword: Optional[str]
    SendCertChain: Optional[str]
    SignatureHashAlg: Optional[str]
    SplitIncludeService: Optional[str]
    SuiteB: Optional[str]
    Type: Optional[str]
    UnitySupport: Optional[str]
    Usrgrp: Optional[str]
    Vdomparam: Optional[str]
    WizardType: Optional[str]
    Xauthtype: Optional[str]
    BackupGateway: Optional[Sequence["_BackupGatewayDefinition"]]
    Certificate: Optional[Sequence["_CertificateDefinition"]]
    Ipv4ExcludeRange: Optional[Sequence["_Ipv4ExcludeRangeDefinition"]]
    Ipv6ExcludeRange: Optional[Sequence["_Ipv6ExcludeRangeDefinition"]]

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
            AcctVerify=json_data.get("AcctVerify"),
            AddGwRoute=json_data.get("AddGwRoute"),
            AddRoute=json_data.get("AddRoute"),
            AssignIp=json_data.get("AssignIp"),
            AssignIpFrom=json_data.get("AssignIpFrom"),
            Authmethod=json_data.get("Authmethod"),
            AuthmethodRemote=json_data.get("AuthmethodRemote"),
            Authpasswd=json_data.get("Authpasswd"),
            Authusr=json_data.get("Authusr"),
            Authusrgrp=json_data.get("Authusrgrp"),
            AutoNegotiate=json_data.get("AutoNegotiate"),
            Banner=json_data.get("Banner"),
            CertIdValidation=json_data.get("CertIdValidation"),
            ChildlessIke=json_data.get("ChildlessIke"),
            ClientAutoNegotiate=json_data.get("ClientAutoNegotiate"),
            ClientKeepAlive=json_data.get("ClientKeepAlive"),
            Comments=json_data.get("Comments"),
            Dhcp6RaLinkaddr=json_data.get("Dhcp6RaLinkaddr"),
            DhcpRaGiaddr=json_data.get("DhcpRaGiaddr"),
            Dhgrp=json_data.get("Dhgrp"),
            DigitalSignatureAuth=json_data.get("DigitalSignatureAuth"),
            Distance=json_data.get("Distance"),
            DnsMode=json_data.get("DnsMode"),
            Domain=json_data.get("Domain"),
            Dpd=json_data.get("Dpd"),
            DpdRetrycount=json_data.get("DpdRetrycount"),
            DpdRetryinterval=json_data.get("DpdRetryinterval"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Eap=json_data.get("Eap"),
            EapExcludePeergrp=json_data.get("EapExcludePeergrp"),
            EapIdentity=json_data.get("EapIdentity"),
            EnforceUniqueId=json_data.get("EnforceUniqueId"),
            FecBase=json_data.get("FecBase"),
            FecCodec=json_data.get("FecCodec"),
            FecEgress=json_data.get("FecEgress"),
            FecIngress=json_data.get("FecIngress"),
            FecReceiveTimeout=json_data.get("FecReceiveTimeout"),
            FecRedundant=json_data.get("FecRedundant"),
            FecSendTimeout=json_data.get("FecSendTimeout"),
            ForticlientEnforcement=json_data.get("ForticlientEnforcement"),
            Fragmentation=json_data.get("Fragmentation"),
            FragmentationMtu=json_data.get("FragmentationMtu"),
            GroupAuthentication=json_data.get("GroupAuthentication"),
            GroupAuthenticationSecret=json_data.get("GroupAuthenticationSecret"),
            HaSyncEspSeqno=json_data.get("HaSyncEspSeqno"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            IdleTimeoutinterval=json_data.get("IdleTimeoutinterval"),
            IkeVersion=json_data.get("IkeVersion"),
            IncludeLocalLan=json_data.get("IncludeLocalLan"),
            Interface=json_data.get("Interface"),
            Ipv4DnsServer1=json_data.get("Ipv4DnsServer1"),
            Ipv4DnsServer2=json_data.get("Ipv4DnsServer2"),
            Ipv4DnsServer3=json_data.get("Ipv4DnsServer3"),
            Ipv4EndIp=json_data.get("Ipv4EndIp"),
            Ipv4Name=json_data.get("Ipv4Name"),
            Ipv4Netmask=json_data.get("Ipv4Netmask"),
            Ipv4SplitExclude=json_data.get("Ipv4SplitExclude"),
            Ipv4SplitInclude=json_data.get("Ipv4SplitInclude"),
            Ipv4StartIp=json_data.get("Ipv4StartIp"),
            Ipv4WinsServer1=json_data.get("Ipv4WinsServer1"),
            Ipv4WinsServer2=json_data.get("Ipv4WinsServer2"),
            Ipv6DnsServer1=json_data.get("Ipv6DnsServer1"),
            Ipv6DnsServer2=json_data.get("Ipv6DnsServer2"),
            Ipv6DnsServer3=json_data.get("Ipv6DnsServer3"),
            Ipv6EndIp=json_data.get("Ipv6EndIp"),
            Ipv6Name=json_data.get("Ipv6Name"),
            Ipv6Prefix=json_data.get("Ipv6Prefix"),
            Ipv6SplitExclude=json_data.get("Ipv6SplitExclude"),
            Ipv6SplitInclude=json_data.get("Ipv6SplitInclude"),
            Ipv6StartIp=json_data.get("Ipv6StartIp"),
            Keepalive=json_data.get("Keepalive"),
            Keylife=json_data.get("Keylife"),
            LocalGw=json_data.get("LocalGw"),
            Localid=json_data.get("Localid"),
            LocalidType=json_data.get("LocalidType"),
            MeshSelectorType=json_data.get("MeshSelectorType"),
            Mode=json_data.get("Mode"),
            ModeCfg=json_data.get("ModeCfg"),
            Name=json_data.get("Name"),
            Nattraversal=json_data.get("Nattraversal"),
            NegotiateTimeout=json_data.get("NegotiateTimeout"),
            NetworkId=json_data.get("NetworkId"),
            NetworkOverlay=json_data.get("NetworkOverlay"),
            Peer=json_data.get("Peer"),
            Peergrp=json_data.get("Peergrp"),
            Peerid=json_data.get("Peerid"),
            Peertype=json_data.get("Peertype"),
            Ppk=json_data.get("Ppk"),
            PpkIdentity=json_data.get("PpkIdentity"),
            PpkSecret=json_data.get("PpkSecret"),
            Priority=json_data.get("Priority"),
            Proposal=json_data.get("Proposal"),
            Psksecret=json_data.get("Psksecret"),
            PsksecretRemote=json_data.get("PsksecretRemote"),
            Reauth=json_data.get("Reauth"),
            Rekey=json_data.get("Rekey"),
            RemoteGw=json_data.get("RemoteGw"),
            RemotegwDdns=json_data.get("RemotegwDdns"),
            RsaSignatureFormat=json_data.get("RsaSignatureFormat"),
            SavePassword=json_data.get("SavePassword"),
            SendCertChain=json_data.get("SendCertChain"),
            SignatureHashAlg=json_data.get("SignatureHashAlg"),
            SplitIncludeService=json_data.get("SplitIncludeService"),
            SuiteB=json_data.get("SuiteB"),
            Type=json_data.get("Type"),
            UnitySupport=json_data.get("UnitySupport"),
            Usrgrp=json_data.get("Usrgrp"),
            Vdomparam=json_data.get("Vdomparam"),
            WizardType=json_data.get("WizardType"),
            Xauthtype=json_data.get("Xauthtype"),
            BackupGateway=deserialize_list(json_data.get("BackupGateway"), BackupGatewayDefinition),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
            Ipv4ExcludeRange=deserialize_list(json_data.get("Ipv4ExcludeRange"), Ipv4ExcludeRangeDefinition),
            Ipv6ExcludeRange=deserialize_list(json_data.get("Ipv6ExcludeRange"), Ipv6ExcludeRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackupGatewayDefinition(BaseModel):
    Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupGatewayDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupGatewayDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupGatewayDefinition = BackupGatewayDefinition


@dataclass
class CertificateDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class Ipv4ExcludeRangeDefinition(BaseModel):
    EndIp: Optional[str]
    Id: Optional[float]
    StartIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4ExcludeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4ExcludeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EndIp=json_data.get("EndIp"),
            Id=json_data.get("Id"),
            StartIp=json_data.get("StartIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4ExcludeRangeDefinition = Ipv4ExcludeRangeDefinition


@dataclass
class Ipv6ExcludeRangeDefinition(BaseModel):
    EndIp: Optional[str]
    Id: Optional[float]
    StartIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6ExcludeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6ExcludeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EndIp=json_data.get("EndIp"),
            Id=json_data.get("Id"),
            StartIp=json_data.get("StartIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6ExcludeRangeDefinition = Ipv6ExcludeRangeDefinition


