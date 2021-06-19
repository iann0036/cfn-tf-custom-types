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
    DefaultVlan: Optional[str]
    Id: Optional[str]
    Nac: Optional[str]
    Quarantine: Optional[str]
    Rspan: Optional[str]
    Vdomparam: Optional[str]
    Video: Optional[str]
    Voice: Optional[str]

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
            DefaultVlan=json_data.get("DefaultVlan"),
            Id=json_data.get("Id"),
            Nac=json_data.get("Nac"),
            Quarantine=json_data.get("Quarantine"),
            Rspan=json_data.get("Rspan"),
            Vdomparam=json_data.get("Vdomparam"),
            Video=json_data.get("Video"),
            Voice=json_data.get("Voice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


