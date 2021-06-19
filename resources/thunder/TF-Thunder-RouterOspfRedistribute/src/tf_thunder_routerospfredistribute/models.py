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
    AsNumber: Optional[str]
    Id: Optional[str]
    IpNat: Optional[float]
    MetricIpNat: Optional[float]
    MetricTypeIpNat: Optional[str]
    ProcessId: Optional[float]
    RouteMapIpNat: Optional[str]
    Sequence: Optional[str]
    TagIpNat: Optional[float]
    Uuid: Optional[str]
    IpNatFloatingList: Optional[Sequence["_IpNatFloatingListDefinition"]]
    OspfList: Optional[Sequence["_OspfListDefinition"]]
    RedistList: Optional[Sequence["_RedistListDefinition"]]
    VipFloatingList: Optional[Sequence["_VipFloatingListDefinition"]]
    VipList: Optional[Sequence["_VipListDefinition"]]

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
            IpNat=json_data.get("IpNat"),
            MetricIpNat=json_data.get("MetricIpNat"),
            MetricTypeIpNat=json_data.get("MetricTypeIpNat"),
            ProcessId=json_data.get("ProcessId"),
            RouteMapIpNat=json_data.get("RouteMapIpNat"),
            Sequence=json_data.get("Sequence"),
            TagIpNat=json_data.get("TagIpNat"),
            Uuid=json_data.get("Uuid"),
            IpNatFloatingList=deserialize_list(json_data.get("IpNatFloatingList"), IpNatFloatingListDefinition),
            OspfList=deserialize_list(json_data.get("OspfList"), OspfListDefinition),
            RedistList=deserialize_list(json_data.get("RedistList"), RedistListDefinition),
            VipFloatingList=deserialize_list(json_data.get("VipFloatingList"), VipFloatingListDefinition),
            VipList=deserialize_list(json_data.get("VipList"), VipListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpNatFloatingListDefinition(BaseModel):
    IpNatFloatingIpForward: Optional[str]
    IpNatPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpNatFloatingListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpNatFloatingListDefinition"]:
        if not json_data:
            return None
        return cls(
            IpNatFloatingIpForward=json_data.get("IpNatFloatingIpForward"),
            IpNatPrefix=json_data.get("IpNatPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpNatFloatingListDefinition = IpNatFloatingListDefinition


@dataclass
class OspfListDefinition(BaseModel):
    MetricOspf: Optional[float]
    MetricTypeOspf: Optional[str]
    Ospf: Optional[float]
    ProcessId: Optional[float]
    RouteMapOspf: Optional[str]
    TagOspf: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OspfListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OspfListDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricOspf=json_data.get("MetricOspf"),
            MetricTypeOspf=json_data.get("MetricTypeOspf"),
            Ospf=json_data.get("Ospf"),
            ProcessId=json_data.get("ProcessId"),
            RouteMapOspf=json_data.get("RouteMapOspf"),
            TagOspf=json_data.get("TagOspf"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OspfListDefinition = OspfListDefinition


@dataclass
class RedistListDefinition(BaseModel):
    Metric: Optional[float]
    MetricType: Optional[str]
    RouteMap: Optional[str]
    Tag: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedistListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedistListDefinition"]:
        if not json_data:
            return None
        return cls(
            Metric=json_data.get("Metric"),
            MetricType=json_data.get("MetricType"),
            RouteMap=json_data.get("RouteMap"),
            Tag=json_data.get("Tag"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedistListDefinition = RedistListDefinition


@dataclass
class VipFloatingListDefinition(BaseModel):
    VipAddress: Optional[str]
    VipFloatingIpForward: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VipFloatingListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipFloatingListDefinition"]:
        if not json_data:
            return None
        return cls(
            VipAddress=json_data.get("VipAddress"),
            VipFloatingIpForward=json_data.get("VipFloatingIpForward"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipFloatingListDefinition = VipFloatingListDefinition


@dataclass
class VipListDefinition(BaseModel):
    MetricTypeVip: Optional[str]
    MetricVip: Optional[float]
    RouteMapVip: Optional[str]
    TagVip: Optional[float]
    TypeVip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VipListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipListDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricTypeVip=json_data.get("MetricTypeVip"),
            MetricVip=json_data.get("MetricVip"),
            RouteMapVip=json_data.get("RouteMapVip"),
            TagVip=json_data.get("TagVip"),
            TypeVip=json_data.get("TypeVip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipListDefinition = VipListDefinition


