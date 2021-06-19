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
    AllowPromiscuousVip: Optional[float]
    Client: Optional[float]
    Dhcp: Optional[float]
    GenerateMembershipQuery: Optional[float]
    Id: Optional[str]
    Ifnum: Optional[float]
    Inside: Optional[float]
    MaxRespTime: Optional[float]
    Outside: Optional[float]
    QueryInterval: Optional[float]
    Server: Optional[float]
    SlbPartitionRedirect: Optional[float]
    TtlIgnore: Optional[float]
    Uuid: Optional[str]
    AddressList: Optional[Sequence["_AddressListDefinition"]]
    HelperAddressList: Optional[Sequence["_HelperAddressListDefinition"]]
    Ospf: Optional[Sequence["_OspfDefinition"]]
    Rip: Optional[Sequence["_RipDefinition"]]
    Router: Optional[Sequence["_RouterDefinition"]]
    StatefulFirewall: Optional[Sequence["_StatefulFirewallDefinition"]]

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
            AllowPromiscuousVip=json_data.get("AllowPromiscuousVip"),
            Client=json_data.get("Client"),
            Dhcp=json_data.get("Dhcp"),
            GenerateMembershipQuery=json_data.get("GenerateMembershipQuery"),
            Id=json_data.get("Id"),
            Ifnum=json_data.get("Ifnum"),
            Inside=json_data.get("Inside"),
            MaxRespTime=json_data.get("MaxRespTime"),
            Outside=json_data.get("Outside"),
            QueryInterval=json_data.get("QueryInterval"),
            Server=json_data.get("Server"),
            SlbPartitionRedirect=json_data.get("SlbPartitionRedirect"),
            TtlIgnore=json_data.get("TtlIgnore"),
            Uuid=json_data.get("Uuid"),
            AddressList=deserialize_list(json_data.get("AddressList"), AddressListDefinition),
            HelperAddressList=deserialize_list(json_data.get("HelperAddressList"), HelperAddressListDefinition),
            Ospf=deserialize_list(json_data.get("Ospf"), OspfDefinition),
            Rip=deserialize_list(json_data.get("Rip"), RipDefinition),
            Router=deserialize_list(json_data.get("Router"), RouterDefinition),
            StatefulFirewall=deserialize_list(json_data.get("StatefulFirewall"), StatefulFirewallDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AddressListDefinition(BaseModel):
    Ipv4Address: Optional[str]
    Ipv4Netmask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddressListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressListDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4Netmask=json_data.get("Ipv4Netmask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressListDefinition = AddressListDefinition


@dataclass
class HelperAddressListDefinition(BaseModel):
    HelperAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HelperAddressListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HelperAddressListDefinition"]:
        if not json_data:
            return None
        return cls(
            HelperAddress=json_data.get("HelperAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HelperAddressListDefinition = HelperAddressListDefinition


@dataclass
class OspfDefinition(BaseModel):
    OspfGlobal: Optional[Sequence["_OspfGlobalDefinition"]]
    OspfIpList: Optional[Sequence["_OspfIpListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OspfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfDefinition"]:
        if not json_data:
            return None
        return cls(
            OspfGlobal=deserialize_list(json_data.get("OspfGlobal"), OspfGlobalDefinition),
            OspfIpList=deserialize_list(json_data.get("OspfIpList"), OspfIpListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfDefinition = OspfDefinition


@dataclass
class OspfGlobalDefinition(BaseModel):
    AuthenticationKey: Optional[str]
    Cost: Optional[float]
    DeadInterval: Optional[float]
    Disable: Optional[str]
    HelloInterval: Optional[float]
    Mtu: Optional[float]
    MtuIgnore: Optional[float]
    Priority: Optional[float]
    RetransmitInterval: Optional[float]
    TransmitDelay: Optional[float]
    Uuid: Optional[str]
    AuthenticationCfg: Optional[Sequence["_AuthenticationCfgDefinition"]]
    BfdCfg: Optional[Sequence["_BfdCfgDefinition"]]
    DatabaseFilterCfg: Optional[Sequence["_DatabaseFilterCfgDefinition"]]
    MessageDigestCfg: Optional[Sequence["_MessageDigestCfgDefinition"]]
    Network: Optional[Sequence["_NetworkDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OspfGlobalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfGlobalDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationKey=json_data.get("AuthenticationKey"),
            Cost=json_data.get("Cost"),
            DeadInterval=json_data.get("DeadInterval"),
            Disable=json_data.get("Disable"),
            HelloInterval=json_data.get("HelloInterval"),
            Mtu=json_data.get("Mtu"),
            MtuIgnore=json_data.get("MtuIgnore"),
            Priority=json_data.get("Priority"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            TransmitDelay=json_data.get("TransmitDelay"),
            Uuid=json_data.get("Uuid"),
            AuthenticationCfg=deserialize_list(json_data.get("AuthenticationCfg"), AuthenticationCfgDefinition),
            BfdCfg=deserialize_list(json_data.get("BfdCfg"), BfdCfgDefinition),
            DatabaseFilterCfg=deserialize_list(json_data.get("DatabaseFilterCfg"), DatabaseFilterCfgDefinition),
            MessageDigestCfg=deserialize_list(json_data.get("MessageDigestCfg"), MessageDigestCfgDefinition),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfGlobalDefinition = OspfGlobalDefinition


@dataclass
class AuthenticationCfgDefinition(BaseModel):
    Authentication: Optional[float]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationCfgDefinition = AuthenticationCfgDefinition


@dataclass
class BfdCfgDefinition(BaseModel):
    Bfd: Optional[float]
    Disable: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BfdCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BfdCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Bfd=json_data.get("Bfd"),
            Disable=json_data.get("Disable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BfdCfgDefinition = BfdCfgDefinition


@dataclass
class DatabaseFilterCfgDefinition(BaseModel):
    DatabaseFilter: Optional[str]
    Out: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseFilterCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseFilterCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseFilter=json_data.get("DatabaseFilter"),
            Out=json_data.get("Out"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseFilterCfgDefinition = DatabaseFilterCfgDefinition


@dataclass
class MessageDigestCfgDefinition(BaseModel):
    MessageDigestKey: Optional[float]
    Md5: Optional[Sequence["_Md5Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MessageDigestCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MessageDigestCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            MessageDigestKey=json_data.get("MessageDigestKey"),
            Md5=deserialize_list(json_data.get("Md5"), Md5Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MessageDigestCfgDefinition = MessageDigestCfgDefinition


@dataclass
class Md5Definition(BaseModel):
    Encrypted: Optional[str]
    Md5Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Md5Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Md5Definition"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            Md5Value=json_data.get("Md5Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Md5Definition = Md5Definition


@dataclass
class NetworkDefinition(BaseModel):
    Broadcast: Optional[float]
    NonBroadcast: Optional[float]
    P2mpNbma: Optional[float]
    PointToMultipoint: Optional[float]
    PointToPoint: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Broadcast=json_data.get("Broadcast"),
            NonBroadcast=json_data.get("NonBroadcast"),
            P2mpNbma=json_data.get("P2mpNbma"),
            PointToMultipoint=json_data.get("PointToMultipoint"),
            PointToPoint=json_data.get("PointToPoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class OspfIpListDefinition(BaseModel):
    Authentication: Optional[float]
    AuthenticationKey: Optional[str]
    Cost: Optional[float]
    DatabaseFilter: Optional[str]
    DeadInterval: Optional[float]
    HelloInterval: Optional[float]
    IpAddr: Optional[str]
    MtuIgnore: Optional[float]
    Out: Optional[float]
    Priority: Optional[float]
    RetransmitInterval: Optional[float]
    TransmitDelay: Optional[float]
    Uuid: Optional[str]
    Value: Optional[str]
    MessageDigestCfg: Optional[Sequence["_MessageDigestCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OspfIpListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfIpListDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            AuthenticationKey=json_data.get("AuthenticationKey"),
            Cost=json_data.get("Cost"),
            DatabaseFilter=json_data.get("DatabaseFilter"),
            DeadInterval=json_data.get("DeadInterval"),
            HelloInterval=json_data.get("HelloInterval"),
            IpAddr=json_data.get("IpAddr"),
            MtuIgnore=json_data.get("MtuIgnore"),
            Out=json_data.get("Out"),
            Priority=json_data.get("Priority"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            TransmitDelay=json_data.get("TransmitDelay"),
            Uuid=json_data.get("Uuid"),
            Value=json_data.get("Value"),
            MessageDigestCfg=deserialize_list(json_data.get("MessageDigestCfg"), MessageDigestCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfIpListDefinition = OspfIpListDefinition


@dataclass
class RipDefinition(BaseModel):
    ReceivePacket: Optional[float]
    SendPacket: Optional[float]
    Uuid: Optional[str]
    Authentication: Optional[Sequence["_AuthenticationDefinition"]]
    ReceiveCfg: Optional[Sequence["_ReceiveCfgDefinition"]]
    SendCfg: Optional[Sequence["_SendCfgDefinition"]]
    SplitHorizonCfg: Optional[Sequence["_SplitHorizonCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RipDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RipDefinition"]:
        if not json_data:
            return None
        return cls(
            ReceivePacket=json_data.get("ReceivePacket"),
            SendPacket=json_data.get("SendPacket"),
            Uuid=json_data.get("Uuid"),
            Authentication=deserialize_list(json_data.get("Authentication"), AuthenticationDefinition),
            ReceiveCfg=deserialize_list(json_data.get("ReceiveCfg"), ReceiveCfgDefinition),
            SendCfg=deserialize_list(json_data.get("SendCfg"), SendCfgDefinition),
            SplitHorizonCfg=deserialize_list(json_data.get("SplitHorizonCfg"), SplitHorizonCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RipDefinition = RipDefinition


@dataclass
class AuthenticationDefinition(BaseModel):
    KeyChain: Optional[Sequence["_KeyChainDefinition"]]
    Mode: Optional[Sequence["_ModeDefinition"]]
    Str: Optional[Sequence["_StrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyChain=deserialize_list(json_data.get("KeyChain"), KeyChainDefinition),
            Mode=deserialize_list(json_data.get("Mode"), ModeDefinition),
            Str=deserialize_list(json_data.get("Str"), StrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationDefinition = AuthenticationDefinition


@dataclass
class KeyChainDefinition(BaseModel):
    KeyChain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyChainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyChainDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyChain=json_data.get("KeyChain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyChainDefinition = KeyChainDefinition


@dataclass
class ModeDefinition(BaseModel):
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModeDefinition"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModeDefinition = ModeDefinition


@dataclass
class StrDefinition(BaseModel):
    String: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StrDefinition"]:
        if not json_data:
            return None
        return cls(
            String=json_data.get("String"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StrDefinition = StrDefinition


@dataclass
class ReceiveCfgDefinition(BaseModel):
    Receive: Optional[float]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReceiveCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReceiveCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Receive=json_data.get("Receive"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReceiveCfgDefinition = ReceiveCfgDefinition


@dataclass
class SendCfgDefinition(BaseModel):
    Send: Optional[float]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SendCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SendCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Send=json_data.get("Send"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SendCfgDefinition = SendCfgDefinition


@dataclass
class SplitHorizonCfgDefinition(BaseModel):
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SplitHorizonCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SplitHorizonCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SplitHorizonCfgDefinition = SplitHorizonCfgDefinition


@dataclass
class RouterDefinition(BaseModel):
    Isis: Optional[Sequence["_IsisDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouterDefinition"]:
        if not json_data:
            return None
        return cls(
            Isis=deserialize_list(json_data.get("Isis"), IsisDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouterDefinition = RouterDefinition


@dataclass
class IsisDefinition(BaseModel):
    Tag: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IsisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsisDefinition"]:
        if not json_data:
            return None
        return cls(
            Tag=json_data.get("Tag"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsisDefinition = IsisDefinition


@dataclass
class StatefulFirewallDefinition(BaseModel):
    AccessList: Optional[float]
    AclId: Optional[float]
    ClassList: Optional[str]
    Inside: Optional[float]
    Outside: Optional[float]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulFirewallDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulFirewallDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessList=json_data.get("AccessList"),
            AclId=json_data.get("AclId"),
            ClassList=json_data.get("ClassList"),
            Inside=json_data.get("Inside"),
            Outside=json_data.get("Outside"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulFirewallDefinition = StatefulFirewallDefinition


