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
    CreatedOrUpdatedBy: Optional[str]
    CreatedOrUpdatedTime: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IntgGuid: Optional[str]
    Name: Optional[str]
    OrgLevel: Optional[bool]
    QueueUrl: Optional[str]
    Retries: Optional[float]
    TypeName: Optional[str]
    Credentials: Optional[Sequence["_CredentialsDefinition"]]
    OrgAccountMappings: Optional[Sequence["_OrgAccountMappingsDefinition"]]

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
            CreatedOrUpdatedBy=json_data.get("CreatedOrUpdatedBy"),
            CreatedOrUpdatedTime=json_data.get("CreatedOrUpdatedTime"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IntgGuid=json_data.get("IntgGuid"),
            Name=json_data.get("Name"),
            OrgLevel=json_data.get("OrgLevel"),
            QueueUrl=json_data.get("QueueUrl"),
            Retries=json_data.get("Retries"),
            TypeName=json_data.get("TypeName"),
            Credentials=deserialize_list(json_data.get("Credentials"), CredentialsDefinition),
            OrgAccountMappings=deserialize_list(json_data.get("OrgAccountMappings"), OrgAccountMappingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CredentialsDefinition(BaseModel):
    ExternalId: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalId=json_data.get("ExternalId"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialsDefinition = CredentialsDefinition


@dataclass
class OrgAccountMappingsDefinition(BaseModel):
    DefaultLaceworkAccount: Optional[str]
    Mapping: Optional[Sequence["_MappingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OrgAccountMappingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrgAccountMappingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultLaceworkAccount=json_data.get("DefaultLaceworkAccount"),
            Mapping=deserialize_list(json_data.get("Mapping"), MappingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrgAccountMappingsDefinition = OrgAccountMappingsDefinition


@dataclass
class MappingDefinition(BaseModel):
    AwsAccounts: Optional[Sequence[str]]
    LaceworkAccount: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingDefinition"]:
        if not json_data:
            return None
        return cls(
            AwsAccounts=json_data.get("AwsAccounts"),
            LaceworkAccount=json_data.get("LaceworkAccount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingDefinition = MappingDefinition


