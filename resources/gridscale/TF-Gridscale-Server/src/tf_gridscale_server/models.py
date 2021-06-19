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
    AutoRecovery: Optional[bool]
    AvailabilityZone: Optional[str]
    ChangeTime: Optional[str]
    ConsoleToken: Optional[str]
    Cores: Optional[float]
    CreateTime: Optional[str]
    CurrentPrice: Optional[float]
    HardwareProfile: Optional[str]
    Id: Optional[str]
    Ipv4: Optional[str]
    Ipv6: Optional[str]
    Isoimage: Optional[str]
    Labels: Optional[Sequence[str]]
    Legacy: Optional[bool]
    LocationUuid: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]
    Power: Optional[bool]
    Status: Optional[str]
    UsageInMinutesCores: Optional[float]
    UsageInMinutesMemory: Optional[float]
    Network: Optional[Sequence["_NetworkDefinition"]]
    Storage: Optional[Sequence["_StorageDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AutoRecovery=json_data.get("AutoRecovery"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ChangeTime=json_data.get("ChangeTime"),
            ConsoleToken=json_data.get("ConsoleToken"),
            Cores=json_data.get("Cores"),
            CreateTime=json_data.get("CreateTime"),
            CurrentPrice=json_data.get("CurrentPrice"),
            HardwareProfile=json_data.get("HardwareProfile"),
            Id=json_data.get("Id"),
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
            Isoimage=json_data.get("Isoimage"),
            Labels=json_data.get("Labels"),
            Legacy=json_data.get("Legacy"),
            LocationUuid=json_data.get("LocationUuid"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            Power=json_data.get("Power"),
            Status=json_data.get("Status"),
            UsageInMinutesCores=json_data.get("UsageInMinutesCores"),
            UsageInMinutesMemory=json_data.get("UsageInMinutesMemory"),
            Network=deserialize_list(json_data.get("Network"), NetworkDefinition),
            Storage=deserialize_list(json_data.get("Storage"), StorageDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkDefinition(BaseModel):
    Bootdevice: Optional[bool]
    FirewallTemplateUuid: Optional[str]
    ObjectUuid: Optional[str]
    Ordering: Optional[float]
    RulesV4In: Optional[Sequence["_RulesV4InDefinition"]]
    RulesV4Out: Optional[Sequence["_RulesV4OutDefinition"]]
    RulesV6In: Optional[Sequence["_RulesV6InDefinition"]]
    RulesV6Out: Optional[Sequence["_RulesV6OutDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            Bootdevice=json_data.get("Bootdevice"),
            FirewallTemplateUuid=json_data.get("FirewallTemplateUuid"),
            ObjectUuid=json_data.get("ObjectUuid"),
            Ordering=json_data.get("Ordering"),
            RulesV4In=deserialize_list(json_data.get("RulesV4In"), RulesV4InDefinition),
            RulesV4Out=deserialize_list(json_data.get("RulesV4Out"), RulesV4OutDefinition),
            RulesV6In=deserialize_list(json_data.get("RulesV6In"), RulesV6InDefinition),
            RulesV6Out=deserialize_list(json_data.get("RulesV6Out"), RulesV6OutDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDefinition = NetworkDefinition


@dataclass
class RulesV4InDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    Order: Optional[float]
    Protocol: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesV4InDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesV4InDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            Order=json_data.get("Order"),
            Protocol=json_data.get("Protocol"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesV4InDefinition = RulesV4InDefinition


@dataclass
class RulesV4OutDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    Order: Optional[float]
    Protocol: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesV4OutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesV4OutDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            Order=json_data.get("Order"),
            Protocol=json_data.get("Protocol"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesV4OutDefinition = RulesV4OutDefinition


@dataclass
class RulesV6InDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    Order: Optional[float]
    Protocol: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesV6InDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesV6InDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            Order=json_data.get("Order"),
            Protocol=json_data.get("Protocol"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesV6InDefinition = RulesV6InDefinition


@dataclass
class RulesV6OutDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    DstCidr: Optional[str]
    DstPort: Optional[str]
    Order: Optional[float]
    Protocol: Optional[str]
    SrcCidr: Optional[str]
    SrcPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesV6OutDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesV6OutDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            DstCidr=json_data.get("DstCidr"),
            DstPort=json_data.get("DstPort"),
            Order=json_data.get("Order"),
            Protocol=json_data.get("Protocol"),
            SrcCidr=json_data.get("SrcCidr"),
            SrcPort=json_data.get("SrcPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesV6OutDefinition = RulesV6OutDefinition


@dataclass
class StorageDefinition(BaseModel):
    ObjectUuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageDefinition"]:
        if not json_data:
            return None
        return cls(
            ObjectUuid=json_data.get("ObjectUuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageDefinition = StorageDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


