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
    ApplyOnlyAtCronInterval: Optional[bool]
    AssociationId: Optional[str]
    AssociationName: Optional[str]
    AutomationTargetParameterName: Optional[str]
    ComplianceSeverity: Optional[str]
    DocumentVersion: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    MaxConcurrency: Optional[str]
    MaxErrors: Optional[str]
    Name: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    ScheduleExpression: Optional[str]
    OutputLocation: Optional[Sequence["_OutputLocationDefinition"]]
    Targets: Optional[Sequence["_TargetsDefinition"]]

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
            ApplyOnlyAtCronInterval=json_data.get("ApplyOnlyAtCronInterval"),
            AssociationId=json_data.get("AssociationId"),
            AssociationName=json_data.get("AssociationName"),
            AutomationTargetParameterName=json_data.get("AutomationTargetParameterName"),
            ComplianceSeverity=json_data.get("ComplianceSeverity"),
            DocumentVersion=json_data.get("DocumentVersion"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            MaxConcurrency=json_data.get("MaxConcurrency"),
            MaxErrors=json_data.get("MaxErrors"),
            Name=json_data.get("Name"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            ScheduleExpression=json_data.get("ScheduleExpression"),
            OutputLocation=deserialize_list(json_data.get("OutputLocation"), OutputLocationDefinition),
            Targets=deserialize_list(json_data.get("Targets"), TargetsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class OutputLocationDefinition(BaseModel):
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputLocationDefinition = OutputLocationDefinition


@dataclass
class TargetsDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetsDefinition = TargetsDefinition


