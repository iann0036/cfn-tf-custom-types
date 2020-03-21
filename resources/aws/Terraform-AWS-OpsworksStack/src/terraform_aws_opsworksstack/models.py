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
    AgentVersion: Optional[str]
    Arn: Optional[str]
    BerkshelfVersion: Optional[str]
    Color: Optional[str]
    ConfigurationManagerName: Optional[str]
    ConfigurationManagerVersion: Optional[str]
    CustomJson: Optional[str]
    DefaultAvailabilityZone: Optional[str]
    DefaultInstanceProfileArn: Optional[str]
    DefaultOs: Optional[str]
    DefaultRootDeviceType: Optional[str]
    DefaultSshKeyName: Optional[str]
    DefaultSubnetId: Optional[str]
    HostnameTheme: Optional[str]
    Id: Optional[str]
    ManageBerkshelf: Optional[bool]
    Name: Optional[str]
    Region: Optional[str]
    ServiceRoleArn: Optional[str]
    StackEndpoint: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    UseCustomCookbooks: Optional[bool]
    UseOpsworksSecurityGroups: Optional[bool]
    VpcId: Optional[str]
    CustomCookbooksSource: Optional[Sequence["_CustomCookbooksSource"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AgentVersion=json_data.get("AgentVersion"),
            Arn=json_data.get("Arn"),
            BerkshelfVersion=json_data.get("BerkshelfVersion"),
            Color=json_data.get("Color"),
            ConfigurationManagerName=json_data.get("ConfigurationManagerName"),
            ConfigurationManagerVersion=json_data.get("ConfigurationManagerVersion"),
            CustomJson=json_data.get("CustomJson"),
            DefaultAvailabilityZone=json_data.get("DefaultAvailabilityZone"),
            DefaultInstanceProfileArn=json_data.get("DefaultInstanceProfileArn"),
            DefaultOs=json_data.get("DefaultOs"),
            DefaultRootDeviceType=json_data.get("DefaultRootDeviceType"),
            DefaultSshKeyName=json_data.get("DefaultSshKeyName"),
            DefaultSubnetId=json_data.get("DefaultSubnetId"),
            HostnameTheme=json_data.get("HostnameTheme"),
            Id=json_data.get("Id"),
            ManageBerkshelf=json_data.get("ManageBerkshelf"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            StackEndpoint=json_data.get("StackEndpoint"),
            Tags=json_data.get("Tags"),
            UseCustomCookbooks=json_data.get("UseCustomCookbooks"),
            UseOpsworksSecurityGroups=json_data.get("UseOpsworksSecurityGroups"),
            VpcId=json_data.get("VpcId"),
            CustomCookbooksSource=json_data.get("CustomCookbooksSource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class CustomCookbooksSource:
    Password: Optional[str]
    Revision: Optional[str]
    SshKey: Optional[str]
    Type: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomCookbooksSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomCookbooksSource"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Revision=json_data.get("Revision"),
            SshKey=json_data.get("SshKey"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomCookbooksSource = CustomCookbooksSource


