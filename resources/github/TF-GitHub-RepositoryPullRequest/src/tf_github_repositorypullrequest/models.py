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
    BaseRef: Optional[str]
    BaseRepository: Optional[str]
    BaseSha: Optional[str]
    Body: Optional[str]
    Draft: Optional[bool]
    HeadRef: Optional[str]
    HeadSha: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence[str]]
    MaintainerCanModify: Optional[bool]
    Number: Optional[float]
    OpenedAt: Optional[float]
    OpenedBy: Optional[str]
    Owner: Optional[str]
    State: Optional[str]
    Title: Optional[str]
    UpdatedAt: Optional[float]

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
            BaseRef=json_data.get("BaseRef"),
            BaseRepository=json_data.get("BaseRepository"),
            BaseSha=json_data.get("BaseSha"),
            Body=json_data.get("Body"),
            Draft=json_data.get("Draft"),
            HeadRef=json_data.get("HeadRef"),
            HeadSha=json_data.get("HeadSha"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            MaintainerCanModify=json_data.get("MaintainerCanModify"),
            Number=json_data.get("Number"),
            OpenedAt=json_data.get("OpenedAt"),
            OpenedBy=json_data.get("OpenedBy"),
            Owner=json_data.get("Owner"),
            State=json_data.get("State"),
            Title=json_data.get("Title"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


