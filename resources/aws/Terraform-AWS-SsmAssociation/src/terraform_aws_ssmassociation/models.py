# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
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
    Parameters: Optional[Sequence["_Parameters"]]
    ScheduleExpression: Optional[str]
    OutputLocation: Optional[Sequence["_OutputLocation"]]
    Targets: Optional[Sequence["_Targets"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
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
            Parameters=json_data.get("Parameters"),
            ScheduleExpression=json_data.get("ScheduleExpression"),
            OutputLocation=json_data.get("OutputLocation"),
            Targets=json_data.get("Targets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Parameters:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class OutputLocation:
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputLocation"]:
        if not json_data:
            return None
        return cls(
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputLocation = OutputLocation


@dataclass
class Targets:
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Targets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Targets"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Targets = Targets


