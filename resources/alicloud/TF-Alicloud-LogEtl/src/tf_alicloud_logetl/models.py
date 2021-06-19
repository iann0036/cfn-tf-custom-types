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
    AccessKeyId: Optional[str]
    AccessKeySecret: Optional[str]
    CreateTime: Optional[float]
    Description: Optional[str]
    DisplayName: Optional[str]
    EtlName: Optional[str]
    EtlType: Optional[str]
    FromTime: Optional[float]
    Id: Optional[str]
    KmsEncryptedAccessKeyId: Optional[str]
    KmsEncryptedAccessKeySecret: Optional[str]
    KmsEncryptionAccessKeyIdContext: Optional[Sequence["_KmsEncryptionAccessKeyIdContextDefinition"]]
    KmsEncryptionAccessKeySecretContext: Optional[Sequence["_KmsEncryptionAccessKeySecretContextDefinition"]]
    LastModifiedTime: Optional[float]
    Logstore: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    Project: Optional[str]
    RoleArn: Optional[str]
    Schedule: Optional[str]
    Script: Optional[str]
    Status: Optional[str]
    ToTime: Optional[float]
    Version: Optional[float]
    EtlSinks: Optional[Sequence["_EtlSinksDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AccessKeyId=json_data.get("AccessKeyId"),
            AccessKeySecret=json_data.get("AccessKeySecret"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            EtlName=json_data.get("EtlName"),
            EtlType=json_data.get("EtlType"),
            FromTime=json_data.get("FromTime"),
            Id=json_data.get("Id"),
            KmsEncryptedAccessKeyId=json_data.get("KmsEncryptedAccessKeyId"),
            KmsEncryptedAccessKeySecret=json_data.get("KmsEncryptedAccessKeySecret"),
            KmsEncryptionAccessKeyIdContext=deserialize_list(json_data.get("KmsEncryptionAccessKeyIdContext"), KmsEncryptionAccessKeyIdContextDefinition),
            KmsEncryptionAccessKeySecretContext=deserialize_list(json_data.get("KmsEncryptionAccessKeySecretContext"), KmsEncryptionAccessKeySecretContextDefinition),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Logstore=json_data.get("Logstore"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Project=json_data.get("Project"),
            RoleArn=json_data.get("RoleArn"),
            Schedule=json_data.get("Schedule"),
            Script=json_data.get("Script"),
            Status=json_data.get("Status"),
            ToTime=json_data.get("ToTime"),
            Version=json_data.get("Version"),
            EtlSinks=deserialize_list(json_data.get("EtlSinks"), EtlSinksDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KmsEncryptionAccessKeyIdContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionAccessKeyIdContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionAccessKeyIdContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionAccessKeyIdContextDefinition = KmsEncryptionAccessKeyIdContextDefinition


@dataclass
class KmsEncryptionAccessKeySecretContextDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionAccessKeySecretContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionAccessKeySecretContextDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionAccessKeySecretContextDefinition = KmsEncryptionAccessKeySecretContextDefinition


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class EtlSinksDefinition(BaseModel):
    AccessKeyId: Optional[str]
    AccessKeySecret: Optional[str]
    Endpoint: Optional[str]
    KmsEncryptedAccessKeyId: Optional[str]
    KmsEncryptedAccessKeySecret: Optional[str]
    Logstore: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    RoleArn: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EtlSinksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EtlSinksDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKeyId=json_data.get("AccessKeyId"),
            AccessKeySecret=json_data.get("AccessKeySecret"),
            Endpoint=json_data.get("Endpoint"),
            KmsEncryptedAccessKeyId=json_data.get("KmsEncryptedAccessKeyId"),
            KmsEncryptedAccessKeySecret=json_data.get("KmsEncryptedAccessKeySecret"),
            Logstore=json_data.get("Logstore"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            RoleArn=json_data.get("RoleArn"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EtlSinksDefinition = EtlSinksDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


