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
    AadAdmin: Optional[Sequence["_AadAdminDefinition"]]
    ConnectivityEndpoints: Optional[Sequence["_ConnectivityEndpointsDefinition"]]
    CustomerManagedKeyVersionlessId: Optional[str]
    DataExfiltrationProtectionEnabled: Optional[bool]
    Id: Optional[str]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    Location: Optional[str]
    ManagedResourceGroupName: Optional[str]
    ManagedVirtualNetworkEnabled: Optional[bool]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SqlAdministratorLogin: Optional[str]
    SqlAdministratorLoginPassword: Optional[str]
    SqlIdentityControlEnabled: Optional[bool]
    StorageDataLakeGen2FilesystemId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    AzureDevopsRepo: Optional[Sequence["_AzureDevopsRepoDefinition"]]
    GithubRepo: Optional[Sequence["_GithubRepoDefinition"]]
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
            AadAdmin=deserialize_list(json_data.get("AadAdmin"), AadAdminDefinition),
            ConnectivityEndpoints=deserialize_list(json_data.get("ConnectivityEndpoints"), ConnectivityEndpointsDefinition),
            CustomerManagedKeyVersionlessId=json_data.get("CustomerManagedKeyVersionlessId"),
            DataExfiltrationProtectionEnabled=json_data.get("DataExfiltrationProtectionEnabled"),
            Id=json_data.get("Id"),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Location=json_data.get("Location"),
            ManagedResourceGroupName=json_data.get("ManagedResourceGroupName"),
            ManagedVirtualNetworkEnabled=json_data.get("ManagedVirtualNetworkEnabled"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SqlAdministratorLogin=json_data.get("SqlAdministratorLogin"),
            SqlAdministratorLoginPassword=json_data.get("SqlAdministratorLoginPassword"),
            SqlIdentityControlEnabled=json_data.get("SqlIdentityControlEnabled"),
            StorageDataLakeGen2FilesystemId=json_data.get("StorageDataLakeGen2FilesystemId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            AzureDevopsRepo=deserialize_list(json_data.get("AzureDevopsRepo"), AzureDevopsRepoDefinition),
            GithubRepo=deserialize_list(json_data.get("GithubRepo"), GithubRepoDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AadAdminDefinition(BaseModel):
    Login: Optional[str]
    ObjectId: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AadAdminDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AadAdminDefinition"]:
        if not json_data:
            return None
        return cls(
            Login=json_data.get("Login"),
            ObjectId=json_data.get("ObjectId"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AadAdminDefinition = AadAdminDefinition


@dataclass
class ConnectivityEndpointsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectivityEndpointsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectivityEndpointsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectivityEndpointsDefinition = ConnectivityEndpointsDefinition


@dataclass
class IdentityDefinition(BaseModel):
    PrincipalId: Optional[str]
    TenantId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            PrincipalId=json_data.get("PrincipalId"),
            TenantId=json_data.get("TenantId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class AzureDevopsRepoDefinition(BaseModel):
    AccountName: Optional[str]
    BranchName: Optional[str]
    ProjectName: Optional[str]
    RepositoryName: Optional[str]
    RootFolder: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureDevopsRepoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureDevopsRepoDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountName=json_data.get("AccountName"),
            BranchName=json_data.get("BranchName"),
            ProjectName=json_data.get("ProjectName"),
            RepositoryName=json_data.get("RepositoryName"),
            RootFolder=json_data.get("RootFolder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureDevopsRepoDefinition = AzureDevopsRepoDefinition


@dataclass
class GithubRepoDefinition(BaseModel):
    AccountName: Optional[str]
    BranchName: Optional[str]
    GitUrl: Optional[str]
    RepositoryName: Optional[str]
    RootFolder: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GithubRepoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GithubRepoDefinition"]:
        if not json_data:
            return None
        return cls(
            AccountName=json_data.get("AccountName"),
            BranchName=json_data.get("BranchName"),
            GitUrl=json_data.get("GitUrl"),
            RepositoryName=json_data.get("RepositoryName"),
            RootFolder=json_data.get("RootFolder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GithubRepoDefinition = GithubRepoDefinition


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


