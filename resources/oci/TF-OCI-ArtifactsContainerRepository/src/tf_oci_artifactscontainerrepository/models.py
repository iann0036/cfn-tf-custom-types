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
    BillableSizeInGbs: Optional[str]
    CompartmentId: Optional[str]
    CreatedBy: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    ImageCount: Optional[float]
    IsImmutable: Optional[bool]
    IsPublic: Optional[bool]
    LayerCount: Optional[float]
    LayersSizeInBytes: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    TimeLastPushed: Optional[str]
    Readme: Optional[Sequence["_ReadmeDefinition"]]
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
            BillableSizeInGbs=json_data.get("BillableSizeInGbs"),
            CompartmentId=json_data.get("CompartmentId"),
            CreatedBy=json_data.get("CreatedBy"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            ImageCount=json_data.get("ImageCount"),
            IsImmutable=json_data.get("IsImmutable"),
            IsPublic=json_data.get("IsPublic"),
            LayerCount=json_data.get("LayerCount"),
            LayersSizeInBytes=json_data.get("LayersSizeInBytes"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            TimeLastPushed=json_data.get("TimeLastPushed"),
            Readme=deserialize_list(json_data.get("Readme"), ReadmeDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ReadmeDefinition(BaseModel):
    Content: Optional[str]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReadmeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadmeDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadmeDefinition = ReadmeDefinition


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


