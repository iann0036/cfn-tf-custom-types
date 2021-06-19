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
    AutoDisableOldProdPools: Optional[bool]
    Description: Optional[str]
    EvaluationDuration: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Scheme: Optional[str]
    TargetTestTrafficRatio: Optional[float]
    TenantRef: Optional[str]
    TestTrafficRatioRampup: Optional[float]
    Uuid: Optional[str]
    WebhookRef: Optional[str]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            AutoDisableOldProdPools=json_data.get("AutoDisableOldProdPools"),
            Description=json_data.get("Description"),
            EvaluationDuration=json_data.get("EvaluationDuration"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Scheme=json_data.get("Scheme"),
            TargetTestTrafficRatio=json_data.get("TargetTestTrafficRatio"),
            TenantRef=json_data.get("TenantRef"),
            TestTrafficRatioRampup=json_data.get("TestTrafficRatioRampup"),
            Uuid=json_data.get("Uuid"),
            WebhookRef=json_data.get("WebhookRef"),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class RulesDefinition(BaseModel):
    MetricId: Optional[str]
    Operator: Optional[str]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricId=json_data.get("MetricId"),
            Operator=json_data.get("Operator"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


