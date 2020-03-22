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
    ActualSize: Optional[float]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    InstanceConfigurationId: Optional[str]
    Size: Optional[float]
    State: Optional[str]
    TimeCreated: Optional[str]
    LoadBalancers: Optional[Sequence["_LoadBalancers"]]
    PlacementConfigurations: Optional[Sequence["_PlacementConfigurations"]]
    Timeouts: Optional["_Timeouts"]
    SecondaryVnicSubnets: Optional[Sequence["_SecondaryVnicSubnets"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActualSize=json_data.get("ActualSize"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            InstanceConfigurationId=json_data.get("InstanceConfigurationId"),
            Size=json_data.get("Size"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            LoadBalancers=json_data.get("LoadBalancers"),
            PlacementConfigurations=json_data.get("PlacementConfigurations"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            SecondaryVnicSubnets=json_data.get("SecondaryVnicSubnets"),
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
class LoadBalancers:
    BackendSetName: Optional[str]
    LoadBalancerId: Optional[str]
    Port: Optional[float]
    VnicSelection: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancers"]:
        if not json_data:
            return None
        return cls(
            BackendSetName=json_data.get("BackendSetName"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Port=json_data.get("Port"),
            VnicSelection=json_data.get("VnicSelection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancers = LoadBalancers


@dataclass
class PlacementConfigurations:
    AvailabilityDomain: Optional[str]
    FaultDomains: Optional[Sequence[str]]
    PrimarySubnetId: Optional[str]
    SecondaryVnicSubnets: Optional[Sequence["_SecondaryVnicSubnets"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConfigurations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConfigurations"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            FaultDomains=json_data.get("FaultDomains"),
            PrimarySubnetId=json_data.get("PrimarySubnetId"),
            SecondaryVnicSubnets=json_data.get("SecondaryVnicSubnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConfigurations = PlacementConfigurations


@dataclass
class SecondaryVnicSubnets:
    DisplayName: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryVnicSubnets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryVnicSubnets"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryVnicSubnets = SecondaryVnicSubnets


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


