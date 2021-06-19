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
    AuthMethod: Optional[str]
    CustomCloudwatchNamespaces: Optional[Sequence[str]]
    EnableAwsUsage: Optional[bool]
    EnableCheckLargeVolume: Optional[bool]
    Enabled: Optional[bool]
    ExternalId: Optional[str]
    Id: Optional[str]
    ImportCloudWatch: Optional[bool]
    IntegrationId: Optional[str]
    Key: Optional[str]
    Name: Optional[str]
    NamedToken: Optional[str]
    PollRate: Optional[float]
    Regions: Optional[Sequence[str]]
    RoleArn: Optional[str]
    Services: Optional[Sequence[str]]
    Token: Optional[str]
    UseGetMetricDataMethod: Optional[bool]
    CustomNamespaceSyncRule: Optional[Sequence["_CustomNamespaceSyncRuleDefinition"]]
    NamespaceSyncRule: Optional[Sequence["_NamespaceSyncRuleDefinition"]]

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
            AuthMethod=json_data.get("AuthMethod"),
            CustomCloudwatchNamespaces=json_data.get("CustomCloudwatchNamespaces"),
            EnableAwsUsage=json_data.get("EnableAwsUsage"),
            EnableCheckLargeVolume=json_data.get("EnableCheckLargeVolume"),
            Enabled=json_data.get("Enabled"),
            ExternalId=json_data.get("ExternalId"),
            Id=json_data.get("Id"),
            ImportCloudWatch=json_data.get("ImportCloudWatch"),
            IntegrationId=json_data.get("IntegrationId"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            NamedToken=json_data.get("NamedToken"),
            PollRate=json_data.get("PollRate"),
            Regions=json_data.get("Regions"),
            RoleArn=json_data.get("RoleArn"),
            Services=json_data.get("Services"),
            Token=json_data.get("Token"),
            UseGetMetricDataMethod=json_data.get("UseGetMetricDataMethod"),
            CustomNamespaceSyncRule=deserialize_list(json_data.get("CustomNamespaceSyncRule"), CustomNamespaceSyncRuleDefinition),
            NamespaceSyncRule=deserialize_list(json_data.get("NamespaceSyncRule"), NamespaceSyncRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomNamespaceSyncRuleDefinition(BaseModel):
    DefaultAction: Optional[str]
    FilterAction: Optional[str]
    FilterSource: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomNamespaceSyncRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomNamespaceSyncRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultAction=json_data.get("DefaultAction"),
            FilterAction=json_data.get("FilterAction"),
            FilterSource=json_data.get("FilterSource"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomNamespaceSyncRuleDefinition = CustomNamespaceSyncRuleDefinition


@dataclass
class NamespaceSyncRuleDefinition(BaseModel):
    DefaultAction: Optional[str]
    FilterAction: Optional[str]
    FilterSource: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NamespaceSyncRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamespaceSyncRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultAction=json_data.get("DefaultAction"),
            FilterAction=json_data.get("FilterAction"),
            FilterSource=json_data.get("FilterSource"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamespaceSyncRuleDefinition = NamespaceSyncRuleDefinition


