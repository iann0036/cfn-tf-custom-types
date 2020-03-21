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
    Arn: Optional[str]
    CacheClusterEnabled: Optional[bool]
    CacheClusterSize: Optional[str]
    ClientCertificateId: Optional[str]
    DeploymentId: Optional[str]
    Description: Optional[str]
    DocumentationVersion: Optional[str]
    ExecutionArn: Optional[str]
    Id: Optional[str]
    InvokeUrl: Optional[str]
    RestApiId: Optional[str]
    StageName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Variables: Optional[Sequence["_Variables"]]
    XrayTracingEnabled: Optional[bool]
    AccessLogSettings: Optional[Sequence["_AccessLogSettings"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            CacheClusterEnabled=json_data.get("CacheClusterEnabled"),
            CacheClusterSize=json_data.get("CacheClusterSize"),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            DocumentationVersion=json_data.get("DocumentationVersion"),
            ExecutionArn=json_data.get("ExecutionArn"),
            Id=json_data.get("Id"),
            InvokeUrl=json_data.get("InvokeUrl"),
            RestApiId=json_data.get("RestApiId"),
            StageName=json_data.get("StageName"),
            Tags=json_data.get("Tags"),
            Variables=json_data.get("Variables"),
            XrayTracingEnabled=json_data.get("XrayTracingEnabled"),
            AccessLogSettings=json_data.get("AccessLogSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Variables:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Variables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Variables"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Variables = Variables


@dataclass
class AccessLogSettings:
    DestinationArn: Optional[str]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogSettings"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogSettings = AccessLogSettings


