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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    VcnId: Optional[str]
    EgressSecurityRules: Optional[Sequence["_EgressSecurityRulesDefinition"]]
    IngressSecurityRules: Optional[Sequence["_IngressSecurityRulesDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            VcnId=json_data.get("VcnId"),
            EgressSecurityRules=deserialize_list(json_data.get("EgressSecurityRules"), EgressSecurityRulesDefinition),
            IngressSecurityRules=deserialize_list(json_data.get("IngressSecurityRules"), IngressSecurityRulesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class EgressSecurityRulesDefinition(BaseModel):
    Description: Optional[str]
    Destination: Optional[str]
    DestinationType: Optional[str]
    Protocol: Optional[str]
    Stateless: Optional[bool]
    IcmpOptions: Optional[Sequence["_IcmpOptionsDefinition"]]
    TcpOptions: Optional[Sequence["_TcpOptionsDefinition"]]
    UdpOptions: Optional[Sequence["_UdpOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EgressSecurityRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressSecurityRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Destination=json_data.get("Destination"),
            DestinationType=json_data.get("DestinationType"),
            Protocol=json_data.get("Protocol"),
            Stateless=json_data.get("Stateless"),
            IcmpOptions=deserialize_list(json_data.get("IcmpOptions"), IcmpOptionsDefinition),
            TcpOptions=deserialize_list(json_data.get("TcpOptions"), TcpOptionsDefinition),
            UdpOptions=deserialize_list(json_data.get("UdpOptions"), UdpOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressSecurityRulesDefinition = EgressSecurityRulesDefinition


@dataclass
class IcmpOptionsDefinition(BaseModel):
    Code: Optional[float]
    Type: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IcmpOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IcmpOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IcmpOptionsDefinition = IcmpOptionsDefinition


@dataclass
class TcpOptionsDefinition(BaseModel):
    Max: Optional[float]
    Min: Optional[float]
    SourcePortRange: Optional[Sequence["_SourcePortRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TcpOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TcpOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            SourcePortRange=deserialize_list(json_data.get("SourcePortRange"), SourcePortRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TcpOptionsDefinition = TcpOptionsDefinition


@dataclass
class SourcePortRangeDefinition(BaseModel):
    Max: Optional[float]
    Min: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SourcePortRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcePortRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcePortRangeDefinition = SourcePortRangeDefinition


@dataclass
class UdpOptionsDefinition(BaseModel):
    Max: Optional[float]
    Min: Optional[float]
    SourcePortRange: Optional[Sequence["_SourcePortRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UdpOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Max=json_data.get("Max"),
            Min=json_data.get("Min"),
            SourcePortRange=deserialize_list(json_data.get("SourcePortRange"), SourcePortRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpOptionsDefinition = UdpOptionsDefinition


@dataclass
class IngressSecurityRulesDefinition(BaseModel):
    Description: Optional[str]
    Protocol: Optional[str]
    Source: Optional[str]
    SourceType: Optional[str]
    Stateless: Optional[bool]
    IcmpOptions: Optional[Sequence["_IcmpOptionsDefinition"]]
    TcpOptions: Optional[Sequence["_TcpOptionsDefinition"]]
    UdpOptions: Optional[Sequence["_UdpOptionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressSecurityRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressSecurityRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Protocol=json_data.get("Protocol"),
            Source=json_data.get("Source"),
            SourceType=json_data.get("SourceType"),
            Stateless=json_data.get("Stateless"),
            IcmpOptions=deserialize_list(json_data.get("IcmpOptions"), IcmpOptionsDefinition),
            TcpOptions=deserialize_list(json_data.get("TcpOptions"), TcpOptionsDefinition),
            UdpOptions=deserialize_list(json_data.get("UdpOptions"), UdpOptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressSecurityRulesDefinition = IngressSecurityRulesDefinition


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


