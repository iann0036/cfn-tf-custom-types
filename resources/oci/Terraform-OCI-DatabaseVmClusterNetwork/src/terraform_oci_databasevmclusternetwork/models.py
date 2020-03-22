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
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    Dns: Optional[Sequence[str]]
    ExadataInfrastructureId: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    Ntp: Optional[Sequence[str]]
    State: Optional[str]
    TimeCreated: Optional[str]
    ValidateVmClusterNetwork: Optional[bool]
    VmClusterId: Optional[str]
    Scans: Optional[Sequence["_Scans"]]
    Timeouts: Optional["_Timeouts"]
    VmNetworks: Optional[Sequence["_VmNetworks"]]
    Nodes: Optional[Sequence["_Nodes"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            Dns=json_data.get("Dns"),
            ExadataInfrastructureId=json_data.get("ExadataInfrastructureId"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Ntp=json_data.get("Ntp"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            ValidateVmClusterNetwork=json_data.get("ValidateVmClusterNetwork"),
            VmClusterId=json_data.get("VmClusterId"),
            Scans=json_data.get("Scans"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VmNetworks=json_data.get("VmNetworks"),
            Nodes=json_data.get("Nodes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class Scans:
    Hostname: Optional[str]
    Ips: Optional[Sequence[str]]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Scans"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scans"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ips=json_data.get("Ips"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scans = Scans


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class VmNetworks:
    DomainName: Optional[str]
    Gateway: Optional[str]
    Netmask: Optional[str]
    NetworkType: Optional[str]
    VlanId: Optional[str]
    Nodes: Optional[Sequence["_Nodes"]]

    @classmethod
    def _deserialize(
        cls: Type["_VmNetworks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmNetworks"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            Gateway=json_data.get("Gateway"),
            Netmask=json_data.get("Netmask"),
            NetworkType=json_data.get("NetworkType"),
            VlanId=json_data.get("VlanId"),
            Nodes=json_data.get("Nodes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmNetworks = VmNetworks


@dataclass
class Nodes:
    Hostname: Optional[str]
    Ip: Optional[str]
    Vip: Optional[str]
    VipHostname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodes"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Ip=json_data.get("Ip"),
            Vip=json_data.get("Vip"),
            VipHostname=json_data.get("VipHostname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodes = Nodes


