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
    Backend: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[str]
    Vhost: Optional[Sequence["_Vhost"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Backend=json_data.get("Backend"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Vhost=json_data.get("Vhost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Vhost:
    Configure: Optional[str]
    Host: Optional[str]
    Read: Optional[str]
    Write: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Vhost"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Vhost"]:
        if not json_data:
            return None
        return cls(
            Configure=json_data.get("Configure"),
            Host=json_data.get("Host"),
            Read=json_data.get("Read"),
            Write=json_data.get("Write"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Vhost = Vhost


