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
    Ctrl: Optional[str]
    Description: Optional[str]
    HelloIntvl: Optional[str]
    HoldIntvl: Optional[str]
    HsrpGroupPolicyType: Optional[str]
    Id: Optional[str]
    Key: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    PreemptDelayMin: Optional[str]
    PreemptDelayReload: Optional[str]
    PreemptDelaySync: Optional[str]
    Prio: Optional[str]
    TenantDn: Optional[str]
    Timeout: Optional[str]

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
            Ctrl=json_data.get("Ctrl"),
            Description=json_data.get("Description"),
            HelloIntvl=json_data.get("HelloIntvl"),
            HoldIntvl=json_data.get("HoldIntvl"),
            HsrpGroupPolicyType=json_data.get("HsrpGroupPolicyType"),
            Id=json_data.get("Id"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            PreemptDelayMin=json_data.get("PreemptDelayMin"),
            PreemptDelayReload=json_data.get("PreemptDelayReload"),
            PreemptDelaySync=json_data.get("PreemptDelaySync"),
            Prio=json_data.get("Prio"),
            TenantDn=json_data.get("TenantDn"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


