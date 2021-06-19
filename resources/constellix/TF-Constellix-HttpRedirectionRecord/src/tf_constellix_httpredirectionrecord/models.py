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
    Description: Optional[str]
    DomainId: Optional[str]
    GtdRegion: Optional[float]
    HardlinkFlag: Optional[bool]
    Id: Optional[str]
    Keywords: Optional[str]
    Name: Optional[str]
    Noanswer: Optional[bool]
    Note: Optional[str]
    Parent: Optional[str]
    Parentid: Optional[float]
    RedirectTypeId: Optional[float]
    Source: Optional[str]
    SourceType: Optional[str]
    Title: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]
    Url: Optional[str]

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
            Description=json_data.get("Description"),
            DomainId=json_data.get("DomainId"),
            GtdRegion=json_data.get("GtdRegion"),
            HardlinkFlag=json_data.get("HardlinkFlag"),
            Id=json_data.get("Id"),
            Keywords=json_data.get("Keywords"),
            Name=json_data.get("Name"),
            Noanswer=json_data.get("Noanswer"),
            Note=json_data.get("Note"),
            Parent=json_data.get("Parent"),
            Parentid=json_data.get("Parentid"),
            RedirectTypeId=json_data.get("RedirectTypeId"),
            Source=json_data.get("Source"),
            SourceType=json_data.get("SourceType"),
            Title=json_data.get("Title"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


