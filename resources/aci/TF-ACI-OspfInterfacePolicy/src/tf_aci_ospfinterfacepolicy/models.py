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
    Cost: Optional[str]
    Ctrl: Optional[Sequence[str]]
    DeadIntvl: Optional[str]
    Description: Optional[str]
    HelloIntvl: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    NwT: Optional[str]
    PfxSuppress: Optional[str]
    Prio: Optional[str]
    RexmitIntvl: Optional[str]
    TenantDn: Optional[str]
    XmitDelay: Optional[str]

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
            Cost=json_data.get("Cost"),
            Ctrl=json_data.get("Ctrl"),
            DeadIntvl=json_data.get("DeadIntvl"),
            Description=json_data.get("Description"),
            HelloIntvl=json_data.get("HelloIntvl"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            NwT=json_data.get("NwT"),
            PfxSuppress=json_data.get("PfxSuppress"),
            Prio=json_data.get("Prio"),
            RexmitIntvl=json_data.get("RexmitIntvl"),
            TenantDn=json_data.get("TenantDn"),
            XmitDelay=json_data.get("XmitDelay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


