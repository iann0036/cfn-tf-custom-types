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
    CharacterSet: Optional[str]
    CompartmentId: Optional[str]
    DatabaseConfiguration: Optional[str]
    DatabaseEdition: Optional[str]
    DatabaseManagementConfig: Optional[Sequence["_DatabaseManagementConfigDefinition"]]
    DatabaseVersion: Optional[str]
    DbId: Optional[str]
    DbPacks: Optional[str]
    DbUniqueName: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    NcharacterSet: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeZone: Optional[str]
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
            CharacterSet=json_data.get("CharacterSet"),
            CompartmentId=json_data.get("CompartmentId"),
            DatabaseConfiguration=json_data.get("DatabaseConfiguration"),
            DatabaseEdition=json_data.get("DatabaseEdition"),
            DatabaseManagementConfig=deserialize_list(json_data.get("DatabaseManagementConfig"), DatabaseManagementConfigDefinition),
            DatabaseVersion=json_data.get("DatabaseVersion"),
            DbId=json_data.get("DbId"),
            DbPacks=json_data.get("DbPacks"),
            DbUniqueName=json_data.get("DbUniqueName"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            NcharacterSet=json_data.get("NcharacterSet"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeZone=json_data.get("TimeZone"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DatabaseManagementConfigDefinition(BaseModel):
    DatabaseManagementConnectionId: Optional[str]
    DatabaseManagementStatus: Optional[str]
    LicenseModel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseManagementConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseManagementConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            DatabaseManagementConnectionId=json_data.get("DatabaseManagementConnectionId"),
            DatabaseManagementStatus=json_data.get("DatabaseManagementStatus"),
            LicenseModel=json_data.get("LicenseModel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseManagementConfigDefinition = DatabaseManagementConfigDefinition


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


