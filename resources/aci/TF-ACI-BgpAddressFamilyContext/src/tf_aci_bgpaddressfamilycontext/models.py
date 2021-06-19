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
    EDist: Optional[str]
    IDist: Optional[str]
    Id: Optional[str]
    LocalDist: Optional[str]
    MaxEcmp: Optional[str]
    MaxEcmpIbgp: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    TenantDn: Optional[str]

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
            EDist=json_data.get("EDist"),
            IDist=json_data.get("IDist"),
            Id=json_data.get("Id"),
            LocalDist=json_data.get("LocalDist"),
            MaxEcmp=json_data.get("MaxEcmp"),
            MaxEcmpIbgp=json_data.get("MaxEcmpIbgp"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            TenantDn=json_data.get("TenantDn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


