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
    App: Optional[str]
    Buildpacks: Optional[Sequence[str]]
    Id: Optional[str]
    LocalChecksum: Optional[str]
    OutputStreamUrl: Optional[str]
    ReleaseId: Optional[str]
    SlugId: Optional[str]
    Source: Optional[Sequence["_Source"]]
    Stack: Optional[str]
    Status: Optional[str]
    User: Optional[Sequence["_User"]]
    Uuid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            App=json_data.get("App"),
            Buildpacks=json_data.get("Buildpacks"),
            Id=json_data.get("Id"),
            LocalChecksum=json_data.get("LocalChecksum"),
            OutputStreamUrl=json_data.get("OutputStreamUrl"),
            ReleaseId=json_data.get("ReleaseId"),
            SlugId=json_data.get("SlugId"),
            Source=json_data.get("Source"),
            Stack=json_data.get("Stack"),
            Status=json_data.get("Status"),
            User=json_data.get("User"),
            Uuid=json_data.get("Uuid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Source:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class User:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_User"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_User"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_User = User


