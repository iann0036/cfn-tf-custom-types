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
    Annotation: Optional[str]
    ArpFlood: Optional[str]
    BridgeDomainType: Optional[str]
    Description: Optional[str]
    EpClear: Optional[str]
    EpMoveDetectMode: Optional[str]
    HostBasedRouting: Optional[str]
    Id: Optional[str]
    IntersiteBumTrafficAllow: Optional[str]
    IntersiteL2Stretch: Optional[str]
    IpLearning: Optional[str]
    Ipv6McastAllow: Optional[str]
    LimitIpLearnToSubnets: Optional[str]
    LlAddr: Optional[str]
    Mac: Optional[str]
    McastAllow: Optional[str]
    MultiDstPktAct: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    OptimizeWanBandwidth: Optional[str]
    RelationFvRsAbdPolMonPol: Optional[str]
    RelationFvRsBdFloodTo: Optional[Sequence[str]]
    RelationFvRsBdToEpRet: Optional[str]
    RelationFvRsBdToFhs: Optional[str]
    RelationFvRsBdToNdP: Optional[str]
    RelationFvRsBdToOut: Optional[Sequence[str]]
    RelationFvRsBdToProfile: Optional[str]
    RelationFvRsBdToRelayP: Optional[str]
    RelationFvRsCtx: Optional[str]
    RelationFvRsIgmpsn: Optional[str]
    RelationFvRsMldsn: Optional[str]
    TenantDn: Optional[str]
    UnicastRoute: Optional[str]
    UnkMacUcastAct: Optional[str]
    UnkMcastAct: Optional[str]
    V6unkMcastAct: Optional[str]
    Vmac: Optional[str]
    RelationFvRsBdToNetflowMonitorPol: Optional[Sequence["_RelationFvRsBdToNetflowMonitorPolDefinition"]]

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
            Annotation=json_data.get("Annotation"),
            ArpFlood=json_data.get("ArpFlood"),
            BridgeDomainType=json_data.get("BridgeDomainType"),
            Description=json_data.get("Description"),
            EpClear=json_data.get("EpClear"),
            EpMoveDetectMode=json_data.get("EpMoveDetectMode"),
            HostBasedRouting=json_data.get("HostBasedRouting"),
            Id=json_data.get("Id"),
            IntersiteBumTrafficAllow=json_data.get("IntersiteBumTrafficAllow"),
            IntersiteL2Stretch=json_data.get("IntersiteL2Stretch"),
            IpLearning=json_data.get("IpLearning"),
            Ipv6McastAllow=json_data.get("Ipv6McastAllow"),
            LimitIpLearnToSubnets=json_data.get("LimitIpLearnToSubnets"),
            LlAddr=json_data.get("LlAddr"),
            Mac=json_data.get("Mac"),
            McastAllow=json_data.get("McastAllow"),
            MultiDstPktAct=json_data.get("MultiDstPktAct"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            OptimizeWanBandwidth=json_data.get("OptimizeWanBandwidth"),
            RelationFvRsAbdPolMonPol=json_data.get("RelationFvRsAbdPolMonPol"),
            RelationFvRsBdFloodTo=json_data.get("RelationFvRsBdFloodTo"),
            RelationFvRsBdToEpRet=json_data.get("RelationFvRsBdToEpRet"),
            RelationFvRsBdToFhs=json_data.get("RelationFvRsBdToFhs"),
            RelationFvRsBdToNdP=json_data.get("RelationFvRsBdToNdP"),
            RelationFvRsBdToOut=json_data.get("RelationFvRsBdToOut"),
            RelationFvRsBdToProfile=json_data.get("RelationFvRsBdToProfile"),
            RelationFvRsBdToRelayP=json_data.get("RelationFvRsBdToRelayP"),
            RelationFvRsCtx=json_data.get("RelationFvRsCtx"),
            RelationFvRsIgmpsn=json_data.get("RelationFvRsIgmpsn"),
            RelationFvRsMldsn=json_data.get("RelationFvRsMldsn"),
            TenantDn=json_data.get("TenantDn"),
            UnicastRoute=json_data.get("UnicastRoute"),
            UnkMacUcastAct=json_data.get("UnkMacUcastAct"),
            UnkMcastAct=json_data.get("UnkMcastAct"),
            V6unkMcastAct=json_data.get("V6unkMcastAct"),
            Vmac=json_data.get("Vmac"),
            RelationFvRsBdToNetflowMonitorPol=deserialize_list(json_data.get("RelationFvRsBdToNetflowMonitorPol"), RelationFvRsBdToNetflowMonitorPolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RelationFvRsBdToNetflowMonitorPolDefinition(BaseModel):
    FltType: Optional[str]
    TnNetflowMonitorPolName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationFvRsBdToNetflowMonitorPolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationFvRsBdToNetflowMonitorPolDefinition"]:
        if not json_data:
            return None
        return cls(
            FltType=json_data.get("FltType"),
            TnNetflowMonitorPolName=json_data.get("TnNetflowMonitorPolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationFvRsBdToNetflowMonitorPolDefinition = RelationFvRsBdToNetflowMonitorPolDefinition


