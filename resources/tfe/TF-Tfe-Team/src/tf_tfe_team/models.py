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
    Name: Optional[str]
    Organization: Optional[str]
    Visibility: Optional[str]
    OrganizationAccess: Optional[Sequence["_OrganizationAccessDefinition"]]

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
            Name=json_data.get("Name"),
            Organization=json_data.get("Organization"),
            Visibility=json_data.get("Visibility"),
            OrganizationAccess=deserialize_list(json_data.get("OrganizationAccess"), OrganizationAccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OrganizationAccessDefinition(BaseModel):
    ManagePolicies: Optional[bool]
    ManagePolicyOverrides: Optional[bool]
    ManageVcsSettings: Optional[bool]
    ManageWorkspaces: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            ManagePolicies=json_data.get("ManagePolicies"),
            ManagePolicyOverrides=json_data.get("ManagePolicyOverrides"),
            ManageVcsSettings=json_data.get("ManageVcsSettings"),
            ManageWorkspaces=json_data.get("ManageWorkspaces"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationAccessDefinition = OrganizationAccessDefinition


