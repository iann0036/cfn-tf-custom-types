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
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OutboundTraffic: Optional[bool]
    Routable: Optional[bool]
    ShutdownAtTime: Optional[str]
    ShutdownOnIdle: Optional[float]
    SuspendAtTime: Optional[str]
    SuspendOnIdle: Optional[float]
    Tags: Optional[Sequence[str]]
    TemplateId: Optional[str]
    UserData: Optional[str]
    Label: Optional[Sequence["_Label"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OutboundTraffic=json_data.get("OutboundTraffic"),
            Routable=json_data.get("Routable"),
            ShutdownAtTime=json_data.get("ShutdownAtTime"),
            ShutdownOnIdle=json_data.get("ShutdownOnIdle"),
            SuspendAtTime=json_data.get("SuspendAtTime"),
            SuspendOnIdle=json_data.get("SuspendOnIdle"),
            Tags=json_data.get("Tags"),
            TemplateId=json_data.get("TemplateId"),
            UserData=json_data.get("UserData"),
            Label=json_data.get("Label"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Label:
    Category: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Label"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Label"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Label = Label


