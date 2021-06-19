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
    DefaultRouteId: Optional[str]
    Id: Optional[str]
    Link: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Templates: Optional[Sequence["_TemplatesDefinition"]]

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
            DefaultRouteId=json_data.get("DefaultRouteId"),
            Id=json_data.get("Id"),
            Link=json_data.get("Link"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Templates=deserialize_list(json_data.get("Templates"), TemplatesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TemplatesDefinition(BaseModel):
    GroupingKey: Optional[str]
    ResolveSignal: Optional[str]
    Slack: Optional[Sequence["_SlackDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplatesDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupingKey=json_data.get("GroupingKey"),
            ResolveSignal=json_data.get("ResolveSignal"),
            Slack=deserialize_list(json_data.get("Slack"), SlackDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplatesDefinition = TemplatesDefinition


@dataclass
class SlackDefinition(BaseModel):
    ImageUrl: Optional[str]
    Message: Optional[str]
    Title: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageUrl=json_data.get("ImageUrl"),
            Message=json_data.get("Message"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackDefinition = SlackDefinition


