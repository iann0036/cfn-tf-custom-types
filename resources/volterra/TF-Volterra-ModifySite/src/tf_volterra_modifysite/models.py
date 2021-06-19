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
    Address: Optional[str]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    BgpPeerAddress: Optional[str]
    BgpRouterId: Optional[str]
    Description: Optional[str]
    DesiredPoolCount: Optional[float]
    Disable: Optional[bool]
    Id: Optional[str]
    InsideNameserver: Optional[str]
    InsideVip: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Namespace: Optional[str]
    OperatingSystemVersion: Optional[str]
    OutsideNameserver: Optional[str]
    OutsideVip: Optional[str]
    Retry: Optional[float]
    SiteToSiteNetworkType: Optional[str]
    SiteToSiteTunnelIp: Optional[str]
    TunnelDeadTimeout: Optional[float]
    TunnelType: Optional[str]
    VipVrrpMode: Optional[str]
    VolterraSoftwareOveride: Optional[str]
    VolterraSoftwareVersion: Optional[str]
    WaitTime: Optional[float]
    Coordinates: Optional[Sequence["_CoordinatesDefinition"]]

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
            Address=json_data.get("Address"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            BgpPeerAddress=json_data.get("BgpPeerAddress"),
            BgpRouterId=json_data.get("BgpRouterId"),
            Description=json_data.get("Description"),
            DesiredPoolCount=json_data.get("DesiredPoolCount"),
            Disable=json_data.get("Disable"),
            Id=json_data.get("Id"),
            InsideNameserver=json_data.get("InsideNameserver"),
            InsideVip=json_data.get("InsideVip"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            OperatingSystemVersion=json_data.get("OperatingSystemVersion"),
            OutsideNameserver=json_data.get("OutsideNameserver"),
            OutsideVip=json_data.get("OutsideVip"),
            Retry=json_data.get("Retry"),
            SiteToSiteNetworkType=json_data.get("SiteToSiteNetworkType"),
            SiteToSiteTunnelIp=json_data.get("SiteToSiteTunnelIp"),
            TunnelDeadTimeout=json_data.get("TunnelDeadTimeout"),
            TunnelType=json_data.get("TunnelType"),
            VipVrrpMode=json_data.get("VipVrrpMode"),
            VolterraSoftwareOveride=json_data.get("VolterraSoftwareOveride"),
            VolterraSoftwareVersion=json_data.get("VolterraSoftwareVersion"),
            WaitTime=json_data.get("WaitTime"),
            Coordinates=deserialize_list(json_data.get("Coordinates"), CoordinatesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class CoordinatesDefinition(BaseModel):
    Latitude: Optional[float]
    Longitude: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CoordinatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoordinatesDefinition"]:
        if not json_data:
            return None
        return cls(
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoordinatesDefinition = CoordinatesDefinition


