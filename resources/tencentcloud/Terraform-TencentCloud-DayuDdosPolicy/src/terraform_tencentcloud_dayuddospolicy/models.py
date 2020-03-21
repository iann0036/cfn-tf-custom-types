# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    BlackIps: Optional[Sequence[str]]
    CreateTime: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[str]
    ResourceType: Optional[str]
    SceneId: Optional[str]
    WatermarkKey: Optional[Sequence["_WatermarkKey"]]
    WhiteIps: Optional[Sequence[str]]
    DropOptions: Optional[Sequence["_DropOptions"]]
    PacketFilters: Optional[Sequence["_PacketFilters"]]
    PortFilters: Optional[Sequence["_PortFilters"]]
    WatermarkFilters: Optional[Sequence["_WatermarkFilters"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BlackIps=json_data.get("BlackIps"),
            CreateTime=json_data.get("CreateTime"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            ResourceType=json_data.get("ResourceType"),
            SceneId=json_data.get("SceneId"),
            WatermarkKey=json_data.get("WatermarkKey"),
            WhiteIps=json_data.get("WhiteIps"),
            DropOptions=json_data.get("DropOptions"),
            PacketFilters=json_data.get("PacketFilters"),
            PortFilters=json_data.get("PortFilters"),
            WatermarkFilters=json_data.get("WatermarkFilters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class WatermarkKey:
    Content: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    OpenSwitch: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_WatermarkKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WatermarkKey"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            OpenSwitch=json_data.get("OpenSwitch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WatermarkKey = WatermarkKey


@dataclass
class DropOptions:
    BadConnThreshold: Optional[float]
    CheckSyncConn: Optional[bool]
    ConnTimeout: Optional[float]
    DConnLimit: Optional[float]
    DNewLimit: Optional[float]
    DropAbroad: Optional[bool]
    DropIcmp: Optional[bool]
    DropOther: Optional[bool]
    DropTcp: Optional[bool]
    DropUdp: Optional[bool]
    IcmpMbpsLimit: Optional[float]
    NullConnEnable: Optional[bool]
    OtherMbpsLimit: Optional[float]
    SConnLimit: Optional[float]
    SNewLimit: Optional[float]
    SynLimit: Optional[float]
    SynRate: Optional[float]
    TcpMbpsLimit: Optional[float]
    UdpMbpsLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DropOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DropOptions"]:
        if not json_data:
            return None
        return cls(
            BadConnThreshold=json_data.get("BadConnThreshold"),
            CheckSyncConn=json_data.get("CheckSyncConn"),
            ConnTimeout=json_data.get("ConnTimeout"),
            DConnLimit=json_data.get("DConnLimit"),
            DNewLimit=json_data.get("DNewLimit"),
            DropAbroad=json_data.get("DropAbroad"),
            DropIcmp=json_data.get("DropIcmp"),
            DropOther=json_data.get("DropOther"),
            DropTcp=json_data.get("DropTcp"),
            DropUdp=json_data.get("DropUdp"),
            IcmpMbpsLimit=json_data.get("IcmpMbpsLimit"),
            NullConnEnable=json_data.get("NullConnEnable"),
            OtherMbpsLimit=json_data.get("OtherMbpsLimit"),
            SConnLimit=json_data.get("SConnLimit"),
            SNewLimit=json_data.get("SNewLimit"),
            SynLimit=json_data.get("SynLimit"),
            SynRate=json_data.get("SynRate"),
            TcpMbpsLimit=json_data.get("TcpMbpsLimit"),
            UdpMbpsLimit=json_data.get("UdpMbpsLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DropOptions = DropOptions


@dataclass
class PacketFilters:
    Action: Optional[str]
    DEndPort: Optional[float]
    DStartPort: Optional[float]
    Depth: Optional[float]
    IsInclude: Optional[bool]
    MatchBegin: Optional[str]
    MatchStr: Optional[str]
    MatchType: Optional[str]
    Offset: Optional[float]
    PktLengthMax: Optional[float]
    PktLengthMin: Optional[float]
    Protocol: Optional[str]
    SEndPort: Optional[float]
    SStartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PacketFilters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PacketFilters"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            DEndPort=json_data.get("DEndPort"),
            DStartPort=json_data.get("DStartPort"),
            Depth=json_data.get("Depth"),
            IsInclude=json_data.get("IsInclude"),
            MatchBegin=json_data.get("MatchBegin"),
            MatchStr=json_data.get("MatchStr"),
            MatchType=json_data.get("MatchType"),
            Offset=json_data.get("Offset"),
            PktLengthMax=json_data.get("PktLengthMax"),
            PktLengthMin=json_data.get("PktLengthMin"),
            Protocol=json_data.get("Protocol"),
            SEndPort=json_data.get("SEndPort"),
            SStartPort=json_data.get("SStartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PacketFilters = PacketFilters


@dataclass
class PortFilters:
    Action: Optional[str]
    EndPort: Optional[float]
    Kind: Optional[float]
    Protocol: Optional[str]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortFilters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortFilters"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            EndPort=json_data.get("EndPort"),
            Kind=json_data.get("Kind"),
            Protocol=json_data.get("Protocol"),
            StartPort=json_data.get("StartPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortFilters = PortFilters


@dataclass
class WatermarkFilters:
    AutoRemove: Optional[bool]
    Offset: Optional[float]
    OpenSwitch: Optional[bool]
    TcpPortList: Optional[Sequence[str]]
    UdpPortList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_WatermarkFilters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WatermarkFilters"]:
        if not json_data:
            return None
        return cls(
            AutoRemove=json_data.get("AutoRemove"),
            Offset=json_data.get("Offset"),
            OpenSwitch=json_data.get("OpenSwitch"),
            TcpPortList=json_data.get("TcpPortList"),
            UdpPortList=json_data.get("UdpPortList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WatermarkFilters = WatermarkFilters


