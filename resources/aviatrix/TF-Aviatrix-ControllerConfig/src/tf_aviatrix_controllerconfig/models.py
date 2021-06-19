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
    AwsGuardDutyScanningInterval: Optional[float]
    BackupAccountName: Optional[str]
    BackupBucketName: Optional[str]
    BackupCloudType: Optional[float]
    BackupConfiguration: Optional[bool]
    BackupContainerName: Optional[str]
    BackupRegion: Optional[str]
    BackupStorageName: Optional[str]
    CaCertificateFilePath: Optional[str]
    EnableVpcDnsServer: Optional[bool]
    FqdnExceptionRule: Optional[bool]
    HttpAccess: Optional[bool]
    Id: Optional[str]
    MultipleBackups: Optional[bool]
    SecurityGroupManagement: Optional[bool]
    ServerPrivateKeyFilePath: Optional[str]
    ServerPublicCertificateFilePath: Optional[str]
    SgManagementAccountName: Optional[str]
    TargetVersion: Optional[str]
    Version: Optional[str]

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
            AwsGuardDutyScanningInterval=json_data.get("AwsGuardDutyScanningInterval"),
            BackupAccountName=json_data.get("BackupAccountName"),
            BackupBucketName=json_data.get("BackupBucketName"),
            BackupCloudType=json_data.get("BackupCloudType"),
            BackupConfiguration=json_data.get("BackupConfiguration"),
            BackupContainerName=json_data.get("BackupContainerName"),
            BackupRegion=json_data.get("BackupRegion"),
            BackupStorageName=json_data.get("BackupStorageName"),
            CaCertificateFilePath=json_data.get("CaCertificateFilePath"),
            EnableVpcDnsServer=json_data.get("EnableVpcDnsServer"),
            FqdnExceptionRule=json_data.get("FqdnExceptionRule"),
            HttpAccess=json_data.get("HttpAccess"),
            Id=json_data.get("Id"),
            MultipleBackups=json_data.get("MultipleBackups"),
            SecurityGroupManagement=json_data.get("SecurityGroupManagement"),
            ServerPrivateKeyFilePath=json_data.get("ServerPrivateKeyFilePath"),
            ServerPublicCertificateFilePath=json_data.get("ServerPublicCertificateFilePath"),
            SgManagementAccountName=json_data.get("SgManagementAccountName"),
            TargetVersion=json_data.get("TargetVersion"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


