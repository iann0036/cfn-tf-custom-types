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
    CatalogId: Optional[str]
    CreatedById: Optional[str]
    DataAssetKey: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    EncProperties: Optional[Sequence["_EncPropertiesDefinition"]]
    ExternalKey: Optional[str]
    Id: Optional[str]
    IsDefault: Optional[bool]
    Key: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition"]]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeStatusUpdated: Optional[str]
    TimeUpdated: Optional[str]
    TypeKey: Optional[str]
    UpdatedById: Optional[str]
    Uri: Optional[str]
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
            CatalogId=json_data.get("CatalogId"),
            CreatedById=json_data.get("CreatedById"),
            DataAssetKey=json_data.get("DataAssetKey"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            EncProperties=deserialize_list(json_data.get("EncProperties"), EncPropertiesDefinition),
            ExternalKey=json_data.get("ExternalKey"),
            Id=json_data.get("Id"),
            IsDefault=json_data.get("IsDefault"),
            Key=json_data.get("Key"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeStatusUpdated=json_data.get("TimeStatusUpdated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            TypeKey=json_data.get("TypeKey"),
            UpdatedById=json_data.get("UpdatedById"),
            Uri=json_data.get("Uri"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EncPropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncPropertiesDefinition = EncPropertiesDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


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


