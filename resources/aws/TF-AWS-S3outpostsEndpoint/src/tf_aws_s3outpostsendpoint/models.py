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
    Arn: Optional[str]
    CidrBlock: Optional[str]
    CreationTime: Optional[str]
    Id: Optional[str]
    NetworkInterfaces: Optional[Sequence["_NetworkInterfacesDefinition"]]
    OutpostId: Optional[str]
    SecurityGroupId: Optional[str]
    SubnetId: Optional[str]

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
            Arn=json_data.get("Arn"),
            CidrBlock=json_data.get("CidrBlock"),
            CreationTime=json_data.get("CreationTime"),
            Id=json_data.get("Id"),
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), NetworkInterfacesDefinition),
            OutpostId=json_data.get("OutpostId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkInterfacesDefinition(BaseModel):
    NetworkInterfaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfacesDefinition = NetworkInterfacesDefinition


