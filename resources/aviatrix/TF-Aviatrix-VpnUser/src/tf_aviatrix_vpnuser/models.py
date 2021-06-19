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
    DnsName: Optional[str]
    GwName: Optional[str]
    Id: Optional[str]
    ManageUserAttachment: Optional[bool]
    Profiles: Optional[Sequence[str]]
    SamlEndpoint: Optional[str]
    UserEmail: Optional[str]
    UserName: Optional[str]
    VpcId: Optional[str]

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
            DnsName=json_data.get("DnsName"),
            GwName=json_data.get("GwName"),
            Id=json_data.get("Id"),
            ManageUserAttachment=json_data.get("ManageUserAttachment"),
            Profiles=json_data.get("Profiles"),
            SamlEndpoint=json_data.get("SamlEndpoint"),
            UserEmail=json_data.get("UserEmail"),
            UserName=json_data.get("UserName"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


