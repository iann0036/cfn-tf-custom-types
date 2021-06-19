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
    DefaultVersionId: Optional[str]
    DeprecatedStatus: Optional[str]
    Description: Optional[str]
    DocumentationUrl: Optional[str]
    ExecutionRoleArn: Optional[str]
    Id: Optional[str]
    IsDefaultVersion: Optional[bool]
    ProvisioningType: Optional[str]
    Schema: Optional[str]
    SchemaHandlerPackage: Optional[str]
    SourceUrl: Optional[str]
    Type: Optional[str]
    TypeArn: Optional[str]
    TypeName: Optional[str]
    VersionId: Optional[str]
    Visibility: Optional[str]
    LoggingConfig: Optional[Sequence["_LoggingConfigDefinition"]]

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
            DefaultVersionId=json_data.get("DefaultVersionId"),
            DeprecatedStatus=json_data.get("DeprecatedStatus"),
            Description=json_data.get("Description"),
            DocumentationUrl=json_data.get("DocumentationUrl"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Id=json_data.get("Id"),
            IsDefaultVersion=json_data.get("IsDefaultVersion"),
            ProvisioningType=json_data.get("ProvisioningType"),
            Schema=json_data.get("Schema"),
            SchemaHandlerPackage=json_data.get("SchemaHandlerPackage"),
            SourceUrl=json_data.get("SourceUrl"),
            Type=json_data.get("Type"),
            TypeArn=json_data.get("TypeArn"),
            TypeName=json_data.get("TypeName"),
            VersionId=json_data.get("VersionId"),
            Visibility=json_data.get("Visibility"),
            LoggingConfig=deserialize_list(json_data.get("LoggingConfig"), LoggingConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LoggingConfigDefinition(BaseModel):
    LogGroupName: Optional[str]
    LogRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            LogGroupName=json_data.get("LogGroupName"),
            LogRoleArn=json_data.get("LogRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfigDefinition = LoggingConfigDefinition


