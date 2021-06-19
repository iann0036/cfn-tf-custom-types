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
    ApiUpdatedMember: Optional[bool]
    DatasetId: Optional[str]
    Domain: Optional[str]
    GroupByEmail: Optional[str]
    IamMember: Optional[str]
    Id: Optional[str]
    Project: Optional[str]
    Role: Optional[str]
    SpecialGroup: Optional[str]
    UserByEmail: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]
    View: Optional[Sequence["_ViewDefinition"]]

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
            ApiUpdatedMember=json_data.get("ApiUpdatedMember"),
            DatasetId=json_data.get("DatasetId"),
            Domain=json_data.get("Domain"),
            GroupByEmail=json_data.get("GroupByEmail"),
            IamMember=json_data.get("IamMember"),
            Id=json_data.get("Id"),
            Project=json_data.get("Project"),
            Role=json_data.get("Role"),
            SpecialGroup=json_data.get("SpecialGroup"),
            UserByEmail=json_data.get("UserByEmail"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            View=deserialize_list(json_data.get("View"), ViewDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class ViewDefinition(BaseModel):
    DatasetId: Optional[str]
    ProjectId: Optional[str]
    TableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ViewDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ViewDefinition"]:
        if not json_data:
            return None
        return cls(
            DatasetId=json_data.get("DatasetId"),
            ProjectId=json_data.get("ProjectId"),
            TableId=json_data.get("TableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ViewDefinition = ViewDefinition


