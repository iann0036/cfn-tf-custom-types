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
    CreateTime: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PostStartupScript: Optional[str]
    Project: Optional[str]
    ContainerImage: Optional[Sequence["_ContainerImageDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VmImage: Optional[Sequence["_VmImageDefinition"]]

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
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PostStartupScript=json_data.get("PostStartupScript"),
            Project=json_data.get("Project"),
            ContainerImage=deserialize_list(json_data.get("ContainerImage"), ContainerImageDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VmImage=deserialize_list(json_data.get("VmImage"), VmImageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ContainerImageDefinition(BaseModel):
    Repository: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerImageDefinition"]:
        if not json_data:
            return None
        return cls(
            Repository=json_data.get("Repository"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerImageDefinition = ContainerImageDefinition


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
class VmImageDefinition(BaseModel):
    ImageFamily: Optional[str]
    ImageName: Optional[str]
    Project: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VmImageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VmImageDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageFamily=json_data.get("ImageFamily"),
            ImageName=json_data.get("ImageName"),
            Project=json_data.get("Project"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VmImageDefinition = VmImageDefinition

