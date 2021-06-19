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
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    StorageAuthenticationType: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    KeyDeliveryAccessControl: Optional[Sequence["_KeyDeliveryAccessControlDefinition"]]
    StorageAccount: Optional[Sequence["_StorageAccountDefinition"]]
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
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            StorageAuthenticationType=json_data.get("StorageAuthenticationType"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            KeyDeliveryAccessControl=deserialize_list(json_data.get("KeyDeliveryAccessControl"), KeyDeliveryAccessControlDefinition),
            StorageAccount=deserialize_list(json_data.get("StorageAccount"), StorageAccountDefinition),
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
class IdentityDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class KeyDeliveryAccessControlDefinition(BaseModel):
    DefaultAction: Optional[str]
    IpAllowList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_KeyDeliveryAccessControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyDeliveryAccessControlDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultAction=json_data.get("DefaultAction"),
            IpAllowList=json_data.get("IpAllowList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyDeliveryAccessControlDefinition = KeyDeliveryAccessControlDefinition


@dataclass
class StorageAccountDefinition(BaseModel):
    Id: Optional[str]
    IsPrimary: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StorageAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            IsPrimary=json_data.get("IsPrimary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageAccountDefinition = StorageAccountDefinition


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


