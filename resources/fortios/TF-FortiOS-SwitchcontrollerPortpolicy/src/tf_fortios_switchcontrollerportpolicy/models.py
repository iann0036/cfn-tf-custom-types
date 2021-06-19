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
    BouncePortLink: Optional[str]
    Description: Optional[str]
    Fortilink: Optional[str]
    Id: Optional[str]
    LldpProfile: Optional[str]
    N8021x: Optional[str]
    Name: Optional[str]
    QosPolicy: Optional[str]
    Vdomparam: Optional[str]
    VlanPolicy: Optional[str]

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
            BouncePortLink=json_data.get("BouncePortLink"),
            Description=json_data.get("Description"),
            Fortilink=json_data.get("Fortilink"),
            Id=json_data.get("Id"),
            LldpProfile=json_data.get("LldpProfile"),
            N8021x=json_data.get("N8021x"),
            Name=json_data.get("Name"),
            QosPolicy=json_data.get("QosPolicy"),
            Vdomparam=json_data.get("Vdomparam"),
            VlanPolicy=json_data.get("VlanPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


