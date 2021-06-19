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
    ApiAccessId: Optional[str]
    ApiAccessIp: Optional[str]
    ApiAccessPort: Optional[float]
    ClusterName: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    IdlType: Optional[str]
    NetworkType: Optional[str]
    OldPasswordExpireLast: Optional[float]
    OldPasswordExpireTime: Optional[str]
    Password: Optional[str]
    PasswordStatus: Optional[str]
    SubnetId: Optional[str]
    VpcId: Optional[str]

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
            ApiAccessId=json_data.get("ApiAccessId"),
            ApiAccessIp=json_data.get("ApiAccessIp"),
            ApiAccessPort=json_data.get("ApiAccessPort"),
            ClusterName=json_data.get("ClusterName"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            IdlType=json_data.get("IdlType"),
            NetworkType=json_data.get("NetworkType"),
            OldPasswordExpireLast=json_data.get("OldPasswordExpireLast"),
            OldPasswordExpireTime=json_data.get("OldPasswordExpireTime"),
            Password=json_data.get("Password"),
            PasswordStatus=json_data.get("PasswordStatus"),
            SubnetId=json_data.get("SubnetId"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


