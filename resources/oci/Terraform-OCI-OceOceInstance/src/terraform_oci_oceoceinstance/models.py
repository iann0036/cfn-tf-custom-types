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
    AdminEmail: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    Description: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Guid: Optional[str]
    Id: Optional[str]
    IdcsAccessToken: Optional[str]
    IdcsTenancy: Optional[str]
    InstanceUsageType: Optional[str]
    Name: Optional[str]
    ObjectStorageNamespace: Optional[str]
    Service: Optional[Sequence["_Service"]]
    State: Optional[str]
    StateMessage: Optional[str]
    TenancyId: Optional[str]
    TenancyName: Optional[str]
    TimeCreated: Optional[str]
    TimeUpdated: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminEmail=json_data.get("AdminEmail"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            Description=json_data.get("Description"),
            FreeformTags=json_data.get("FreeformTags"),
            Guid=json_data.get("Guid"),
            Id=json_data.get("Id"),
            IdcsAccessToken=json_data.get("IdcsAccessToken"),
            IdcsTenancy=json_data.get("IdcsTenancy"),
            InstanceUsageType=json_data.get("InstanceUsageType"),
            Name=json_data.get("Name"),
            ObjectStorageNamespace=json_data.get("ObjectStorageNamespace"),
            Service=json_data.get("Service"),
            State=json_data.get("State"),
            StateMessage=json_data.get("StateMessage"),
            TenancyId=json_data.get("TenancyId"),
            TenancyName=json_data.get("TenancyName"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeUpdated=json_data.get("TimeUpdated"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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
class Service:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Service"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Service"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Service = Service


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


