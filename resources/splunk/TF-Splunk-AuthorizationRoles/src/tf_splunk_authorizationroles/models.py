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
    Capabilities: Optional[Sequence[str]]
    CumulativeRealtimeSearchJobsQuota: Optional[float]
    CumulativeSearchJobsQuota: Optional[float]
    DefaultApp: Optional[str]
    Id: Optional[str]
    ImportedRoles: Optional[Sequence[str]]
    Name: Optional[str]
    RealtimeSearchJobsQuota: Optional[float]
    SearchDiskQuota: Optional[float]
    SearchFilter: Optional[str]
    SearchIndexesAllowed: Optional[Sequence[str]]
    SearchIndexesDefault: Optional[Sequence[str]]
    SearchJobsQuota: Optional[float]
    SearchTimeWin: Optional[float]

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
            Capabilities=json_data.get("Capabilities"),
            CumulativeRealtimeSearchJobsQuota=json_data.get("CumulativeRealtimeSearchJobsQuota"),
            CumulativeSearchJobsQuota=json_data.get("CumulativeSearchJobsQuota"),
            DefaultApp=json_data.get("DefaultApp"),
            Id=json_data.get("Id"),
            ImportedRoles=json_data.get("ImportedRoles"),
            Name=json_data.get("Name"),
            RealtimeSearchJobsQuota=json_data.get("RealtimeSearchJobsQuota"),
            SearchDiskQuota=json_data.get("SearchDiskQuota"),
            SearchFilter=json_data.get("SearchFilter"),
            SearchIndexesAllowed=json_data.get("SearchIndexesAllowed"),
            SearchIndexesDefault=json_data.get("SearchIndexesDefault"),
            SearchJobsQuota=json_data.get("SearchJobsQuota"),
            SearchTimeWin=json_data.get("SearchTimeWin"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


