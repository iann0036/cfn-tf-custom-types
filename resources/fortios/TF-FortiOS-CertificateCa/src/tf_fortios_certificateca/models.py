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
    AutoUpdateDays: Optional[float]
    AutoUpdateDaysWarning: Optional[float]
    Ca: Optional[str]
    Id: Optional[str]
    LastUpdated: Optional[float]
    Name: Optional[str]
    Range: Optional[str]
    ScepUrl: Optional[str]
    Source: Optional[str]
    SourceIp: Optional[str]
    SslInspectionTrusted: Optional[str]
    Trusted: Optional[str]
    Vdomparam: Optional[str]

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
            AutoUpdateDays=json_data.get("AutoUpdateDays"),
            AutoUpdateDaysWarning=json_data.get("AutoUpdateDaysWarning"),
            Ca=json_data.get("Ca"),
            Id=json_data.get("Id"),
            LastUpdated=json_data.get("LastUpdated"),
            Name=json_data.get("Name"),
            Range=json_data.get("Range"),
            ScepUrl=json_data.get("ScepUrl"),
            Source=json_data.get("Source"),
            SourceIp=json_data.get("SourceIp"),
            SslInspectionTrusted=json_data.get("SslInspectionTrusted"),
            Trusted=json_data.get("Trusted"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


