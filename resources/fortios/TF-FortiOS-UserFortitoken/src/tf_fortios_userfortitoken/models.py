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
    ActivationCode: Optional[str]
    ActivationExpire: Optional[float]
    Comments: Optional[str]
    Id: Optional[str]
    License: Optional[str]
    OsVer: Optional[str]
    RegId: Optional[str]
    Seed: Optional[str]
    SerialNumber: Optional[str]
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
            ActivationCode=json_data.get("ActivationCode"),
            ActivationExpire=json_data.get("ActivationExpire"),
            Comments=json_data.get("Comments"),
            Id=json_data.get("Id"),
            License=json_data.get("License"),
            OsVer=json_data.get("OsVer"),
            RegId=json_data.get("RegId"),
            Seed=json_data.get("Seed"),
            SerialNumber=json_data.get("SerialNumber"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


