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
    Id: Optional[str]
    LicenseType: Optional[str]
    Location: Optional[str]
    MaxSizeBytes: Optional[float]
    MaxSizeGb: Optional[float]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ServerName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    ZoneRedundant: Optional[bool]
    PerDatabaseSettings: Optional[Sequence["_PerDatabaseSettingsDefinition"]]
    Sku: Optional[Sequence["_SkuDefinition"]]
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
            Id=json_data.get("Id"),
            LicenseType=json_data.get("LicenseType"),
            Location=json_data.get("Location"),
            MaxSizeBytes=json_data.get("MaxSizeBytes"),
            MaxSizeGb=json_data.get("MaxSizeGb"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ServerName=json_data.get("ServerName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ZoneRedundant=json_data.get("ZoneRedundant"),
            PerDatabaseSettings=deserialize_list(json_data.get("PerDatabaseSettings"), PerDatabaseSettingsDefinition),
            Sku=deserialize_list(json_data.get("Sku"), SkuDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class PerDatabaseSettingsDefinition(BaseModel):
    MaxCapacity: Optional[float]
    MinCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PerDatabaseSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PerDatabaseSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PerDatabaseSettingsDefinition = PerDatabaseSettingsDefinition


@dataclass
class SkuDefinition(BaseModel):
    Capacity: Optional[float]
    Family: Optional[str]
    Name: Optional[str]
    Tier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SkuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkuDefinition"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Family=json_data.get("Family"),
            Name=json_data.get("Name"),
            Tier=json_data.get("Tier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkuDefinition = SkuDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


