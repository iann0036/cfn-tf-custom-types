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
    AlertConfigurationId: Optional[str]
    Created: Optional[str]
    Enabled: Optional[bool]
    EventType: Optional[str]
    Id: Optional[str]
    MetricThreshold: Optional[Sequence["_MetricThresholdDefinition"]]
    ProjectId: Optional[str]
    Threshold: Optional[Sequence["_ThresholdDefinition"]]
    Updated: Optional[str]
    Matcher: Optional[Sequence["_MatcherDefinition"]]
    Notification: Optional[Sequence["_NotificationDefinition"]]

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
            AlertConfigurationId=json_data.get("AlertConfigurationId"),
            Created=json_data.get("Created"),
            Enabled=json_data.get("Enabled"),
            EventType=json_data.get("EventType"),
            Id=json_data.get("Id"),
            MetricThreshold=deserialize_list(json_data.get("MetricThreshold"), MetricThresholdDefinition),
            ProjectId=json_data.get("ProjectId"),
            Threshold=deserialize_list(json_data.get("Threshold"), ThresholdDefinition),
            Updated=json_data.get("Updated"),
            Matcher=deserialize_list(json_data.get("Matcher"), MatcherDefinition),
            Notification=deserialize_list(json_data.get("Notification"), NotificationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetricThresholdDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricThresholdDefinition = MetricThresholdDefinition


@dataclass
class ThresholdDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThresholdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThresholdDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThresholdDefinition = ThresholdDefinition


@dataclass
class MatcherDefinition(BaseModel):
    FieldName: Optional[str]
    Operator: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatcherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatcherDefinition"]:
        if not json_data:
            return None
        return cls(
            FieldName=json_data.get("FieldName"),
            Operator=json_data.get("Operator"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatcherDefinition = MatcherDefinition


@dataclass
class NotificationDefinition(BaseModel):
    ApiToken: Optional[str]
    ChannelName: Optional[str]
    DatadogApiKey: Optional[str]
    DatadogRegion: Optional[str]
    DelayMin: Optional[float]
    EmailAddress: Optional[str]
    EmailEnabled: Optional[bool]
    FlowName: Optional[str]
    FlowdockApiToken: Optional[str]
    IntervalMin: Optional[float]
    MobileNumber: Optional[str]
    OpsGenieApiKey: Optional[str]
    OpsGenieRegion: Optional[str]
    OrgName: Optional[str]
    Roles: Optional[Sequence[str]]
    ServiceKey: Optional[str]
    SmsEnabled: Optional[bool]
    TeamId: Optional[str]
    TypeName: Optional[str]
    Username: Optional[str]
    VictorOpsApiKey: Optional[str]
    VictorOpsRoutingKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiToken=json_data.get("ApiToken"),
            ChannelName=json_data.get("ChannelName"),
            DatadogApiKey=json_data.get("DatadogApiKey"),
            DatadogRegion=json_data.get("DatadogRegion"),
            DelayMin=json_data.get("DelayMin"),
            EmailAddress=json_data.get("EmailAddress"),
            EmailEnabled=json_data.get("EmailEnabled"),
            FlowName=json_data.get("FlowName"),
            FlowdockApiToken=json_data.get("FlowdockApiToken"),
            IntervalMin=json_data.get("IntervalMin"),
            MobileNumber=json_data.get("MobileNumber"),
            OpsGenieApiKey=json_data.get("OpsGenieApiKey"),
            OpsGenieRegion=json_data.get("OpsGenieRegion"),
            OrgName=json_data.get("OrgName"),
            Roles=json_data.get("Roles"),
            ServiceKey=json_data.get("ServiceKey"),
            SmsEnabled=json_data.get("SmsEnabled"),
            TeamId=json_data.get("TeamId"),
            TypeName=json_data.get("TypeName"),
            Username=json_data.get("Username"),
            VictorOpsApiKey=json_data.get("VictorOpsApiKey"),
            VictorOpsRoutingKey=json_data.get("VictorOpsRoutingKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationDefinition = NotificationDefinition


