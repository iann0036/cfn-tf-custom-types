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
    AccountMoid: Optional[str]
    Actions: Optional[Sequence["_ActionsDefinition3"]]
    AdditionalProperties: Optional[str]
    AdvisoryDetails: Optional[Sequence["_AdvisoryDetailsDefinition"]]
    AdvisoryId: Optional[str]
    Ancestors: Optional[Sequence["_AncestorsDefinition"]]
    ApiDataSources: Optional[Sequence["_ApiDataSourcesDefinition2"]]
    ClassId: Optional[str]
    CreateTime: Optional[str]
    DatePublished: Optional[str]
    DateUpdated: Optional[str]
    Description: Optional[str]
    DomainGroupMoid: Optional[str]
    ExternalUrl: Optional[str]
    Id: Optional[str]
    ModTime: Optional[str]
    Moid: Optional[str]
    Name: Optional[str]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    Organization: Optional[Sequence["_OrganizationDefinition"]]
    Owners: Optional[Sequence[str]]
    Parent: Optional[Sequence["_ParentDefinition"]]
    PermissionResources: Optional[Sequence["_PermissionResourcesDefinition"]]
    Recommendation: Optional[str]
    S3DataSources: Optional[Sequence["_S3DataSourcesDefinition2"]]
    Severity: Optional[Sequence["_SeverityDefinition"]]
    SharedScope: Optional[str]
    State: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Type: Optional[str]
    VersionContext: Optional[Sequence["_VersionContextDefinition3"]]
    Workaround: Optional[str]

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
            AccountMoid=json_data.get("AccountMoid"),
            Actions=deserialize_list(json_data.get("Actions"), ActionsDefinition3),
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AdvisoryDetails=deserialize_list(json_data.get("AdvisoryDetails"), AdvisoryDetailsDefinition),
            AdvisoryId=json_data.get("AdvisoryId"),
            Ancestors=deserialize_list(json_data.get("Ancestors"), AncestorsDefinition),
            ApiDataSources=deserialize_list(json_data.get("ApiDataSources"), ApiDataSourcesDefinition2),
            ClassId=json_data.get("ClassId"),
            CreateTime=json_data.get("CreateTime"),
            DatePublished=json_data.get("DatePublished"),
            DateUpdated=json_data.get("DateUpdated"),
            Description=json_data.get("Description"),
            DomainGroupMoid=json_data.get("DomainGroupMoid"),
            ExternalUrl=json_data.get("ExternalUrl"),
            Id=json_data.get("Id"),
            ModTime=json_data.get("ModTime"),
            Moid=json_data.get("Moid"),
            Name=json_data.get("Name"),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
            Owners=json_data.get("Owners"),
            Parent=deserialize_list(json_data.get("Parent"), ParentDefinition),
            PermissionResources=deserialize_list(json_data.get("PermissionResources"), PermissionResourcesDefinition),
            Recommendation=json_data.get("Recommendation"),
            S3DataSources=deserialize_list(json_data.get("S3DataSources"), S3DataSourcesDefinition2),
            Severity=deserialize_list(json_data.get("Severity"), SeverityDefinition),
            SharedScope=json_data.get("SharedScope"),
            State=json_data.get("State"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Type=json_data.get("Type"),
            VersionContext=deserialize_list(json_data.get("VersionContext"), VersionContextDefinition3),
            Workaround=json_data.get("Workaround"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActionsDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    AffectedObjectType: Optional[str]
    AlertType: Optional[str]
    ClassId: Optional[str]
    Identifiers: Optional[Sequence["_ActionsDefinition"]]
    Name: Optional[str]
    ObjectType: Optional[str]
    OperationType: Optional[str]
    Queries: Optional[Sequence["_ActionsDefinition2"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            AffectedObjectType=json_data.get("AffectedObjectType"),
            AlertType=json_data.get("AlertType"),
            ClassId=json_data.get("ClassId"),
            Identifiers=deserialize_list(json_data.get("Identifiers"), ActionsDefinition),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            OperationType=json_data.get("OperationType"),
            Queries=deserialize_list(json_data.get("Queries"), ActionsDefinition2),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition3 = ActionsDefinition3


@dataclass
class ActionsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition = ActionsDefinition


@dataclass
class ActionsDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Priority: Optional[float]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionsDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Priority=json_data.get("Priority"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionsDefinition2 = ActionsDefinition2


@dataclass
class AdvisoryDetailsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Description: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvisoryDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvisoryDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Description=json_data.get("Description"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvisoryDetailsDefinition = AdvisoryDetailsDefinition


@dataclass
class AncestorsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AncestorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AncestorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AncestorsDefinition = AncestorsDefinition


@dataclass
class ApiDataSourcesDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    MoType: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Queries: Optional[Sequence["_ApiDataSourcesDefinition"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiDataSourcesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiDataSourcesDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            MoType=json_data.get("MoType"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Queries=deserialize_list(json_data.get("Queries"), ApiDataSourcesDefinition),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiDataSourcesDefinition2 = ApiDataSourcesDefinition2


@dataclass
class ApiDataSourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Priority: Optional[float]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiDataSourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiDataSourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Priority=json_data.get("Priority"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiDataSourcesDefinition = ApiDataSourcesDefinition


@dataclass
class OrganizationDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationDefinition = OrganizationDefinition


@dataclass
class ParentDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParentDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParentDefinition = ParentDefinition


@dataclass
class PermissionResourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionResourcesDefinition = PermissionResourcesDefinition


@dataclass
class S3DataSourcesDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Queries: Optional[Sequence["_S3DataSourcesDefinition"]]
    S3Path: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3DataSourcesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3DataSourcesDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Queries=deserialize_list(json_data.get("Queries"), S3DataSourcesDefinition),
            S3Path=json_data.get("S3Path"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3DataSourcesDefinition2 = S3DataSourcesDefinition2


@dataclass
class S3DataSourcesDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Name: Optional[str]
    ObjectType: Optional[str]
    Priority: Optional[float]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3DataSourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3DataSourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Name=json_data.get("Name"),
            ObjectType=json_data.get("ObjectType"),
            Priority=json_data.get("Priority"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3DataSourcesDefinition = S3DataSourcesDefinition


@dataclass
class SeverityDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    ObjectType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeverityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeverityDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            ObjectType=json_data.get("ObjectType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeverityDefinition = SeverityDefinition


@dataclass
class TagsDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class VersionContextDefinition3(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    InterestedMos: Optional[Sequence["_VersionContextDefinition"]]
    NrVersion: Optional[str]
    ObjectType: Optional[str]
    RefMo: Optional[Sequence["_VersionContextDefinition2"]]
    Timestamp: Optional[str]
    VersionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition3"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            InterestedMos=deserialize_list(json_data.get("InterestedMos"), VersionContextDefinition),
            NrVersion=json_data.get("NrVersion"),
            ObjectType=json_data.get("ObjectType"),
            RefMo=deserialize_list(json_data.get("RefMo"), VersionContextDefinition2),
            Timestamp=json_data.get("Timestamp"),
            VersionType=json_data.get("VersionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition3 = VersionContextDefinition3


@dataclass
class VersionContextDefinition(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition = VersionContextDefinition


@dataclass
class VersionContextDefinition2(BaseModel):
    AdditionalProperties: Optional[str]
    ClassId: Optional[str]
    Moid: Optional[str]
    ObjectType: Optional[str]
    Selector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionContextDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionContextDefinition2"]:
        if not json_data:
            return None
        return cls(
            AdditionalProperties=json_data.get("AdditionalProperties"),
            ClassId=json_data.get("ClassId"),
            Moid=json_data.get("Moid"),
            ObjectType=json_data.get("ObjectType"),
            Selector=json_data.get("Selector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionContextDefinition2 = VersionContextDefinition2


