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
    ActualSize: Optional[float]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    InstanceConfigurationId: Optional[str]
    Size: Optional[float]
    State: Optional[str]
    TimeCreated: Optional[str]
    LoadBalancers: Optional[Sequence["_LoadBalancersDefinition"]]
    PlacementConfigurations: Optional[Sequence["_PlacementConfigurationsDefinition"]]
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
            ActualSize=json_data.get("ActualSize"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            InstanceConfigurationId=json_data.get("InstanceConfigurationId"),
            Size=json_data.get("Size"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            LoadBalancers=deserialize_list(json_data.get("LoadBalancers"), LoadBalancersDefinition),
            PlacementConfigurations=deserialize_list(json_data.get("PlacementConfigurations"), PlacementConfigurationsDefinition),
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
class LoadBalancersDefinition(BaseModel):
    BackendSetName: Optional[str]
    LoadBalancerId: Optional[str]
    Port: Optional[float]
    VnicSelection: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancersDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendSetName=json_data.get("BackendSetName"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Port=json_data.get("Port"),
            VnicSelection=json_data.get("VnicSelection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancersDefinition = LoadBalancersDefinition


@dataclass
class PlacementConfigurationsDefinition(BaseModel):
    AvailabilityDomain: Optional[str]
    FaultDomains: Optional[Sequence[str]]
    PrimarySubnetId: Optional[str]
    SecondaryVnicSubnets: Optional[Sequence["_SecondaryVnicSubnetsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConfigurationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConfigurationsDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            FaultDomains=json_data.get("FaultDomains"),
            PrimarySubnetId=json_data.get("PrimarySubnetId"),
            SecondaryVnicSubnets=deserialize_list(json_data.get("SecondaryVnicSubnets"), SecondaryVnicSubnetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConfigurationsDefinition = PlacementConfigurationsDefinition


@dataclass
class SecondaryVnicSubnetsDefinition(BaseModel):
    DisplayName: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryVnicSubnetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryVnicSubnetsDefinition"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryVnicSubnetsDefinition = SecondaryVnicSubnetsDefinition


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


