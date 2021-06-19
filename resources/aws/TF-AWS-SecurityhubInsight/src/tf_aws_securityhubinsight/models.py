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
    Arn: Optional[str]
    GroupByAttribute: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Filters: Optional[Sequence["_FiltersDefinition"]]

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
            Arn=json_data.get("Arn"),
            GroupByAttribute=json_data.get("GroupByAttribute"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FiltersDefinition(BaseModel):
    AwsAccountId: Optional[Sequence["_AwsAccountIdDefinition"]]
    CompanyName: Optional[Sequence["_CompanyNameDefinition"]]
    ComplianceStatus: Optional[Sequence["_ComplianceStatusDefinition"]]
    Confidence: Optional[Sequence["_ConfidenceDefinition"]]
    CreatedAt: Optional[Sequence["_CreatedAtDefinition"]]
    Criticality: Optional[Sequence["_CriticalityDefinition"]]
    Description: Optional[Sequence["_DescriptionDefinition"]]
    FindingProviderFieldsConfidence: Optional[Sequence["_FindingProviderFieldsConfidenceDefinition"]]
    FindingProviderFieldsCriticality: Optional[Sequence["_FindingProviderFieldsCriticalityDefinition"]]
    FindingProviderFieldsRelatedFindingsId: Optional[Sequence["_FindingProviderFieldsRelatedFindingsIdDefinition"]]
    FindingProviderFieldsRelatedFindingsProductArn: Optional[Sequence["_FindingProviderFieldsRelatedFindingsProductArnDefinition"]]
    FindingProviderFieldsSeverityLabel: Optional[Sequence["_FindingProviderFieldsSeverityLabelDefinition"]]
    FindingProviderFieldsSeverityOriginal: Optional[Sequence["_FindingProviderFieldsSeverityOriginalDefinition"]]
    FindingProviderFieldsTypes: Optional[Sequence["_FindingProviderFieldsTypesDefinition"]]
    FirstObservedAt: Optional[Sequence["_FirstObservedAtDefinition"]]
    GeneratorId: Optional[Sequence["_GeneratorIdDefinition"]]
    Id: Optional[Sequence["_IdDefinition"]]
    Keyword: Optional[Sequence["_KeywordDefinition"]]
    LastObservedAt: Optional[Sequence["_LastObservedAtDefinition"]]
    MalwareName: Optional[Sequence["_MalwareNameDefinition"]]
    MalwarePath: Optional[Sequence["_MalwarePathDefinition"]]
    MalwareState: Optional[Sequence["_MalwareStateDefinition"]]
    MalwareType: Optional[Sequence["_MalwareTypeDefinition"]]
    NetworkDestinationDomain: Optional[Sequence["_NetworkDestinationDomainDefinition"]]
    NetworkDestinationIpv4: Optional[Sequence["_NetworkDestinationIpv4Definition"]]
    NetworkDestinationIpv6: Optional[Sequence["_NetworkDestinationIpv6Definition"]]
    NetworkDestinationPort: Optional[Sequence["_NetworkDestinationPortDefinition"]]
    NetworkDirection: Optional[Sequence["_NetworkDirectionDefinition"]]
    NetworkProtocol: Optional[Sequence["_NetworkProtocolDefinition"]]
    NetworkSourceDomain: Optional[Sequence["_NetworkSourceDomainDefinition"]]
    NetworkSourceIpv4: Optional[Sequence["_NetworkSourceIpv4Definition"]]
    NetworkSourceIpv6: Optional[Sequence["_NetworkSourceIpv6Definition"]]
    NetworkSourceMac: Optional[Sequence["_NetworkSourceMacDefinition"]]
    NetworkSourcePort: Optional[Sequence["_NetworkSourcePortDefinition"]]
    NoteText: Optional[Sequence["_NoteTextDefinition"]]
    NoteUpdatedAt: Optional[Sequence["_NoteUpdatedAtDefinition"]]
    NoteUpdatedBy: Optional[Sequence["_NoteUpdatedByDefinition"]]
    ProcessLaunchedAt: Optional[Sequence["_ProcessLaunchedAtDefinition"]]
    ProcessName: Optional[Sequence["_ProcessNameDefinition"]]
    ProcessParentPid: Optional[Sequence["_ProcessParentPidDefinition"]]
    ProcessPath: Optional[Sequence["_ProcessPathDefinition"]]
    ProcessPid: Optional[Sequence["_ProcessPidDefinition"]]
    ProcessTerminatedAt: Optional[Sequence["_ProcessTerminatedAtDefinition"]]
    ProductArn: Optional[Sequence["_ProductArnDefinition"]]
    ProductFields: Optional[Sequence["_ProductFieldsDefinition"]]
    ProductName: Optional[Sequence["_ProductNameDefinition"]]
    RecommendationText: Optional[Sequence["_RecommendationTextDefinition"]]
    RecordState: Optional[Sequence["_RecordStateDefinition"]]
    RelatedFindingsId: Optional[Sequence["_RelatedFindingsIdDefinition"]]
    RelatedFindingsProductArn: Optional[Sequence["_RelatedFindingsProductArnDefinition"]]
    ResourceAwsEc2InstanceIamInstanceProfileArn: Optional[Sequence["_ResourceAwsEc2InstanceIamInstanceProfileArnDefinition"]]
    ResourceAwsEc2InstanceImageId: Optional[Sequence["_ResourceAwsEc2InstanceImageIdDefinition"]]
    ResourceAwsEc2InstanceIpv4Addresses: Optional[Sequence["_ResourceAwsEc2InstanceIpv4AddressesDefinition"]]
    ResourceAwsEc2InstanceIpv6Addresses: Optional[Sequence["_ResourceAwsEc2InstanceIpv6AddressesDefinition"]]
    ResourceAwsEc2InstanceKeyName: Optional[Sequence["_ResourceAwsEc2InstanceKeyNameDefinition"]]
    ResourceAwsEc2InstanceLaunchedAt: Optional[Sequence["_ResourceAwsEc2InstanceLaunchedAtDefinition"]]
    ResourceAwsEc2InstanceSubnetId: Optional[Sequence["_ResourceAwsEc2InstanceSubnetIdDefinition"]]
    ResourceAwsEc2InstanceType: Optional[Sequence["_ResourceAwsEc2InstanceTypeDefinition"]]
    ResourceAwsEc2InstanceVpcId: Optional[Sequence["_ResourceAwsEc2InstanceVpcIdDefinition"]]
    ResourceAwsIamAccessKeyCreatedAt: Optional[Sequence["_ResourceAwsIamAccessKeyCreatedAtDefinition"]]
    ResourceAwsIamAccessKeyStatus: Optional[Sequence["_ResourceAwsIamAccessKeyStatusDefinition"]]
    ResourceAwsIamAccessKeyUserName: Optional[Sequence["_ResourceAwsIamAccessKeyUserNameDefinition"]]
    ResourceAwsS3BucketOwnerId: Optional[Sequence["_ResourceAwsS3BucketOwnerIdDefinition"]]
    ResourceAwsS3BucketOwnerName: Optional[Sequence["_ResourceAwsS3BucketOwnerNameDefinition"]]
    ResourceContainerImageId: Optional[Sequence["_ResourceContainerImageIdDefinition"]]
    ResourceContainerImageName: Optional[Sequence["_ResourceContainerImageNameDefinition"]]
    ResourceContainerLaunchedAt: Optional[Sequence["_ResourceContainerLaunchedAtDefinition"]]
    ResourceContainerName: Optional[Sequence["_ResourceContainerNameDefinition"]]
    ResourceDetailsOther: Optional[Sequence["_ResourceDetailsOtherDefinition"]]
    ResourceId: Optional[Sequence["_ResourceIdDefinition"]]
    ResourcePartition: Optional[Sequence["_ResourcePartitionDefinition"]]
    ResourceRegion: Optional[Sequence["_ResourceRegionDefinition"]]
    ResourceTags: Optional[Sequence["_ResourceTagsDefinition"]]
    ResourceType: Optional[Sequence["_ResourceTypeDefinition"]]
    SeverityLabel: Optional[Sequence["_SeverityLabelDefinition"]]
    SourceUrl: Optional[Sequence["_SourceUrlDefinition"]]
    ThreatIntelIndicatorCategory: Optional[Sequence["_ThreatIntelIndicatorCategoryDefinition"]]
    ThreatIntelIndicatorLastObservedAt: Optional[Sequence["_ThreatIntelIndicatorLastObservedAtDefinition"]]
    ThreatIntelIndicatorSource: Optional[Sequence["_ThreatIntelIndicatorSourceDefinition"]]
    ThreatIntelIndicatorSourceUrl: Optional[Sequence["_ThreatIntelIndicatorSourceUrlDefinition"]]
    ThreatIntelIndicatorType: Optional[Sequence["_ThreatIntelIndicatorTypeDefinition"]]
    ThreatIntelIndicatorValue: Optional[Sequence["_ThreatIntelIndicatorValueDefinition"]]
    Title: Optional[Sequence["_TitleDefinition"]]
    Type: Optional[Sequence["_TypeDefinition"]]
    UpdatedAt: Optional[Sequence["_UpdatedAtDefinition"]]
    UserDefinedValues: Optional[Sequence["_UserDefinedValuesDefinition"]]
    VerificationState: Optional[Sequence["_VerificationStateDefinition"]]
    WorkflowStatus: Optional[Sequence["_WorkflowStatusDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            AwsAccountId=deserialize_list(json_data.get("AwsAccountId"), AwsAccountIdDefinition),
            CompanyName=deserialize_list(json_data.get("CompanyName"), CompanyNameDefinition),
            ComplianceStatus=deserialize_list(json_data.get("ComplianceStatus"), ComplianceStatusDefinition),
            Confidence=deserialize_list(json_data.get("Confidence"), ConfidenceDefinition),
            CreatedAt=deserialize_list(json_data.get("CreatedAt"), CreatedAtDefinition),
            Criticality=deserialize_list(json_data.get("Criticality"), CriticalityDefinition),
            Description=deserialize_list(json_data.get("Description"), DescriptionDefinition),
            FindingProviderFieldsConfidence=deserialize_list(json_data.get("FindingProviderFieldsConfidence"), FindingProviderFieldsConfidenceDefinition),
            FindingProviderFieldsCriticality=deserialize_list(json_data.get("FindingProviderFieldsCriticality"), FindingProviderFieldsCriticalityDefinition),
            FindingProviderFieldsRelatedFindingsId=deserialize_list(json_data.get("FindingProviderFieldsRelatedFindingsId"), FindingProviderFieldsRelatedFindingsIdDefinition),
            FindingProviderFieldsRelatedFindingsProductArn=deserialize_list(json_data.get("FindingProviderFieldsRelatedFindingsProductArn"), FindingProviderFieldsRelatedFindingsProductArnDefinition),
            FindingProviderFieldsSeverityLabel=deserialize_list(json_data.get("FindingProviderFieldsSeverityLabel"), FindingProviderFieldsSeverityLabelDefinition),
            FindingProviderFieldsSeverityOriginal=deserialize_list(json_data.get("FindingProviderFieldsSeverityOriginal"), FindingProviderFieldsSeverityOriginalDefinition),
            FindingProviderFieldsTypes=deserialize_list(json_data.get("FindingProviderFieldsTypes"), FindingProviderFieldsTypesDefinition),
            FirstObservedAt=deserialize_list(json_data.get("FirstObservedAt"), FirstObservedAtDefinition),
            GeneratorId=deserialize_list(json_data.get("GeneratorId"), GeneratorIdDefinition),
            Id=deserialize_list(json_data.get("Id"), IdDefinition),
            Keyword=deserialize_list(json_data.get("Keyword"), KeywordDefinition),
            LastObservedAt=deserialize_list(json_data.get("LastObservedAt"), LastObservedAtDefinition),
            MalwareName=deserialize_list(json_data.get("MalwareName"), MalwareNameDefinition),
            MalwarePath=deserialize_list(json_data.get("MalwarePath"), MalwarePathDefinition),
            MalwareState=deserialize_list(json_data.get("MalwareState"), MalwareStateDefinition),
            MalwareType=deserialize_list(json_data.get("MalwareType"), MalwareTypeDefinition),
            NetworkDestinationDomain=deserialize_list(json_data.get("NetworkDestinationDomain"), NetworkDestinationDomainDefinition),
            NetworkDestinationIpv4=deserialize_list(json_data.get("NetworkDestinationIpv4"), NetworkDestinationIpv4Definition),
            NetworkDestinationIpv6=deserialize_list(json_data.get("NetworkDestinationIpv6"), NetworkDestinationIpv6Definition),
            NetworkDestinationPort=deserialize_list(json_data.get("NetworkDestinationPort"), NetworkDestinationPortDefinition),
            NetworkDirection=deserialize_list(json_data.get("NetworkDirection"), NetworkDirectionDefinition),
            NetworkProtocol=deserialize_list(json_data.get("NetworkProtocol"), NetworkProtocolDefinition),
            NetworkSourceDomain=deserialize_list(json_data.get("NetworkSourceDomain"), NetworkSourceDomainDefinition),
            NetworkSourceIpv4=deserialize_list(json_data.get("NetworkSourceIpv4"), NetworkSourceIpv4Definition),
            NetworkSourceIpv6=deserialize_list(json_data.get("NetworkSourceIpv6"), NetworkSourceIpv6Definition),
            NetworkSourceMac=deserialize_list(json_data.get("NetworkSourceMac"), NetworkSourceMacDefinition),
            NetworkSourcePort=deserialize_list(json_data.get("NetworkSourcePort"), NetworkSourcePortDefinition),
            NoteText=deserialize_list(json_data.get("NoteText"), NoteTextDefinition),
            NoteUpdatedAt=deserialize_list(json_data.get("NoteUpdatedAt"), NoteUpdatedAtDefinition),
            NoteUpdatedBy=deserialize_list(json_data.get("NoteUpdatedBy"), NoteUpdatedByDefinition),
            ProcessLaunchedAt=deserialize_list(json_data.get("ProcessLaunchedAt"), ProcessLaunchedAtDefinition),
            ProcessName=deserialize_list(json_data.get("ProcessName"), ProcessNameDefinition),
            ProcessParentPid=deserialize_list(json_data.get("ProcessParentPid"), ProcessParentPidDefinition),
            ProcessPath=deserialize_list(json_data.get("ProcessPath"), ProcessPathDefinition),
            ProcessPid=deserialize_list(json_data.get("ProcessPid"), ProcessPidDefinition),
            ProcessTerminatedAt=deserialize_list(json_data.get("ProcessTerminatedAt"), ProcessTerminatedAtDefinition),
            ProductArn=deserialize_list(json_data.get("ProductArn"), ProductArnDefinition),
            ProductFields=deserialize_list(json_data.get("ProductFields"), ProductFieldsDefinition),
            ProductName=deserialize_list(json_data.get("ProductName"), ProductNameDefinition),
            RecommendationText=deserialize_list(json_data.get("RecommendationText"), RecommendationTextDefinition),
            RecordState=deserialize_list(json_data.get("RecordState"), RecordStateDefinition),
            RelatedFindingsId=deserialize_list(json_data.get("RelatedFindingsId"), RelatedFindingsIdDefinition),
            RelatedFindingsProductArn=deserialize_list(json_data.get("RelatedFindingsProductArn"), RelatedFindingsProductArnDefinition),
            ResourceAwsEc2InstanceIamInstanceProfileArn=deserialize_list(json_data.get("ResourceAwsEc2InstanceIamInstanceProfileArn"), ResourceAwsEc2InstanceIamInstanceProfileArnDefinition),
            ResourceAwsEc2InstanceImageId=deserialize_list(json_data.get("ResourceAwsEc2InstanceImageId"), ResourceAwsEc2InstanceImageIdDefinition),
            ResourceAwsEc2InstanceIpv4Addresses=deserialize_list(json_data.get("ResourceAwsEc2InstanceIpv4Addresses"), ResourceAwsEc2InstanceIpv4AddressesDefinition),
            ResourceAwsEc2InstanceIpv6Addresses=deserialize_list(json_data.get("ResourceAwsEc2InstanceIpv6Addresses"), ResourceAwsEc2InstanceIpv6AddressesDefinition),
            ResourceAwsEc2InstanceKeyName=deserialize_list(json_data.get("ResourceAwsEc2InstanceKeyName"), ResourceAwsEc2InstanceKeyNameDefinition),
            ResourceAwsEc2InstanceLaunchedAt=deserialize_list(json_data.get("ResourceAwsEc2InstanceLaunchedAt"), ResourceAwsEc2InstanceLaunchedAtDefinition),
            ResourceAwsEc2InstanceSubnetId=deserialize_list(json_data.get("ResourceAwsEc2InstanceSubnetId"), ResourceAwsEc2InstanceSubnetIdDefinition),
            ResourceAwsEc2InstanceType=deserialize_list(json_data.get("ResourceAwsEc2InstanceType"), ResourceAwsEc2InstanceTypeDefinition),
            ResourceAwsEc2InstanceVpcId=deserialize_list(json_data.get("ResourceAwsEc2InstanceVpcId"), ResourceAwsEc2InstanceVpcIdDefinition),
            ResourceAwsIamAccessKeyCreatedAt=deserialize_list(json_data.get("ResourceAwsIamAccessKeyCreatedAt"), ResourceAwsIamAccessKeyCreatedAtDefinition),
            ResourceAwsIamAccessKeyStatus=deserialize_list(json_data.get("ResourceAwsIamAccessKeyStatus"), ResourceAwsIamAccessKeyStatusDefinition),
            ResourceAwsIamAccessKeyUserName=deserialize_list(json_data.get("ResourceAwsIamAccessKeyUserName"), ResourceAwsIamAccessKeyUserNameDefinition),
            ResourceAwsS3BucketOwnerId=deserialize_list(json_data.get("ResourceAwsS3BucketOwnerId"), ResourceAwsS3BucketOwnerIdDefinition),
            ResourceAwsS3BucketOwnerName=deserialize_list(json_data.get("ResourceAwsS3BucketOwnerName"), ResourceAwsS3BucketOwnerNameDefinition),
            ResourceContainerImageId=deserialize_list(json_data.get("ResourceContainerImageId"), ResourceContainerImageIdDefinition),
            ResourceContainerImageName=deserialize_list(json_data.get("ResourceContainerImageName"), ResourceContainerImageNameDefinition),
            ResourceContainerLaunchedAt=deserialize_list(json_data.get("ResourceContainerLaunchedAt"), ResourceContainerLaunchedAtDefinition),
            ResourceContainerName=deserialize_list(json_data.get("ResourceContainerName"), ResourceContainerNameDefinition),
            ResourceDetailsOther=deserialize_list(json_data.get("ResourceDetailsOther"), ResourceDetailsOtherDefinition),
            ResourceId=deserialize_list(json_data.get("ResourceId"), ResourceIdDefinition),
            ResourcePartition=deserialize_list(json_data.get("ResourcePartition"), ResourcePartitionDefinition),
            ResourceRegion=deserialize_list(json_data.get("ResourceRegion"), ResourceRegionDefinition),
            ResourceTags=deserialize_list(json_data.get("ResourceTags"), ResourceTagsDefinition),
            ResourceType=deserialize_list(json_data.get("ResourceType"), ResourceTypeDefinition),
            SeverityLabel=deserialize_list(json_data.get("SeverityLabel"), SeverityLabelDefinition),
            SourceUrl=deserialize_list(json_data.get("SourceUrl"), SourceUrlDefinition),
            ThreatIntelIndicatorCategory=deserialize_list(json_data.get("ThreatIntelIndicatorCategory"), ThreatIntelIndicatorCategoryDefinition),
            ThreatIntelIndicatorLastObservedAt=deserialize_list(json_data.get("ThreatIntelIndicatorLastObservedAt"), ThreatIntelIndicatorLastObservedAtDefinition),
            ThreatIntelIndicatorSource=deserialize_list(json_data.get("ThreatIntelIndicatorSource"), ThreatIntelIndicatorSourceDefinition),
            ThreatIntelIndicatorSourceUrl=deserialize_list(json_data.get("ThreatIntelIndicatorSourceUrl"), ThreatIntelIndicatorSourceUrlDefinition),
            ThreatIntelIndicatorType=deserialize_list(json_data.get("ThreatIntelIndicatorType"), ThreatIntelIndicatorTypeDefinition),
            ThreatIntelIndicatorValue=deserialize_list(json_data.get("ThreatIntelIndicatorValue"), ThreatIntelIndicatorValueDefinition),
            Title=deserialize_list(json_data.get("Title"), TitleDefinition),
            Type=deserialize_list(json_data.get("Type"), TypeDefinition),
            UpdatedAt=deserialize_list(json_data.get("UpdatedAt"), UpdatedAtDefinition),
            UserDefinedValues=deserialize_list(json_data.get("UserDefinedValues"), UserDefinedValuesDefinition),
            VerificationState=deserialize_list(json_data.get("VerificationState"), VerificationStateDefinition),
            WorkflowStatus=deserialize_list(json_data.get("WorkflowStatus"), WorkflowStatusDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


@dataclass
class AwsAccountIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAccountIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAccountIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAccountIdDefinition = AwsAccountIdDefinition


@dataclass
class CompanyNameDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CompanyNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompanyNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompanyNameDefinition = CompanyNameDefinition


@dataclass
class ComplianceStatusDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComplianceStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComplianceStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComplianceStatusDefinition = ComplianceStatusDefinition


@dataclass
class ConfidenceDefinition(BaseModel):
    Eq: Optional[str]
    Gte: Optional[str]
    Lte: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfidenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfidenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            Gte=json_data.get("Gte"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfidenceDefinition = ConfidenceDefinition


@dataclass
class CreatedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CreatedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreatedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreatedAtDefinition = CreatedAtDefinition


@dataclass
class DateRangeDefinition(BaseModel):
    Unit: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DateRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Unit=json_data.get("Unit"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateRangeDefinition = DateRangeDefinition


@dataclass
class CriticalityDefinition(BaseModel):
    Eq: Optional[str]
    Gte: Optional[str]
    Lte: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CriticalityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriticalityDefinition"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            Gte=json_data.get("Gte"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriticalityDefinition = CriticalityDefinition


@dataclass
class DescriptionDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DescriptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DescriptionDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DescriptionDefinition = DescriptionDefinition


@dataclass
class FindingProviderFieldsConfidenceDefinition(BaseModel):
    Eq: Optional[str]
    Gte: Optional[str]
    Lte: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FindingProviderFieldsConfidenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingProviderFieldsConfidenceDefinition"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            Gte=json_data.get("Gte"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingProviderFieldsConfidenceDefinition = FindingProviderFieldsConfidenceDefinition


@dataclass
class FindingProviderFieldsCriticalityDefinition(BaseModel):
    Eq: Optional[str]
    Gte: Optional[str]
    Lte: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FindingProviderFieldsCriticalityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingProviderFieldsCriticalityDefinition"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            Gte=json_data.get("Gte"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingProviderFieldsCriticalityDefinition = FindingProviderFieldsCriticalityDefinition


@dataclass
class FindingProviderFieldsRelatedFindingsIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FindingProviderFieldsRelatedFindingsIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingProviderFieldsRelatedFindingsIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingProviderFieldsRelatedFindingsIdDefinition = FindingProviderFieldsRelatedFindingsIdDefinition


@dataclass
class FindingProviderFieldsRelatedFindingsProductArnDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FindingProviderFieldsRelatedFindingsProductArnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingProviderFieldsRelatedFindingsProductArnDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingProviderFieldsRelatedFindingsProductArnDefinition = FindingProviderFieldsRelatedFindingsProductArnDefinition


@dataclass
class FindingProviderFieldsSeverityLabelDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FindingProviderFieldsSeverityLabelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingProviderFieldsSeverityLabelDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingProviderFieldsSeverityLabelDefinition = FindingProviderFieldsSeverityLabelDefinition


@dataclass
class FindingProviderFieldsSeverityOriginalDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FindingProviderFieldsSeverityOriginalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingProviderFieldsSeverityOriginalDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingProviderFieldsSeverityOriginalDefinition = FindingProviderFieldsSeverityOriginalDefinition


@dataclass
class FindingProviderFieldsTypesDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FindingProviderFieldsTypesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingProviderFieldsTypesDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingProviderFieldsTypesDefinition = FindingProviderFieldsTypesDefinition


@dataclass
class FirstObservedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FirstObservedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirstObservedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirstObservedAtDefinition = FirstObservedAtDefinition


@dataclass
class GeneratorIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeneratorIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeneratorIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeneratorIdDefinition = GeneratorIdDefinition


@dataclass
class IdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdDefinition = IdDefinition


@dataclass
class KeywordDefinition(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeywordDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeywordDefinition"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeywordDefinition = KeywordDefinition


@dataclass
class LastObservedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LastObservedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastObservedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastObservedAtDefinition = LastObservedAtDefinition


@dataclass
class MalwareNameDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MalwareNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MalwareNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MalwareNameDefinition = MalwareNameDefinition


@dataclass
class MalwarePathDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MalwarePathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MalwarePathDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MalwarePathDefinition = MalwarePathDefinition


@dataclass
class MalwareStateDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MalwareStateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MalwareStateDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MalwareStateDefinition = MalwareStateDefinition


@dataclass
class MalwareTypeDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MalwareTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MalwareTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MalwareTypeDefinition = MalwareTypeDefinition


@dataclass
class NetworkDestinationDomainDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDestinationDomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDestinationDomainDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDestinationDomainDefinition = NetworkDestinationDomainDefinition


@dataclass
class NetworkDestinationIpv4Definition(BaseModel):
    Cidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDestinationIpv4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDestinationIpv4Definition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDestinationIpv4Definition = NetworkDestinationIpv4Definition


@dataclass
class NetworkDestinationIpv6Definition(BaseModel):
    Cidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDestinationIpv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDestinationIpv6Definition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDestinationIpv6Definition = NetworkDestinationIpv6Definition


@dataclass
class NetworkDestinationPortDefinition(BaseModel):
    Eq: Optional[str]
    Gte: Optional[str]
    Lte: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDestinationPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDestinationPortDefinition"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            Gte=json_data.get("Gte"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDestinationPortDefinition = NetworkDestinationPortDefinition


@dataclass
class NetworkDirectionDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkDirectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkDirectionDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkDirectionDefinition = NetworkDirectionDefinition


@dataclass
class NetworkProtocolDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkProtocolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkProtocolDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkProtocolDefinition = NetworkProtocolDefinition


@dataclass
class NetworkSourceDomainDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkSourceDomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkSourceDomainDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkSourceDomainDefinition = NetworkSourceDomainDefinition


@dataclass
class NetworkSourceIpv4Definition(BaseModel):
    Cidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkSourceIpv4Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkSourceIpv4Definition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkSourceIpv4Definition = NetworkSourceIpv4Definition


@dataclass
class NetworkSourceIpv6Definition(BaseModel):
    Cidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkSourceIpv6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkSourceIpv6Definition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkSourceIpv6Definition = NetworkSourceIpv6Definition


@dataclass
class NetworkSourceMacDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkSourceMacDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkSourceMacDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkSourceMacDefinition = NetworkSourceMacDefinition


@dataclass
class NetworkSourcePortDefinition(BaseModel):
    Eq: Optional[str]
    Gte: Optional[str]
    Lte: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkSourcePortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkSourcePortDefinition"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            Gte=json_data.get("Gte"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkSourcePortDefinition = NetworkSourcePortDefinition


@dataclass
class NoteTextDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NoteTextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoteTextDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoteTextDefinition = NoteTextDefinition


@dataclass
class NoteUpdatedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NoteUpdatedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoteUpdatedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoteUpdatedAtDefinition = NoteUpdatedAtDefinition


@dataclass
class NoteUpdatedByDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NoteUpdatedByDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoteUpdatedByDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoteUpdatedByDefinition = NoteUpdatedByDefinition


@dataclass
class ProcessLaunchedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessLaunchedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessLaunchedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessLaunchedAtDefinition = ProcessLaunchedAtDefinition


@dataclass
class ProcessNameDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessNameDefinition = ProcessNameDefinition


@dataclass
class ProcessParentPidDefinition(BaseModel):
    Eq: Optional[str]
    Gte: Optional[str]
    Lte: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessParentPidDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessParentPidDefinition"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            Gte=json_data.get("Gte"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessParentPidDefinition = ProcessParentPidDefinition


@dataclass
class ProcessPathDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessPathDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessPathDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessPathDefinition = ProcessPathDefinition


@dataclass
class ProcessPidDefinition(BaseModel):
    Eq: Optional[str]
    Gte: Optional[str]
    Lte: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessPidDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessPidDefinition"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            Gte=json_data.get("Gte"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessPidDefinition = ProcessPidDefinition


@dataclass
class ProcessTerminatedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessTerminatedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessTerminatedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessTerminatedAtDefinition = ProcessTerminatedAtDefinition


@dataclass
class ProductArnDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProductArnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProductArnDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProductArnDefinition = ProductArnDefinition


@dataclass
class ProductFieldsDefinition(BaseModel):
    Comparison: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProductFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProductFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProductFieldsDefinition = ProductFieldsDefinition


@dataclass
class ProductNameDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProductNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProductNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProductNameDefinition = ProductNameDefinition


@dataclass
class RecommendationTextDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecommendationTextDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecommendationTextDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecommendationTextDefinition = RecommendationTextDefinition


@dataclass
class RecordStateDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordStateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordStateDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordStateDefinition = RecordStateDefinition


@dataclass
class RelatedFindingsIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelatedFindingsIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelatedFindingsIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelatedFindingsIdDefinition = RelatedFindingsIdDefinition


@dataclass
class RelatedFindingsProductArnDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelatedFindingsProductArnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelatedFindingsProductArnDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelatedFindingsProductArnDefinition = RelatedFindingsProductArnDefinition


@dataclass
class ResourceAwsEc2InstanceIamInstanceProfileArnDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsEc2InstanceIamInstanceProfileArnDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsEc2InstanceIamInstanceProfileArnDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsEc2InstanceIamInstanceProfileArnDefinition = ResourceAwsEc2InstanceIamInstanceProfileArnDefinition


@dataclass
class ResourceAwsEc2InstanceImageIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsEc2InstanceImageIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsEc2InstanceImageIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsEc2InstanceImageIdDefinition = ResourceAwsEc2InstanceImageIdDefinition


@dataclass
class ResourceAwsEc2InstanceIpv4AddressesDefinition(BaseModel):
    Cidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsEc2InstanceIpv4AddressesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsEc2InstanceIpv4AddressesDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsEc2InstanceIpv4AddressesDefinition = ResourceAwsEc2InstanceIpv4AddressesDefinition


@dataclass
class ResourceAwsEc2InstanceIpv6AddressesDefinition(BaseModel):
    Cidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsEc2InstanceIpv6AddressesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsEc2InstanceIpv6AddressesDefinition"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsEc2InstanceIpv6AddressesDefinition = ResourceAwsEc2InstanceIpv6AddressesDefinition


@dataclass
class ResourceAwsEc2InstanceKeyNameDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsEc2InstanceKeyNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsEc2InstanceKeyNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsEc2InstanceKeyNameDefinition = ResourceAwsEc2InstanceKeyNameDefinition


@dataclass
class ResourceAwsEc2InstanceLaunchedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsEc2InstanceLaunchedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsEc2InstanceLaunchedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsEc2InstanceLaunchedAtDefinition = ResourceAwsEc2InstanceLaunchedAtDefinition


@dataclass
class ResourceAwsEc2InstanceSubnetIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsEc2InstanceSubnetIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsEc2InstanceSubnetIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsEc2InstanceSubnetIdDefinition = ResourceAwsEc2InstanceSubnetIdDefinition


@dataclass
class ResourceAwsEc2InstanceTypeDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsEc2InstanceTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsEc2InstanceTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsEc2InstanceTypeDefinition = ResourceAwsEc2InstanceTypeDefinition


@dataclass
class ResourceAwsEc2InstanceVpcIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsEc2InstanceVpcIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsEc2InstanceVpcIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsEc2InstanceVpcIdDefinition = ResourceAwsEc2InstanceVpcIdDefinition


@dataclass
class ResourceAwsIamAccessKeyCreatedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsIamAccessKeyCreatedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsIamAccessKeyCreatedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsIamAccessKeyCreatedAtDefinition = ResourceAwsIamAccessKeyCreatedAtDefinition


@dataclass
class ResourceAwsIamAccessKeyStatusDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsIamAccessKeyStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsIamAccessKeyStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsIamAccessKeyStatusDefinition = ResourceAwsIamAccessKeyStatusDefinition


@dataclass
class ResourceAwsIamAccessKeyUserNameDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsIamAccessKeyUserNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsIamAccessKeyUserNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsIamAccessKeyUserNameDefinition = ResourceAwsIamAccessKeyUserNameDefinition


@dataclass
class ResourceAwsS3BucketOwnerIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsS3BucketOwnerIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsS3BucketOwnerIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsS3BucketOwnerIdDefinition = ResourceAwsS3BucketOwnerIdDefinition


@dataclass
class ResourceAwsS3BucketOwnerNameDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAwsS3BucketOwnerNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAwsS3BucketOwnerNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAwsS3BucketOwnerNameDefinition = ResourceAwsS3BucketOwnerNameDefinition


@dataclass
class ResourceContainerImageIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceContainerImageIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceContainerImageIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceContainerImageIdDefinition = ResourceContainerImageIdDefinition


@dataclass
class ResourceContainerImageNameDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceContainerImageNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceContainerImageNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceContainerImageNameDefinition = ResourceContainerImageNameDefinition


@dataclass
class ResourceContainerLaunchedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceContainerLaunchedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceContainerLaunchedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceContainerLaunchedAtDefinition = ResourceContainerLaunchedAtDefinition


@dataclass
class ResourceContainerNameDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceContainerNameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceContainerNameDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceContainerNameDefinition = ResourceContainerNameDefinition


@dataclass
class ResourceDetailsOtherDefinition(BaseModel):
    Comparison: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceDetailsOtherDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceDetailsOtherDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceDetailsOtherDefinition = ResourceDetailsOtherDefinition


@dataclass
class ResourceIdDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceIdDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceIdDefinition = ResourceIdDefinition


@dataclass
class ResourcePartitionDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcePartitionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcePartitionDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcePartitionDefinition = ResourcePartitionDefinition


@dataclass
class ResourceRegionDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceRegionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceRegionDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceRegionDefinition = ResourceRegionDefinition


@dataclass
class ResourceTagsDefinition(BaseModel):
    Comparison: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceTagsDefinition = ResourceTagsDefinition


@dataclass
class ResourceTypeDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceTypeDefinition = ResourceTypeDefinition


@dataclass
class SeverityLabelDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SeverityLabelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeverityLabelDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeverityLabelDefinition = SeverityLabelDefinition


@dataclass
class SourceUrlDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceUrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceUrlDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceUrlDefinition = SourceUrlDefinition


@dataclass
class ThreatIntelIndicatorCategoryDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatIntelIndicatorCategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatIntelIndicatorCategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatIntelIndicatorCategoryDefinition = ThreatIntelIndicatorCategoryDefinition


@dataclass
class ThreatIntelIndicatorLastObservedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatIntelIndicatorLastObservedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatIntelIndicatorLastObservedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatIntelIndicatorLastObservedAtDefinition = ThreatIntelIndicatorLastObservedAtDefinition


@dataclass
class ThreatIntelIndicatorSourceDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatIntelIndicatorSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatIntelIndicatorSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatIntelIndicatorSourceDefinition = ThreatIntelIndicatorSourceDefinition


@dataclass
class ThreatIntelIndicatorSourceUrlDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatIntelIndicatorSourceUrlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatIntelIndicatorSourceUrlDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatIntelIndicatorSourceUrlDefinition = ThreatIntelIndicatorSourceUrlDefinition


@dataclass
class ThreatIntelIndicatorTypeDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatIntelIndicatorTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatIntelIndicatorTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatIntelIndicatorTypeDefinition = ThreatIntelIndicatorTypeDefinition


@dataclass
class ThreatIntelIndicatorValueDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThreatIntelIndicatorValueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThreatIntelIndicatorValueDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThreatIntelIndicatorValueDefinition = ThreatIntelIndicatorValueDefinition


@dataclass
class TitleDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TitleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TitleDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TitleDefinition = TitleDefinition


@dataclass
class TypeDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TypeDefinition = TypeDefinition


@dataclass
class UpdatedAtDefinition(BaseModel):
    End: Optional[str]
    Start: Optional[str]
    DateRange: Optional[Sequence["_DateRangeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UpdatedAtDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdatedAtDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
            DateRange=deserialize_list(json_data.get("DateRange"), DateRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdatedAtDefinition = UpdatedAtDefinition


@dataclass
class UserDefinedValuesDefinition(BaseModel):
    Comparison: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinedValuesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinedValuesDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinedValuesDefinition = UserDefinedValuesDefinition


@dataclass
class VerificationStateDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VerificationStateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VerificationStateDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VerificationStateDefinition = VerificationStateDefinition


@dataclass
class WorkflowStatusDefinition(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowStatusDefinition = WorkflowStatusDefinition


