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
    Database: Optional[str]
    Id: Optional[str]
    ObjectType: Optional[str]
    Privileges: Optional[Sequence[str]]
    Role: Optional[str]
    Schema: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Database=json_data.get("Database"),
            Id=json_data.get("Id"),
            ObjectType=json_data.get("ObjectType"),
            Privileges=json_data.get("Privileges"),
            Role=json_data.get("Role"),
            Schema=json_data.get("Schema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


