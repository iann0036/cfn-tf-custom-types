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
    Audible: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    Groups: Optional[Sequence["_GroupsDefinition"]]

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
            Audible=json_data.get("Audible"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            Groups=deserialize_list(json_data.get("Groups"), GroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class GroupsDefinition(BaseModel):
    AdminAuthFailureThreshold: Optional[float]
    AdminAuthLockoutThreshold: Optional[float]
    DecryptionFailureThreshold: Optional[float]
    EncryptionFailureThreshold: Optional[float]
    FwPolicyId: Optional[float]
    FwPolicyIdThreshold: Optional[float]
    Id: Optional[float]
    LogFullWarningThreshold: Optional[float]
    Period: Optional[float]
    ReplayAttemptThreshold: Optional[float]
    SelfTestFailureThreshold: Optional[float]
    UserAuthFailureThreshold: Optional[float]
    UserAuthLockoutThreshold: Optional[float]
    FwPolicyViolations: Optional[Sequence["_FwPolicyViolationsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdminAuthFailureThreshold=json_data.get("AdminAuthFailureThreshold"),
            AdminAuthLockoutThreshold=json_data.get("AdminAuthLockoutThreshold"),
            DecryptionFailureThreshold=json_data.get("DecryptionFailureThreshold"),
            EncryptionFailureThreshold=json_data.get("EncryptionFailureThreshold"),
            FwPolicyId=json_data.get("FwPolicyId"),
            FwPolicyIdThreshold=json_data.get("FwPolicyIdThreshold"),
            Id=json_data.get("Id"),
            LogFullWarningThreshold=json_data.get("LogFullWarningThreshold"),
            Period=json_data.get("Period"),
            ReplayAttemptThreshold=json_data.get("ReplayAttemptThreshold"),
            SelfTestFailureThreshold=json_data.get("SelfTestFailureThreshold"),
            UserAuthFailureThreshold=json_data.get("UserAuthFailureThreshold"),
            UserAuthLockoutThreshold=json_data.get("UserAuthLockoutThreshold"),
            FwPolicyViolations=deserialize_list(json_data.get("FwPolicyViolations"), FwPolicyViolationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupsDefinition = GroupsDefinition


@dataclass
class FwPolicyViolationsDefinition(BaseModel):
    DstIp: Optional[str]
    DstPort: Optional[float]
    Id: Optional[float]
    SrcIp: Optional[str]
    SrcPort: Optional[float]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FwPolicyViolationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FwPolicyViolationsDefinition"]:
        if not json_data:
            return None
        return cls(
            DstIp=json_data.get("DstIp"),
            DstPort=json_data.get("DstPort"),
            Id=json_data.get("Id"),
            SrcIp=json_data.get("SrcIp"),
            SrcPort=json_data.get("SrcPort"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FwPolicyViolationsDefinition = FwPolicyViolationsDefinition


