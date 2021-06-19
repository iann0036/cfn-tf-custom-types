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
    Alias: Optional[str]
    CustomerUserName: Optional[str]
    DirectoryId: Optional[str]
    DirectoryName: Optional[str]
    DirectoryType: Optional[str]
    DnsIpAddresses: Optional[Sequence[str]]
    IamRoleId: Optional[str]
    Id: Optional[str]
    IpGroupIds: Optional[Sequence[str]]
    RegistrationCode: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    WorkspaceSecurityGroupId: Optional[str]
    SelfServicePermissions: Optional[Sequence["_SelfServicePermissionsDefinition"]]
    WorkspaceAccessProperties: Optional[Sequence["_WorkspaceAccessPropertiesDefinition"]]
    WorkspaceCreationProperties: Optional[Sequence["_WorkspaceCreationPropertiesDefinition"]]

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
            Alias=json_data.get("Alias"),
            CustomerUserName=json_data.get("CustomerUserName"),
            DirectoryId=json_data.get("DirectoryId"),
            DirectoryName=json_data.get("DirectoryName"),
            DirectoryType=json_data.get("DirectoryType"),
            DnsIpAddresses=json_data.get("DnsIpAddresses"),
            IamRoleId=json_data.get("IamRoleId"),
            Id=json_data.get("Id"),
            IpGroupIds=json_data.get("IpGroupIds"),
            RegistrationCode=json_data.get("RegistrationCode"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            WorkspaceSecurityGroupId=json_data.get("WorkspaceSecurityGroupId"),
            SelfServicePermissions=deserialize_list(json_data.get("SelfServicePermissions"), SelfServicePermissionsDefinition),
            WorkspaceAccessProperties=deserialize_list(json_data.get("WorkspaceAccessProperties"), WorkspaceAccessPropertiesDefinition),
            WorkspaceCreationProperties=deserialize_list(json_data.get("WorkspaceCreationProperties"), WorkspaceCreationPropertiesDefinition),
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


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class SelfServicePermissionsDefinition(BaseModel):
    ChangeComputeType: Optional[bool]
    IncreaseVolumeSize: Optional[bool]
    RebuildWorkspace: Optional[bool]
    RestartWorkspace: Optional[bool]
    SwitchRunningMode: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SelfServicePermissionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfServicePermissionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ChangeComputeType=json_data.get("ChangeComputeType"),
            IncreaseVolumeSize=json_data.get("IncreaseVolumeSize"),
            RebuildWorkspace=json_data.get("RebuildWorkspace"),
            RestartWorkspace=json_data.get("RestartWorkspace"),
            SwitchRunningMode=json_data.get("SwitchRunningMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelfServicePermissionsDefinition = SelfServicePermissionsDefinition


@dataclass
class WorkspaceAccessPropertiesDefinition(BaseModel):
    DeviceTypeAndroid: Optional[str]
    DeviceTypeChromeos: Optional[str]
    DeviceTypeIos: Optional[str]
    DeviceTypeOsx: Optional[str]
    DeviceTypeWeb: Optional[str]
    DeviceTypeWindows: Optional[str]
    DeviceTypeZeroclient: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkspaceAccessPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkspaceAccessPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceTypeAndroid=json_data.get("DeviceTypeAndroid"),
            DeviceTypeChromeos=json_data.get("DeviceTypeChromeos"),
            DeviceTypeIos=json_data.get("DeviceTypeIos"),
            DeviceTypeOsx=json_data.get("DeviceTypeOsx"),
            DeviceTypeWeb=json_data.get("DeviceTypeWeb"),
            DeviceTypeWindows=json_data.get("DeviceTypeWindows"),
            DeviceTypeZeroclient=json_data.get("DeviceTypeZeroclient"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkspaceAccessPropertiesDefinition = WorkspaceAccessPropertiesDefinition


@dataclass
class WorkspaceCreationPropertiesDefinition(BaseModel):
    CustomSecurityGroupId: Optional[str]
    DefaultOu: Optional[str]
    EnableInternetAccess: Optional[bool]
    EnableMaintenanceMode: Optional[bool]
    UserEnabledAsLocalAdministrator: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_WorkspaceCreationPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkspaceCreationPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomSecurityGroupId=json_data.get("CustomSecurityGroupId"),
            DefaultOu=json_data.get("DefaultOu"),
            EnableInternetAccess=json_data.get("EnableInternetAccess"),
            EnableMaintenanceMode=json_data.get("EnableMaintenanceMode"),
            UserEnabledAsLocalAdministrator=json_data.get("UserEnabledAsLocalAdministrator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkspaceCreationPropertiesDefinition = WorkspaceCreationPropertiesDefinition


