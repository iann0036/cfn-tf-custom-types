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
    Comment: Optional[str]
    DoneDate: Optional[str]
    Function: Optional[str]
    Id: Optional[str]
    Keepers: Optional[Sequence[str]]
    LastUpdate: Optional[str]
    ServiceName: Optional[str]
    StartDate: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Comment=json_data.get("Comment"),
            DoneDate=json_data.get("DoneDate"),
            Function=json_data.get("Function"),
            Id=json_data.get("Id"),
            Keepers=json_data.get("Keepers"),
            LastUpdate=json_data.get("LastUpdate"),
            ServiceName=json_data.get("ServiceName"),
            StartDate=json_data.get("StartDate"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


