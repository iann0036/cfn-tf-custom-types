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
    Capabilities: Optional[Sequence[str]]
    CreationTime: Optional[str]
    Description: Optional[str]
    DisableRollback: Optional[bool]
    EnvironmentOpts: Optional[Sequence["_EnvironmentOpts"]]
    Name: Optional[str]
    NotificationTopics: Optional[Sequence[str]]
    Parameters: Optional[Sequence["_Parameters"]]
    Region: Optional[str]
    Status: Optional[str]
    StatusReason: Optional[str]
    Tags: Optional[Sequence[str]]
    TemplateDescription: Optional[str]
    TemplateOpts: Optional[Sequence["_TemplateOpts"]]
    Timeout: Optional[float]
    UpdatedTime: Optional[str]
    Outputs: Optional[Sequence["_Outputs"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Capabilities=json_data.get("Capabilities"),
            CreationTime=json_data.get("CreationTime"),
            Description=json_data.get("Description"),
            DisableRollback=json_data.get("DisableRollback"),
            EnvironmentOpts=json_data.get("EnvironmentOpts"),
            Name=json_data.get("Name"),
            NotificationTopics=json_data.get("NotificationTopics"),
            Parameters=json_data.get("Parameters"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            StatusReason=json_data.get("StatusReason"),
            Tags=json_data.get("Tags"),
            TemplateDescription=json_data.get("TemplateDescription"),
            TemplateOpts=json_data.get("TemplateOpts"),
            Timeout=json_data.get("Timeout"),
            UpdatedTime=json_data.get("UpdatedTime"),
            Outputs=json_data.get("Outputs"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvironmentOpts:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentOpts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentOpts"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentOpts = EnvironmentOpts


@dataclass
class Parameters:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class TemplateOpts:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateOpts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateOpts"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateOpts = TemplateOpts


@dataclass
class Outputs:
    Description: Optional[str]
    OutputKey: Optional[str]
    OutputValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Outputs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Outputs"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            OutputKey=json_data.get("OutputKey"),
            OutputValue=json_data.get("OutputValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Outputs = Outputs


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


