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
    AccessMode: Optional[str]
    BasicAuthEnabled: Optional[bool]
    BasicAuthPassword: Optional[str]
    BasicAuthUsername: Optional[str]
    DatabaseName: Optional[str]
    Id: Optional[str]
    IsDefault: Optional[bool]
    Name: Optional[str]
    Password: Optional[str]
    Type: Optional[str]
    Url: Optional[str]
    Username: Optional[str]
    JsonData: Optional[Sequence["_JsonData"]]
    SecureJsonData: Optional[Sequence["_SecureJsonData"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessMode=json_data.get("AccessMode"),
            BasicAuthEnabled=json_data.get("BasicAuthEnabled"),
            BasicAuthPassword=json_data.get("BasicAuthPassword"),
            BasicAuthUsername=json_data.get("BasicAuthUsername"),
            DatabaseName=json_data.get("DatabaseName"),
            Id=json_data.get("Id"),
            IsDefault=json_data.get("IsDefault"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
            JsonData=json_data.get("JsonData"),
            SecureJsonData=json_data.get("SecureJsonData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class JsonData:
    AssumeRoleArn: Optional[str]
    AuthType: Optional[str]
    CustomMetricsNamespaces: Optional[str]
    DefaultRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonData"]:
        if not json_data:
            return None
        return cls(
            AssumeRoleArn=json_data.get("AssumeRoleArn"),
            AuthType=json_data.get("AuthType"),
            CustomMetricsNamespaces=json_data.get("CustomMetricsNamespaces"),
            DefaultRegion=json_data.get("DefaultRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonData = JsonData


@dataclass
class SecureJsonData:
    AccessKey: Optional[str]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecureJsonData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecureJsonData"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecureJsonData = SecureJsonData


