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
    AppProfileId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IgnoreWarnings: Optional[bool]
    Instance: Optional[str]
    MultiClusterRoutingUseAny: Optional[bool]
    Name: Optional[str]
    Project: Optional[str]
    SingleClusterRouting: Optional[Sequence["_SingleClusterRoutingDefinition"]]
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
            AppProfileId=json_data.get("AppProfileId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Instance=json_data.get("Instance"),
            MultiClusterRoutingUseAny=json_data.get("MultiClusterRoutingUseAny"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SingleClusterRouting=deserialize_list(json_data.get("SingleClusterRouting"), SingleClusterRoutingDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SingleClusterRoutingDefinition(BaseModel):
    AllowTransactionalWrites: Optional[bool]
    ClusterId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingleClusterRoutingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingleClusterRoutingDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowTransactionalWrites=json_data.get("AllowTransactionalWrites"),
            ClusterId=json_data.get("ClusterId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingleClusterRoutingDefinition = SingleClusterRoutingDefinition


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


