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
    ApiList: Optional[Sequence["_ApiListDefinition"]]
    CreateTime: Optional[str]
    ExclusiveSetName: Optional[str]
    Id: Optional[str]
    InnerHttpPort: Optional[float]
    InnerHttpsPort: Optional[float]
    InternalSubDomain: Optional[str]
    IpVersion: Optional[str]
    ModifyTime: Optional[str]
    NetType: Optional[Sequence[str]]
    OuterSubDomain: Optional[str]
    PreLimit: Optional[float]
    Protocol: Optional[str]
    ReleaseLimit: Optional[float]
    ServiceDesc: Optional[str]
    ServiceName: Optional[str]
    TestLimit: Optional[float]
    UsagePlanList: Optional[Sequence["_UsagePlanListDefinition"]]

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
            ApiList=deserialize_list(json_data.get("ApiList"), ApiListDefinition),
            CreateTime=json_data.get("CreateTime"),
            ExclusiveSetName=json_data.get("ExclusiveSetName"),
            Id=json_data.get("Id"),
            InnerHttpPort=json_data.get("InnerHttpPort"),
            InnerHttpsPort=json_data.get("InnerHttpsPort"),
            InternalSubDomain=json_data.get("InternalSubDomain"),
            IpVersion=json_data.get("IpVersion"),
            ModifyTime=json_data.get("ModifyTime"),
            NetType=json_data.get("NetType"),
            OuterSubDomain=json_data.get("OuterSubDomain"),
            PreLimit=json_data.get("PreLimit"),
            Protocol=json_data.get("Protocol"),
            ReleaseLimit=json_data.get("ReleaseLimit"),
            ServiceDesc=json_data.get("ServiceDesc"),
            ServiceName=json_data.get("ServiceName"),
            TestLimit=json_data.get("TestLimit"),
            UsagePlanList=deserialize_list(json_data.get("UsagePlanList"), UsagePlanListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApiListDefinition(BaseModel):
    ApiDesc: Optional[str]
    ApiId: Optional[str]
    ApiName: Optional[str]
    Method: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiListDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiDesc=json_data.get("ApiDesc"),
            ApiId=json_data.get("ApiId"),
            ApiName=json_data.get("ApiName"),
            Method=json_data.get("Method"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiListDefinition = ApiListDefinition


@dataclass
class UsagePlanListDefinition(BaseModel):
    ApiId: Optional[str]
    BindType: Optional[str]
    UsagePlanId: Optional[str]
    UsagePlanName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UsagePlanListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UsagePlanListDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiId=json_data.get("ApiId"),
            BindType=json_data.get("BindType"),
            UsagePlanId=json_data.get("UsagePlanId"),
            UsagePlanName=json_data.get("UsagePlanName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UsagePlanListDefinition = UsagePlanListDefinition


