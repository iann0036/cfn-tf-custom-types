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
    ApiserverUrl: Optional[str]
    Authorization: Optional[Sequence["_AuthorizationDefinition"]]
    AuthorizationType: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    ProjectId: Optional[str]
    ServiceEndpointName: Optional[str]
    AzureSubscription: Optional[Sequence["_AzureSubscriptionDefinition"]]
    Kubeconfig: Optional[Sequence["_KubeconfigDefinition"]]
    ServiceAccount: Optional[Sequence["_ServiceAccountDefinition"]]
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
            ApiserverUrl=json_data.get("ApiserverUrl"),
            Authorization=deserialize_list(json_data.get("Authorization"), AuthorizationDefinition),
            AuthorizationType=json_data.get("AuthorizationType"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ProjectId=json_data.get("ProjectId"),
            ServiceEndpointName=json_data.get("ServiceEndpointName"),
            AzureSubscription=deserialize_list(json_data.get("AzureSubscription"), AzureSubscriptionDefinition),
            Kubeconfig=deserialize_list(json_data.get("Kubeconfig"), KubeconfigDefinition),
            ServiceAccount=deserialize_list(json_data.get("ServiceAccount"), ServiceAccountDefinition),
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
class AzureSubscriptionDefinition(BaseModel):
    AzureEnvironment: Optional[str]
    ClusterAdmin: Optional[bool]
    ClusterName: Optional[str]
    Namespace: Optional[str]
    ResourcegroupId: Optional[str]
    SubscriptionId: Optional[str]
    SubscriptionName: Optional[str]
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureSubscriptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureSubscriptionDefinition"]:
        if not json_data:
            return None
        return cls(
            AzureEnvironment=json_data.get("AzureEnvironment"),
            ClusterAdmin=json_data.get("ClusterAdmin"),
            ClusterName=json_data.get("ClusterName"),
            Namespace=json_data.get("Namespace"),
            ResourcegroupId=json_data.get("ResourcegroupId"),
            SubscriptionId=json_data.get("SubscriptionId"),
            SubscriptionName=json_data.get("SubscriptionName"),
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureSubscriptionDefinition = AzureSubscriptionDefinition


@dataclass
class KubeconfigDefinition(BaseModel):
    AcceptUntrustedCerts: Optional[bool]
    ClusterContext: Optional[str]
    KubeConfig: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeconfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeconfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AcceptUntrustedCerts=json_data.get("AcceptUntrustedCerts"),
            ClusterContext=json_data.get("ClusterContext"),
            KubeConfig=json_data.get("KubeConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeconfigDefinition = KubeconfigDefinition


@dataclass
class ServiceAccountDefinition(BaseModel):
    CaCert: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            CaCert=json_data.get("CaCert"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceAccountDefinition = ServiceAccountDefinition


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


