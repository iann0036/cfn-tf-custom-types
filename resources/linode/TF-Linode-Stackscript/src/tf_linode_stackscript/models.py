# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
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
    UserDefinedFields: Optional[Sequence["_UserDefinedFieldsDefinition"]]
    UserGravatarId: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
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
            UserDefinedFields=deserialize_list(json_data.get("UserDefinedFields"), UserDefinedFieldsDefinition),
            UserGravatarId=json_data.get("UserGravatarId"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class UserDefinedFieldsDefinition(BaseModel):
    Default: Optional[str]
    Example: Optional[str]
    Label: Optional[str]
    ManyOf: Optional[str]
    Name: Optional[str]
    OneOf: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinedFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinedFieldsDefinition"]:
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
_UserDefinedFieldsDefinition = UserDefinedFieldsDefinition


