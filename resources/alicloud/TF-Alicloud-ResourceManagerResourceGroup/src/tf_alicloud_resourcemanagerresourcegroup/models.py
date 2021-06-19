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
    AccountId: Optional[str]
    CreateDate: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RegionStatuses: Optional[Sequence["_RegionStatusesDefinition"]]
    ResourceGroupName: Optional[str]
    Status: Optional[str]
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
            AccountId=json_data.get("AccountId"),
            CreateDate=json_data.get("CreateDate"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RegionStatuses=deserialize_list(json_data.get("RegionStatuses"), RegionStatusesDefinition),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Status=json_data.get("Status"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RegionStatusesDefinition(BaseModel):
    RegionId: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegionStatusesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegionStatusesDefinition"]:
        if not json_data:
            return None
        return cls(
            RegionId=json_data.get("RegionId"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegionStatusesDefinition = RegionStatusesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


