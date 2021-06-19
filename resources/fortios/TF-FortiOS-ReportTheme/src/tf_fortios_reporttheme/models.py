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
    BulletListStyle: Optional[str]
    ColumnCount: Optional[str]
    DefaultHtmlStyle: Optional[str]
    DefaultPdfStyle: Optional[str]
    GraphChartStyle: Optional[str]
    Heading1Style: Optional[str]
    Heading2Style: Optional[str]
    Heading3Style: Optional[str]
    Heading4Style: Optional[str]
    HlineStyle: Optional[str]
    Id: Optional[str]
    ImageStyle: Optional[str]
    Name: Optional[str]
    NormalTextStyle: Optional[str]
    NumberedListStyle: Optional[str]
    PageFooterStyle: Optional[str]
    PageHeaderStyle: Optional[str]
    PageOrient: Optional[str]
    PageStyle: Optional[str]
    ReportSubtitleStyle: Optional[str]
    ReportTitleStyle: Optional[str]
    TableChartCaptionStyle: Optional[str]
    TableChartEvenRowStyle: Optional[str]
    TableChartHeadStyle: Optional[str]
    TableChartOddRowStyle: Optional[str]
    TableChartStyle: Optional[str]
    TocHeading1Style: Optional[str]
    TocHeading2Style: Optional[str]
    TocHeading3Style: Optional[str]
    TocHeading4Style: Optional[str]
    TocTitleStyle: Optional[str]
    Vdomparam: Optional[str]

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
            BulletListStyle=json_data.get("BulletListStyle"),
            ColumnCount=json_data.get("ColumnCount"),
            DefaultHtmlStyle=json_data.get("DefaultHtmlStyle"),
            DefaultPdfStyle=json_data.get("DefaultPdfStyle"),
            GraphChartStyle=json_data.get("GraphChartStyle"),
            Heading1Style=json_data.get("Heading1Style"),
            Heading2Style=json_data.get("Heading2Style"),
            Heading3Style=json_data.get("Heading3Style"),
            Heading4Style=json_data.get("Heading4Style"),
            HlineStyle=json_data.get("HlineStyle"),
            Id=json_data.get("Id"),
            ImageStyle=json_data.get("ImageStyle"),
            Name=json_data.get("Name"),
            NormalTextStyle=json_data.get("NormalTextStyle"),
            NumberedListStyle=json_data.get("NumberedListStyle"),
            PageFooterStyle=json_data.get("PageFooterStyle"),
            PageHeaderStyle=json_data.get("PageHeaderStyle"),
            PageOrient=json_data.get("PageOrient"),
            PageStyle=json_data.get("PageStyle"),
            ReportSubtitleStyle=json_data.get("ReportSubtitleStyle"),
            ReportTitleStyle=json_data.get("ReportTitleStyle"),
            TableChartCaptionStyle=json_data.get("TableChartCaptionStyle"),
            TableChartEvenRowStyle=json_data.get("TableChartEvenRowStyle"),
            TableChartHeadStyle=json_data.get("TableChartHeadStyle"),
            TableChartOddRowStyle=json_data.get("TableChartOddRowStyle"),
            TableChartStyle=json_data.get("TableChartStyle"),
            TocHeading1Style=json_data.get("TocHeading1Style"),
            TocHeading2Style=json_data.get("TocHeading2Style"),
            TocHeading3Style=json_data.get("TocHeading3Style"),
            TocHeading4Style=json_data.get("TocHeading4Style"),
            TocTitleStyle=json_data.get("TocTitleStyle"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


