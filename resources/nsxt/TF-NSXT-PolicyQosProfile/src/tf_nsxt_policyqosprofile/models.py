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
    ClassOfService: Optional[float]
    Description: Optional[str]
    DisplayName: Optional[str]
    DscpPriority: Optional[float]
    DscpTrusted: Optional[bool]
    Id: Optional[str]
    NsxId: Optional[str]
    Path: Optional[str]
    Revision: Optional[float]
    EgressRateShaper: Optional[Sequence["_EgressRateShaperDefinition"]]
    IngressBroadcastRateShaper: Optional[Sequence["_IngressBroadcastRateShaperDefinition"]]
    IngressRateShaper: Optional[Sequence["_IngressRateShaperDefinition"]]
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
            ClassOfService=json_data.get("ClassOfService"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            DscpPriority=json_data.get("DscpPriority"),
            DscpTrusted=json_data.get("DscpTrusted"),
            Id=json_data.get("Id"),
            NsxId=json_data.get("NsxId"),
            Path=json_data.get("Path"),
            Revision=json_data.get("Revision"),
            EgressRateShaper=deserialize_list(json_data.get("EgressRateShaper"), EgressRateShaperDefinition),
            IngressBroadcastRateShaper=deserialize_list(json_data.get("IngressBroadcastRateShaper"), IngressBroadcastRateShaperDefinition),
            IngressRateShaper=deserialize_list(json_data.get("IngressRateShaper"), IngressRateShaperDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EgressRateShaperDefinition(BaseModel):
    AverageBwMbps: Optional[float]
    BurstSize: Optional[float]
    Enabled: Optional[bool]
    PeakBwMbps: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EgressRateShaperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressRateShaperDefinition"]:
        if not json_data:
            return None
        return cls(
            AverageBwMbps=json_data.get("AverageBwMbps"),
            BurstSize=json_data.get("BurstSize"),
            Enabled=json_data.get("Enabled"),
            PeakBwMbps=json_data.get("PeakBwMbps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressRateShaperDefinition = EgressRateShaperDefinition


@dataclass
class IngressBroadcastRateShaperDefinition(BaseModel):
    AverageBwKbps: Optional[float]
    BurstSize: Optional[float]
    Enabled: Optional[bool]
    PeakBwKbps: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IngressBroadcastRateShaperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressBroadcastRateShaperDefinition"]:
        if not json_data:
            return None
        return cls(
            AverageBwKbps=json_data.get("AverageBwKbps"),
            BurstSize=json_data.get("BurstSize"),
            Enabled=json_data.get("Enabled"),
            PeakBwKbps=json_data.get("PeakBwKbps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressBroadcastRateShaperDefinition = IngressBroadcastRateShaperDefinition


@dataclass
class IngressRateShaperDefinition(BaseModel):
    AverageBwMbps: Optional[float]
    BurstSize: Optional[float]
    Enabled: Optional[bool]
    PeakBwMbps: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IngressRateShaperDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressRateShaperDefinition"]:
        if not json_data:
            return None
        return cls(
            AverageBwMbps=json_data.get("AverageBwMbps"),
            BurstSize=json_data.get("BurstSize"),
            Enabled=json_data.get("Enabled"),
            PeakBwMbps=json_data.get("PeakBwMbps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressRateShaperDefinition = IngressRateShaperDefinition


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


