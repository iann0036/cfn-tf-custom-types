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
    Config: Optional[str]
    ConfigMns: Optional[str]
    Function: Optional[str]
    LastModified: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Role: Optional[str]
    Service: Optional[str]
    SourceArn: Optional[str]
    TriggerId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Config=json_data.get("Config"),
            ConfigMns=json_data.get("ConfigMns"),
            Function=json_data.get("Function"),
            LastModified=json_data.get("LastModified"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Role=json_data.get("Role"),
            Service=json_data.get("Service"),
            SourceArn=json_data.get("SourceArn"),
            TriggerId=json_data.get("TriggerId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


