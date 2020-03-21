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
    DisplayName: Optional[str]
    Field: Optional[str]
    Id: Optional[str]
    Match: Optional[str]
    Negate: Optional[bool]
    Pattern: Optional[str]
    RouteId: Optional[str]
    ServiceName: Optional[str]
    SubField: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DisplayName=json_data.get("DisplayName"),
            Field=json_data.get("Field"),
            Id=json_data.get("Id"),
            Match=json_data.get("Match"),
            Negate=json_data.get("Negate"),
            Pattern=json_data.get("Pattern"),
            RouteId=json_data.get("RouteId"),
            ServiceName=json_data.get("ServiceName"),
            SubField=json_data.get("SubField"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


