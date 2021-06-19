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
    AntiAffinity: Optional[bool]
    Autoscale: Optional[bool]
    AvailableNodes: Optional[float]
    CreatedAt: Optional[str]
    CurrentNodes: Optional[float]
    DesiredNodes: Optional[float]
    Flavor: Optional[str]
    FlavorName: Optional[str]
    Id: Optional[str]
    KubeId: Optional[str]
    MaxNodes: Optional[float]
    MinNodes: Optional[float]
    MonthlyBilled: Optional[bool]
    Name: Optional[str]
    ProjectId: Optional[str]
    ServiceName: Optional[str]
    SizeStatus: Optional[str]
    Status: Optional[str]
    UpToDateNodes: Optional[float]
    UpdatedAt: Optional[str]

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
            AntiAffinity=json_data.get("AntiAffinity"),
            Autoscale=json_data.get("Autoscale"),
            AvailableNodes=json_data.get("AvailableNodes"),
            CreatedAt=json_data.get("CreatedAt"),
            CurrentNodes=json_data.get("CurrentNodes"),
            DesiredNodes=json_data.get("DesiredNodes"),
            Flavor=json_data.get("Flavor"),
            FlavorName=json_data.get("FlavorName"),
            Id=json_data.get("Id"),
            KubeId=json_data.get("KubeId"),
            MaxNodes=json_data.get("MaxNodes"),
            MinNodes=json_data.get("MinNodes"),
            MonthlyBilled=json_data.get("MonthlyBilled"),
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
            ServiceName=json_data.get("ServiceName"),
            SizeStatus=json_data.get("SizeStatus"),
            Status=json_data.get("Status"),
            UpToDateNodes=json_data.get("UpToDateNodes"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


