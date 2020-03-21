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
    CreationDate: Optional[str]
    DefaultKeyFlag: Optional[str]
    DomainId: Optional[str]
    ExpirationTime: Optional[str]
    IsEnabled: Optional[bool]
    KeyAlias: Optional[str]
    KeyDescription: Optional[str]
    Origin: Optional[str]
    PendingDays: Optional[str]
    Realm: Optional[str]
    ScheduledDeletionDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreationDate=json_data.get("CreationDate"),
            DefaultKeyFlag=json_data.get("DefaultKeyFlag"),
            DomainId=json_data.get("DomainId"),
            ExpirationTime=json_data.get("ExpirationTime"),
            IsEnabled=json_data.get("IsEnabled"),
            KeyAlias=json_data.get("KeyAlias"),
            KeyDescription=json_data.get("KeyDescription"),
            Origin=json_data.get("Origin"),
            PendingDays=json_data.get("PendingDays"),
            Realm=json_data.get("Realm"),
            ScheduledDeletionDate=json_data.get("ScheduledDeletionDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


