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
    ConnectionName: Optional[str]
    ConnectionType: Optional[str]
    EnableLearnedCidrsApproval: Optional[bool]
    Id: Optional[str]
    InsideIpCidrTun1: Optional[str]
    InsideIpCidrTun2: Optional[str]
    PreSharedKeyTun1: Optional[str]
    PreSharedKeyTun2: Optional[str]
    PublicIp: Optional[str]
    RemoteAsNumber: Optional[str]
    RemoteCidr: Optional[str]
    RouteDomainName: Optional[str]
    TgwName: Optional[str]
    VpnId: Optional[str]

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
            ConnectionName=json_data.get("ConnectionName"),
            ConnectionType=json_data.get("ConnectionType"),
            EnableLearnedCidrsApproval=json_data.get("EnableLearnedCidrsApproval"),
            Id=json_data.get("Id"),
            InsideIpCidrTun1=json_data.get("InsideIpCidrTun1"),
            InsideIpCidrTun2=json_data.get("InsideIpCidrTun2"),
            PreSharedKeyTun1=json_data.get("PreSharedKeyTun1"),
            PreSharedKeyTun2=json_data.get("PreSharedKeyTun2"),
            PublicIp=json_data.get("PublicIp"),
            RemoteAsNumber=json_data.get("RemoteAsNumber"),
            RemoteCidr=json_data.get("RemoteCidr"),
            RouteDomainName=json_data.get("RouteDomainName"),
            TgwName=json_data.get("TgwName"),
            VpnId=json_data.get("VpnId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


