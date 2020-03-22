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
    OriginalPacket: Optional[Sequence["_OriginalPacket"]]
    Target: Optional[Sequence["_Target"]]
    TranslatedPacket: Optional[Sequence["_TranslatedPacket"]]
    Destination: Optional[Sequence["_Destination"]]
    Source: Optional[Sequence["_Source"]]
    Dynamic: Optional[Sequence["_Dynamic"]]
    DynamicTranslation: Optional[Sequence["_DynamicTranslation"]]
    Static: Optional[Sequence["_Static"]]
    StaticTranslation: Optional[Sequence["_StaticTranslation"]]
    DynamicIp: Optional[Sequence["_DynamicIp"]]
    DynamicIpAndPort: Optional[Sequence["_DynamicIpAndPort"]]
    StaticIp: Optional[Sequence["_StaticIp"]]
    Fallback: Optional[Sequence["_Fallback"]]
    InterfaceAddress: Optional[Sequence["_InterfaceAddress"]]
    TranslatedAddress: Optional[Sequence["_TranslatedAddress"]]

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
            OriginalPacket=json_data.get("OriginalPacket"),
            Target=json_data.get("Target"),
            TranslatedPacket=json_data.get("TranslatedPacket"),
            Destination=json_data.get("Destination"),
            Source=json_data.get("Source"),
            Dynamic=json_data.get("Dynamic"),
            DynamicTranslation=json_data.get("DynamicTranslation"),
            Static=json_data.get("Static"),
            StaticTranslation=json_data.get("StaticTranslation"),
            DynamicIp=json_data.get("DynamicIp"),
            DynamicIpAndPort=json_data.get("DynamicIpAndPort"),
            StaticIp=json_data.get("StaticIp"),
            Fallback=json_data.get("Fallback"),
            InterfaceAddress=json_data.get("InterfaceAddress"),
            TranslatedAddress=json_data.get("TranslatedAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    Description: Optional[str]
    Disabled: Optional[bool]
    Name: Optional[str]
    NegateTarget: Optional[bool]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    OriginalPacket: Optional[Sequence["_OriginalPacket"]]
    Target: Optional[Sequence["_Target"]]
    TranslatedPacket: Optional[Sequence["_TranslatedPacket"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            Name=json_data.get("Name"),
            NegateTarget=json_data.get("NegateTarget"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            OriginalPacket=json_data.get("OriginalPacket"),
            Target=json_data.get("Target"),
            TranslatedPacket=json_data.get("TranslatedPacket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class OriginalPacket:
    DestinationAddresses: Optional[Sequence[str]]
    DestinationInterface: Optional[str]
    DestinationZone: Optional[str]
    Service: Optional[str]
    SourceAddresses: Optional[Sequence[str]]
    SourceZones: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginalPacket"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginalPacket"]:
        if not json_data:
            return None
        return cls(
            DestinationAddresses=json_data.get("DestinationAddresses"),
            DestinationInterface=json_data.get("DestinationInterface"),
            DestinationZone=json_data.get("DestinationZone"),
            Service=json_data.get("Service"),
            SourceAddresses=json_data.get("SourceAddresses"),
            SourceZones=json_data.get("SourceZones"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginalPacket = OriginalPacket


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


@dataclass
class TranslatedPacket:
    Destination: Optional[Sequence["_Destination"]]
    Source: Optional[Sequence["_Source"]]

    @classmethod
    def _deserialize(
        cls: Type["_TranslatedPacket"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TranslatedPacket"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TranslatedPacket = TranslatedPacket


@dataclass
class Destination:
    Dynamic: Optional[Sequence["_Dynamic"]]
    DynamicTranslation: Optional[Sequence["_DynamicTranslation"]]
    Static: Optional[Sequence["_Static"]]
    StaticTranslation: Optional[Sequence["_StaticTranslation"]]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            Dynamic=json_data.get("Dynamic"),
            DynamicTranslation=json_data.get("DynamicTranslation"),
            Static=json_data.get("Static"),
            StaticTranslation=json_data.get("StaticTranslation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


@dataclass
class Dynamic:
    Address: Optional[str]
    Distribution: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Dynamic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dynamic"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Distribution=json_data.get("Distribution"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dynamic = Dynamic


@dataclass
class DynamicTranslation:
    Address: Optional[str]
    Distribution: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicTranslation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicTranslation"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Distribution=json_data.get("Distribution"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicTranslation = DynamicTranslation


@dataclass
class Static:
    Address: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Static"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Static"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Static = Static


@dataclass
class StaticTranslation:
    Address: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StaticTranslation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticTranslation"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticTranslation = StaticTranslation


@dataclass
class Source:
    DynamicIp: Optional[Sequence["_DynamicIp"]]
    DynamicIpAndPort: Optional[Sequence["_DynamicIpAndPort"]]
    StaticIp: Optional[Sequence["_StaticIp"]]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            DynamicIp=json_data.get("DynamicIp"),
            DynamicIpAndPort=json_data.get("DynamicIpAndPort"),
            StaticIp=json_data.get("StaticIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class DynamicIp:
    TranslatedAddresses: Optional[Sequence[str]]
    Fallback: Optional[Sequence["_Fallback"]]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicIp"]:
        if not json_data:
            return None
        return cls(
            TranslatedAddresses=json_data.get("TranslatedAddresses"),
            Fallback=json_data.get("Fallback"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicIp = DynamicIp


@dataclass
class Fallback:
    InterfaceAddress: Optional[Sequence["_InterfaceAddress"]]
    TranslatedAddress: Optional[Sequence["_TranslatedAddress"]]

    @classmethod
    def _deserialize(
        cls: Type["_Fallback"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Fallback"]:
        if not json_data:
            return None
        return cls(
            InterfaceAddress=json_data.get("InterfaceAddress"),
            TranslatedAddress=json_data.get("TranslatedAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Fallback = Fallback


@dataclass
class InterfaceAddress:
    Interface: Optional[str]
    IpAddress: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceAddress"]:
        if not json_data:
            return None
        return cls(
            Interface=json_data.get("Interface"),
            IpAddress=json_data.get("IpAddress"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceAddress = InterfaceAddress


@dataclass
class TranslatedAddress:
    TranslatedAddresses: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TranslatedAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TranslatedAddress"]:
        if not json_data:
            return None
        return cls(
            TranslatedAddresses=json_data.get("TranslatedAddresses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TranslatedAddress = TranslatedAddress


@dataclass
class DynamicIpAndPort:
    InterfaceAddress: Optional[Sequence["_InterfaceAddress"]]
    TranslatedAddress: Optional[Sequence["_TranslatedAddress"]]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicIpAndPort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicIpAndPort"]:
        if not json_data:
            return None
        return cls(
            InterfaceAddress=json_data.get("InterfaceAddress"),
            TranslatedAddress=json_data.get("TranslatedAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicIpAndPort = DynamicIpAndPort


@dataclass
class StaticIp:
    BiDirectional: Optional[bool]
    TranslatedAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticIp"]:
        if not json_data:
            return None
        return cls(
            BiDirectional=json_data.get("BiDirectional"),
            TranslatedAddress=json_data.get("TranslatedAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticIp = StaticIp


