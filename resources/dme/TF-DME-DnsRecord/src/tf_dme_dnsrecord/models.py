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
    CaaType: Optional[str]
    Description: Optional[str]
    DomainId: Optional[str]
    DynamicDns: Optional[str]
    GtdLocation: Optional[str]
    Hardlink: Optional[str]
    Id: Optional[str]
    IssuerCritical: Optional[str]
    Keywords: Optional[str]
    MxLevel: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[str]
    Priority: Optional[str]
    RedirectType: Optional[str]
    Title: Optional[str]
    Ttl: Optional[str]
    Type: Optional[str]
    Value: Optional[str]
    Weight: Optional[str]

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
            CaaType=json_data.get("CaaType"),
            Description=json_data.get("Description"),
            DomainId=json_data.get("DomainId"),
            DynamicDns=json_data.get("DynamicDns"),
            GtdLocation=json_data.get("GtdLocation"),
            Hardlink=json_data.get("Hardlink"),
            Id=json_data.get("Id"),
            IssuerCritical=json_data.get("IssuerCritical"),
            Keywords=json_data.get("Keywords"),
            MxLevel=json_data.get("MxLevel"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            RedirectType=json_data.get("RedirectType"),
            Title=json_data.get("Title"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


