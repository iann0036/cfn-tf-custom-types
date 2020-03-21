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
    Account: Optional[str]
    Check: Optional[str]
    Id: Optional[str]
    Notes: Optional[str]
    RuleSet: Optional[str]
    Severities: Optional[Sequence[str]]
    Start: Optional[str]
    Stop: Optional[str]
    Tags: Optional[Sequence[str]]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Account=json_data.get("Account"),
            Check=json_data.get("Check"),
            Id=json_data.get("Id"),
            Notes=json_data.get("Notes"),
            RuleSet=json_data.get("RuleSet"),
            Severities=json_data.get("Severities"),
            Start=json_data.get("Start"),
            Stop=json_data.get("Stop"),
            Tags=json_data.get("Tags"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


