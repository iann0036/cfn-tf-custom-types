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
    ApiId: Optional[str]
    Arn: Optional[str]
    AutoDeploy: Optional[bool]
    ClientCertificateId: Optional[str]
    DeploymentId: Optional[str]
    Description: Optional[str]
    ExecutionArn: Optional[str]
    Id: Optional[str]
    InvokeUrl: Optional[str]
    Name: Optional[str]
    StageVariables: Optional[Sequence["_StageVariablesDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    AccessLogSettings: Optional[Sequence["_AccessLogSettingsDefinition"]]
    DefaultRouteSettings: Optional[Sequence["_DefaultRouteSettingsDefinition"]]
    RouteSettings: Optional[Sequence["_RouteSettingsDefinition"]]

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
            ApiId=json_data.get("ApiId"),
            Arn=json_data.get("Arn"),
            AutoDeploy=json_data.get("AutoDeploy"),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            ExecutionArn=json_data.get("ExecutionArn"),
            Id=json_data.get("Id"),
            InvokeUrl=json_data.get("InvokeUrl"),
            Name=json_data.get("Name"),
            StageVariables=deserialize_list(json_data.get("StageVariables"), StageVariablesDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            AccessLogSettings=deserialize_list(json_data.get("AccessLogSettings"), AccessLogSettingsDefinition),
            DefaultRouteSettings=deserialize_list(json_data.get("DefaultRouteSettings"), DefaultRouteSettingsDefinition),
            RouteSettings=deserialize_list(json_data.get("RouteSettings"), RouteSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StageVariablesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StageVariablesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageVariablesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageVariablesDefinition = StageVariablesDefinition


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
class AccessLogSettingsDefinition(BaseModel):
    DestinationArn: Optional[str]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogSettingsDefinition = AccessLogSettingsDefinition


@dataclass
class DefaultRouteSettingsDefinition(BaseModel):
    DataTraceEnabled: Optional[bool]
    DetailedMetricsEnabled: Optional[bool]
    LoggingLevel: Optional[str]
    ThrottlingBurstLimit: Optional[float]
    ThrottlingRateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultRouteSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultRouteSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DataTraceEnabled=json_data.get("DataTraceEnabled"),
            DetailedMetricsEnabled=json_data.get("DetailedMetricsEnabled"),
            LoggingLevel=json_data.get("LoggingLevel"),
            ThrottlingBurstLimit=json_data.get("ThrottlingBurstLimit"),
            ThrottlingRateLimit=json_data.get("ThrottlingRateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultRouteSettingsDefinition = DefaultRouteSettingsDefinition


@dataclass
class RouteSettingsDefinition(BaseModel):
    DataTraceEnabled: Optional[bool]
    DetailedMetricsEnabled: Optional[bool]
    LoggingLevel: Optional[str]
    RouteKey: Optional[str]
    ThrottlingBurstLimit: Optional[float]
    ThrottlingRateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RouteSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DataTraceEnabled=json_data.get("DataTraceEnabled"),
            DetailedMetricsEnabled=json_data.get("DetailedMetricsEnabled"),
            LoggingLevel=json_data.get("LoggingLevel"),
            RouteKey=json_data.get("RouteKey"),
            ThrottlingBurstLimit=json_data.get("ThrottlingBurstLimit"),
            ThrottlingRateLimit=json_data.get("ThrottlingRateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteSettingsDefinition = RouteSettingsDefinition


