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
    BlackIps: Optional[Sequence[str]]
    CreateTime: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PolicyId: Optional[str]
    ResourceType: Optional[str]
    SceneId: Optional[str]
    WatermarkKey: Optional[Sequence["_WatermarkKeyDefinition"]]
    WhiteIps: Optional[Sequence[str]]
    DropOptions: Optional[Sequence["_DropOptionsDefinition"]]
    PacketFilters: Optional[Sequence["_PacketFiltersDefinition"]]
    PortFilters: Optional[Sequence["_PortFiltersDefinition"]]
    WatermarkFilters: Optional[Sequence["_WatermarkFiltersDefinition"]]

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
            BlackIps=json_data.get("BlackIps"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            ResourceType=json_data.get("ResourceType"),
            SceneId=json_data.get("SceneId"),
            WatermarkKey=deserialize_list(json_data.get("WatermarkKey"), WatermarkKeyDefinition),
            WhiteIps=json_data.get("WhiteIps"),
            DropOptions=deserialize_list(json_data.get("DropOptions"), DropOptionsDefinition),
            PacketFilters=deserialize_list(json_data.get("PacketFilters"), PacketFiltersDefinition),
            PortFilters=deserialize_list(json_data.get("PortFilters"), PortFiltersDefinition),
            WatermarkFilters=deserialize_list(json_data.get("WatermarkFilters"), WatermarkFiltersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class WatermarkKeyDefinition(BaseModel):
    Content: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    OpenSwitch: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_WatermarkKeyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WatermarkKeyDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            OpenSwitch=json_data.get("OpenSwitch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WatermarkKeyDefinition = WatermarkKeyDefinition


@dataclass
class DropOptionsDefinition(BaseModel):
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
        cls: Type["_DropOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DropOptionsDefinition"]:
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
_DropOptionsDefinition = DropOptionsDefinition


@dataclass
class PacketFiltersDefinition(BaseModel):
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
        cls: Type["_PacketFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PacketFiltersDefinition"]:
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
_PacketFiltersDefinition = PacketFiltersDefinition


@dataclass
class PortFiltersDefinition(BaseModel):
    Action: Optional[str]
    EndPort: Optional[float]
    Kind: Optional[float]
    Protocol: Optional[str]
    StartPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortFiltersDefinition"]:
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
_PortFiltersDefinition = PortFiltersDefinition


@dataclass
class WatermarkFiltersDefinition(BaseModel):
    AutoRemove: Optional[bool]
    Offset: Optional[float]
    OpenSwitch: Optional[bool]
    TcpPortList: Optional[Sequence[str]]
    UdpPortList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_WatermarkFiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WatermarkFiltersDefinition"]:
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
_WatermarkFiltersDefinition = WatermarkFiltersDefinition


