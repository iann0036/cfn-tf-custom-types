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
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    CallTimeout: Optional[float]
    Certificate: Optional[str]
    CloudServerType: Optional[str]
    FortinetoneCloudAuthentication: Optional[str]
    HttpsPort: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    PullAvatars: Optional[str]
    PullSysinfo: Optional[str]
    PullTags: Optional[str]
    PullVulnerabilities: Optional[str]
    SerialNumber: Optional[str]
    Server: Optional[str]
    SourceIp: Optional[str]
    Vdomparam: Optional[str]

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
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            CallTimeout=json_data.get("CallTimeout"),
            Certificate=json_data.get("Certificate"),
            CloudServerType=json_data.get("CloudServerType"),
            FortinetoneCloudAuthentication=json_data.get("FortinetoneCloudAuthentication"),
            HttpsPort=json_data.get("HttpsPort"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PullAvatars=json_data.get("PullAvatars"),
            PullSysinfo=json_data.get("PullSysinfo"),
            PullTags=json_data.get("PullTags"),
            PullVulnerabilities=json_data.get("PullVulnerabilities"),
            SerialNumber=json_data.get("SerialNumber"),
            Server=json_data.get("Server"),
            SourceIp=json_data.get("SourceIp"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


