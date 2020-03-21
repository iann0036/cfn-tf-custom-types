# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Agency: Optional[str]
    Created: Optional[str]
    CurrentTask: Optional[str]
    Flavor: Optional[str]
    Id: Optional[str]
    InnerEndpoint: Optional[str]
    Name: Optional[str]
    PublicEndpoint: Optional[str]
    Region: Optional[str]
    Status: Optional[str]
    Updated: Optional[str]
    Version: Optional[str]
    MrsCluster: Optional[Sequence["_MrsCluster"]]
    Network: Optional[Sequence["_Network"]]
    Timeouts: Optional["_Timeouts"]
    PublicIp: Optional[Sequence["_PublicIp"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Agency=json_data.get("Agency"),
            Created=json_data.get("Created"),
            CurrentTask=json_data.get("CurrentTask"),
            Flavor=json_data.get("Flavor"),
            Id=json_data.get("Id"),
            InnerEndpoint=json_data.get("InnerEndpoint"),
            Name=json_data.get("Name"),
            PublicEndpoint=json_data.get("PublicEndpoint"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Updated=json_data.get("Updated"),
            Version=json_data.get("Version"),
            MrsCluster=json_data.get("MrsCluster"),
            Network=json_data.get("Network"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            PublicIp=json_data.get("PublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MrsCluster:
    Id: Optional[str]
    UserName: Optional[str]
    UserPassword: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MrsCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MrsCluster"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            UserName=json_data.get("UserName"),
            UserPassword=json_data.get("UserPassword"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MrsCluster = MrsCluster


@dataclass
class Network:
    AvailableZone: Optional[str]
    NetworkId: Optional[str]
    SecurityGroupId: Optional[str]
    VpcId: Optional[str]
    PublicIp: Optional[Sequence["_PublicIp"]]

    @classmethod
    def _deserialize(
        cls: Type["_Network"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Network"]:
        if not json_data:
            return None
        return cls(
            AvailableZone=json_data.get("AvailableZone"),
            NetworkId=json_data.get("NetworkId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            VpcId=json_data.get("VpcId"),
            PublicIp=json_data.get("PublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Network = Network


@dataclass
class PublicIp:
    BindType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIp"]:
        if not json_data:
            return None
        return cls(
            BindType=json_data.get("BindType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIp = PublicIp


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


