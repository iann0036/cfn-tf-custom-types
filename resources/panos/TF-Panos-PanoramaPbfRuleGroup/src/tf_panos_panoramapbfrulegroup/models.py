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
    DeviceGroup: Optional[str]
    Id: Optional[str]
    PositionKeyword: Optional[str]
    PositionReference: Optional[str]
    Rulebase: Optional[str]
    Rule: Optional[Sequence["_RuleDefinition"]]

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
            DeviceGroup=json_data.get("DeviceGroup"),
            Id=json_data.get("Id"),
            PositionKeyword=json_data.get("PositionKeyword"),
            PositionReference=json_data.get("PositionReference"),
            Rulebase=json_data.get("Rulebase"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    ActiveActiveDeviceBinding: Optional[str]
    Description: Optional[str]
    Disabled: Optional[bool]
    Name: Optional[str]
    NegateTarget: Optional[bool]
    Schedule: Optional[str]
    Tags: Optional[Sequence[str]]
    Uuid: Optional[str]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    Forwarding: Optional[Sequence["_ForwardingDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]
    Target: Optional[Sequence["_TargetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ActiveActiveDeviceBinding=json_data.get("ActiveActiveDeviceBinding"),
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            Name=json_data.get("Name"),
            NegateTarget=json_data.get("NegateTarget"),
            Schedule=json_data.get("Schedule"),
            Tags=json_data.get("Tags"),
            Uuid=json_data.get("Uuid"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            Forwarding=deserialize_list(json_data.get("Forwarding"), ForwardingDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
            Target=deserialize_list(json_data.get("Target"), TargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class DestinationDefinition(BaseModel):
    Addresses: Optional[Sequence[str]]
    Applications: Optional[Sequence[str]]
    Negate: Optional[bool]
    Services: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            Addresses=json_data.get("Addresses"),
            Applications=json_data.get("Applications"),
            Negate=json_data.get("Negate"),
            Services=json_data.get("Services"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class ForwardingDefinition(BaseModel):
    Action: Optional[str]
    EgressInterface: Optional[str]
    NextHopType: Optional[str]
    NextHopValue: Optional[str]
    Vsys: Optional[str]
    Monitor: Optional[Sequence["_MonitorDefinition"]]
    SymmetricReturn: Optional[Sequence["_SymmetricReturnDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            EgressInterface=json_data.get("EgressInterface"),
            NextHopType=json_data.get("NextHopType"),
            NextHopValue=json_data.get("NextHopValue"),
            Vsys=json_data.get("Vsys"),
            Monitor=deserialize_list(json_data.get("Monitor"), MonitorDefinition),
            SymmetricReturn=deserialize_list(json_data.get("SymmetricReturn"), SymmetricReturnDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingDefinition = ForwardingDefinition


@dataclass
class MonitorDefinition(BaseModel):
    DisableIfUnreachable: Optional[bool]
    IpAddress: Optional[str]
    Profile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitorDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitorDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableIfUnreachable=json_data.get("DisableIfUnreachable"),
            IpAddress=json_data.get("IpAddress"),
            Profile=json_data.get("Profile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitorDefinition = MonitorDefinition


@dataclass
class SymmetricReturnDefinition(BaseModel):
    Addresses: Optional[Sequence[str]]
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SymmetricReturnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SymmetricReturnDefinition"]:
        if not json_data:
            return None
        return cls(
            Addresses=json_data.get("Addresses"),
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SymmetricReturnDefinition = SymmetricReturnDefinition


@dataclass
class SourceDefinition(BaseModel):
    Addresses: Optional[Sequence[str]]
    Interfaces: Optional[Sequence[str]]
    Negate: Optional[bool]
    Users: Optional[Sequence[str]]
    Zones: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Addresses=json_data.get("Addresses"),
            Interfaces=json_data.get("Interfaces"),
            Negate=json_data.get("Negate"),
            Users=json_data.get("Users"),
            Zones=json_data.get("Zones"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class TargetDefinition(BaseModel):
    Serial: Optional[str]
    VsysList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Serial=json_data.get("Serial"),
            VsysList=json_data.get("VsysList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDefinition = TargetDefinition


