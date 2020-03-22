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
    Kind: Optional[str]
    Owner: Optional[str]
    Pattern: Optional[str]
    Repository: Optional[str]
    Users: Optional[Sequence[str]]
    Value: Optional[float]
    Groups: Optional[Sequence["_Groups"]]

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
            Kind=json_data.get("Kind"),
            Owner=json_data.get("Owner"),
            Pattern=json_data.get("Pattern"),
            Repository=json_data.get("Repository"),
            Users=json_data.get("Users"),
            Value=json_data.get("Value"),
            Groups=json_data.get("Groups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Groups:
    Owner: Optional[str]
    Slug: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Groups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Groups"]:
        if not json_data:
            return None
        return cls(
            Owner=json_data.get("Owner"),
            Slug=json_data.get("Slug"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Groups = Groups


