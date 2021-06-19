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
    Comment: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    Sccp: Optional[Sequence["_SccpDefinition"]]
    Sip: Optional[Sequence["_SipDefinition"]]

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
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            Sccp=deserialize_list(json_data.get("Sccp"), SccpDefinition),
            Sip=deserialize_list(json_data.get("Sip"), SipDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SccpDefinition(BaseModel):
    BlockMcast: Optional[str]
    LogCallSummary: Optional[str]
    LogViolations: Optional[str]
    MaxCalls: Optional[float]
    Status: Optional[str]
    VerifyHeader: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SccpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SccpDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockMcast=json_data.get("BlockMcast"),
            LogCallSummary=json_data.get("LogCallSummary"),
            LogViolations=json_data.get("LogViolations"),
            MaxCalls=json_data.get("MaxCalls"),
            Status=json_data.get("Status"),
            VerifyHeader=json_data.get("VerifyHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SccpDefinition = SccpDefinition


@dataclass
class SipDefinition(BaseModel):
    AckRate: Optional[float]
    BlockAck: Optional[str]
    BlockBye: Optional[str]
    BlockCancel: Optional[str]
    BlockGeoRedOptions: Optional[str]
    BlockInfo: Optional[str]
    BlockInvite: Optional[str]
    BlockLongLines: Optional[str]
    BlockMessage: Optional[str]
    BlockNotify: Optional[str]
    BlockOptions: Optional[str]
    BlockPrack: Optional[str]
    BlockPublish: Optional[str]
    BlockRefer: Optional[str]
    BlockRegister: Optional[str]
    BlockSubscribe: Optional[str]
    BlockUnknown: Optional[str]
    BlockUpdate: Optional[str]
    ByeRate: Optional[float]
    CallKeepalive: Optional[float]
    CancelRate: Optional[float]
    ContactFixup: Optional[str]
    HntRestrictSourceIp: Optional[str]
    HostedNatTraversal: Optional[str]
    InfoRate: Optional[float]
    InviteRate: Optional[float]
    IpsRtp: Optional[str]
    LogCallSummary: Optional[str]
    LogViolations: Optional[str]
    MalformedHeaderAllow: Optional[str]
    MalformedHeaderCallId: Optional[str]
    MalformedHeaderContact: Optional[str]
    MalformedHeaderContentLength: Optional[str]
    MalformedHeaderContentType: Optional[str]
    MalformedHeaderCseq: Optional[str]
    MalformedHeaderExpires: Optional[str]
    MalformedHeaderFrom: Optional[str]
    MalformedHeaderMaxForwards: Optional[str]
    MalformedHeaderPAssertedIdentity: Optional[str]
    MalformedHeaderRack: Optional[str]
    MalformedHeaderRecordRoute: Optional[str]
    MalformedHeaderRoute: Optional[str]
    MalformedHeaderRseq: Optional[str]
    MalformedHeaderSdpA: Optional[str]
    MalformedHeaderSdpB: Optional[str]
    MalformedHeaderSdpC: Optional[str]
    MalformedHeaderSdpI: Optional[str]
    MalformedHeaderSdpK: Optional[str]
    MalformedHeaderSdpM: Optional[str]
    MalformedHeaderSdpO: Optional[str]
    MalformedHeaderSdpR: Optional[str]
    MalformedHeaderSdpS: Optional[str]
    MalformedHeaderSdpT: Optional[str]
    MalformedHeaderSdpV: Optional[str]
    MalformedHeaderSdpZ: Optional[str]
    MalformedHeaderTo: Optional[str]
    MalformedHeaderVia: Optional[str]
    MalformedRequestLine: Optional[str]
    MaxBodyLength: Optional[float]
    MaxDialogs: Optional[float]
    MaxIdleDialogs: Optional[float]
    MaxLineLength: Optional[float]
    MessageRate: Optional[float]
    NatPortRange: Optional[str]
    NatTrace: Optional[str]
    NoSdpFixup: Optional[str]
    NotifyRate: Optional[float]
    OpenContactPinhole: Optional[str]
    OpenRecordRoutePinhole: Optional[str]
    OpenRegisterPinhole: Optional[str]
    OpenViaPinhole: Optional[str]
    OptionsRate: Optional[float]
    PrackRate: Optional[float]
    PreserveOverride: Optional[str]
    ProvisionalInviteExpiryTime: Optional[float]
    PublishRate: Optional[float]
    ReferRate: Optional[float]
    RegisterContactTrace: Optional[str]
    RegisterRate: Optional[float]
    Rfc2543Branch: Optional[str]
    Rtp: Optional[str]
    SslAlgorithm: Optional[str]
    SslAuthClient: Optional[str]
    SslAuthServer: Optional[str]
    SslClientCertificate: Optional[str]
    SslClientRenegotiation: Optional[str]
    SslMaxVersion: Optional[str]
    SslMinVersion: Optional[str]
    SslMode: Optional[str]
    SslPfs: Optional[str]
    SslSendEmptyFrags: Optional[str]
    SslServerCertificate: Optional[str]
    Status: Optional[str]
    StrictRegister: Optional[str]
    SubscribeRate: Optional[float]
    UnknownHeader: Optional[str]
    UpdateRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SipDefinition"]:
        if not json_data:
            return None
        return cls(
            AckRate=json_data.get("AckRate"),
            BlockAck=json_data.get("BlockAck"),
            BlockBye=json_data.get("BlockBye"),
            BlockCancel=json_data.get("BlockCancel"),
            BlockGeoRedOptions=json_data.get("BlockGeoRedOptions"),
            BlockInfo=json_data.get("BlockInfo"),
            BlockInvite=json_data.get("BlockInvite"),
            BlockLongLines=json_data.get("BlockLongLines"),
            BlockMessage=json_data.get("BlockMessage"),
            BlockNotify=json_data.get("BlockNotify"),
            BlockOptions=json_data.get("BlockOptions"),
            BlockPrack=json_data.get("BlockPrack"),
            BlockPublish=json_data.get("BlockPublish"),
            BlockRefer=json_data.get("BlockRefer"),
            BlockRegister=json_data.get("BlockRegister"),
            BlockSubscribe=json_data.get("BlockSubscribe"),
            BlockUnknown=json_data.get("BlockUnknown"),
            BlockUpdate=json_data.get("BlockUpdate"),
            ByeRate=json_data.get("ByeRate"),
            CallKeepalive=json_data.get("CallKeepalive"),
            CancelRate=json_data.get("CancelRate"),
            ContactFixup=json_data.get("ContactFixup"),
            HntRestrictSourceIp=json_data.get("HntRestrictSourceIp"),
            HostedNatTraversal=json_data.get("HostedNatTraversal"),
            InfoRate=json_data.get("InfoRate"),
            InviteRate=json_data.get("InviteRate"),
            IpsRtp=json_data.get("IpsRtp"),
            LogCallSummary=json_data.get("LogCallSummary"),
            LogViolations=json_data.get("LogViolations"),
            MalformedHeaderAllow=json_data.get("MalformedHeaderAllow"),
            MalformedHeaderCallId=json_data.get("MalformedHeaderCallId"),
            MalformedHeaderContact=json_data.get("MalformedHeaderContact"),
            MalformedHeaderContentLength=json_data.get("MalformedHeaderContentLength"),
            MalformedHeaderContentType=json_data.get("MalformedHeaderContentType"),
            MalformedHeaderCseq=json_data.get("MalformedHeaderCseq"),
            MalformedHeaderExpires=json_data.get("MalformedHeaderExpires"),
            MalformedHeaderFrom=json_data.get("MalformedHeaderFrom"),
            MalformedHeaderMaxForwards=json_data.get("MalformedHeaderMaxForwards"),
            MalformedHeaderPAssertedIdentity=json_data.get("MalformedHeaderPAssertedIdentity"),
            MalformedHeaderRack=json_data.get("MalformedHeaderRack"),
            MalformedHeaderRecordRoute=json_data.get("MalformedHeaderRecordRoute"),
            MalformedHeaderRoute=json_data.get("MalformedHeaderRoute"),
            MalformedHeaderRseq=json_data.get("MalformedHeaderRseq"),
            MalformedHeaderSdpA=json_data.get("MalformedHeaderSdpA"),
            MalformedHeaderSdpB=json_data.get("MalformedHeaderSdpB"),
            MalformedHeaderSdpC=json_data.get("MalformedHeaderSdpC"),
            MalformedHeaderSdpI=json_data.get("MalformedHeaderSdpI"),
            MalformedHeaderSdpK=json_data.get("MalformedHeaderSdpK"),
            MalformedHeaderSdpM=json_data.get("MalformedHeaderSdpM"),
            MalformedHeaderSdpO=json_data.get("MalformedHeaderSdpO"),
            MalformedHeaderSdpR=json_data.get("MalformedHeaderSdpR"),
            MalformedHeaderSdpS=json_data.get("MalformedHeaderSdpS"),
            MalformedHeaderSdpT=json_data.get("MalformedHeaderSdpT"),
            MalformedHeaderSdpV=json_data.get("MalformedHeaderSdpV"),
            MalformedHeaderSdpZ=json_data.get("MalformedHeaderSdpZ"),
            MalformedHeaderTo=json_data.get("MalformedHeaderTo"),
            MalformedHeaderVia=json_data.get("MalformedHeaderVia"),
            MalformedRequestLine=json_data.get("MalformedRequestLine"),
            MaxBodyLength=json_data.get("MaxBodyLength"),
            MaxDialogs=json_data.get("MaxDialogs"),
            MaxIdleDialogs=json_data.get("MaxIdleDialogs"),
            MaxLineLength=json_data.get("MaxLineLength"),
            MessageRate=json_data.get("MessageRate"),
            NatPortRange=json_data.get("NatPortRange"),
            NatTrace=json_data.get("NatTrace"),
            NoSdpFixup=json_data.get("NoSdpFixup"),
            NotifyRate=json_data.get("NotifyRate"),
            OpenContactPinhole=json_data.get("OpenContactPinhole"),
            OpenRecordRoutePinhole=json_data.get("OpenRecordRoutePinhole"),
            OpenRegisterPinhole=json_data.get("OpenRegisterPinhole"),
            OpenViaPinhole=json_data.get("OpenViaPinhole"),
            OptionsRate=json_data.get("OptionsRate"),
            PrackRate=json_data.get("PrackRate"),
            PreserveOverride=json_data.get("PreserveOverride"),
            ProvisionalInviteExpiryTime=json_data.get("ProvisionalInviteExpiryTime"),
            PublishRate=json_data.get("PublishRate"),
            ReferRate=json_data.get("ReferRate"),
            RegisterContactTrace=json_data.get("RegisterContactTrace"),
            RegisterRate=json_data.get("RegisterRate"),
            Rfc2543Branch=json_data.get("Rfc2543Branch"),
            Rtp=json_data.get("Rtp"),
            SslAlgorithm=json_data.get("SslAlgorithm"),
            SslAuthClient=json_data.get("SslAuthClient"),
            SslAuthServer=json_data.get("SslAuthServer"),
            SslClientCertificate=json_data.get("SslClientCertificate"),
            SslClientRenegotiation=json_data.get("SslClientRenegotiation"),
            SslMaxVersion=json_data.get("SslMaxVersion"),
            SslMinVersion=json_data.get("SslMinVersion"),
            SslMode=json_data.get("SslMode"),
            SslPfs=json_data.get("SslPfs"),
            SslSendEmptyFrags=json_data.get("SslSendEmptyFrags"),
            SslServerCertificate=json_data.get("SslServerCertificate"),
            Status=json_data.get("Status"),
            StrictRegister=json_data.get("StrictRegister"),
            SubscribeRate=json_data.get("SubscribeRate"),
            UnknownHeader=json_data.get("UnknownHeader"),
            UpdateRate=json_data.get("UpdateRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SipDefinition = SipDefinition


