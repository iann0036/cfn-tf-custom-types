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
    AvailabilityDomain: Optional[str]
    BootstrapBucketName: Optional[str]
    BootstrapStorageName: Optional[str]
    CloudType: Optional[float]
    ContainerFolder: Optional[str]
    EgressInterface: Optional[str]
    EgressSubnet: Optional[str]
    EgressVpcId: Optional[str]
    FaultDomain: Optional[str]
    FileShareFolder: Optional[str]
    FirenetGwName: Optional[str]
    FirewallImage: Optional[str]
    FirewallImageId: Optional[str]
    FirewallImageVersion: Optional[str]
    FirewallName: Optional[str]
    FirewallSize: Optional[str]
    GcpVpcId: Optional[str]
    IamRole: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    KeyName: Optional[str]
    LanInterface: Optional[str]
    ManagementInterface: Optional[str]
    ManagementSubnet: Optional[str]
    ManagementVpcId: Optional[str]
    Password: Optional[str]
    PublicIp: Optional[str]
    SasUrlConfig: Optional[str]
    SasUrlLicense: Optional[str]
    ShareDirectory: Optional[str]
    SicKey: Optional[str]
    SshPublicKey: Optional[str]
    StorageAccessKey: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UserData: Optional[str]
    Username: Optional[str]
    VpcId: Optional[str]
    Zone: Optional[str]

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
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            BootstrapBucketName=json_data.get("BootstrapBucketName"),
            BootstrapStorageName=json_data.get("BootstrapStorageName"),
            CloudType=json_data.get("CloudType"),
            ContainerFolder=json_data.get("ContainerFolder"),
            EgressInterface=json_data.get("EgressInterface"),
            EgressSubnet=json_data.get("EgressSubnet"),
            EgressVpcId=json_data.get("EgressVpcId"),
            FaultDomain=json_data.get("FaultDomain"),
            FileShareFolder=json_data.get("FileShareFolder"),
            FirenetGwName=json_data.get("FirenetGwName"),
            FirewallImage=json_data.get("FirewallImage"),
            FirewallImageId=json_data.get("FirewallImageId"),
            FirewallImageVersion=json_data.get("FirewallImageVersion"),
            FirewallName=json_data.get("FirewallName"),
            FirewallSize=json_data.get("FirewallSize"),
            GcpVpcId=json_data.get("GcpVpcId"),
            IamRole=json_data.get("IamRole"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            KeyName=json_data.get("KeyName"),
            LanInterface=json_data.get("LanInterface"),
            ManagementInterface=json_data.get("ManagementInterface"),
            ManagementSubnet=json_data.get("ManagementSubnet"),
            ManagementVpcId=json_data.get("ManagementVpcId"),
            Password=json_data.get("Password"),
            PublicIp=json_data.get("PublicIp"),
            SasUrlConfig=json_data.get("SasUrlConfig"),
            SasUrlLicense=json_data.get("SasUrlLicense"),
            ShareDirectory=json_data.get("ShareDirectory"),
            SicKey=json_data.get("SicKey"),
            SshPublicKey=json_data.get("SshPublicKey"),
            StorageAccessKey=json_data.get("StorageAccessKey"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UserData=json_data.get("UserData"),
            Username=json_data.get("Username"),
            VpcId=json_data.get("VpcId"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


