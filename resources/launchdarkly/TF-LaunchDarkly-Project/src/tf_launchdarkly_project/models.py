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
    Id: Optional[str]
    IncludeInSnippet: Optional[bool]
    Key: Optional[str]
    Name: Optional[str]
    Tags: Optional[Sequence[str]]
    Environments: Optional[Sequence["_EnvironmentsDefinition"]]

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
            Id=json_data.get("Id"),
            IncludeInSnippet=json_data.get("IncludeInSnippet"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Environments=deserialize_list(json_data.get("Environments"), EnvironmentsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EnvironmentsDefinition(BaseModel):
    Color: Optional[str]
    ConfirmChanges: Optional[bool]
    DefaultTrackEvents: Optional[bool]
    DefaultTtl: Optional[float]
    Key: Optional[str]
    Name: Optional[str]
    RequireComments: Optional[bool]
    SecureMode: Optional[bool]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentsDefinition"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            ConfirmChanges=json_data.get("ConfirmChanges"),
            DefaultTrackEvents=json_data.get("DefaultTrackEvents"),
            DefaultTtl=json_data.get("DefaultTtl"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            RequireComments=json_data.get("RequireComments"),
            SecureMode=json_data.get("SecureMode"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentsDefinition = EnvironmentsDefinition


