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
    AttachApiKeys: Optional[Sequence[str]]
    AttachList: Optional[Sequence["_AttachListDefinition"]]
    CreateTime: Optional[str]
    Id: Optional[str]
    MaxRequestNum: Optional[float]
    MaxRequestNumPreSec: Optional[float]
    ModifyTime: Optional[str]
    UsagePlanDesc: Optional[str]
    UsagePlanName: Optional[str]

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
            AttachApiKeys=json_data.get("AttachApiKeys"),
            AttachList=deserialize_list(json_data.get("AttachList"), AttachListDefinition),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            MaxRequestNum=json_data.get("MaxRequestNum"),
            MaxRequestNumPreSec=json_data.get("MaxRequestNumPreSec"),
            ModifyTime=json_data.get("ModifyTime"),
            UsagePlanDesc=json_data.get("UsagePlanDesc"),
            UsagePlanName=json_data.get("UsagePlanName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttachListDefinition(BaseModel):
    ApiId: Optional[str]
    ApiName: Optional[str]
    CreateTime: Optional[str]
    Environment: Optional[str]
    Method: Optional[str]
    ModifyTime: Optional[str]
    Path: Optional[str]
    ServiceId: Optional[str]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttachListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachListDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiId=json_data.get("ApiId"),
            ApiName=json_data.get("ApiName"),
            CreateTime=json_data.get("CreateTime"),
            Environment=json_data.get("Environment"),
            Method=json_data.get("Method"),
            ModifyTime=json_data.get("ModifyTime"),
            Path=json_data.get("Path"),
            ServiceId=json_data.get("ServiceId"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachListDefinition = AttachListDefinition


