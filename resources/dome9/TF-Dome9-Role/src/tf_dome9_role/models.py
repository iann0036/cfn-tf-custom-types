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
    Create: Optional[Sequence[str]]
    CrossAccountAccess: Optional[Sequence[str]]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PermitAlertActions: Optional[bool]
    PermitNotifications: Optional[bool]
    PermitOnBoarding: Optional[bool]
    PermitPolicies: Optional[bool]
    PermitRulesets: Optional[bool]
    Access: Optional[Sequence["_AccessDefinition"]]
    Manage: Optional[Sequence["_ManageDefinition"]]
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
            Create=json_data.get("Create"),
            CrossAccountAccess=json_data.get("CrossAccountAccess"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PermitAlertActions=json_data.get("PermitAlertActions"),
            PermitNotifications=json_data.get("PermitNotifications"),
            PermitOnBoarding=json_data.get("PermitOnBoarding"),
            PermitPolicies=json_data.get("PermitPolicies"),
            PermitRulesets=json_data.get("PermitRulesets"),
            Access=deserialize_list(json_data.get("Access"), AccessDefinition),
            Manage=deserialize_list(json_data.get("Manage"), ManageDefinition),
            View=deserialize_list(json_data.get("View"), ViewDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessDefinition(BaseModel):
    MainId: Optional[str]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    Traffic: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessDefinition"]:
        if not json_data:
            return None
        return cls(
            MainId=json_data.get("MainId"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Traffic=json_data.get("Traffic"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessDefinition = AccessDefinition


@dataclass
class ManageDefinition(BaseModel):
    MainId: Optional[str]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    Traffic: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManageDefinition"]:
        if not json_data:
            return None
        return cls(
            MainId=json_data.get("MainId"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Traffic=json_data.get("Traffic"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManageDefinition = ManageDefinition


@dataclass
class ViewDefinition(BaseModel):
    MainId: Optional[str]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    Traffic: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ViewDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ViewDefinition"]:
        if not json_data:
            return None
        return cls(
            MainId=json_data.get("MainId"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Traffic=json_data.get("Traffic"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ViewDefinition = ViewDefinition


