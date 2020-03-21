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
    DomainId: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    Priority: Optional[float]
    Protocol: Optional[str]
    RecordType: Optional[str]
    Service: Optional[str]
    Tag: Optional[str]
    Target: Optional[str]
    TtlSec: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DomainId=json_data.get("DomainId"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            Protocol=json_data.get("Protocol"),
            RecordType=json_data.get("RecordType"),
            Service=json_data.get("Service"),
            Tag=json_data.get("Tag"),
            Target=json_data.get("Target"),
            TtlSec=json_data.get("TtlSec"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


