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
    EndTimeInSeconds: Optional[float]
    HostTagGroupHostNamesGroupAnded: Optional[bool]
    Id: Optional[str]
    Reason: Optional[str]
    RelevantCustomerTags: Optional[Sequence[str]]
    RelevantHostNames: Optional[Sequence[str]]
    RelevantHostTags: Optional[Sequence[str]]
    RelevantHostTagsAnded: Optional[bool]
    StartTimeInSeconds: Optional[float]
    Title: Optional[str]

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
            EndTimeInSeconds=json_data.get("EndTimeInSeconds"),
            HostTagGroupHostNamesGroupAnded=json_data.get("HostTagGroupHostNamesGroupAnded"),
            Id=json_data.get("Id"),
            Reason=json_data.get("Reason"),
            RelevantCustomerTags=json_data.get("RelevantCustomerTags"),
            RelevantHostNames=json_data.get("RelevantHostNames"),
            RelevantHostTags=json_data.get("RelevantHostTags"),
            RelevantHostTagsAnded=json_data.get("RelevantHostTagsAnded"),
            StartTimeInSeconds=json_data.get("StartTimeInSeconds"),
            Title=json_data.get("Title"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


