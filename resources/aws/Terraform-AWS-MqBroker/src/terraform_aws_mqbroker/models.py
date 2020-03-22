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
    ApplyImmediately: Optional[bool]
    Arn: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    BrokerName: Optional[str]
    DeploymentMode: Optional[str]
    EngineType: Optional[str]
    EngineVersion: Optional[str]
    HostInstanceType: Optional[str]
    Id: Optional[str]
    Instances: Optional[Sequence["_Instances"]]
    PubliclyAccessible: Optional[bool]
    SecurityGroups: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    Configuration: Optional[Sequence["_Configuration"]]
    EncryptionOptions: Optional[Sequence["_EncryptionOptions"]]
    Logs: Optional[Sequence["_Logs"]]
    MaintenanceWindowStartTime: Optional[Sequence["_MaintenanceWindowStartTime"]]
    User: Optional[Sequence["_User"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApplyImmediately=json_data.get("ApplyImmediately"),
            Arn=json_data.get("Arn"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            BrokerName=json_data.get("BrokerName"),
            DeploymentMode=json_data.get("DeploymentMode"),
            EngineType=json_data.get("EngineType"),
            EngineVersion=json_data.get("EngineVersion"),
            HostInstanceType=json_data.get("HostInstanceType"),
            Id=json_data.get("Id"),
            Instances=json_data.get("Instances"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            Configuration=json_data.get("Configuration"),
            EncryptionOptions=json_data.get("EncryptionOptions"),
            Logs=json_data.get("Logs"),
            MaintenanceWindowStartTime=json_data.get("MaintenanceWindowStartTime"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Instances:
    ConsoleUrl: Optional[str]
    Endpoints: Optional[Sequence[str]]
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Instances"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Instances"]:
        if not json_data:
            return None
        return cls(
            ConsoleUrl=json_data.get("ConsoleUrl"),
            Endpoints=json_data.get("Endpoints"),
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Instances = Instances


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Configuration:
    Id: Optional[str]
    Revision: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configuration"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Revision=json_data.get("Revision"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configuration = Configuration


@dataclass
class EncryptionOptions:
    KmsKeyId: Optional[str]
    UseAwsOwnedKey: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionOptions"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            UseAwsOwnedKey=json_data.get("UseAwsOwnedKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionOptions = EncryptionOptions


@dataclass
class Logs:
    Audit: Optional[bool]
    General: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Logs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logs"]:
        if not json_data:
            return None
        return cls(
            Audit=json_data.get("Audit"),
            General=json_data.get("General"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logs = Logs


@dataclass
class MaintenanceWindowStartTime:
    DayOfWeek: Optional[str]
    TimeOfDay: Optional[str]
    TimeZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowStartTime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowStartTime"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            TimeOfDay=json_data.get("TimeOfDay"),
            TimeZone=json_data.get("TimeZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowStartTime = MaintenanceWindowStartTime


@dataclass
class User:
    ConsoleAccess: Optional[bool]
    Groups: Optional[Sequence[str]]
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_User"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_User"]:
        if not json_data:
            return None
        return cls(
            ConsoleAccess=json_data.get("ConsoleAccess"),
            Groups=json_data.get("Groups"),
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_User = User


