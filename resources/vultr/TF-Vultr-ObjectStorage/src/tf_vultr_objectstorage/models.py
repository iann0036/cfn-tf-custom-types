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
    ClusterId: Optional[float]
    DateCreated: Optional[str]
    Id: Optional[str]
    Label: Optional[str]
    Location: Optional[str]
    Region: Optional[str]
    S3AccessKey: Optional[str]
    S3Hostname: Optional[str]
    S3SecretKey: Optional[str]
    Status: Optional[str]

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
            ClusterId=json_data.get("ClusterId"),
            DateCreated=json_data.get("DateCreated"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            Location=json_data.get("Location"),
            Region=json_data.get("Region"),
            S3AccessKey=json_data.get("S3AccessKey"),
            S3Hostname=json_data.get("S3Hostname"),
            S3SecretKey=json_data.get("S3SecretKey"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

