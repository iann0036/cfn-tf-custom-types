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
    ClusterId: Optional[str]
    ClusterName: Optional[str]
    Id: Optional[str]
    NextSnapshot: Optional[str]
    ProjectId: Optional[str]
    ReferenceHourOfDay: Optional[float]
    ReferenceMinuteOfHour: Optional[float]
    RestoreWindowDays: Optional[float]
    UpdateSnapshots: Optional[bool]
    Policies: Optional[Sequence["_PoliciesDefinition"]]

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
            ClusterId=json_data.get("ClusterId"),
            ClusterName=json_data.get("ClusterName"),
            Id=json_data.get("Id"),
            NextSnapshot=json_data.get("NextSnapshot"),
            ProjectId=json_data.get("ProjectId"),
            ReferenceHourOfDay=json_data.get("ReferenceHourOfDay"),
            ReferenceMinuteOfHour=json_data.get("ReferenceMinuteOfHour"),
            RestoreWindowDays=json_data.get("RestoreWindowDays"),
            UpdateSnapshots=json_data.get("UpdateSnapshots"),
            Policies=deserialize_list(json_data.get("Policies"), PoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PoliciesDefinition(BaseModel):
    Id: Optional[str]
    PolicyItem: Optional[Sequence["_PolicyItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            PolicyItem=deserialize_list(json_data.get("PolicyItem"), PolicyItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PoliciesDefinition = PoliciesDefinition


@dataclass
class PolicyItemDefinition(BaseModel):
    FrequencyInterval: Optional[float]
    FrequencyType: Optional[str]
    Id: Optional[str]
    RetentionUnit: Optional[str]
    RetentionValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyItemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyItemDefinition"]:
        if not json_data:
            return None
        return cls(
            FrequencyInterval=json_data.get("FrequencyInterval"),
            FrequencyType=json_data.get("FrequencyType"),
            Id=json_data.get("Id"),
            RetentionUnit=json_data.get("RetentionUnit"),
            RetentionValue=json_data.get("RetentionValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyItemDefinition = PolicyItemDefinition


