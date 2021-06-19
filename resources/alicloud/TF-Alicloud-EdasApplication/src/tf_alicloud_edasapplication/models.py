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
    ApplicationName: Optional[str]
    BuildPackId: Optional[float]
    ClusterId: Optional[str]
    Descriotion: Optional[str]
    EcuInfo: Optional[Sequence[str]]
    GroupId: Optional[str]
    HealthCheckUrl: Optional[str]
    Id: Optional[str]
    LogicalRegionId: Optional[str]
    PackageType: Optional[str]
    PackageVersion: Optional[str]
    WarUrl: Optional[str]

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
            ApplicationName=json_data.get("ApplicationName"),
            BuildPackId=json_data.get("BuildPackId"),
            ClusterId=json_data.get("ClusterId"),
            Descriotion=json_data.get("Descriotion"),
            EcuInfo=json_data.get("EcuInfo"),
            GroupId=json_data.get("GroupId"),
            HealthCheckUrl=json_data.get("HealthCheckUrl"),
            Id=json_data.get("Id"),
            LogicalRegionId=json_data.get("LogicalRegionId"),
            PackageType=json_data.get("PackageType"),
            PackageVersion=json_data.get("PackageVersion"),
            WarUrl=json_data.get("WarUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


