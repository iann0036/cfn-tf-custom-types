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
    Authorization: Optional[str]
    ClusterId: Optional[str]
    ClusterPolicyId: Optional[str]
    DirectoryId: Optional[str]
    DirectoryPath: Optional[str]
    Id: Optional[str]
    InstancePoolId: Optional[str]
    JobId: Optional[str]
    NotebookId: Optional[str]
    NotebookPath: Optional[str]
    ObjectType: Optional[str]
    SqlAlertId: Optional[str]
    SqlDashboardId: Optional[str]
    SqlEndpointId: Optional[str]
    SqlQueryId: Optional[str]
    AccessControl: Optional[Sequence["_AccessControlDefinition"]]

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
            Authorization=json_data.get("Authorization"),
            ClusterId=json_data.get("ClusterId"),
            ClusterPolicyId=json_data.get("ClusterPolicyId"),
            DirectoryId=json_data.get("DirectoryId"),
            DirectoryPath=json_data.get("DirectoryPath"),
            Id=json_data.get("Id"),
            InstancePoolId=json_data.get("InstancePoolId"),
            JobId=json_data.get("JobId"),
            NotebookId=json_data.get("NotebookId"),
            NotebookPath=json_data.get("NotebookPath"),
            ObjectType=json_data.get("ObjectType"),
            SqlAlertId=json_data.get("SqlAlertId"),
            SqlDashboardId=json_data.get("SqlDashboardId"),
            SqlEndpointId=json_data.get("SqlEndpointId"),
            SqlQueryId=json_data.get("SqlQueryId"),
            AccessControl=deserialize_list(json_data.get("AccessControl"), AccessControlDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccessControlDefinition(BaseModel):
    GroupName: Optional[str]
    PermissionLevel: Optional[str]
    ServicePrincipalName: Optional[str]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
            PermissionLevel=json_data.get("PermissionLevel"),
            ServicePrincipalName=json_data.get("ServicePrincipalName"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlDefinition = AccessControlDefinition


