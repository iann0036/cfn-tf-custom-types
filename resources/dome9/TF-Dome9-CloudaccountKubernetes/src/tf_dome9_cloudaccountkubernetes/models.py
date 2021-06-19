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
    ClusterVersion: Optional[str]
    CreationDate: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrganizationalUnitId: Optional[str]
    OrganizationalUnitName: Optional[str]
    OrganizationalUnitPath: Optional[str]
    Vendor: Optional[str]

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
            ClusterVersion=json_data.get("ClusterVersion"),
            CreationDate=json_data.get("CreationDate"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrganizationalUnitId=json_data.get("OrganizationalUnitId"),
            OrganizationalUnitName=json_data.get("OrganizationalUnitName"),
            OrganizationalUnitPath=json_data.get("OrganizationalUnitPath"),
            Vendor=json_data.get("Vendor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


