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
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    InstancePools: Optional[Sequence["_InstancePools"]]
    PlacementConfiguration: Optional[Sequence["_PlacementConfiguration"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            InstancePools=json_data.get("InstancePools"),
            PlacementConfiguration=json_data.get("PlacementConfiguration"),
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
class InstancePools:
    DefinedTags: Optional[Sequence["_DefinedTags2"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags2"]]
    InstanceConfigurationId: Optional[str]
    Size: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InstancePools"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancePools"]:
        if not json_data:
            return None
        return cls(
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            InstanceConfigurationId=json_data.get("InstanceConfigurationId"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancePools = InstancePools


@dataclass
class DefinedTags2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags2 = DefinedTags2


@dataclass
class FreeformTags2:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags2 = FreeformTags2


@dataclass
class PlacementConfiguration:
    AvailabilityDomain: Optional[str]
    PrimarySubnetId: Optional[str]
    SecondaryVnicSubnets: Optional[Sequence["_SecondaryVnicSubnets"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConfiguration"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            PrimarySubnetId=json_data.get("PrimarySubnetId"),
            SecondaryVnicSubnets=json_data.get("SecondaryVnicSubnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConfiguration = PlacementConfiguration


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


