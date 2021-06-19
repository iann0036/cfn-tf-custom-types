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
    Actions: Optional[Sequence["_ActionsDefinition"]]
    ApprovalDeadline: Optional[str]
    ApprovalExpire: Optional[str]
    Approver: Optional[bool]
    ApproverId: Optional[str]
    ApproverType: Optional[str]
    Descriptions: Optional[Sequence["_DescriptionsDefinition"]]
    ExternalRequestId: Optional[str]
    Id: Optional[str]
    RegisteredTime: Optional[str]
    RequestId: Optional[str]
    RequestUser: Optional[bool]
    RequestUserId: Optional[str]
    Service: Optional[str]
    Status: Optional[str]
    UpdatedTime: Optional[str]

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
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition),
            ApprovalDeadline=json_data.get("ApprovalDeadline"),
            ApprovalExpire=json_data.get("ApprovalExpire"),
            Approver=json_data.get("Approver"),
            ApproverId=json_data.get("ApproverId"),
            ApproverType=json_data.get("ApproverType"),
            Descriptions=deserialize_list(json_data.get("Descriptions"), DescriptionsDefinition),
            ExternalRequestId=json_data.get("ExternalRequestId"),
            Id=json_data.get("Id"),
            RegisteredTime=json_data.get("RegisteredTime"),
            RequestId=json_data.get("RequestId"),
            RequestUser=json_data.get("RequestUser"),
            RequestUserId=json_data.get("RequestUserId"),
            Service=json_data.get("Service"),
            Status=json_data.get("Status"),
            UpdatedTime=json_data.get("UpdatedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionsDefinition(BaseModel):
    ApiPath: Optional[str]
    Body: Optional[str]
    Method: Optional[str]
    Region: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiPath=json_data.get("ApiPath"),
            Body=json_data.get("Body"),
            Method=json_data.get("Method"),
            Region=json_data.get("Region"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class DescriptionsDefinition(BaseModel):
    Lang: Optional[str]
    Text: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DescriptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DescriptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Lang=json_data.get("Lang"),
            Text=json_data.get("Text"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DescriptionsDefinition = DescriptionsDefinition


