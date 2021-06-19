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
    AuthDatabaseName: Optional[str]
    AwsIamType: Optional[str]
    DatabaseName: Optional[str]
    Id: Optional[str]
    LdapAuthType: Optional[str]
    Password: Optional[str]
    ProjectId: Optional[str]
    Username: Optional[str]
    X509Type: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Roles: Optional[Sequence["_RolesDefinition"]]
    Scopes: Optional[Sequence["_ScopesDefinition"]]

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
            AuthDatabaseName=json_data.get("AuthDatabaseName"),
            AwsIamType=json_data.get("AwsIamType"),
            DatabaseName=json_data.get("DatabaseName"),
            Id=json_data.get("Id"),
            LdapAuthType=json_data.get("LdapAuthType"),
            Password=json_data.get("Password"),
            ProjectId=json_data.get("ProjectId"),
            Username=json_data.get("Username"),
            X509Type=json_data.get("X509Type"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Roles=deserialize_list(json_data.get("Roles"), RolesDefinition),
            Scopes=deserialize_list(json_data.get("Scopes"), ScopesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class RolesDefinition(BaseModel):
    CollectionName: Optional[str]
    DatabaseName: Optional[str]
    RoleName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RolesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RolesDefinition"]:
        if not json_data:
            return None
        return cls(
            CollectionName=json_data.get("CollectionName"),
            DatabaseName=json_data.get("DatabaseName"),
            RoleName=json_data.get("RoleName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RolesDefinition = RolesDefinition


@dataclass
class ScopesDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScopesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopesDefinition = ScopesDefinition


