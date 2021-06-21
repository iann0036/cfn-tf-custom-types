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
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    IpAddrBlock: Optional[str]
    Name: Optional[str]
    OneArmIpsUrlfilter: Optional[str]
    Vdomparam: Optional[str]
    Entries: Optional[Sequence["_EntriesDefinition"]]

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
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            IpAddrBlock=json_data.get("IpAddrBlock"),
            Name=json_data.get("Name"),
            OneArmIpsUrlfilter=json_data.get("OneArmIpsUrlfilter"),
            Vdomparam=json_data.get("Vdomparam"),
            Entries=deserialize_list(json_data.get("Entries"), EntriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EntriesDefinition(BaseModel):
    Action: Optional[str]
    AntiphishAction: Optional[str]
    DnsAddressFamily: Optional[str]
    Exempt: Optional[str]
    Id: Optional[float]
    ReferrerHost: Optional[str]
    Status: Optional[str]
    Type: Optional[str]
    Url: Optional[str]
    WebProxyProfile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AntiphishAction=json_data.get("AntiphishAction"),
            DnsAddressFamily=json_data.get("DnsAddressFamily"),
            Exempt=json_data.get("Exempt"),
            Id=json_data.get("Id"),
            ReferrerHost=json_data.get("ReferrerHost"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            WebProxyProfile=json_data.get("WebProxyProfile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntriesDefinition = EntriesDefinition

