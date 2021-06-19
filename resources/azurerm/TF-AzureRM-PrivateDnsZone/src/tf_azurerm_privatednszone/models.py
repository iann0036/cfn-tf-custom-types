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
    MaxNumberOfRecordSets: Optional[float]
    MaxNumberOfVirtualNetworkLinks: Optional[float]
    MaxNumberOfVirtualNetworkLinksWithRegistration: Optional[float]
    Name: Optional[str]
    NumberOfRecordSets: Optional[float]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    SoaRecord: Optional[Sequence["_SoaRecordDefinition"]]
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
            MaxNumberOfRecordSets=json_data.get("MaxNumberOfRecordSets"),
            MaxNumberOfVirtualNetworkLinks=json_data.get("MaxNumberOfVirtualNetworkLinks"),
            MaxNumberOfVirtualNetworkLinksWithRegistration=json_data.get("MaxNumberOfVirtualNetworkLinksWithRegistration"),
            Name=json_data.get("Name"),
            NumberOfRecordSets=json_data.get("NumberOfRecordSets"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            SoaRecord=deserialize_list(json_data.get("SoaRecord"), SoaRecordDefinition),
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
class SoaRecordDefinition(BaseModel):
    Email: Optional[str]
    ExpireTime: Optional[float]
    MinimumTtl: Optional[float]
    RefreshTime: Optional[float]
    RetryTime: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition2"]]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SoaRecordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoaRecordDefinition"]:
        if not json_data:
            return None
        return cls(
            Email=json_data.get("Email"),
            ExpireTime=json_data.get("ExpireTime"),
            MinimumTtl=json_data.get("MinimumTtl"),
            RefreshTime=json_data.get("RefreshTime"),
            RetryTime=json_data.get("RetryTime"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition2),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoaRecordDefinition = SoaRecordDefinition


@dataclass
class TagsDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition2 = TagsDefinition2


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


