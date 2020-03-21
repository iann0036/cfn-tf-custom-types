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
    BucketPolicyOnly: Optional[bool]
    DefaultEventBasedHold: Optional[bool]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Location: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    RequesterPays: Optional[bool]
    SelfLink: Optional[str]
    StorageClass: Optional[str]
    Url: Optional[str]
    Cors: Optional[Sequence["_Cors"]]
    Encryption: Optional[Sequence["_Encryption"]]
    LifecycleRule: Optional[Sequence["_LifecycleRule"]]
    Logging: Optional[Sequence["_Logging"]]
    RetentionPolicy: Optional[Sequence["_RetentionPolicy"]]
    Versioning: Optional[Sequence["_Versioning"]]
    Website: Optional[Sequence["_Website"]]
    Action: Optional[Sequence["_Action"]]
    Condition: Optional[Sequence["_Condition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BucketPolicyOnly=json_data.get("BucketPolicyOnly"),
            DefaultEventBasedHold=json_data.get("DefaultEventBasedHold"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            RequesterPays=json_data.get("RequesterPays"),
            SelfLink=json_data.get("SelfLink"),
            StorageClass=json_data.get("StorageClass"),
            Url=json_data.get("Url"),
            Cors=json_data.get("Cors"),
            Encryption=json_data.get("Encryption"),
            LifecycleRule=json_data.get("LifecycleRule"),
            Logging=json_data.get("Logging"),
            RetentionPolicy=json_data.get("RetentionPolicy"),
            Versioning=json_data.get("Versioning"),
            Website=json_data.get("Website"),
            Action=json_data.get("Action"),
            Condition=json_data.get("Condition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Cors:
    MaxAgeSeconds: Optional[float]
    Method: Optional[Sequence[str]]
    Origin: Optional[Sequence[str]]
    ResponseHeader: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Cors"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cors"]:
        if not json_data:
            return None
        return cls(
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
            Method=json_data.get("Method"),
            Origin=json_data.get("Origin"),
            ResponseHeader=json_data.get("ResponseHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cors = Cors


@dataclass
class Encryption:
    DefaultKmsKeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Encryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Encryption"]:
        if not json_data:
            return None
        return cls(
            DefaultKmsKeyName=json_data.get("DefaultKmsKeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Encryption = Encryption


@dataclass
class LifecycleRule:
    Action: Optional[Sequence["_Action"]]
    Condition: Optional[Sequence["_Condition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleRule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Condition=json_data.get("Condition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleRule = LifecycleRule


@dataclass
class Action:
    StorageClass: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            StorageClass=json_data.get("StorageClass"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Condition:
    Age: Optional[float]
    CreatedBefore: Optional[str]
    IsLive: Optional[bool]
    MatchesStorageClass: Optional[Sequence[str]]
    NumNewerVersions: Optional[float]
    WithState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            Age=json_data.get("Age"),
            CreatedBefore=json_data.get("CreatedBefore"),
            IsLive=json_data.get("IsLive"),
            MatchesStorageClass=json_data.get("MatchesStorageClass"),
            NumNewerVersions=json_data.get("NumNewerVersions"),
            WithState=json_data.get("WithState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


@dataclass
class Logging:
    LogBucket: Optional[str]
    LogObjectPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            LogBucket=json_data.get("LogBucket"),
            LogObjectPrefix=json_data.get("LogObjectPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class RetentionPolicy:
    IsLocked: Optional[bool]
    RetentionPeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicy"]:
        if not json_data:
            return None
        return cls(
            IsLocked=json_data.get("IsLocked"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicy = RetentionPolicy


@dataclass
class Versioning:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Versioning"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Versioning"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Versioning = Versioning


@dataclass
class Website:
    MainPageSuffix: Optional[str]
    NotFoundPage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Website"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Website"]:
        if not json_data:
            return None
        return cls(
            MainPageSuffix=json_data.get("MainPageSuffix"),
            NotFoundPage=json_data.get("NotFoundPage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Website = Website


