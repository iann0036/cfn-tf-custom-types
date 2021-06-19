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
    Dns: Optional[Sequence[str]]
    ExadataInfrastructureId: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    Ntp: Optional[Sequence[str]]
    State: Optional[str]
    TimeCreated: Optional[str]
    ValidateVmClusterNetwork: Optional[bool]
    VmClusterId: Optional[str]
    Scans: Optional[Sequence["_ScansDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VmNetworks: Optional[Sequence["_VmNetworksDefinition"]]

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
            Dns=json_data.get("Dns"),
            ExadataInfrastructureId=json_data.get("ExadataInfrastructureId"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Ntp=json_data.get("Ntp"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            ValidateVmClusterNetwork=json_data.get("ValidateVmClusterNetwork"),
            VmClusterId=json_data.get("VmClusterId"),
            Scans=deserialize_list(json_data.get("Scans"), ScansDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VmNetworks=deserialize_list(json_data.get("VmNetworks"), VmNetworksDefinition),
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
class ScansDefinition(BaseModel):
    Hostname: Optional[str]
    Ips: Optional[Sequence[str]]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScansDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScansDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ips=json_data.get("Ips"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScansDefinition = ScansDefinition


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


@dataclass
class VmNetworksDefinition(BaseModel):
    DomainName: Optional[str]
    Gateway: Optional[str]
    Netmask: Optional[str]
    NetworkType: Optional[str]
    VlanId: Optional[str]
    Nodes: Optional[Sequence["_NodesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VmNetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmNetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            Gateway=json_data.get("Gateway"),
            Netmask=json_data.get("Netmask"),
            NetworkType=json_data.get("NetworkType"),
            VlanId=json_data.get("VlanId"),
            Nodes=deserialize_list(json_data.get("Nodes"), NodesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmNetworksDefinition = VmNetworksDefinition


@dataclass
class NodesDefinition(BaseModel):
    Hostname: Optional[str]
    Ip: Optional[str]
    Vip: Optional[str]
    VipHostname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ip=json_data.get("Ip"),
            Vip=json_data.get("Vip"),
            VipHostname=json_data.get("VipHostname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


