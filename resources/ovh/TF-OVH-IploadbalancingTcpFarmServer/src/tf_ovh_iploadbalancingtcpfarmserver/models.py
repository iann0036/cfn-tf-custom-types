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
    Address: Optional[str]
    Backup: Optional[bool]
    Chain: Optional[str]
    DisplayName: Optional[str]
    FarmId: Optional[float]
    Id: Optional[str]
    Port: Optional[float]
    Probe: Optional[bool]
    ProxyProtocolVersion: Optional[str]
    ServiceName: Optional[str]
    Ssl: Optional[bool]
    Status: Optional[str]
    Weight: Optional[float]

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
            Address=json_data.get("Address"),
            Backup=json_data.get("Backup"),
            Chain=json_data.get("Chain"),
            DisplayName=json_data.get("DisplayName"),
            FarmId=json_data.get("FarmId"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
            Probe=json_data.get("Probe"),
            ProxyProtocolVersion=json_data.get("ProxyProtocolVersion"),
            ServiceName=json_data.get("ServiceName"),
            Ssl=json_data.get("Ssl"),
            Status=json_data.get("Status"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


