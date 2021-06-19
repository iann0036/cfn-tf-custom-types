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
    Id: Optional[str]
    Name: Optional[str]
    Namespace: Optional[str]
    SiteType: Optional[str]
    VipParamsPerAz: Optional[Sequence["_VipParamsPerAzDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            SiteType=json_data.get("SiteType"),
            VipParamsPerAz=deserialize_list(json_data.get("VipParamsPerAz"), VipParamsPerAzDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VipParamsPerAzDefinition(BaseModel):
    AzName: Optional[str]
    InsideVip: Optional[Sequence[str]]
    InsideVipCname: Optional[str]
    OutsideVip: Optional[Sequence[str]]
    OutsideVipCname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VipParamsPerAzDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VipParamsPerAzDefinition"]:
        if not json_data:
            return None
        return cls(
            AzName=json_data.get("AzName"),
            InsideVip=json_data.get("InsideVip"),
            InsideVipCname=json_data.get("InsideVipCname"),
            OutsideVip=json_data.get("OutsideVip"),
            OutsideVipCname=json_data.get("OutsideVipCname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VipParamsPerAzDefinition = VipParamsPerAzDefinition


