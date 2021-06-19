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
    AdjacencyCheck: Optional[str]
    AdjacencyCheck6: Optional[str]
    AdvPassiveOnly: Optional[str]
    AdvPassiveOnly6: Optional[str]
    AuthKeychainL1: Optional[str]
    AuthKeychainL2: Optional[str]
    AuthModeL1: Optional[str]
    AuthModeL2: Optional[str]
    AuthPasswordL1: Optional[str]
    AuthPasswordL2: Optional[str]
    AuthSendonlyL1: Optional[str]
    AuthSendonlyL2: Optional[str]
    DefaultOriginate: Optional[str]
    DefaultOriginate6: Optional[str]
    DynamicHostname: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    IgnoreLspErrors: Optional[str]
    IsType: Optional[str]
    LspGenIntervalL1: Optional[float]
    LspGenIntervalL2: Optional[float]
    LspRefreshInterval: Optional[float]
    MaxLspLifetime: Optional[float]
    MetricStyle: Optional[str]
    OverloadBit: Optional[str]
    OverloadBitOnStartup: Optional[float]
    OverloadBitSuppress: Optional[str]
    Redistribute6L1: Optional[str]
    Redistribute6L1List: Optional[str]
    Redistribute6L2: Optional[str]
    Redistribute6L2List: Optional[str]
    RedistributeL1: Optional[str]
    RedistributeL1List: Optional[str]
    RedistributeL2: Optional[str]
    RedistributeL2List: Optional[str]
    SpfIntervalExpL1: Optional[str]
    SpfIntervalExpL2: Optional[str]
    Vdomparam: Optional[str]
    IsisInterface: Optional[Sequence["_IsisInterfaceDefinition"]]
    IsisNet: Optional[Sequence["_IsisNetDefinition"]]
    Redistribute: Optional[Sequence["_RedistributeDefinition"]]
    Redistribute6: Optional[Sequence["_Redistribute6Definition"]]
    SummaryAddress: Optional[Sequence["_SummaryAddressDefinition"]]
    SummaryAddress6: Optional[Sequence["_SummaryAddress6Definition"]]

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
            AdjacencyCheck=json_data.get("AdjacencyCheck"),
            AdjacencyCheck6=json_data.get("AdjacencyCheck6"),
            AdvPassiveOnly=json_data.get("AdvPassiveOnly"),
            AdvPassiveOnly6=json_data.get("AdvPassiveOnly6"),
            AuthKeychainL1=json_data.get("AuthKeychainL1"),
            AuthKeychainL2=json_data.get("AuthKeychainL2"),
            AuthModeL1=json_data.get("AuthModeL1"),
            AuthModeL2=json_data.get("AuthModeL2"),
            AuthPasswordL1=json_data.get("AuthPasswordL1"),
            AuthPasswordL2=json_data.get("AuthPasswordL2"),
            AuthSendonlyL1=json_data.get("AuthSendonlyL1"),
            AuthSendonlyL2=json_data.get("AuthSendonlyL2"),
            DefaultOriginate=json_data.get("DefaultOriginate"),
            DefaultOriginate6=json_data.get("DefaultOriginate6"),
            DynamicHostname=json_data.get("DynamicHostname"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            IgnoreLspErrors=json_data.get("IgnoreLspErrors"),
            IsType=json_data.get("IsType"),
            LspGenIntervalL1=json_data.get("LspGenIntervalL1"),
            LspGenIntervalL2=json_data.get("LspGenIntervalL2"),
            LspRefreshInterval=json_data.get("LspRefreshInterval"),
            MaxLspLifetime=json_data.get("MaxLspLifetime"),
            MetricStyle=json_data.get("MetricStyle"),
            OverloadBit=json_data.get("OverloadBit"),
            OverloadBitOnStartup=json_data.get("OverloadBitOnStartup"),
            OverloadBitSuppress=json_data.get("OverloadBitSuppress"),
            Redistribute6L1=json_data.get("Redistribute6L1"),
            Redistribute6L1List=json_data.get("Redistribute6L1List"),
            Redistribute6L2=json_data.get("Redistribute6L2"),
            Redistribute6L2List=json_data.get("Redistribute6L2List"),
            RedistributeL1=json_data.get("RedistributeL1"),
            RedistributeL1List=json_data.get("RedistributeL1List"),
            RedistributeL2=json_data.get("RedistributeL2"),
            RedistributeL2List=json_data.get("RedistributeL2List"),
            SpfIntervalExpL1=json_data.get("SpfIntervalExpL1"),
            SpfIntervalExpL2=json_data.get("SpfIntervalExpL2"),
            Vdomparam=json_data.get("Vdomparam"),
            IsisInterface=deserialize_list(json_data.get("IsisInterface"), IsisInterfaceDefinition),
            IsisNet=deserialize_list(json_data.get("IsisNet"), IsisNetDefinition),
            Redistribute=deserialize_list(json_data.get("Redistribute"), RedistributeDefinition),
            Redistribute6=deserialize_list(json_data.get("Redistribute6"), Redistribute6Definition),
            SummaryAddress=deserialize_list(json_data.get("SummaryAddress"), SummaryAddressDefinition),
            SummaryAddress6=deserialize_list(json_data.get("SummaryAddress6"), SummaryAddress6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IsisInterfaceDefinition(BaseModel):
    AuthKeychainL1: Optional[str]
    AuthKeychainL2: Optional[str]
    AuthModeL1: Optional[str]
    AuthModeL2: Optional[str]
    AuthPasswordL1: Optional[str]
    AuthPasswordL2: Optional[str]
    AuthSendOnlyL1: Optional[str]
    AuthSendOnlyL2: Optional[str]
    CircuitType: Optional[str]
    CsnpIntervalL1: Optional[float]
    CsnpIntervalL2: Optional[float]
    HelloIntervalL1: Optional[float]
    HelloIntervalL2: Optional[float]
    HelloMultiplierL1: Optional[float]
    HelloMultiplierL2: Optional[float]
    HelloPadding: Optional[str]
    LspInterval: Optional[float]
    LspRetransmitInterval: Optional[float]
    MeshGroup: Optional[str]
    MeshGroupId: Optional[float]
    MetricL1: Optional[float]
    MetricL2: Optional[float]
    Name: Optional[str]
    NetworkType: Optional[str]
    PriorityL1: Optional[float]
    PriorityL2: Optional[float]
    Status: Optional[str]
    Status6: Optional[str]
    WideMetricL1: Optional[float]
    WideMetricL2: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IsisInterfaceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsisInterfaceDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthKeychainL1=json_data.get("AuthKeychainL1"),
            AuthKeychainL2=json_data.get("AuthKeychainL2"),
            AuthModeL1=json_data.get("AuthModeL1"),
            AuthModeL2=json_data.get("AuthModeL2"),
            AuthPasswordL1=json_data.get("AuthPasswordL1"),
            AuthPasswordL2=json_data.get("AuthPasswordL2"),
            AuthSendOnlyL1=json_data.get("AuthSendOnlyL1"),
            AuthSendOnlyL2=json_data.get("AuthSendOnlyL2"),
            CircuitType=json_data.get("CircuitType"),
            CsnpIntervalL1=json_data.get("CsnpIntervalL1"),
            CsnpIntervalL2=json_data.get("CsnpIntervalL2"),
            HelloIntervalL1=json_data.get("HelloIntervalL1"),
            HelloIntervalL2=json_data.get("HelloIntervalL2"),
            HelloMultiplierL1=json_data.get("HelloMultiplierL1"),
            HelloMultiplierL2=json_data.get("HelloMultiplierL2"),
            HelloPadding=json_data.get("HelloPadding"),
            LspInterval=json_data.get("LspInterval"),
            LspRetransmitInterval=json_data.get("LspRetransmitInterval"),
            MeshGroup=json_data.get("MeshGroup"),
            MeshGroupId=json_data.get("MeshGroupId"),
            MetricL1=json_data.get("MetricL1"),
            MetricL2=json_data.get("MetricL2"),
            Name=json_data.get("Name"),
            NetworkType=json_data.get("NetworkType"),
            PriorityL1=json_data.get("PriorityL1"),
            PriorityL2=json_data.get("PriorityL2"),
            Status=json_data.get("Status"),
            Status6=json_data.get("Status6"),
            WideMetricL1=json_data.get("WideMetricL1"),
            WideMetricL2=json_data.get("WideMetricL2"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsisInterfaceDefinition = IsisInterfaceDefinition


@dataclass
class IsisNetDefinition(BaseModel):
    Id: Optional[float]
    Net: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IsisNetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IsisNetDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Net=json_data.get("Net"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IsisNetDefinition = IsisNetDefinition


@dataclass
class RedistributeDefinition(BaseModel):
    Level: Optional[str]
    Metric: Optional[float]
    MetricType: Optional[str]
    Protocol: Optional[str]
    Routemap: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedistributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedistributeDefinition"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
            Metric=json_data.get("Metric"),
            MetricType=json_data.get("MetricType"),
            Protocol=json_data.get("Protocol"),
            Routemap=json_data.get("Routemap"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedistributeDefinition = RedistributeDefinition


@dataclass
class Redistribute6Definition(BaseModel):
    Level: Optional[str]
    Metric: Optional[float]
    MetricType: Optional[str]
    Protocol: Optional[str]
    Routemap: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Redistribute6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Redistribute6Definition"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
            Metric=json_data.get("Metric"),
            MetricType=json_data.get("MetricType"),
            Protocol=json_data.get("Protocol"),
            Routemap=json_data.get("Routemap"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Redistribute6Definition = Redistribute6Definition


@dataclass
class SummaryAddressDefinition(BaseModel):
    Id: Optional[float]
    Level: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SummaryAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SummaryAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Level=json_data.get("Level"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SummaryAddressDefinition = SummaryAddressDefinition


@dataclass
class SummaryAddress6Definition(BaseModel):
    Id: Optional[float]
    Level: Optional[str]
    Prefix6: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SummaryAddress6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SummaryAddress6Definition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Level=json_data.get("Level"),
            Prefix6=json_data.get("Prefix6"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SummaryAddress6Definition = SummaryAddress6Definition


