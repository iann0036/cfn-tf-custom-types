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
    AssociatedDatabases: Optional[Sequence["_AssociatedDatabasesDefinition"]]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]
    TypeDetails: Optional[Sequence["_TypeDetailsDefinition"]]

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
            AssociatedDatabases=deserialize_list(json_data.get("AssociatedDatabases"), AssociatedDatabasesDefinition),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            TypeDetails=deserialize_list(json_data.get("TypeDetails"), TypeDetailsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AssociatedDatabasesDefinition(BaseModel):
    DbName: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssociatedDatabasesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssociatedDatabasesDefinition"]:
        if not json_data:
            return None
        return cls(
            DbName=json_data.get("DbName"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssociatedDatabasesDefinition = AssociatedDatabasesDefinition


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


@dataclass
class TypeDetailsDefinition(BaseModel):
    AdminUsername: Optional[str]
    ConnectionIps: Optional[Sequence[str]]
    SecretId: Optional[str]
    Type: Optional[str]
    VaultId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TypeDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminUsername=json_data.get("AdminUsername"),
            ConnectionIps=json_data.get("ConnectionIps"),
            SecretId=json_data.get("SecretId"),
            Type=json_data.get("Type"),
            VaultId=json_data.get("VaultId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TypeDetailsDefinition = TypeDetailsDefinition


