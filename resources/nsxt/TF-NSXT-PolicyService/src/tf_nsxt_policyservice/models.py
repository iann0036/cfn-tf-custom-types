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
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    NsxId: Optional[str]
    Path: Optional[str]
    Revision: Optional[float]
    AlgorithmEntry: Optional[Sequence["_AlgorithmEntryDefinition"]]
    EtherTypeEntry: Optional[Sequence["_EtherTypeEntryDefinition"]]
    IcmpEntry: Optional[Sequence["_IcmpEntryDefinition"]]
    IgmpEntry: Optional[Sequence["_IgmpEntryDefinition"]]
    IpProtocolEntry: Optional[Sequence["_IpProtocolEntryDefinition"]]
    L4PortSetEntry: Optional[Sequence["_L4PortSetEntryDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            AlgorithmEntry=deserialize_list(json_data.get("AlgorithmEntry"), AlgorithmEntryDefinition),
            EtherTypeEntry=deserialize_list(json_data.get("EtherTypeEntry"), EtherTypeEntryDefinition),
            IcmpEntry=deserialize_list(json_data.get("IcmpEntry"), IcmpEntryDefinition),
            IgmpEntry=deserialize_list(json_data.get("IgmpEntry"), IgmpEntryDefinition),
            IpProtocolEntry=deserialize_list(json_data.get("IpProtocolEntry"), IpProtocolEntryDefinition),
            L4PortSetEntry=deserialize_list(json_data.get("L4PortSetEntry"), L4PortSetEntryDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlgorithmEntryDefinition(BaseModel):
    Algorithm: Optional[str]
    Description: Optional[str]
    DestinationPort: Optional[str]
    DisplayName: Optional[str]
    SourcePorts: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AlgorithmEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlgorithmEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Description=json_data.get("Description"),
            DestinationPort=json_data.get("DestinationPort"),
            DisplayName=json_data.get("DisplayName"),
            SourcePorts=json_data.get("SourcePorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlgorithmEntryDefinition = AlgorithmEntryDefinition


@dataclass
class EtherTypeEntryDefinition(BaseModel):
    Description: Optional[str]
    DisplayName: Optional[str]
    EtherType: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EtherTypeEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EtherTypeEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            EtherType=json_data.get("EtherType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EtherTypeEntryDefinition = EtherTypeEntryDefinition


@dataclass
class IcmpEntryDefinition(BaseModel):
    Description: Optional[str]
    DisplayName: Optional[str]
    IcmpCode: Optional[str]
    IcmpType: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpEntryDefinition = IcmpEntryDefinition


@dataclass
class IgmpEntryDefinition(BaseModel):
    Description: Optional[str]
    DisplayName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IgmpEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IgmpEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IgmpEntryDefinition = IgmpEntryDefinition


@dataclass
class IpProtocolEntryDefinition(BaseModel):
    Description: Optional[str]
    DisplayName: Optional[str]
    Protocol: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpProtocolEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpProtocolEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpProtocolEntryDefinition = IpProtocolEntryDefinition


@dataclass
class L4PortSetEntryDefinition(BaseModel):
    Description: Optional[str]
    DestinationPorts: Optional[Sequence[str]]
    DisplayName: Optional[str]
    Protocol: Optional[str]
    SourcePorts: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_L4PortSetEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_L4PortSetEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DestinationPorts=json_data.get("DestinationPorts"),
            DisplayName=json_data.get("DisplayName"),
            Protocol=json_data.get("Protocol"),
            SourcePorts=json_data.get("SourcePorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_L4PortSetEntryDefinition = L4PortSetEntryDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


