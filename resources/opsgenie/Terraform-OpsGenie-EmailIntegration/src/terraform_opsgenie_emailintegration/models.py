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
    EmailUsername: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IgnoreRespondersFromPayload: Optional[bool]
    Name: Optional[str]
    OwnerTeamId: Optional[str]
    SuppressNotifications: Optional[bool]
    Responders: Optional[Sequence["_Responders"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EmailUsername=json_data.get("EmailUsername"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IgnoreRespondersFromPayload=json_data.get("IgnoreRespondersFromPayload"),
            Name=json_data.get("Name"),
            OwnerTeamId=json_data.get("OwnerTeamId"),
            SuppressNotifications=json_data.get("SuppressNotifications"),
            Responders=json_data.get("Responders"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Responders:
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Responders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Responders"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Responders = Responders


