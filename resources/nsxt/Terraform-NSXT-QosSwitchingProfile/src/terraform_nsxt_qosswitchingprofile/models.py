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
    ClassOfService: Optional[float]
    Description: Optional[str]
    DisplayName: Optional[str]
    DscpPriority: Optional[float]
    DscpTrusted: Optional[bool]
    Revision: Optional[float]
    EgressRateShaper: Optional[Sequence["_EgressRateShaper"]]
    IngressBroadcastRateShaper: Optional[Sequence["_IngressBroadcastRateShaper"]]
    IngressRateShaper: Optional[Sequence["_IngressRateShaper"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClassOfService=json_data.get("ClassOfService"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            DscpPriority=json_data.get("DscpPriority"),
            DscpTrusted=json_data.get("DscpTrusted"),
            Revision=json_data.get("Revision"),
            EgressRateShaper=json_data.get("EgressRateShaper"),
            IngressBroadcastRateShaper=json_data.get("IngressBroadcastRateShaper"),
            IngressRateShaper=json_data.get("IngressRateShaper"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EgressRateShaper:
    AverageBwMbps: Optional[float]
    BurstSize: Optional[float]
    Enabled: Optional[bool]
    PeakBwMbps: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EgressRateShaper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressRateShaper"]:
        if not json_data:
            return None
        return cls(
            AverageBwMbps=json_data.get("AverageBwMbps"),
            BurstSize=json_data.get("BurstSize"),
            Enabled=json_data.get("Enabled"),
            PeakBwMbps=json_data.get("PeakBwMbps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressRateShaper = EgressRateShaper


@dataclass
class IngressBroadcastRateShaper:
    AverageBwKbps: Optional[float]
    BurstSize: Optional[float]
    Enabled: Optional[bool]
    PeakBwKbps: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IngressBroadcastRateShaper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressBroadcastRateShaper"]:
        if not json_data:
            return None
        return cls(
            AverageBwKbps=json_data.get("AverageBwKbps"),
            BurstSize=json_data.get("BurstSize"),
            Enabled=json_data.get("Enabled"),
            PeakBwKbps=json_data.get("PeakBwKbps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressBroadcastRateShaper = IngressBroadcastRateShaper


@dataclass
class IngressRateShaper:
    AverageBwMbps: Optional[float]
    BurstSize: Optional[float]
    Enabled: Optional[bool]
    PeakBwMbps: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IngressRateShaper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressRateShaper"]:
        if not json_data:
            return None
        return cls(
            AverageBwMbps=json_data.get("AverageBwMbps"),
            BurstSize=json_data.get("BurstSize"),
            Enabled=json_data.get("Enabled"),
            PeakBwMbps=json_data.get("PeakBwMbps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressRateShaper = IngressRateShaper


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


