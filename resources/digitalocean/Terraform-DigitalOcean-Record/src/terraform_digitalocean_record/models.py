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
    Domain: Optional[str]
    Flags: Optional[float]
    Fqdn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Port: Optional[float]
    Priority: Optional[float]
    Tag: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]
    Value: Optional[str]
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
            Domain=json_data.get("Domain"),
            Flags=json_data.get("Flags"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            Tag=json_data.get("Tag"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


