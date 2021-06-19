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
    Action: Optional[str]
    AvailabilityZone: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Port: Optional[float]
    Provider2: Optional[str]
    Region: Optional[str]
    SecretValue: Optional[str]
    UseMgmtPort: Optional[float]
    UserName: Optional[str]
    ThunderMgmtIp: Optional[Sequence["_ThunderMgmtIpDefinition"]]

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
            Action=json_data.get("Action"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
            Provider2=json_data.get("Provider2"),
            Region=json_data.get("Region"),
            SecretValue=json_data.get("SecretValue"),
            UseMgmtPort=json_data.get("UseMgmtPort"),
            UserName=json_data.get("UserName"),
            ThunderMgmtIp=deserialize_list(json_data.get("ThunderMgmtIp"), ThunderMgmtIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ThunderMgmtIpDefinition(BaseModel):
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThunderMgmtIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThunderMgmtIpDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThunderMgmtIpDefinition = ThunderMgmtIpDefinition


