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
    Anomaly: Optional[str]
    DlpArchive: Optional[str]
    DynamicSortSubtable: Optional[str]
    Filter: Optional[str]
    FilterType: Optional[str]
    ForwardTraffic: Optional[str]
    Gtp: Optional[str]
    Id: Optional[str]
    LocalTraffic: Optional[str]
    MulticastTraffic: Optional[str]
    Severity: Optional[str]
    SnifferTraffic: Optional[str]
    Vdomparam: Optional[str]
    Voip: Optional[str]
    FreeStyle: Optional[Sequence["_FreeStyleDefinition"]]

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
            Anomaly=json_data.get("Anomaly"),
            DlpArchive=json_data.get("DlpArchive"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Filter=json_data.get("Filter"),
            FilterType=json_data.get("FilterType"),
            ForwardTraffic=json_data.get("ForwardTraffic"),
            Gtp=json_data.get("Gtp"),
            Id=json_data.get("Id"),
            LocalTraffic=json_data.get("LocalTraffic"),
            MulticastTraffic=json_data.get("MulticastTraffic"),
            Severity=json_data.get("Severity"),
            SnifferTraffic=json_data.get("SnifferTraffic"),
            Vdomparam=json_data.get("Vdomparam"),
            Voip=json_data.get("Voip"),
            FreeStyle=deserialize_list(json_data.get("FreeStyle"), FreeStyleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FreeStyleDefinition(BaseModel):
    Category: Optional[str]
    Filter: Optional[str]
    FilterType: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FreeStyleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeStyleDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Filter=json_data.get("Filter"),
            FilterType=json_data.get("FilterType"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeStyleDefinition = FreeStyleDefinition


