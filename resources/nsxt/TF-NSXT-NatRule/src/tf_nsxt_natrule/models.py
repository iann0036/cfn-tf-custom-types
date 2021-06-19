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
    Action: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Logging: Optional[bool]
    LogicalRouterId: Optional[str]
    MatchDestinationNetwork: Optional[str]
    MatchSourceNetwork: Optional[str]
    NatPass: Optional[bool]
    Revision: Optional[float]
    RulePriority: Optional[float]
    TranslatedNetwork: Optional[str]
    TranslatedPorts: Optional[str]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Logging=json_data.get("Logging"),
            LogicalRouterId=json_data.get("LogicalRouterId"),
            MatchDestinationNetwork=json_data.get("MatchDestinationNetwork"),
            MatchSourceNetwork=json_data.get("MatchSourceNetwork"),
            NatPass=json_data.get("NatPass"),
            Revision=json_data.get("Revision"),
            RulePriority=json_data.get("RulePriority"),
            TranslatedNetwork=json_data.get("TranslatedNetwork"),
            TranslatedPorts=json_data.get("TranslatedPorts"),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


