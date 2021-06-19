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
    DomainId: Optional[str]
    GtdRegion: Optional[float]
    Id: Optional[str]
    Name: Optional[str]
    Noanswer: Optional[bool]
    Note: Optional[str]
    SourceType: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]
    Roundrobin: Optional[Sequence["_RoundrobinDefinition"]]

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
            DomainId=json_data.get("DomainId"),
            GtdRegion=json_data.get("GtdRegion"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Noanswer=json_data.get("Noanswer"),
            Note=json_data.get("Note"),
            SourceType=json_data.get("SourceType"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Roundrobin=deserialize_list(json_data.get("Roundrobin"), RoundrobinDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RoundrobinDefinition(BaseModel):
    DisableFlag: Optional[str]
    Level: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoundrobinDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoundrobinDefinition"]:
        if not json_data:
            return None
        return cls(
            DisableFlag=json_data.get("DisableFlag"),
            Level=json_data.get("Level"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoundrobinDefinition = RoundrobinDefinition


