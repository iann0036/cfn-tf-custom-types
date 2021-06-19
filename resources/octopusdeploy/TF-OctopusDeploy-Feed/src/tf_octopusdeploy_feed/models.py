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
    ApiVersion: Optional[str]
    DeleteUnreleasedPackagesAfterDays: Optional[float]
    DownloadAttempts: Optional[float]
    DownloadRetryBackoffSeconds: Optional[float]
    FeedType: Optional[str]
    FeedUri: Optional[str]
    Id: Optional[str]
    IsEnhancedMode: Optional[bool]
    Name: Optional[str]
    PackageAcquisitionLocationOptions: Optional[Sequence[str]]
    Password: Optional[str]
    Region: Optional[str]
    RegistryPath: Optional[str]
    SecretKey: Optional[str]
    SpaceId: Optional[str]
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
            ApiVersion=json_data.get("ApiVersion"),
            DeleteUnreleasedPackagesAfterDays=json_data.get("DeleteUnreleasedPackagesAfterDays"),
            DownloadAttempts=json_data.get("DownloadAttempts"),
            DownloadRetryBackoffSeconds=json_data.get("DownloadRetryBackoffSeconds"),
            FeedType=json_data.get("FeedType"),
            FeedUri=json_data.get("FeedUri"),
            Id=json_data.get("Id"),
            IsEnhancedMode=json_data.get("IsEnhancedMode"),
            Name=json_data.get("Name"),
            PackageAcquisitionLocationOptions=json_data.get("PackageAcquisitionLocationOptions"),
            Password=json_data.get("Password"),
            Region=json_data.get("Region"),
            RegistryPath=json_data.get("RegistryPath"),
            SecretKey=json_data.get("SecretKey"),
            SpaceId=json_data.get("SpaceId"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


