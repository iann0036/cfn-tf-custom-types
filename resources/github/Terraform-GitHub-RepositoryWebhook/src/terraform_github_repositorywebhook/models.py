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
    Active: Optional[bool]
    Etag: Optional[str]
    Events: Optional[Sequence[str]]
    Id: Optional[str]
    Name: Optional[str]
    Repository: Optional[str]
    Url: Optional[str]
    Configuration: Optional[Sequence["_Configuration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Active=json_data.get("Active"),
            Etag=json_data.get("Etag"),
            Events=json_data.get("Events"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Repository=json_data.get("Repository"),
            Url=json_data.get("Url"),
            Configuration=json_data.get("Configuration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Configuration:
    ContentType: Optional[str]
    InsecureSsl: Optional[bool]
    Secret: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configuration"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            InsecureSsl=json_data.get("InsecureSsl"),
            Secret=json_data.get("Secret"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configuration = Configuration


