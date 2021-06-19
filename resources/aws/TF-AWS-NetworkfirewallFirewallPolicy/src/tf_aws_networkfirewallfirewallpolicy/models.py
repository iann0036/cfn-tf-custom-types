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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UpdateToken: Optional[str]
    FirewallPolicy: Optional[Sequence["_FirewallPolicyDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UpdateToken=json_data.get("UpdateToken"),
            FirewallPolicy=deserialize_list(json_data.get("FirewallPolicy"), FirewallPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class FirewallPolicyDefinition(BaseModel):
    StatelessDefaultActions: Optional[Sequence[str]]
    StatelessFragmentDefaultActions: Optional[Sequence[str]]
    StatefulRuleGroupReference: Optional[Sequence["_StatefulRuleGroupReferenceDefinition"]]
    StatelessCustomAction: Optional[Sequence["_StatelessCustomActionDefinition"]]
    StatelessRuleGroupReference: Optional[Sequence["_StatelessRuleGroupReferenceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            StatelessDefaultActions=json_data.get("StatelessDefaultActions"),
            StatelessFragmentDefaultActions=json_data.get("StatelessFragmentDefaultActions"),
            StatefulRuleGroupReference=deserialize_list(json_data.get("StatefulRuleGroupReference"), StatefulRuleGroupReferenceDefinition),
            StatelessCustomAction=deserialize_list(json_data.get("StatelessCustomAction"), StatelessCustomActionDefinition),
            StatelessRuleGroupReference=deserialize_list(json_data.get("StatelessRuleGroupReference"), StatelessRuleGroupReferenceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallPolicyDefinition = FirewallPolicyDefinition


@dataclass
class StatefulRuleGroupReferenceDefinition(BaseModel):
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulRuleGroupReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulRuleGroupReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulRuleGroupReferenceDefinition = StatefulRuleGroupReferenceDefinition


@dataclass
class StatelessCustomActionDefinition(BaseModel):
    ActionName: Optional[str]
    ActionDefinition: Optional[Sequence["_ActionDefinitionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatelessCustomActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatelessCustomActionDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionName=json_data.get("ActionName"),
            ActionDefinition=deserialize_list(json_data.get("ActionDefinition"), ActionDefinitionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatelessCustomActionDefinition = StatelessCustomActionDefinition


@dataclass
class ActionDefinitionDefinition(BaseModel):
    PublishMetricAction: Optional[Sequence["_PublishMetricActionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinitionDefinition"]:
        if not json_data:
            return None
        return cls(
            PublishMetricAction=deserialize_list(json_data.get("PublishMetricAction"), PublishMetricActionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinitionDefinition = ActionDefinitionDefinition


@dataclass
class PublishMetricActionDefinition(BaseModel):
    Dimension: Optional[Sequence["_DimensionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublishMetricActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishMetricActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Dimension=deserialize_list(json_data.get("Dimension"), DimensionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishMetricActionDefinition = PublishMetricActionDefinition


@dataclass
class DimensionDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionDefinition = DimensionDefinition


@dataclass
class StatelessRuleGroupReferenceDefinition(BaseModel):
    Priority: Optional[float]
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatelessRuleGroupReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatelessRuleGroupReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatelessRuleGroupReferenceDefinition = StatelessRuleGroupReferenceDefinition


