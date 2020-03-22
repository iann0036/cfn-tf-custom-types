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
    DeviceGroup: Optional[str]
    Id: Optional[str]
    PositionKeyword: Optional[str]
    PositionReference: Optional[str]
    Rulebase: Optional[str]
    Rule: Optional[Sequence["_Rule"]]
    Destination: Optional[Sequence["_Destination"]]
    Forwarding: Optional[Sequence["_Forwarding"]]
    Source: Optional[Sequence["_Source"]]
    Target: Optional[Sequence["_Target"]]
    Monitor: Optional[Sequence["_Monitor"]]
    SymmetricReturn: Optional[Sequence["_SymmetricReturn"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DeviceGroup=json_data.get("DeviceGroup"),
            Id=json_data.get("Id"),
            PositionKeyword=json_data.get("PositionKeyword"),
            PositionReference=json_data.get("PositionReference"),
            Rulebase=json_data.get("Rulebase"),
            Rule=json_data.get("Rule"),
            Destination=json_data.get("Destination"),
            Forwarding=json_data.get("Forwarding"),
            Source=json_data.get("Source"),
            Target=json_data.get("Target"),
            Monitor=json_data.get("Monitor"),
            SymmetricReturn=json_data.get("SymmetricReturn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    ActiveActiveDeviceBinding: Optional[str]
    Description: Optional[str]
    Disabled: Optional[bool]
    Name: Optional[str]
    NegateTarget: Optional[bool]
    Schedule: Optional[str]
    Tags: Optional[Sequence[str]]
    Uuid: Optional[str]
    Destination: Optional[Sequence["_Destination"]]
    Forwarding: Optional[Sequence["_Forwarding"]]
    Source: Optional[Sequence["_Source"]]
    Target: Optional[Sequence["_Target"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
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
            Destination=json_data.get("Destination"),
            Forwarding=json_data.get("Forwarding"),
            Source=json_data.get("Source"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Destination:
    Addresses: Optional[Sequence[str]]
    Applications: Optional[Sequence[str]]
    Negate: Optional[bool]
    Services: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            Addresses=json_data.get("Addresses"),
            Applications=json_data.get("Applications"),
            Negate=json_data.get("Negate"),
            Services=json_data.get("Services"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


@dataclass
class Forwarding:
    Action: Optional[str]
    EgressInterface: Optional[str]
    NextHopType: Optional[str]
    NextHopValue: Optional[str]
    Vsys: Optional[str]
    Monitor: Optional[Sequence["_Monitor"]]
    SymmetricReturn: Optional[Sequence["_SymmetricReturn"]]

    @classmethod
    def _deserialize(
        cls: Type["_Forwarding"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Forwarding"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            EgressInterface=json_data.get("EgressInterface"),
            NextHopType=json_data.get("NextHopType"),
            NextHopValue=json_data.get("NextHopValue"),
            Vsys=json_data.get("Vsys"),
            Monitor=json_data.get("Monitor"),
            SymmetricReturn=json_data.get("SymmetricReturn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Forwarding = Forwarding


@dataclass
class Monitor:
    DisableIfUnreachable: Optional[bool]
    IpAddress: Optional[str]
    Profile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Monitor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Monitor"]:
        if not json_data:
            return None
        return cls(
            DisableIfUnreachable=json_data.get("DisableIfUnreachable"),
            IpAddress=json_data.get("IpAddress"),
            Profile=json_data.get("Profile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Monitor = Monitor


@dataclass
class SymmetricReturn:
    Addresses: Optional[Sequence[str]]
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SymmetricReturn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SymmetricReturn"]:
        if not json_data:
            return None
        return cls(
            Addresses=json_data.get("Addresses"),
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SymmetricReturn = SymmetricReturn


@dataclass
class Source:
    Addresses: Optional[Sequence[str]]
    Interfaces: Optional[Sequence[str]]
    Negate: Optional[bool]
    Users: Optional[Sequence[str]]
    Zones: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
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
_Source = Source


@dataclass
class Target:
    Serial: Optional[str]
    VsysList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            Serial=json_data.get("Serial"),
            VsysList=json_data.get("VsysList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


