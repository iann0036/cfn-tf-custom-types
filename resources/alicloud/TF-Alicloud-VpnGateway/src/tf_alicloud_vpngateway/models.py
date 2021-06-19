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
    Bandwidth: Optional[float]
    BusinessStatus: Optional[str]
    Description: Optional[str]
    EnableIpsec: Optional[bool]
    EnableSsl: Optional[bool]
    Id: Optional[str]
    InstanceChargeType: Optional[str]
    InternetIp: Optional[str]
    Name: Optional[str]
    Period: Optional[float]
    SslConnections: Optional[float]
    Status: Optional[str]
    VpcId: Optional[str]
    VswitchId: Optional[str]

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
            Bandwidth=json_data.get("Bandwidth"),
            BusinessStatus=json_data.get("BusinessStatus"),
            Description=json_data.get("Description"),
            EnableIpsec=json_data.get("EnableIpsec"),
            EnableSsl=json_data.get("EnableSsl"),
            Id=json_data.get("Id"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InternetIp=json_data.get("InternetIp"),
            Name=json_data.get("Name"),
            Period=json_data.get("Period"),
            SslConnections=json_data.get("SslConnections"),
            Status=json_data.get("Status"),
            VpcId=json_data.get("VpcId"),
            VswitchId=json_data.get("VswitchId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


