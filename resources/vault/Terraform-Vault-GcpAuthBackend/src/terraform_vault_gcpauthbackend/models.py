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
    ClientEmail: Optional[str]
    ClientId: Optional[str]
    Credentials: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Path: Optional[str]
    PrivateKeyId: Optional[str]
    ProjectId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClientEmail=json_data.get("ClientEmail"),
            ClientId=json_data.get("ClientId"),
            Credentials=json_data.get("Credentials"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Path=json_data.get("Path"),
            PrivateKeyId=json_data.get("PrivateKeyId"),
            ProjectId=json_data.get("ProjectId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


