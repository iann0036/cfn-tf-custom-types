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
    Id: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ServicebusNamespace: Optional[str]
    SharedAccessPolicyKey: Optional[str]
    SharedAccessPolicyName: Optional[str]
    StreamAnalyticsJobName: Optional[str]
    TopicName: Optional[str]
    Serialization: Optional[Sequence["_Serialization"]]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ServicebusNamespace=json_data.get("ServicebusNamespace"),
            SharedAccessPolicyKey=json_data.get("SharedAccessPolicyKey"),
            SharedAccessPolicyName=json_data.get("SharedAccessPolicyName"),
            StreamAnalyticsJobName=json_data.get("StreamAnalyticsJobName"),
            TopicName=json_data.get("TopicName"),
            Serialization=json_data.get("Serialization"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Serialization:
    Encoding: Optional[str]
    FieldDelimiter: Optional[str]
    Format: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Serialization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Serialization"]:
        if not json_data:
            return None
        return cls(
            Encoding=json_data.get("Encoding"),
            FieldDelimiter=json_data.get("FieldDelimiter"),
            Format=json_data.get("Format"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Serialization = Serialization


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


