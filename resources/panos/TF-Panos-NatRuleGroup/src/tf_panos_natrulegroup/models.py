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
    Id: Optional[str]
    PositionKeyword: Optional[str]
    PositionReference: Optional[str]
    Vsys: Optional[str]
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
            Id=json_data.get("Id"),
            PositionKeyword=json_data.get("PositionKeyword"),
            PositionReference=json_data.get("PositionReference"),
            Vsys=json_data.get("Vsys"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    Description: Optional[str]
    Disabled: Optional[bool]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    OriginalPacket: Optional[Sequence["_OriginalPacketDefinition"]]
    TranslatedPacket: Optional[Sequence["_TranslatedPacketDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Disabled=json_data.get("Disabled"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            OriginalPacket=deserialize_list(json_data.get("OriginalPacket"), OriginalPacketDefinition),
            TranslatedPacket=deserialize_list(json_data.get("TranslatedPacket"), TranslatedPacketDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class OriginalPacketDefinition(BaseModel):
    DestinationAddresses: Optional[Sequence[str]]
    DestinationInterface: Optional[str]
    DestinationZone: Optional[str]
    Service: Optional[str]
    SourceAddresses: Optional[Sequence[str]]
    SourceZones: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginalPacketDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginalPacketDefinition"]:
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
_OriginalPacketDefinition = OriginalPacketDefinition


@dataclass
class TranslatedPacketDefinition(BaseModel):
    Destination: Optional[Sequence["_DestinationDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TranslatedPacketDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TranslatedPacketDefinition"]:
        if not json_data:
            return None
        return cls(
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TranslatedPacketDefinition = TranslatedPacketDefinition


@dataclass
class DestinationDefinition(BaseModel):
    Dynamic: Optional[Sequence["_DynamicDefinition"]]
    DynamicTranslation: Optional[Sequence["_DynamicTranslationDefinition"]]
    Static: Optional[Sequence["_StaticDefinition"]]
    StaticTranslation: Optional[Sequence["_StaticTranslationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            Dynamic=deserialize_list(json_data.get("Dynamic"), DynamicDefinition),
            DynamicTranslation=deserialize_list(json_data.get("DynamicTranslation"), DynamicTranslationDefinition),
            Static=deserialize_list(json_data.get("Static"), StaticDefinition),
            StaticTranslation=deserialize_list(json_data.get("StaticTranslation"), StaticTranslationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class DynamicDefinition(BaseModel):
    Address: Optional[str]
    Distribution: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Distribution=json_data.get("Distribution"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicDefinition = DynamicDefinition


@dataclass
class DynamicTranslationDefinition(BaseModel):
    Address: Optional[str]
    Distribution: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicTranslationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicTranslationDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Distribution=json_data.get("Distribution"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicTranslationDefinition = DynamicTranslationDefinition


@dataclass
class StaticDefinition(BaseModel):
    Address: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StaticDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticDefinition = StaticDefinition


@dataclass
class StaticTranslationDefinition(BaseModel):
    Address: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StaticTranslationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticTranslationDefinition"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticTranslationDefinition = StaticTranslationDefinition


@dataclass
class SourceDefinition(BaseModel):
    DynamicIp: Optional[Sequence["_DynamicIpDefinition"]]
    DynamicIpAndPort: Optional[Sequence["_DynamicIpAndPortDefinition"]]
    StaticIp: Optional[Sequence["_StaticIpDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            DynamicIp=deserialize_list(json_data.get("DynamicIp"), DynamicIpDefinition),
            DynamicIpAndPort=deserialize_list(json_data.get("DynamicIpAndPort"), DynamicIpAndPortDefinition),
            StaticIp=deserialize_list(json_data.get("StaticIp"), StaticIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


@dataclass
class DynamicIpDefinition(BaseModel):
    TranslatedAddresses: Optional[Sequence[str]]
    Fallback: Optional[Sequence["_FallbackDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicIpDefinition"]:
        if not json_data:
            return None
        return cls(
            TranslatedAddresses=json_data.get("TranslatedAddresses"),
            Fallback=deserialize_list(json_data.get("Fallback"), FallbackDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicIpDefinition = DynamicIpDefinition


@dataclass
class FallbackDefinition(BaseModel):
    InterfaceAddress: Optional[Sequence["_InterfaceAddressDefinition"]]
    TranslatedAddress: Optional[Sequence["_TranslatedAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FallbackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FallbackDefinition"]:
        if not json_data:
            return None
        return cls(
            InterfaceAddress=deserialize_list(json_data.get("InterfaceAddress"), InterfaceAddressDefinition),
            TranslatedAddress=deserialize_list(json_data.get("TranslatedAddress"), TranslatedAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FallbackDefinition = FallbackDefinition


@dataclass
class InterfaceAddressDefinition(BaseModel):
    Interface: Optional[str]
    IpAddress: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterfaceAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfaceAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Interface=json_data.get("Interface"),
            IpAddress=json_data.get("IpAddress"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfaceAddressDefinition = InterfaceAddressDefinition


@dataclass
class TranslatedAddressDefinition(BaseModel):
    TranslatedAddresses: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TranslatedAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TranslatedAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            TranslatedAddresses=json_data.get("TranslatedAddresses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TranslatedAddressDefinition = TranslatedAddressDefinition


@dataclass
class DynamicIpAndPortDefinition(BaseModel):
    InterfaceAddress: Optional[Sequence["_InterfaceAddressDefinition"]]
    TranslatedAddress: Optional[Sequence["_TranslatedAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicIpAndPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicIpAndPortDefinition"]:
        if not json_data:
            return None
        return cls(
            InterfaceAddress=deserialize_list(json_data.get("InterfaceAddress"), InterfaceAddressDefinition),
            TranslatedAddress=deserialize_list(json_data.get("TranslatedAddress"), TranslatedAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicIpAndPortDefinition = DynamicIpAndPortDefinition


@dataclass
class StaticIpDefinition(BaseModel):
    BiDirectional: Optional[bool]
    TranslatedAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticIpDefinition"]:
        if not json_data:
            return None
        return cls(
            BiDirectional=json_data.get("BiDirectional"),
            TranslatedAddress=json_data.get("TranslatedAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticIpDefinition = StaticIpDefinition


