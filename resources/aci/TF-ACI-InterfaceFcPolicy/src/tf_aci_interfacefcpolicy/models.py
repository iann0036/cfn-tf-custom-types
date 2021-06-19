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
    Annotation: Optional[str]
    Automaxspeed: Optional[str]
    Description: Optional[str]
    FillPattern: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    PortMode: Optional[str]
    RxBbCredit: Optional[str]
    Speed: Optional[str]
    TrunkMode: Optional[str]

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
            Annotation=json_data.get("Annotation"),
            Automaxspeed=json_data.get("Automaxspeed"),
            Description=json_data.get("Description"),
            FillPattern=json_data.get("FillPattern"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            PortMode=json_data.get("PortMode"),
            RxBbCredit=json_data.get("RxBbCredit"),
            Speed=json_data.get("Speed"),
            TrunkMode=json_data.get("TrunkMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


