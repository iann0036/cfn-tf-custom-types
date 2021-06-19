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
    CompletedAt: Optional[str]
    CronTiming: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    Name: Optional[str]
    NextExecution: Optional[str]
    Region: Optional[str]
    RequestedAt: Optional[str]
    Safe: Optional[bool]
    SizeGb: Optional[float]
    State: Optional[str]
    TemplateId: Optional[str]

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
            CompletedAt=json_data.get("CompletedAt"),
            CronTiming=json_data.get("CronTiming"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            Name=json_data.get("Name"),
            NextExecution=json_data.get("NextExecution"),
            Region=json_data.get("Region"),
            RequestedAt=json_data.get("RequestedAt"),
            Safe=json_data.get("Safe"),
            SizeGb=json_data.get("SizeGb"),
            State=json_data.get("State"),
            TemplateId=json_data.get("TemplateId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


