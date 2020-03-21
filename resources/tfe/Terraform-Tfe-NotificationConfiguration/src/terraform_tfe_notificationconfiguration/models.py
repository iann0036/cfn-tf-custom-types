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
    DestinationType: Optional[str]
    Enabled: Optional[bool]
    Name: Optional[str]
    Token: Optional[str]
    Triggers: Optional[Sequence[str]]
    Url: Optional[str]
    WorkspaceExternalId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DestinationType=json_data.get("DestinationType"),
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Token=json_data.get("Token"),
            Triggers=json_data.get("Triggers"),
            Url=json_data.get("Url"),
            WorkspaceExternalId=json_data.get("WorkspaceExternalId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


