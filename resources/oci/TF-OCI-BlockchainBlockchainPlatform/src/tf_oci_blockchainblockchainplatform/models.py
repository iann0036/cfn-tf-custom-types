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
    CaCertArchiveText: Optional[str]
    CompartmentId: Optional[str]
    ComponentDetails: Optional[Sequence["_ComponentDetailsDefinition5"]]
    ComputeShape: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    FederatedUserId: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    HostOcpuUtilizationInfo: Optional[Sequence["_HostOcpuUtilizationInfoDefinition"]]
    Id: Optional[str]
    IdcsAccessToken: Optional[str]
    IsByol: Optional[bool]
    IsMultiAd: Optional[bool]
    LifecycleDetails: Optional[str]
    LoadBalancerShape: Optional[str]
    PlatformRole: Optional[str]
    PlatformShapeType: Optional[str]
    ServiceEndpoint: Optional[str]
    ServiceVersion: Optional[str]
    State: Optional[str]
    StorageSizeInTbs: Optional[float]
    StorageUsedInTbs: Optional[float]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    TotalOcpuCapacity: Optional[float]
    Replicas: Optional[Sequence["_ReplicasDefinition"]]
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
            CaCertArchiveText=json_data.get("CaCertArchiveText"),
            CompartmentId=json_data.get("CompartmentId"),
            ComponentDetails=deserialize_list(json_data.get("ComponentDetails"), ComponentDetailsDefinition5),
            ComputeShape=json_data.get("ComputeShape"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FederatedUserId=json_data.get("FederatedUserId"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            HostOcpuUtilizationInfo=deserialize_list(json_data.get("HostOcpuUtilizationInfo"), HostOcpuUtilizationInfoDefinition),
            Id=json_data.get("Id"),
            IdcsAccessToken=json_data.get("IdcsAccessToken"),
            IsByol=json_data.get("IsByol"),
            IsMultiAd=json_data.get("IsMultiAd"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            LoadBalancerShape=json_data.get("LoadBalancerShape"),
            PlatformRole=json_data.get("PlatformRole"),
            PlatformShapeType=json_data.get("PlatformShapeType"),
            ServiceEndpoint=json_data.get("ServiceEndpoint"),
            ServiceVersion=json_data.get("ServiceVersion"),
            State=json_data.get("State"),
            StorageSizeInTbs=json_data.get("StorageSizeInTbs"),
            StorageUsedInTbs=json_data.get("StorageUsedInTbs"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            TotalOcpuCapacity=json_data.get("TotalOcpuCapacity"),
            Replicas=deserialize_list(json_data.get("Replicas"), ReplicasDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ComponentDetailsDefinition5(BaseModel):
    Osns: Optional[Sequence["_ComponentDetailsDefinition2"]]
    Peers: Optional[Sequence["_ComponentDetailsDefinition4"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentDetailsDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentDetailsDefinition5"]:
        if not json_data:
            return None
        return cls(
            Osns=deserialize_list(json_data.get("Osns"), ComponentDetailsDefinition2),
            Peers=deserialize_list(json_data.get("Peers"), ComponentDetailsDefinition4),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentDetailsDefinition5 = ComponentDetailsDefinition5


@dataclass
class ComponentDetailsDefinition2(BaseModel):
    Ad: Optional[str]
    OcpuAllocationParam: Optional[Sequence["_ComponentDetailsDefinition"]]
    OsnKey: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentDetailsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentDetailsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Ad=json_data.get("Ad"),
            OcpuAllocationParam=deserialize_list(json_data.get("OcpuAllocationParam"), ComponentDetailsDefinition),
            OsnKey=json_data.get("OsnKey"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentDetailsDefinition2 = ComponentDetailsDefinition2


@dataclass
class ComponentDetailsDefinition(BaseModel):
    OcpuAllocationNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            OcpuAllocationNumber=json_data.get("OcpuAllocationNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentDetailsDefinition = ComponentDetailsDefinition


@dataclass
class ComponentDetailsDefinition4(BaseModel):
    Ad: Optional[str]
    Alias: Optional[str]
    Host: Optional[str]
    OcpuAllocationParam: Optional[Sequence["_ComponentDetailsDefinition3"]]
    PeerKey: Optional[str]
    Role: Optional[str]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentDetailsDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentDetailsDefinition4"]:
        if not json_data:
            return None
        return cls(
            Ad=json_data.get("Ad"),
            Alias=json_data.get("Alias"),
            Host=json_data.get("Host"),
            OcpuAllocationParam=deserialize_list(json_data.get("OcpuAllocationParam"), ComponentDetailsDefinition3),
            PeerKey=json_data.get("PeerKey"),
            Role=json_data.get("Role"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentDetailsDefinition4 = ComponentDetailsDefinition4


@dataclass
class ComponentDetailsDefinition3(BaseModel):
    OcpuAllocationNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentDetailsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentDetailsDefinition3"]:
        if not json_data:
            return None
        return cls(
            OcpuAllocationNumber=json_data.get("OcpuAllocationNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentDetailsDefinition3 = ComponentDetailsDefinition3


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
class HostOcpuUtilizationInfoDefinition(BaseModel):
    Host: Optional[str]
    OcpuCapacityNumber: Optional[float]
    OcpuUtilizationNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HostOcpuUtilizationInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostOcpuUtilizationInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            OcpuCapacityNumber=json_data.get("OcpuCapacityNumber"),
            OcpuUtilizationNumber=json_data.get("OcpuUtilizationNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostOcpuUtilizationInfoDefinition = HostOcpuUtilizationInfoDefinition


@dataclass
class ReplicasDefinition(BaseModel):
    CaCount: Optional[float]
    ConsoleCount: Optional[float]
    ProxyCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicasDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCount=json_data.get("CaCount"),
            ConsoleCount=json_data.get("ConsoleCount"),
            ProxyCount=json_data.get("ProxyCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicasDefinition = ReplicasDefinition


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


