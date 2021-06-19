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
    AutoCostReferenceBandwidth: Optional[float]
    BfdAllInterfaces: Optional[float]
    DefaultMetric: Optional[float]
    Id: Optional[str]
    MaxConcurrentDd: Optional[float]
    MaximumArea: Optional[float]
    ProcessId: Optional[float]
    Rfc1583Compatible: Optional[float]
    Sequence: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    AreaList: Optional[Sequence["_AreaListDefinition"]]
    DefaultInformation: Optional[Sequence["_DefaultInformationDefinition"]]
    Distance: Optional[Sequence["_DistanceDefinition"]]
    DistributeInternalList: Optional[Sequence["_DistributeInternalListDefinition"]]
    DistributeLists: Optional[Sequence["_DistributeListsDefinition"]]
    HaStandbyExtraCost: Optional[Sequence["_HaStandbyExtraCostDefinition"]]
    HostList: Optional[Sequence["_HostListDefinition"]]
    LogAdjacencyChangesCfg: Optional[Sequence["_LogAdjacencyChangesCfgDefinition"]]
    NeighborList: Optional[Sequence["_NeighborListDefinition"]]
    NetworkList: Optional[Sequence["_NetworkListDefinition"]]
    Ospf1: Optional[Sequence["_Ospf1Definition"]]
    Overflow: Optional[Sequence["_OverflowDefinition"]]
    PassiveInterface: Optional[Sequence["_PassiveInterfaceDefinition"]]
    Redistribute: Optional[Sequence["_RedistributeDefinition"]]
    RouterId: Optional[Sequence["_RouterIdDefinition"]]
    SummaryAddressList: Optional[Sequence["_SummaryAddressListDefinition"]]
    Timers: Optional[Sequence["_TimersDefinition"]]

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
            AutoCostReferenceBandwidth=json_data.get("AutoCostReferenceBandwidth"),
            BfdAllInterfaces=json_data.get("BfdAllInterfaces"),
            DefaultMetric=json_data.get("DefaultMetric"),
            Id=json_data.get("Id"),
            MaxConcurrentDd=json_data.get("MaxConcurrentDd"),
            MaximumArea=json_data.get("MaximumArea"),
            ProcessId=json_data.get("ProcessId"),
            Rfc1583Compatible=json_data.get("Rfc1583Compatible"),
            Sequence=json_data.get("Sequence"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            AreaList=deserialize_list(json_data.get("AreaList"), AreaListDefinition),
            DefaultInformation=deserialize_list(json_data.get("DefaultInformation"), DefaultInformationDefinition),
            Distance=deserialize_list(json_data.get("Distance"), DistanceDefinition),
            DistributeInternalList=deserialize_list(json_data.get("DistributeInternalList"), DistributeInternalListDefinition),
            DistributeLists=deserialize_list(json_data.get("DistributeLists"), DistributeListsDefinition),
            HaStandbyExtraCost=deserialize_list(json_data.get("HaStandbyExtraCost"), HaStandbyExtraCostDefinition),
            HostList=deserialize_list(json_data.get("HostList"), HostListDefinition),
            LogAdjacencyChangesCfg=deserialize_list(json_data.get("LogAdjacencyChangesCfg"), LogAdjacencyChangesCfgDefinition),
            NeighborList=deserialize_list(json_data.get("NeighborList"), NeighborListDefinition),
            NetworkList=deserialize_list(json_data.get("NetworkList"), NetworkListDefinition),
            Ospf1=deserialize_list(json_data.get("Ospf1"), Ospf1Definition),
            Overflow=deserialize_list(json_data.get("Overflow"), OverflowDefinition),
            PassiveInterface=deserialize_list(json_data.get("PassiveInterface"), PassiveInterfaceDefinition),
            Redistribute=deserialize_list(json_data.get("Redistribute"), RedistributeDefinition),
            RouterId=deserialize_list(json_data.get("RouterId"), RouterIdDefinition),
            SummaryAddressList=deserialize_list(json_data.get("SummaryAddressList"), SummaryAddressListDefinition),
            Timers=deserialize_list(json_data.get("Timers"), TimersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AreaListDefinition(BaseModel):
    AreaIpv4: Optional[str]
    AreaNum: Optional[float]
    DefaultCost: Optional[float]
    Shortcut: Optional[str]
    Uuid: Optional[str]
    AuthCfg: Optional[Sequence["_AuthCfgDefinition"]]
    FilterLists: Optional[Sequence["_FilterListsDefinition"]]
    NssaCfg: Optional[Sequence["_NssaCfgDefinition"]]
    RangeList: Optional[Sequence["_RangeListDefinition"]]
    StubCfg: Optional[Sequence["_StubCfgDefinition"]]
    VirtualLinkList: Optional[Sequence["_VirtualLinkListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AreaListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AreaListDefinition"]:
        if not json_data:
            return None
        return cls(
            AreaIpv4=json_data.get("AreaIpv4"),
            AreaNum=json_data.get("AreaNum"),
            DefaultCost=json_data.get("DefaultCost"),
            Shortcut=json_data.get("Shortcut"),
            Uuid=json_data.get("Uuid"),
            AuthCfg=deserialize_list(json_data.get("AuthCfg"), AuthCfgDefinition),
            FilterLists=deserialize_list(json_data.get("FilterLists"), FilterListsDefinition),
            NssaCfg=deserialize_list(json_data.get("NssaCfg"), NssaCfgDefinition),
            RangeList=deserialize_list(json_data.get("RangeList"), RangeListDefinition),
            StubCfg=deserialize_list(json_data.get("StubCfg"), StubCfgDefinition),
            VirtualLinkList=deserialize_list(json_data.get("VirtualLinkList"), VirtualLinkListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AreaListDefinition = AreaListDefinition


@dataclass
class AuthCfgDefinition(BaseModel):
    Authentication: Optional[float]
    MessageDigest: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AuthCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            MessageDigest=json_data.get("MessageDigest"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthCfgDefinition = AuthCfgDefinition


@dataclass
class FilterListsDefinition(BaseModel):
    AclDirection: Optional[str]
    AclName: Optional[str]
    FilterList: Optional[float]
    PlistDirection: Optional[str]
    PlistName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterListsDefinition"]:
        if not json_data:
            return None
        return cls(
            AclDirection=json_data.get("AclDirection"),
            AclName=json_data.get("AclName"),
            FilterList=json_data.get("FilterList"),
            PlistDirection=json_data.get("PlistDirection"),
            PlistName=json_data.get("PlistName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterListsDefinition = FilterListsDefinition


@dataclass
class NssaCfgDefinition(BaseModel):
    DefaultInformationOriginate: Optional[float]
    Metric: Optional[float]
    MetricType: Optional[float]
    NoRedistribution: Optional[float]
    NoSummary: Optional[float]
    Nssa: Optional[float]
    TranslatorRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NssaCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NssaCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultInformationOriginate=json_data.get("DefaultInformationOriginate"),
            Metric=json_data.get("Metric"),
            MetricType=json_data.get("MetricType"),
            NoRedistribution=json_data.get("NoRedistribution"),
            NoSummary=json_data.get("NoSummary"),
            Nssa=json_data.get("Nssa"),
            TranslatorRole=json_data.get("TranslatorRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NssaCfgDefinition = NssaCfgDefinition


@dataclass
class RangeListDefinition(BaseModel):
    AreaRangePrefix: Optional[str]
    Option: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RangeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeListDefinition"]:
        if not json_data:
            return None
        return cls(
            AreaRangePrefix=json_data.get("AreaRangePrefix"),
            Option=json_data.get("Option"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeListDefinition = RangeListDefinition


@dataclass
class StubCfgDefinition(BaseModel):
    NoSummary: Optional[float]
    Stub: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StubCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StubCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            NoSummary=json_data.get("NoSummary"),
            Stub=json_data.get("Stub"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StubCfgDefinition = StubCfgDefinition


@dataclass
class VirtualLinkListDefinition(BaseModel):
    AuthenticationKey: Optional[str]
    Bfd: Optional[float]
    DeadInterval: Optional[float]
    HelloInterval: Optional[float]
    Md5: Optional[str]
    MessageDigestKey: Optional[float]
    RetransmitInterval: Optional[float]
    TransmitDelay: Optional[float]
    VirtualLinkAuthType: Optional[str]
    VirtualLinkAuthentication: Optional[float]
    VirtualLinkIpAddr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualLinkListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualLinkListDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationKey=json_data.get("AuthenticationKey"),
            Bfd=json_data.get("Bfd"),
            DeadInterval=json_data.get("DeadInterval"),
            HelloInterval=json_data.get("HelloInterval"),
            Md5=json_data.get("Md5"),
            MessageDigestKey=json_data.get("MessageDigestKey"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            TransmitDelay=json_data.get("TransmitDelay"),
            VirtualLinkAuthType=json_data.get("VirtualLinkAuthType"),
            VirtualLinkAuthentication=json_data.get("VirtualLinkAuthentication"),
            VirtualLinkIpAddr=json_data.get("VirtualLinkIpAddr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualLinkListDefinition = VirtualLinkListDefinition


@dataclass
class DefaultInformationDefinition(BaseModel):
    Always: Optional[float]
    Metric: Optional[float]
    MetricType: Optional[float]
    Originate: Optional[float]
    RouteMap: Optional[str]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultInformationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultInformationDefinition"]:
        if not json_data:
            return None
        return cls(
            Always=json_data.get("Always"),
            Metric=json_data.get("Metric"),
            MetricType=json_data.get("MetricType"),
            Originate=json_data.get("Originate"),
            RouteMap=json_data.get("RouteMap"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultInformationDefinition = DefaultInformationDefinition


@dataclass
class DistanceDefinition(BaseModel):
    DistanceValue: Optional[float]
    DistanceOspf: Optional[Sequence["_DistanceOspfDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DistanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistanceDefinition"]:
        if not json_data:
            return None
        return cls(
            DistanceValue=json_data.get("DistanceValue"),
            DistanceOspf=deserialize_list(json_data.get("DistanceOspf"), DistanceOspfDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistanceDefinition = DistanceDefinition


@dataclass
class DistanceOspfDefinition(BaseModel):
    DistanceExternal: Optional[float]
    DistanceInterArea: Optional[float]
    DistanceIntraArea: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DistanceOspfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistanceOspfDefinition"]:
        if not json_data:
            return None
        return cls(
            DistanceExternal=json_data.get("DistanceExternal"),
            DistanceInterArea=json_data.get("DistanceInterArea"),
            DistanceIntraArea=json_data.get("DistanceIntraArea"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistanceOspfDefinition = DistanceOspfDefinition


@dataclass
class DistributeInternalListDefinition(BaseModel):
    DiAreaIpv4: Optional[str]
    DiAreaNum: Optional[float]
    DiCost: Optional[float]
    DiType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DistributeInternalListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributeInternalListDefinition"]:
        if not json_data:
            return None
        return cls(
            DiAreaIpv4=json_data.get("DiAreaIpv4"),
            DiAreaNum=json_data.get("DiAreaNum"),
            DiCost=json_data.get("DiCost"),
            DiType=json_data.get("DiType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributeInternalListDefinition = DistributeInternalListDefinition


@dataclass
class DistributeListsDefinition(BaseModel):
    Direction: Optional[str]
    Option: Optional[str]
    OspfId: Optional[float]
    Protocol: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DistributeListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributeListsDefinition"]:
        if not json_data:
            return None
        return cls(
            Direction=json_data.get("Direction"),
            Option=json_data.get("Option"),
            OspfId=json_data.get("OspfId"),
            Protocol=json_data.get("Protocol"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributeListsDefinition = DistributeListsDefinition


@dataclass
class HaStandbyExtraCostDefinition(BaseModel):
    ExtraCost: Optional[float]
    Group: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HaStandbyExtraCostDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HaStandbyExtraCostDefinition"]:
        if not json_data:
            return None
        return cls(
            ExtraCost=json_data.get("ExtraCost"),
            Group=json_data.get("Group"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HaStandbyExtraCostDefinition = HaStandbyExtraCostDefinition


@dataclass
class HostListDefinition(BaseModel):
    HostAddress: Optional[str]
    AreaCfg: Optional[Sequence["_AreaCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostListDefinition"]:
        if not json_data:
            return None
        return cls(
            HostAddress=json_data.get("HostAddress"),
            AreaCfg=deserialize_list(json_data.get("AreaCfg"), AreaCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostListDefinition = HostListDefinition


@dataclass
class AreaCfgDefinition(BaseModel):
    AreaIpv4: Optional[str]
    AreaNum: Optional[float]
    Cost: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AreaCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AreaCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            AreaIpv4=json_data.get("AreaIpv4"),
            AreaNum=json_data.get("AreaNum"),
            Cost=json_data.get("Cost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AreaCfgDefinition = AreaCfgDefinition


@dataclass
class LogAdjacencyChangesCfgDefinition(BaseModel):
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogAdjacencyChangesCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogAdjacencyChangesCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogAdjacencyChangesCfgDefinition = LogAdjacencyChangesCfgDefinition


@dataclass
class NeighborListDefinition(BaseModel):
    Address: Optional[str]
    Cost: Optional[float]
    PollInterval: Optional[float]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborListDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Cost=json_data.get("Cost"),
            PollInterval=json_data.get("PollInterval"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborListDefinition = NeighborListDefinition


@dataclass
class NetworkListDefinition(BaseModel):
    NetworkIpv4: Optional[str]
    NetworkIpv4Cidr: Optional[str]
    NetworkIpv4Mask: Optional[str]
    NetworkArea: Optional[Sequence["_NetworkAreaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkListDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkIpv4=json_data.get("NetworkIpv4"),
            NetworkIpv4Cidr=json_data.get("NetworkIpv4Cidr"),
            NetworkIpv4Mask=json_data.get("NetworkIpv4Mask"),
            NetworkArea=deserialize_list(json_data.get("NetworkArea"), NetworkAreaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkListDefinition = NetworkListDefinition


@dataclass
class NetworkAreaDefinition(BaseModel):
    InstanceValue: Optional[float]
    NetworkAreaIpv4: Optional[str]
    NetworkAreaNum: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkAreaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkAreaDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceValue=json_data.get("InstanceValue"),
            NetworkAreaIpv4=json_data.get("NetworkAreaIpv4"),
            NetworkAreaNum=json_data.get("NetworkAreaNum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkAreaDefinition = NetworkAreaDefinition


@dataclass
class Ospf1Definition(BaseModel):
    AbrType: Optional[Sequence["_AbrTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Ospf1Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ospf1Definition"]:
        if not json_data:
            return None
        return cls(
            AbrType=deserialize_list(json_data.get("AbrType"), AbrTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ospf1Definition = Ospf1Definition


@dataclass
class AbrTypeDefinition(BaseModel):
    Option: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AbrTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbrTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Option=json_data.get("Option"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbrTypeDefinition = AbrTypeDefinition


@dataclass
class OverflowDefinition(BaseModel):
    Database: Optional[Sequence["_DatabaseDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OverflowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverflowDefinition"]:
        if not json_data:
            return None
        return cls(
            Database=deserialize_list(json_data.get("Database"), DatabaseDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverflowDefinition = OverflowDefinition


@dataclass
class DatabaseDefinition(BaseModel):
    Count: Optional[float]
    DbExternal: Optional[float]
    Limit: Optional[str]
    RecoveryTime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseDefinition"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            DbExternal=json_data.get("DbExternal"),
            Limit=json_data.get("Limit"),
            RecoveryTime=json_data.get("RecoveryTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseDefinition = DatabaseDefinition


@dataclass
class PassiveInterfaceDefinition(BaseModel):
    EthCfg: Optional[Sequence["_EthCfgDefinition"]]
    LifCfg: Optional[Sequence["_LifCfgDefinition"]]
    LoopbackCfg: Optional[Sequence["_LoopbackCfgDefinition"]]
    TrunkCfg: Optional[Sequence["_TrunkCfgDefinition"]]
    TunnelCfg: Optional[Sequence["_TunnelCfgDefinition"]]
    VeCfg: Optional[Sequence["_VeCfgDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PassiveInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PassiveInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            EthCfg=deserialize_list(json_data.get("EthCfg"), EthCfgDefinition),
            LifCfg=deserialize_list(json_data.get("LifCfg"), LifCfgDefinition),
            LoopbackCfg=deserialize_list(json_data.get("LoopbackCfg"), LoopbackCfgDefinition),
            TrunkCfg=deserialize_list(json_data.get("TrunkCfg"), TrunkCfgDefinition),
            TunnelCfg=deserialize_list(json_data.get("TunnelCfg"), TunnelCfgDefinition),
            VeCfg=deserialize_list(json_data.get("VeCfg"), VeCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PassiveInterfaceDefinition = PassiveInterfaceDefinition


@dataclass
class EthCfgDefinition(BaseModel):
    EthAddress: Optional[str]
    Ethernet: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EthCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EthCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            EthAddress=json_data.get("EthAddress"),
            Ethernet=json_data.get("Ethernet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EthCfgDefinition = EthCfgDefinition


@dataclass
class LifCfgDefinition(BaseModel):
    Lif: Optional[float]
    LifAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LifCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Lif=json_data.get("Lif"),
            LifAddress=json_data.get("LifAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifCfgDefinition = LifCfgDefinition


@dataclass
class LoopbackCfgDefinition(BaseModel):
    Loopback: Optional[float]
    LoopbackAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoopbackCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoopbackCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Loopback=json_data.get("Loopback"),
            LoopbackAddress=json_data.get("LoopbackAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoopbackCfgDefinition = LoopbackCfgDefinition


@dataclass
class TrunkCfgDefinition(BaseModel):
    Trunk: Optional[float]
    TrunkAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrunkCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrunkCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Trunk=json_data.get("Trunk"),
            TrunkAddress=json_data.get("TrunkAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrunkCfgDefinition = TrunkCfgDefinition


@dataclass
class TunnelCfgDefinition(BaseModel):
    Tunnel: Optional[float]
    TunnelAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TunnelCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TunnelCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Tunnel=json_data.get("Tunnel"),
            TunnelAddress=json_data.get("TunnelAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TunnelCfgDefinition = TunnelCfgDefinition


@dataclass
class VeCfgDefinition(BaseModel):
    Ve: Optional[float]
    VeAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VeCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VeCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Ve=json_data.get("Ve"),
            VeAddress=json_data.get("VeAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VeCfgDefinition = VeCfgDefinition


@dataclass
class RedistributeDefinition(BaseModel):
    IpNat: Optional[float]
    MetricIpNat: Optional[float]
    MetricTypeIpNat: Optional[str]
    RouteMapIpNat: Optional[str]
    TagIpNat: Optional[float]
    Uuid: Optional[str]
    IpNatFloatingList: Optional[Sequence["_IpNatFloatingListDefinition"]]
    OspfList: Optional[Sequence["_OspfListDefinition"]]
    RedistList: Optional[Sequence["_RedistListDefinition"]]
    VipFloatingList: Optional[Sequence["_VipFloatingListDefinition"]]
    VipList: Optional[Sequence["_VipListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RedistributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedistributeDefinition"]:
        if not json_data:
            return None
        return cls(
            IpNat=json_data.get("IpNat"),
            MetricIpNat=json_data.get("MetricIpNat"),
            MetricTypeIpNat=json_data.get("MetricTypeIpNat"),
            RouteMapIpNat=json_data.get("RouteMapIpNat"),
            TagIpNat=json_data.get("TagIpNat"),
            Uuid=json_data.get("Uuid"),
            IpNatFloatingList=deserialize_list(json_data.get("IpNatFloatingList"), IpNatFloatingListDefinition),
            OspfList=deserialize_list(json_data.get("OspfList"), OspfListDefinition),
            RedistList=deserialize_list(json_data.get("RedistList"), RedistListDefinition),
            VipFloatingList=deserialize_list(json_data.get("VipFloatingList"), VipFloatingListDefinition),
            VipList=deserialize_list(json_data.get("VipList"), VipListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedistributeDefinition = RedistributeDefinition


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


@dataclass
class RouterIdDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouterIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouterIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouterIdDefinition = RouterIdDefinition


@dataclass
class SummaryAddressListDefinition(BaseModel):
    NotAdvertise: Optional[float]
    SummaryAddress: Optional[str]
    Tag: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SummaryAddressListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SummaryAddressListDefinition"]:
        if not json_data:
            return None
        return cls(
            NotAdvertise=json_data.get("NotAdvertise"),
            SummaryAddress=json_data.get("SummaryAddress"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SummaryAddressListDefinition = SummaryAddressListDefinition


@dataclass
class TimersDefinition(BaseModel):
    Spf: Optional[Sequence["_SpfDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TimersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimersDefinition"]:
        if not json_data:
            return None
        return cls(
            Spf=deserialize_list(json_data.get("Spf"), SpfDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimersDefinition = TimersDefinition


@dataclass
class SpfDefinition(BaseModel):
    Exp: Optional[Sequence["_ExpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpfDefinition"]:
        if not json_data:
            return None
        return cls(
            Exp=deserialize_list(json_data.get("Exp"), ExpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpfDefinition = SpfDefinition


@dataclass
class ExpDefinition(BaseModel):
    MaxDelay: Optional[float]
    MinDelay: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExpDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxDelay=json_data.get("MaxDelay"),
            MinDelay=json_data.get("MinDelay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExpDefinition = ExpDefinition


