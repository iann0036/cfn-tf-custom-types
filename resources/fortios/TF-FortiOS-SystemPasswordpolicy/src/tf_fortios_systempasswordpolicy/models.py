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
    ApplyTo: Optional[str]
    Change4Characters: Optional[str]
    ExpireDay: Optional[float]
    ExpireStatus: Optional[str]
    Id: Optional[str]
    MinLowerCaseLetter: Optional[float]
    MinNonAlphanumeric: Optional[float]
    MinNumber: Optional[float]
    MinUpperCaseLetter: Optional[float]
    MinimumLength: Optional[float]
    ReusePassword: Optional[str]
    Status: Optional[str]
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
            ApplyTo=json_data.get("ApplyTo"),
            Change4Characters=json_data.get("Change4Characters"),
            ExpireDay=json_data.get("ExpireDay"),
            ExpireStatus=json_data.get("ExpireStatus"),
            Id=json_data.get("Id"),
            MinLowerCaseLetter=json_data.get("MinLowerCaseLetter"),
            MinNonAlphanumeric=json_data.get("MinNonAlphanumeric"),
            MinNumber=json_data.get("MinNumber"),
            MinUpperCaseLetter=json_data.get("MinUpperCaseLetter"),
            MinimumLength=json_data.get("MinimumLength"),
            ReusePassword=json_data.get("ReusePassword"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


