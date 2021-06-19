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
    AccessKey: Optional[str]
    AccountType: Optional[str]
    ActiveDirectoryEndpointBaseUri: Optional[str]
    ApplicationId: Optional[str]
    AuthenticationEndpoint: Optional[str]
    AzureEnvironment: Optional[str]
    CertificateData: Optional[str]
    CertificateThumbprint: Optional[str]
    ClientSecret: Optional[str]
    Description: Optional[str]
    Environments: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    PrivateKeyFile: Optional[str]
    PrivateKeyPassphrase: Optional[str]
    ResourceManagerEndpoint: Optional[str]
    SecretKey: Optional[str]
    ServiceManagementEndpointBaseUri: Optional[str]
    ServiceManagementEndpointSuffix: Optional[str]
    SpaceId: Optional[str]
    SubscriptionId: Optional[str]
    TenantId: Optional[str]
    TenantTags: Optional[Sequence[str]]
    TenantedDeploymentParticipation: Optional[str]
    Tenants: Optional[Sequence[str]]
    Token: Optional[str]
    Username: Optional[str]

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
            AccessKey=json_data.get("AccessKey"),
            AccountType=json_data.get("AccountType"),
            ActiveDirectoryEndpointBaseUri=json_data.get("ActiveDirectoryEndpointBaseUri"),
            ApplicationId=json_data.get("ApplicationId"),
            AuthenticationEndpoint=json_data.get("AuthenticationEndpoint"),
            AzureEnvironment=json_data.get("AzureEnvironment"),
            CertificateData=json_data.get("CertificateData"),
            CertificateThumbprint=json_data.get("CertificateThumbprint"),
            ClientSecret=json_data.get("ClientSecret"),
            Description=json_data.get("Description"),
            Environments=json_data.get("Environments"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PrivateKeyFile=json_data.get("PrivateKeyFile"),
            PrivateKeyPassphrase=json_data.get("PrivateKeyPassphrase"),
            ResourceManagerEndpoint=json_data.get("ResourceManagerEndpoint"),
            SecretKey=json_data.get("SecretKey"),
            ServiceManagementEndpointBaseUri=json_data.get("ServiceManagementEndpointBaseUri"),
            ServiceManagementEndpointSuffix=json_data.get("ServiceManagementEndpointSuffix"),
            SpaceId=json_data.get("SpaceId"),
            SubscriptionId=json_data.get("SubscriptionId"),
            TenantId=json_data.get("TenantId"),
            TenantTags=json_data.get("TenantTags"),
            TenantedDeploymentParticipation=json_data.get("TenantedDeploymentParticipation"),
            Tenants=json_data.get("Tenants"),
            Token=json_data.get("Token"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


