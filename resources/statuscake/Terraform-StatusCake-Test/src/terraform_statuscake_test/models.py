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
    BasicPass: Optional[str]
    BasicUser: Optional[str]
    Branding: Optional[float]
    CheckRate: Optional[float]
    Confirmations: Optional[float]
    ContactGroup: Optional[Sequence[str]]
    ContactId: Optional[float]
    CustomHeader: Optional[str]
    DoNotFind: Optional[bool]
    EnableSslAlert: Optional[bool]
    FinalEndpoint: Optional[str]
    FindString: Optional[str]
    FollowRedirect: Optional[bool]
    LogoImage: Optional[str]
    NodeLocations: Optional[Sequence[str]]
    Paused: Optional[bool]
    PingUrl: Optional[str]
    Port: Optional[float]
    PostRaw: Optional[str]
    Public: Optional[float]
    RealBrowser: Optional[float]
    Status: Optional[str]
    StatusCodes: Optional[str]
    TestId: Optional[str]
    TestTags: Optional[Sequence[str]]
    TestType: Optional[str]
    Timeout: Optional[float]
    TriggerRate: Optional[float]
    Uptime: Optional[float]
    UseJar: Optional[float]
    UserAgent: Optional[str]
    Virus: Optional[float]
    WebsiteHost: Optional[str]
    WebsiteName: Optional[str]
    WebsiteUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BasicPass=json_data.get("BasicPass"),
            BasicUser=json_data.get("BasicUser"),
            Branding=json_data.get("Branding"),
            CheckRate=json_data.get("CheckRate"),
            Confirmations=json_data.get("Confirmations"),
            ContactGroup=json_data.get("ContactGroup"),
            ContactId=json_data.get("ContactId"),
            CustomHeader=json_data.get("CustomHeader"),
            DoNotFind=json_data.get("DoNotFind"),
            EnableSslAlert=json_data.get("EnableSslAlert"),
            FinalEndpoint=json_data.get("FinalEndpoint"),
            FindString=json_data.get("FindString"),
            FollowRedirect=json_data.get("FollowRedirect"),
            LogoImage=json_data.get("LogoImage"),
            NodeLocations=json_data.get("NodeLocations"),
            Paused=json_data.get("Paused"),
            PingUrl=json_data.get("PingUrl"),
            Port=json_data.get("Port"),
            PostRaw=json_data.get("PostRaw"),
            Public=json_data.get("Public"),
            RealBrowser=json_data.get("RealBrowser"),
            Status=json_data.get("Status"),
            StatusCodes=json_data.get("StatusCodes"),
            TestId=json_data.get("TestId"),
            TestTags=json_data.get("TestTags"),
            TestType=json_data.get("TestType"),
            Timeout=json_data.get("Timeout"),
            TriggerRate=json_data.get("TriggerRate"),
            Uptime=json_data.get("Uptime"),
            UseJar=json_data.get("UseJar"),
            UserAgent=json_data.get("UserAgent"),
            Virus=json_data.get("Virus"),
            WebsiteHost=json_data.get("WebsiteHost"),
            WebsiteName=json_data.get("WebsiteName"),
            WebsiteUrl=json_data.get("WebsiteUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


