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
    Ip: Optional[str]
    Name: Optional[str]
    ParentPool: Optional[str]
    Permanent: Optional[bool]
    Tags: Optional[Sequence[str]]
    Used: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Ip=json_data.get("Ip"),
            Name=json_data.get("Name"),
            ParentPool=json_data.get("ParentPool"),
            Permanent=json_data.get("Permanent"),
            Tags=json_data.get("Tags"),
            Used=json_data.get("Used"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


