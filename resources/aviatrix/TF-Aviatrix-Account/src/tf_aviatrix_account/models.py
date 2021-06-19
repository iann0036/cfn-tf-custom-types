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
    AccountName: Optional[str]
    AlicloudAccessKey: Optional[str]
    AlicloudAccountId: Optional[str]
    AlicloudSecretKey: Optional[str]
    ArmApplicationId: Optional[str]
    ArmApplicationKey: Optional[str]
    ArmDirectoryId: Optional[str]
    ArmSubscriptionId: Optional[str]
    AuditAccount: Optional[bool]
    AwsAccessKey: Optional[str]
    AwsAccountNumber: Optional[str]
    AwsGatewayRoleApp: Optional[str]
    AwsGatewayRoleEc2: Optional[str]
    AwsIam: Optional[bool]
    AwsRoleApp: Optional[str]
    AwsRoleEc2: Optional[str]
    AwsSecretKey: Optional[str]
    AwschinaAccessKey: Optional[str]
    AwschinaAccountNumber: Optional[str]
    AwschinaIam: Optional[bool]
    AwschinaRoleApp: Optional[str]
    AwschinaRoleEc2: Optional[str]
    AwschinaSecretKey: Optional[str]
    AwsgovAccessKey: Optional[str]
    AwsgovAccountNumber: Optional[str]
    AwsgovIam: Optional[bool]
    AwsgovRoleApp: Optional[str]
    AwsgovRoleEc2: Optional[str]
    AwsgovSecretKey: Optional[str]
    AzurechinaApplicationId: Optional[str]
    AzurechinaApplicationKey: Optional[str]
    AzurechinaDirectoryId: Optional[str]
    AzurechinaSubscriptionId: Optional[str]
    AzuregovApplicationId: Optional[str]
    AzuregovApplicationKey: Optional[str]
    AzuregovDirectoryId: Optional[str]
    AzuregovSubscriptionId: Optional[str]
    CloudType: Optional[float]
    GcloudProjectCredentialsFilepath: Optional[str]
    GcloudProjectId: Optional[str]
    Id: Optional[str]
    OciApiPrivateKeyFilepath: Optional[str]
    OciCompartmentId: Optional[str]
    OciTenancyId: Optional[str]
    OciUserId: Optional[str]

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
            AccountName=json_data.get("AccountName"),
            AlicloudAccessKey=json_data.get("AlicloudAccessKey"),
            AlicloudAccountId=json_data.get("AlicloudAccountId"),
            AlicloudSecretKey=json_data.get("AlicloudSecretKey"),
            ArmApplicationId=json_data.get("ArmApplicationId"),
            ArmApplicationKey=json_data.get("ArmApplicationKey"),
            ArmDirectoryId=json_data.get("ArmDirectoryId"),
            ArmSubscriptionId=json_data.get("ArmSubscriptionId"),
            AuditAccount=json_data.get("AuditAccount"),
            AwsAccessKey=json_data.get("AwsAccessKey"),
            AwsAccountNumber=json_data.get("AwsAccountNumber"),
            AwsGatewayRoleApp=json_data.get("AwsGatewayRoleApp"),
            AwsGatewayRoleEc2=json_data.get("AwsGatewayRoleEc2"),
            AwsIam=json_data.get("AwsIam"),
            AwsRoleApp=json_data.get("AwsRoleApp"),
            AwsRoleEc2=json_data.get("AwsRoleEc2"),
            AwsSecretKey=json_data.get("AwsSecretKey"),
            AwschinaAccessKey=json_data.get("AwschinaAccessKey"),
            AwschinaAccountNumber=json_data.get("AwschinaAccountNumber"),
            AwschinaIam=json_data.get("AwschinaIam"),
            AwschinaRoleApp=json_data.get("AwschinaRoleApp"),
            AwschinaRoleEc2=json_data.get("AwschinaRoleEc2"),
            AwschinaSecretKey=json_data.get("AwschinaSecretKey"),
            AwsgovAccessKey=json_data.get("AwsgovAccessKey"),
            AwsgovAccountNumber=json_data.get("AwsgovAccountNumber"),
            AwsgovIam=json_data.get("AwsgovIam"),
            AwsgovRoleApp=json_data.get("AwsgovRoleApp"),
            AwsgovRoleEc2=json_data.get("AwsgovRoleEc2"),
            AwsgovSecretKey=json_data.get("AwsgovSecretKey"),
            AzurechinaApplicationId=json_data.get("AzurechinaApplicationId"),
            AzurechinaApplicationKey=json_data.get("AzurechinaApplicationKey"),
            AzurechinaDirectoryId=json_data.get("AzurechinaDirectoryId"),
            AzurechinaSubscriptionId=json_data.get("AzurechinaSubscriptionId"),
            AzuregovApplicationId=json_data.get("AzuregovApplicationId"),
            AzuregovApplicationKey=json_data.get("AzuregovApplicationKey"),
            AzuregovDirectoryId=json_data.get("AzuregovDirectoryId"),
            AzuregovSubscriptionId=json_data.get("AzuregovSubscriptionId"),
            CloudType=json_data.get("CloudType"),
            GcloudProjectCredentialsFilepath=json_data.get("GcloudProjectCredentialsFilepath"),
            GcloudProjectId=json_data.get("GcloudProjectId"),
            Id=json_data.get("Id"),
            OciApiPrivateKeyFilepath=json_data.get("OciApiPrivateKeyFilepath"),
            OciCompartmentId=json_data.get("OciCompartmentId"),
            OciTenancyId=json_data.get("OciTenancyId"),
            OciUserId=json_data.get("OciUserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


