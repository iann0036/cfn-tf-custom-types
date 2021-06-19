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
    CustomizedRouteAdvertisement: Optional[str]
    CustomizedRoutes: Optional[str]
    DisableLocalRoutePropagation: Optional[bool]
    EdgeAttachment: Optional[str]
    Id: Optional[str]
    Region: Optional[str]
    RouteTables: Optional[str]
    SecurityDomainName: Optional[str]
    Subnets: Optional[str]
    TgwName: Optional[str]
    VpcAccountName: Optional[str]
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
            CustomizedRouteAdvertisement=json_data.get("CustomizedRouteAdvertisement"),
            CustomizedRoutes=json_data.get("CustomizedRoutes"),
            DisableLocalRoutePropagation=json_data.get("DisableLocalRoutePropagation"),
            EdgeAttachment=json_data.get("EdgeAttachment"),
            Id=json_data.get("Id"),
            Region=json_data.get("Region"),
            RouteTables=json_data.get("RouteTables"),
            SecurityDomainName=json_data.get("SecurityDomainName"),
            Subnets=json_data.get("Subnets"),
            TgwName=json_data.get("TgwName"),
            VpcAccountName=json_data.get("VpcAccountName"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


