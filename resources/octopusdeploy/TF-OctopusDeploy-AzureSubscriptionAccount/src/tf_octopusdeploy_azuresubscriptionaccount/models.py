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
    AzureEnvironment: Optional[str]
    Certificate: Optional[str]
    CertificateThumbprint: Optional[str]
    Description: Optional[str]
    Environments: Optional[Sequence[str]]
    Id: Optional[str]
    ManagementEndpoint: Optional[str]
    Name: Optional[str]
    SpaceId: Optional[str]
    StorageEndpointSuffix: Optional[str]
    SubscriptionId: Optional[str]
    TenantTags: Optional[Sequence[str]]
    TenantedDeploymentParticipation: Optional[str]
    Tenants: Optional[Sequence[str]]

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
            AzureEnvironment=json_data.get("AzureEnvironment"),
            Certificate=json_data.get("Certificate"),
            CertificateThumbprint=json_data.get("CertificateThumbprint"),
            Description=json_data.get("Description"),
            Environments=json_data.get("Environments"),
            Id=json_data.get("Id"),
            ManagementEndpoint=json_data.get("ManagementEndpoint"),
            Name=json_data.get("Name"),
            SpaceId=json_data.get("SpaceId"),
            StorageEndpointSuffix=json_data.get("StorageEndpointSuffix"),
            SubscriptionId=json_data.get("SubscriptionId"),
            TenantTags=json_data.get("TenantTags"),
            TenantedDeploymentParticipation=json_data.get("TenantedDeploymentParticipation"),
            Tenants=json_data.get("Tenants"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

