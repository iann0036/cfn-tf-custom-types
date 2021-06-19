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
    AsNumber: Optional[float]
    Id: Optional[str]
    ProcessId: Optional[str]
    Sequence: Optional[float]
    Tag: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    Match: Optional[Sequence["_MatchDefinition"]]
    Set: Optional[Sequence["_SetDefinition"]]

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
            AsNumber=json_data.get("AsNumber"),
            Id=json_data.get("Id"),
            ProcessId=json_data.get("ProcessId"),
            Sequence=json_data.get("Sequence"),
            Tag=json_data.get("Tag"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
            Set=deserialize_list(json_data.get("Set"), SetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MatchDefinition(BaseModel):
    Uuid: Optional[str]
    AsPath: Optional[Sequence["_AsPathDefinition"]]
    Community: Optional[Sequence["_CommunityDefinition"]]
    Extcommunity: Optional[Sequence["_ExtcommunityDefinition"]]
    Group: Optional[Sequence["_GroupDefinition"]]
    Interface: Optional[Sequence["_InterfaceDefinition"]]
    Ip: Optional[Sequence["_IpDefinition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]
    LocalPreference: Optional[Sequence["_LocalPreferenceDefinition"]]
    Metric: Optional[Sequence["_MetricDefinition"]]
    Origin: Optional[Sequence["_OriginDefinition"]]
    RouteType: Optional[Sequence["_RouteTypeDefinition"]]
    Scaleout: Optional[Sequence["_ScaleoutDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Uuid=json_data.get("Uuid"),
            AsPath=deserialize_list(json_data.get("AsPath"), AsPathDefinition),
            Community=deserialize_list(json_data.get("Community"), CommunityDefinition),
            Extcommunity=deserialize_list(json_data.get("Extcommunity"), ExtcommunityDefinition),
            Group=deserialize_list(json_data.get("Group"), GroupDefinition),
            Interface=deserialize_list(json_data.get("Interface"), InterfaceDefinition),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
            LocalPreference=deserialize_list(json_data.get("LocalPreference"), LocalPreferenceDefinition),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
            Origin=deserialize_list(json_data.get("Origin"), OriginDefinition),
            RouteType=deserialize_list(json_data.get("RouteType"), RouteTypeDefinition),
            Scaleout=deserialize_list(json_data.get("Scaleout"), ScaleoutDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class AsPathDefinition(BaseModel):
    Num: Optional[float]
    Num2: Optional[float]
    Prepend: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AsPathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsPathDefinition"]:
        if not json_data:
            return None
        return cls(
            Num=json_data.get("Num"),
            Num2=json_data.get("Num2"),
            Prepend=json_data.get("Prepend"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsPathDefinition = AsPathDefinition


@dataclass
class CommunityDefinition(BaseModel):
    NameCfg: Optional[Sequence["_NameCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CommunityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommunityDefinition"]:
        if not json_data:
            return None
        return cls(
            NameCfg=deserialize_list(json_data.get("NameCfg"), NameCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommunityDefinition = CommunityDefinition


@dataclass
class NameCfgDefinition(BaseModel):
    ExactMatch: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NameCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NameCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            ExactMatch=json_data.get("ExactMatch"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NameCfgDefinition = NameCfgDefinition


@dataclass
class ExtcommunityDefinition(BaseModel):
    Rt: Optional[Sequence["_RtDefinition"]]
    Soo: Optional[Sequence["_SooDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExtcommunityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtcommunityDefinition"]:
        if not json_data:
            return None
        return cls(
            Rt=deserialize_list(json_data.get("Rt"), RtDefinition),
            Soo=deserialize_list(json_data.get("Soo"), SooDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtcommunityDefinition = ExtcommunityDefinition


@dataclass
class RtDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RtDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RtDefinition = RtDefinition


@dataclass
class SooDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SooDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SooDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SooDefinition = SooDefinition


@dataclass
class GroupDefinition(BaseModel):
    GroupId: Optional[float]
    HaState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
            HaState=json_data.get("HaState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupDefinition = GroupDefinition


@dataclass
class InterfaceDefinition(BaseModel):
    Ethernet: Optional[float]
    Loopback: Optional[float]
    Trunk: Optional[float]
    Tunnel: Optional[float]
    Ve: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            Ethernet=json_data.get("Ethernet"),
            Loopback=json_data.get("Loopback"),
            Trunk=json_data.get("Trunk"),
            Tunnel=json_data.get("Tunnel"),
            Ve=json_data.get("Ve"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceDefinition = InterfaceDefinition


@dataclass
class IpDefinition(BaseModel):
    NextHop: Optional[Sequence["_NextHopDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpDefinition"]:
        if not json_data:
            return None
        return cls(
            NextHop=deserialize_list(json_data.get("NextHop"), NextHopDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpDefinition = IpDefinition


@dataclass
class NextHopDefinition(BaseModel):
    Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NextHopDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NextHopDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NextHopDefinition = NextHopDefinition


@dataclass
class Ipv6Definition(BaseModel):
    NextHop1: Optional[Sequence["_NextHop1Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6Definition"]:
        if not json_data:
            return None
        return cls(
            NextHop1=deserialize_list(json_data.get("NextHop1"), NextHop1Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6Definition = Ipv6Definition


@dataclass
class NextHop1Definition(BaseModel):
    Address: Optional[str]
    Local: Optional[Sequence["_LocalDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NextHop1Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NextHop1Definition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Local=deserialize_list(json_data.get("Local"), LocalDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NextHop1Definition = NextHop1Definition


@dataclass
class LocalDefinition(BaseModel):
    Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalDefinition = LocalDefinition


@dataclass
class LocalPreferenceDefinition(BaseModel):
    Val: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LocalPreferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalPreferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Val=json_data.get("Val"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalPreferenceDefinition = LocalPreferenceDefinition


@dataclass
class MetricDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


@dataclass
class OriginDefinition(BaseModel):
    Egp: Optional[float]
    Igp: Optional[float]
    Incomplete: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OriginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginDefinition"]:
        if not json_data:
            return None
        return cls(
            Egp=json_data.get("Egp"),
            Igp=json_data.get("Igp"),
            Incomplete=json_data.get("Incomplete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginDefinition = OriginDefinition


@dataclass
class RouteTypeDefinition(BaseModel):
    External: Optional[Sequence["_ExternalDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RouteTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            External=deserialize_list(json_data.get("External"), ExternalDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteTypeDefinition = RouteTypeDefinition


@dataclass
class ExternalDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalDefinition = ExternalDefinition


@dataclass
class ScaleoutDefinition(BaseModel):
    ClusterId: Optional[float]
    OperationalState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScaleoutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScaleoutDefinition"]:
        if not json_data:
            return None
        return cls(
            ClusterId=json_data.get("ClusterId"),
            OperationalState=json_data.get("OperationalState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScaleoutDefinition = ScaleoutDefinition


@dataclass
class TagDefinition(BaseModel):
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


@dataclass
class SetDefinition(BaseModel):
    AtomicAggregate: Optional[float]
    Community: Optional[str]
    Uuid: Optional[str]
    Aggregator: Optional[Sequence["_AggregatorDefinition"]]
    AsPath: Optional[Sequence["_AsPathDefinition"]]
    CommList: Optional[Sequence["_CommListDefinition"]]
    DampeningCfg: Optional[Sequence["_DampeningCfgDefinition"]]
    Ddos: Optional[Sequence["_DdosDefinition"]]
    Extcommunity: Optional[Sequence["_ExtcommunityDefinition"]]
    Ip: Optional[Sequence["_IpDefinition"]]
    Ipv6: Optional[Sequence["_Ipv6Definition"]]
    Level: Optional[Sequence["_LevelDefinition"]]
    LocalPreference: Optional[Sequence["_LocalPreferenceDefinition"]]
    Metric: Optional[Sequence["_MetricDefinition"]]
    MetricType: Optional[Sequence["_MetricTypeDefinition"]]
    Origin: Optional[Sequence["_OriginDefinition"]]
    OriginatorId: Optional[Sequence["_OriginatorIdDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]
    Weight: Optional[Sequence["_WeightDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetDefinition"]:
        if not json_data:
            return None
        return cls(
            AtomicAggregate=json_data.get("AtomicAggregate"),
            Community=json_data.get("Community"),
            Uuid=json_data.get("Uuid"),
            Aggregator=deserialize_list(json_data.get("Aggregator"), AggregatorDefinition),
            AsPath=deserialize_list(json_data.get("AsPath"), AsPathDefinition),
            CommList=deserialize_list(json_data.get("CommList"), CommListDefinition),
            DampeningCfg=deserialize_list(json_data.get("DampeningCfg"), DampeningCfgDefinition),
            Ddos=deserialize_list(json_data.get("Ddos"), DdosDefinition),
            Extcommunity=deserialize_list(json_data.get("Extcommunity"), ExtcommunityDefinition),
            Ip=deserialize_list(json_data.get("Ip"), IpDefinition),
            Ipv6=deserialize_list(json_data.get("Ipv6"), Ipv6Definition),
            Level=deserialize_list(json_data.get("Level"), LevelDefinition),
            LocalPreference=deserialize_list(json_data.get("LocalPreference"), LocalPreferenceDefinition),
            Metric=deserialize_list(json_data.get("Metric"), MetricDefinition),
            MetricType=deserialize_list(json_data.get("MetricType"), MetricTypeDefinition),
            Origin=deserialize_list(json_data.get("Origin"), OriginDefinition),
            OriginatorId=deserialize_list(json_data.get("OriginatorId"), OriginatorIdDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
            Weight=deserialize_list(json_data.get("Weight"), WeightDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetDefinition = SetDefinition


@dataclass
class AggregatorDefinition(BaseModel):
    AggregatorAs: Optional[Sequence["_AggregatorAsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AggregatorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregatorDefinition"]:
        if not json_data:
            return None
        return cls(
            AggregatorAs=deserialize_list(json_data.get("AggregatorAs"), AggregatorAsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregatorDefinition = AggregatorDefinition


@dataclass
class AggregatorAsDefinition(BaseModel):
    Asn: Optional[float]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregatorAsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregatorAsDefinition"]:
        if not json_data:
            return None
        return cls(
            Asn=json_data.get("Asn"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregatorAsDefinition = AggregatorAsDefinition


@dataclass
class CommListDefinition(BaseModel):
    Delete: Optional[float]
    Name: Optional[str]
    NameDelete: Optional[float]
    VExp: Optional[float]
    VExpDelete: Optional[float]
    VStd: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CommListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CommListDefinition"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
            Name=json_data.get("Name"),
            NameDelete=json_data.get("NameDelete"),
            VExp=json_data.get("VExp"),
            VExpDelete=json_data.get("VExpDelete"),
            VStd=json_data.get("VStd"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CommListDefinition = CommListDefinition


@dataclass
class DampeningCfgDefinition(BaseModel):
    Dampening: Optional[float]
    DampeningHalfTime: Optional[float]
    DampeningMaxSupress: Optional[float]
    DampeningPenalty: Optional[float]
    DampeningReuse: Optional[float]
    DampeningSupress: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DampeningCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DampeningCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Dampening=json_data.get("Dampening"),
            DampeningHalfTime=json_data.get("DampeningHalfTime"),
            DampeningMaxSupress=json_data.get("DampeningMaxSupress"),
            DampeningPenalty=json_data.get("DampeningPenalty"),
            DampeningReuse=json_data.get("DampeningReuse"),
            DampeningSupress=json_data.get("DampeningSupress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DampeningCfgDefinition = DampeningCfgDefinition


@dataclass
class DdosDefinition(BaseModel):
    ClassListCid: Optional[float]
    ClassListName: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DdosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DdosDefinition"]:
        if not json_data:
            return None
        return cls(
            ClassListCid=json_data.get("ClassListCid"),
            ClassListName=json_data.get("ClassListName"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DdosDefinition = DdosDefinition


@dataclass
class LevelDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LevelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LevelDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LevelDefinition = LevelDefinition


@dataclass
class MetricTypeDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricTypeDefinition = MetricTypeDefinition


@dataclass
class OriginatorIdDefinition(BaseModel):
    OriginatorIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginatorIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginatorIdDefinition"]:
        if not json_data:
            return None
        return cls(
            OriginatorIp=json_data.get("OriginatorIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginatorIdDefinition = OriginatorIdDefinition


@dataclass
class WeightDefinition(BaseModel):
    WeightVal: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WeightDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightDefinition"]:
        if not json_data:
            return None
        return cls(
            WeightVal=json_data.get("WeightVal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightDefinition = WeightDefinition


