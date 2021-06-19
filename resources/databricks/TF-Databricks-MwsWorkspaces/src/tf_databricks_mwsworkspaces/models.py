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
    AccountId: Optional[str]
    AwsRegion: Optional[str]
    CreationTime: Optional[float]
    CredentialsId: Optional[str]
    CustomerManagedKeyId: Optional[str]
    DeploymentName: Optional[str]
    Id: Optional[str]
    IsNoPublicIpEnabled: Optional[bool]
    ManagedServicesCustomerManagedKeyId: Optional[str]
    NetworkId: Optional[str]
    PricingTier: Optional[str]
    PrivateAccessSettingsId: Optional[str]
    StorageConfigurationId: Optional[str]
    StorageCustomerManagedKeyId: Optional[str]
    WorkspaceId: Optional[float]
    WorkspaceName: Optional[str]
    WorkspaceStatus: Optional[str]
    WorkspaceStatusMessage: Optional[str]
    WorkspaceUrl: Optional[str]
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
            AccountId=json_data.get("AccountId"),
            AwsRegion=json_data.get("AwsRegion"),
            CreationTime=json_data.get("CreationTime"),
            CredentialsId=json_data.get("CredentialsId"),
            CustomerManagedKeyId=json_data.get("CustomerManagedKeyId"),
            DeploymentName=json_data.get("DeploymentName"),
            Id=json_data.get("Id"),
            IsNoPublicIpEnabled=json_data.get("IsNoPublicIpEnabled"),
            ManagedServicesCustomerManagedKeyId=json_data.get("ManagedServicesCustomerManagedKeyId"),
            NetworkId=json_data.get("NetworkId"),
            PricingTier=json_data.get("PricingTier"),
            PrivateAccessSettingsId=json_data.get("PrivateAccessSettingsId"),
            StorageConfigurationId=json_data.get("StorageConfigurationId"),
            StorageCustomerManagedKeyId=json_data.get("StorageCustomerManagedKeyId"),
            WorkspaceId=json_data.get("WorkspaceId"),
            WorkspaceName=json_data.get("WorkspaceName"),
            WorkspaceStatus=json_data.get("WorkspaceStatus"),
            WorkspaceStatusMessage=json_data.get("WorkspaceStatusMessage"),
            WorkspaceUrl=json_data.get("WorkspaceUrl"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


