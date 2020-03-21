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
    Created: Optional[str]
    DeploymentsActive: Optional[float]
    DeploymentsTotal: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    Images: Optional[Sequence[str]]
    IsPublic: Optional[bool]
    Label: Optional[str]
    RevNote: Optional[str]
    Script: Optional[str]
    Updated: Optional[str]
    UserDefinedFields: Optional[Sequence["_UserDefinedFields"]]
    UserGravatarId: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Created=json_data.get("Created"),
            DeploymentsActive=json_data.get("DeploymentsActive"),
            DeploymentsTotal=json_data.get("DeploymentsTotal"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Images=json_data.get("Images"),
            IsPublic=json_data.get("IsPublic"),
            Label=json_data.get("Label"),
            RevNote=json_data.get("RevNote"),
            Script=json_data.get("Script"),
            Updated=json_data.get("Updated"),
            UserDefinedFields=json_data.get("UserDefinedFields"),
            UserGravatarId=json_data.get("UserGravatarId"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UserDefinedFields:
    Default: Optional[str]
    Example: Optional[str]
    Label: Optional[str]
    ManyOf: Optional[str]
    Name: Optional[str]
    OneOf: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinedFields"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinedFields"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
            Example=json_data.get("Example"),
            Label=json_data.get("Label"),
            ManyOf=json_data.get("ManyOf"),
            Name=json_data.get("Name"),
            OneOf=json_data.get("OneOf"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinedFields = UserDefinedFields


