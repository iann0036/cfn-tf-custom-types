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
    ClusterName: Optional[str]
    ClusterSize: Optional[float]
    ConnectedRegion: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Latitude: Optional[float]
    Longitude: Optional[float]
    RegistrationName: Optional[str]
    Retry: Optional[float]
    WaitTime: Optional[float]

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
            ClusterName=json_data.get("ClusterName"),
            ClusterSize=json_data.get("ClusterSize"),
            ConnectedRegion=json_data.get("ConnectedRegion"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
            RegistrationName=json_data.get("RegistrationName"),
            Retry=json_data.get("Retry"),
            WaitTime=json_data.get("WaitTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


