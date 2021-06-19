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
    ApplyImmediately: Optional[bool]
    Arn: Optional[str]
    AuthenticationStrategy: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    BrokerName: Optional[str]
    DeploymentMode: Optional[str]
    EngineType: Optional[str]
    EngineVersion: Optional[str]
    HostInstanceType: Optional[str]
    Id: Optional[str]
    Instances: Optional[Sequence["_InstancesDefinition"]]
    PubliclyAccessible: Optional[bool]
    SecurityGroups: Optional[Sequence[str]]
    StorageType: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Configuration: Optional[Sequence["_ConfigurationDefinition"]]
    EncryptionOptions: Optional[Sequence["_EncryptionOptionsDefinition"]]
    LdapServerMetadata: Optional[Sequence["_LdapServerMetadataDefinition"]]
    Logs: Optional[Sequence["_LogsDefinition"]]
    MaintenanceWindowStartTime: Optional[Sequence["_MaintenanceWindowStartTimeDefinition"]]
    User: Optional[Sequence["_UserDefinition"]]

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
            ApplyImmediately=json_data.get("ApplyImmediately"),
            Arn=json_data.get("Arn"),
            AuthenticationStrategy=json_data.get("AuthenticationStrategy"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            BrokerName=json_data.get("BrokerName"),
            DeploymentMode=json_data.get("DeploymentMode"),
            EngineType=json_data.get("EngineType"),
            EngineVersion=json_data.get("EngineVersion"),
            HostInstanceType=json_data.get("HostInstanceType"),
            Id=json_data.get("Id"),
            Instances=deserialize_list(json_data.get("Instances"), InstancesDefinition),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            SecurityGroups=json_data.get("SecurityGroups"),
            StorageType=json_data.get("StorageType"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationDefinition),
            EncryptionOptions=deserialize_list(json_data.get("EncryptionOptions"), EncryptionOptionsDefinition),
            LdapServerMetadata=deserialize_list(json_data.get("LdapServerMetadata"), LdapServerMetadataDefinition),
            Logs=deserialize_list(json_data.get("Logs"), LogsDefinition),
            MaintenanceWindowStartTime=deserialize_list(json_data.get("MaintenanceWindowStartTime"), MaintenanceWindowStartTimeDefinition),
            User=deserialize_list(json_data.get("User"), UserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InstancesDefinition(BaseModel):
    ConsoleUrl: Optional[str]
    Endpoints: Optional[Sequence[str]]
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstancesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancesDefinition"]:
        if not json_data:
            return None
        return cls(
            ConsoleUrl=json_data.get("ConsoleUrl"),
            Endpoints=json_data.get("Endpoints"),
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancesDefinition = InstancesDefinition


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
class ConfigurationDefinition(BaseModel):
    Id: Optional[str]
    Revision: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Revision=json_data.get("Revision"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDefinition = ConfigurationDefinition


@dataclass
class EncryptionOptionsDefinition(BaseModel):
    KmsKeyId: Optional[str]
    UseAwsOwnedKey: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            UseAwsOwnedKey=json_data.get("UseAwsOwnedKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionOptionsDefinition = EncryptionOptionsDefinition


@dataclass
class LdapServerMetadataDefinition(BaseModel):
    Hosts: Optional[Sequence[str]]
    RoleBase: Optional[str]
    RoleName: Optional[str]
    RoleSearchMatching: Optional[str]
    RoleSearchSubtree: Optional[bool]
    ServiceAccountPassword: Optional[str]
    ServiceAccountUsername: Optional[str]
    UserBase: Optional[str]
    UserRoleName: Optional[str]
    UserSearchMatching: Optional[str]
    UserSearchSubtree: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LdapServerMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LdapServerMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            Hosts=json_data.get("Hosts"),
            RoleBase=json_data.get("RoleBase"),
            RoleName=json_data.get("RoleName"),
            RoleSearchMatching=json_data.get("RoleSearchMatching"),
            RoleSearchSubtree=json_data.get("RoleSearchSubtree"),
            ServiceAccountPassword=json_data.get("ServiceAccountPassword"),
            ServiceAccountUsername=json_data.get("ServiceAccountUsername"),
            UserBase=json_data.get("UserBase"),
            UserRoleName=json_data.get("UserRoleName"),
            UserSearchMatching=json_data.get("UserSearchMatching"),
            UserSearchSubtree=json_data.get("UserSearchSubtree"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LdapServerMetadataDefinition = LdapServerMetadataDefinition


@dataclass
class LogsDefinition(BaseModel):
    Audit: Optional[str]
    General: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogsDefinition"]:
        if not json_data:
            return None
        return cls(
            Audit=json_data.get("Audit"),
            General=json_data.get("General"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogsDefinition = LogsDefinition


@dataclass
class MaintenanceWindowStartTimeDefinition(BaseModel):
    DayOfWeek: Optional[str]
    TimeOfDay: Optional[str]
    TimeZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowStartTimeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowStartTimeDefinition"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            TimeOfDay=json_data.get("TimeOfDay"),
            TimeZone=json_data.get("TimeZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowStartTimeDefinition = MaintenanceWindowStartTimeDefinition


@dataclass
class UserDefinition(BaseModel):
    ConsoleAccess: Optional[bool]
    Groups: Optional[Sequence[str]]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinition"]:
        if not json_data:
            return None
        return cls(
            ConsoleAccess=json_data.get("ConsoleAccess"),
            Groups=json_data.get("Groups"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinition = UserDefinition


