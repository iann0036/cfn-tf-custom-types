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
    AccountId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Schedule: Optional[str]
    Type: Optional[str]
    Input: Optional[Sequence["_InputDefinition"]]
    Match: Optional[Sequence["_MatchDefinition"]]

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
            AccountId=json_data.get("AccountId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Schedule=json_data.get("Schedule"),
            Type=json_data.get("Type"),
            Input=deserialize_list(json_data.get("Input"), InputDefinition),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InputDefinition(BaseModel):
    Exists: Optional[bool]
    Id: Optional[str]
    Path: Optional[str]
    Running: Optional[bool]
    Sha256: Optional[str]
    Thumbprint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinition"]:
        if not json_data:
            return None
        return cls(
            Exists=json_data.get("Exists"),
            Id=json_data.get("Id"),
            Path=json_data.get("Path"),
            Running=json_data.get("Running"),
            Sha256=json_data.get("Sha256"),
            Thumbprint=json_data.get("Thumbprint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDefinition = InputDefinition


@dataclass
class MatchDefinition(BaseModel):
    Platform: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Platform=json_data.get("Platform"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


