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
    AwsAccessKey: Optional[str]
    AwsBucketId: Optional[str]
    AwsSecretAccess: Optional[str]
    BackupFilePrefix: Optional[str]
    BackupPassphrase: Optional[str]
    Id: Optional[str]
    MaximumBackupsStored: Optional[float]
    Name: Optional[str]
    RemoteDirectory: Optional[str]
    RemoteHostname: Optional[str]
    SaveLocal: Optional[bool]
    SshUserRef: Optional[str]
    TenantRef: Optional[str]
    UploadToRemoteHost: Optional[bool]
    UploadToS3: Optional[bool]
    Uuid: Optional[str]

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
            AwsAccessKey=json_data.get("AwsAccessKey"),
            AwsBucketId=json_data.get("AwsBucketId"),
            AwsSecretAccess=json_data.get("AwsSecretAccess"),
            BackupFilePrefix=json_data.get("BackupFilePrefix"),
            BackupPassphrase=json_data.get("BackupPassphrase"),
            Id=json_data.get("Id"),
            MaximumBackupsStored=json_data.get("MaximumBackupsStored"),
            Name=json_data.get("Name"),
            RemoteDirectory=json_data.get("RemoteDirectory"),
            RemoteHostname=json_data.get("RemoteHostname"),
            SaveLocal=json_data.get("SaveLocal"),
            SshUserRef=json_data.get("SshUserRef"),
            TenantRef=json_data.get("TenantRef"),
            UploadToRemoteHost=json_data.get("UploadToRemoteHost"),
            UploadToS3=json_data.get("UploadToS3"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


