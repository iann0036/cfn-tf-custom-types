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
    HttpGet: Optional[str]
    HttpMatch: Optional[str]
    HttpMaxRedirects: Optional[float]
    Id: Optional[str]
    Interval: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    Retry: Optional[float]
    SrcIp: Optional[str]
    Timeout: Optional[float]
    Type: Optional[str]
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
            HttpGet=json_data.get("HttpGet"),
            HttpMatch=json_data.get("HttpMatch"),
            HttpMaxRedirects=json_data.get("HttpMaxRedirects"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Retry=json_data.get("Retry"),
            SrcIp=json_data.get("SrcIp"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


