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
    AllowedIps: Optional[Sequence[str]]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PartitionCount: Optional[float]
    PrimaryKey: Optional[str]
    PublicNetworkAccessEnabled: Optional[bool]
    QueryKeys: Optional[Sequence["_QueryKeysDefinition"]]
    ReplicaCount: Optional[float]
    ResourceGroupName: Optional[str]
    SecondaryKey: Optional[str]
    Sku: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
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
            AllowedIps=json_data.get("AllowedIps"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PartitionCount=json_data.get("PartitionCount"),
            PrimaryKey=json_data.get("PrimaryKey"),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            QueryKeys=deserialize_list(json_data.get("QueryKeys"), QueryKeysDefinition),
            ReplicaCount=json_data.get("ReplicaCount"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryKey=json_data.get("SecondaryKey"),
            Sku=json_data.get("Sku"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class QueryKeysDefinition(BaseModel):
    Key: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryKeysDefinition = QueryKeysDefinition


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


