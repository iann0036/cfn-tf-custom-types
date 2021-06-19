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
    Category: Optional[str]
    Description: Optional[str]
    DynamicSortSubtable: Optional[str]
    EmsTag: Optional[str]
    Family: Optional[str]
    Host: Optional[str]
    HwVendor: Optional[str]
    HwVersion: Optional[str]
    Id: Optional[str]
    Mac: Optional[str]
    Name: Optional[str]
    Os: Optional[str]
    Src: Optional[str]
    Status: Optional[str]
    SwVersion: Optional[str]
    SwitchAutoAuth: Optional[str]
    SwitchFortilink: Optional[str]
    SwitchMacPolicy: Optional[str]
    SwitchPortPolicy: Optional[str]
    Type: Optional[str]
    User: Optional[str]
    UserGroup: Optional[str]
    Vdomparam: Optional[str]
    SwitchScope: Optional[Sequence["_SwitchScopeDefinition"]]

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
            Category=json_data.get("Category"),
            Description=json_data.get("Description"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EmsTag=json_data.get("EmsTag"),
            Family=json_data.get("Family"),
            Host=json_data.get("Host"),
            HwVendor=json_data.get("HwVendor"),
            HwVersion=json_data.get("HwVersion"),
            Id=json_data.get("Id"),
            Mac=json_data.get("Mac"),
            Name=json_data.get("Name"),
            Os=json_data.get("Os"),
            Src=json_data.get("Src"),
            Status=json_data.get("Status"),
            SwVersion=json_data.get("SwVersion"),
            SwitchAutoAuth=json_data.get("SwitchAutoAuth"),
            SwitchFortilink=json_data.get("SwitchFortilink"),
            SwitchMacPolicy=json_data.get("SwitchMacPolicy"),
            SwitchPortPolicy=json_data.get("SwitchPortPolicy"),
            Type=json_data.get("Type"),
            User=json_data.get("User"),
            UserGroup=json_data.get("UserGroup"),
            Vdomparam=json_data.get("Vdomparam"),
            SwitchScope=deserialize_list(json_data.get("SwitchScope"), SwitchScopeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SwitchScopeDefinition(BaseModel):
    SwitchId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SwitchScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SwitchScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            SwitchId=json_data.get("SwitchId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SwitchScopeDefinition = SwitchScopeDefinition


