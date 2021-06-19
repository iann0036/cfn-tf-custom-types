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
    Description: Optional[str]
    EgressPriTagging: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Priority0: Optional[str]
    Priority1: Optional[str]
    Priority2: Optional[str]
    Priority3: Optional[str]
    Priority4: Optional[str]
    Priority5: Optional[str]
    Priority6: Optional[str]
    Priority7: Optional[str]
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
            Description=json_data.get("Description"),
            EgressPriTagging=json_data.get("EgressPriTagging"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Priority0=json_data.get("Priority0"),
            Priority1=json_data.get("Priority1"),
            Priority2=json_data.get("Priority2"),
            Priority3=json_data.get("Priority3"),
            Priority4=json_data.get("Priority4"),
            Priority5=json_data.get("Priority5"),
            Priority6=json_data.get("Priority6"),
            Priority7=json_data.get("Priority7"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


