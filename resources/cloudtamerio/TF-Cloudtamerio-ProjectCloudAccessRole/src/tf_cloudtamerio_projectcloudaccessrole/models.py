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
    ApplyToAllAccounts: Optional[bool]
    AwsIamPath: Optional[str]
    AwsIamPermissionsBoundary: Optional[float]
    AwsIamRoleName: Optional[str]
    FutureAccounts: Optional[bool]
    Id: Optional[str]
    LastUpdated: Optional[str]
    LongTermAccessKeys: Optional[bool]
    Name: Optional[str]
    ProjectId: Optional[float]
    ShortTermAccessKeys: Optional[bool]
    WebAccess: Optional[bool]
    Accounts: Optional[Sequence["_AccountsDefinition"]]
    AwsIamPolicies: Optional[Sequence["_AwsIamPoliciesDefinition"]]
    AzureRoleDefinitions: Optional[Sequence["_AzureRoleDefinitionsDefinition"]]
    UserGroups: Optional[Sequence["_UserGroupsDefinition"]]
    Users: Optional[Sequence["_UsersDefinition"]]

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
            ApplyToAllAccounts=json_data.get("ApplyToAllAccounts"),
            AwsIamPath=json_data.get("AwsIamPath"),
            AwsIamPermissionsBoundary=json_data.get("AwsIamPermissionsBoundary"),
            AwsIamRoleName=json_data.get("AwsIamRoleName"),
            FutureAccounts=json_data.get("FutureAccounts"),
            Id=json_data.get("Id"),
            LastUpdated=json_data.get("LastUpdated"),
            LongTermAccessKeys=json_data.get("LongTermAccessKeys"),
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
            ShortTermAccessKeys=json_data.get("ShortTermAccessKeys"),
            WebAccess=json_data.get("WebAccess"),
            Accounts=deserialize_list(json_data.get("Accounts"), AccountsDefinition),
            AwsIamPolicies=deserialize_list(json_data.get("AwsIamPolicies"), AwsIamPoliciesDefinition),
            AzureRoleDefinitions=deserialize_list(json_data.get("AzureRoleDefinitions"), AzureRoleDefinitionsDefinition),
            UserGroups=deserialize_list(json_data.get("UserGroups"), UserGroupsDefinition),
            Users=deserialize_list(json_data.get("Users"), UsersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccountsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AccountsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountsDefinition = AccountsDefinition


@dataclass
class AwsIamPoliciesDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIamPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIamPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIamPoliciesDefinition = AwsIamPoliciesDefinition


@dataclass
class AzureRoleDefinitionsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AzureRoleDefinitionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureRoleDefinitionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureRoleDefinitionsDefinition = AzureRoleDefinitionsDefinition


@dataclass
class UserGroupsDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UserGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserGroupsDefinition = UserGroupsDefinition


@dataclass
class UsersDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UsersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsersDefinition = UsersDefinition

