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
    Arn: Optional[str]
    AutomaticRotation: Optional[str]
    CreationDate: Optional[str]
    Creator: Optional[str]
    DeleteDate: Optional[str]
    DeletionWindowInDays: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    IsEnabled: Optional[bool]
    KeySpec: Optional[str]
    KeyState: Optional[str]
    KeyUsage: Optional[str]
    LastRotationDate: Optional[str]
    MaterialExpireTime: Optional[str]
    NextRotationDate: Optional[str]
    Origin: Optional[str]
    PendingWindowInDays: Optional[float]
    PrimaryKeyVersion: Optional[str]
    ProtectionLevel: Optional[str]
    RotationInterval: Optional[str]
    Status: Optional[str]

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
            Arn=json_data.get("Arn"),
            AutomaticRotation=json_data.get("AutomaticRotation"),
            CreationDate=json_data.get("CreationDate"),
            Creator=json_data.get("Creator"),
            DeleteDate=json_data.get("DeleteDate"),
            DeletionWindowInDays=json_data.get("DeletionWindowInDays"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IsEnabled=json_data.get("IsEnabled"),
            KeySpec=json_data.get("KeySpec"),
            KeyState=json_data.get("KeyState"),
            KeyUsage=json_data.get("KeyUsage"),
            LastRotationDate=json_data.get("LastRotationDate"),
            MaterialExpireTime=json_data.get("MaterialExpireTime"),
            NextRotationDate=json_data.get("NextRotationDate"),
            Origin=json_data.get("Origin"),
            PendingWindowInDays=json_data.get("PendingWindowInDays"),
            PrimaryKeyVersion=json_data.get("PrimaryKeyVersion"),
            ProtectionLevel=json_data.get("ProtectionLevel"),
            RotationInterval=json_data.get("RotationInterval"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


