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
    AppObjectId: Optional[str]
    Authorization: Optional[Sequence["_AuthorizationDefinition"]]
    AzSpnRoleAssignmentId: Optional[str]
    AzSpnRolePermissions: Optional[str]
    AzurecrName: Optional[str]
    AzurecrSpnTenantid: Optional[str]
    AzurecrSubscriptionId: Optional[str]
    AzurecrSubscriptionName: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    ProjectId: Optional[str]
    ResourceGroup: Optional[str]
    ServiceEndpointName: Optional[str]
    ServicePrincipalId: Optional[str]
    SpnObjectId: Optional[str]
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
            AppObjectId=json_data.get("AppObjectId"),
            Authorization=deserialize_list(json_data.get("Authorization"), AuthorizationDefinition),
            AzSpnRoleAssignmentId=json_data.get("AzSpnRoleAssignmentId"),
            AzSpnRolePermissions=json_data.get("AzSpnRolePermissions"),
            AzurecrName=json_data.get("AzurecrName"),
            AzurecrSpnTenantid=json_data.get("AzurecrSpnTenantid"),
            AzurecrSubscriptionId=json_data.get("AzurecrSubscriptionId"),
            AzurecrSubscriptionName=json_data.get("AzurecrSubscriptionName"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
            ResourceGroup=json_data.get("ResourceGroup"),
            ServiceEndpointName=json_data.get("ServiceEndpointName"),
            ServicePrincipalId=json_data.get("ServicePrincipalId"),
            SpnObjectId=json_data.get("SpnObjectId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthorizationDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationDefinition = AuthorizationDefinition


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


