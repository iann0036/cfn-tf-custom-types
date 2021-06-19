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
    AllowedSource: Optional[Sequence[str]]
    DedicatedIpfo: Optional[Sequence[str]]
    DefaultFarmId: Optional[float]
    DefaultSslId: Optional[float]
    Disabled: Optional[bool]
    DisplayName: Optional[str]
    Id: Optional[str]
    Port: Optional[str]
    RedirectLocation: Optional[str]
    ServiceName: Optional[str]
    Ssl: Optional[bool]
    Zone: Optional[str]

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
            AllowedSource=json_data.get("AllowedSource"),
            DedicatedIpfo=json_data.get("DedicatedIpfo"),
            DefaultFarmId=json_data.get("DefaultFarmId"),
            DefaultSslId=json_data.get("DefaultSslId"),
            Disabled=json_data.get("Disabled"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
            RedirectLocation=json_data.get("RedirectLocation"),
            ServiceName=json_data.get("ServiceName"),
            Ssl=json_data.get("Ssl"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


