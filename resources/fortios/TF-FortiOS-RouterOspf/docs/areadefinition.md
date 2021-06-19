# TF::FortiOS::RouterOspf AreaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
    "<a href="#defaultcost" title="DefaultCost">DefaultCost</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#nssadefaultinformationoriginate" title="NssaDefaultInformationOriginate">NssaDefaultInformationOriginate</a>" : <i>String</i>,
    "<a href="#nssadefaultinformationoriginatemetric" title="NssaDefaultInformationOriginateMetric">NssaDefaultInformationOriginateMetric</a>" : <i>Double</i>,
    "<a href="#nssadefaultinformationoriginatemetrictype" title="NssaDefaultInformationOriginateMetricType">NssaDefaultInformationOriginateMetricType</a>" : <i>String</i>,
    "<a href="#nssaredistribution" title="NssaRedistribution">NssaRedistribution</a>" : <i>String</i>,
    "<a href="#nssatranslatorrole" title="NssaTranslatorRole">NssaTranslatorRole</a>" : <i>String</i>,
    "<a href="#shortcut" title="Shortcut">Shortcut</a>" : <i>String</i>,
    "<a href="#stubtype" title="StubType">StubType</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#filterlist" title="FilterList">FilterList</a>" : <i>[ <a href="filterlistdefinition.md">FilterListDefinition</a>, ... ]</i>,
    "<a href="#range" title="Range">Range</a>" : <i>[ <a href="rangedefinition.md">RangeDefinition</a>, ... ]</i>,
    "<a href="#virtuallink" title="VirtualLink">VirtualLink</a>" : <i>[ <a href="virtuallinkdefinition.md">VirtualLinkDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
<a href="#defaultcost" title="DefaultCost">DefaultCost</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#nssadefaultinformationoriginate" title="NssaDefaultInformationOriginate">NssaDefaultInformationOriginate</a>: <i>String</i>
<a href="#nssadefaultinformationoriginatemetric" title="NssaDefaultInformationOriginateMetric">NssaDefaultInformationOriginateMetric</a>: <i>Double</i>
<a href="#nssadefaultinformationoriginatemetrictype" title="NssaDefaultInformationOriginateMetricType">NssaDefaultInformationOriginateMetricType</a>: <i>String</i>
<a href="#nssaredistribution" title="NssaRedistribution">NssaRedistribution</a>: <i>String</i>
<a href="#nssatranslatorrole" title="NssaTranslatorRole">NssaTranslatorRole</a>: <i>String</i>
<a href="#shortcut" title="Shortcut">Shortcut</a>: <i>String</i>
<a href="#stubtype" title="StubType">StubType</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#filterlist" title="FilterList">FilterList</a>: <i>
      - <a href="filterlistdefinition.md">FilterListDefinition</a></i>
<a href="#range" title="Range">Range</a>: <i>
      - <a href="rangedefinition.md">RangeDefinition</a></i>
<a href="#virtuallink" title="VirtualLink">VirtualLink</a>: <i>
      - <a href="virtuallinkdefinition.md">VirtualLinkDefinition</a></i>
</pre>

## Properties

#### Authentication

Authentication type. Valid values: `none`, `text`, `md5`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCost

Summary default cost of stub or NSSA area.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Area entry IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssaDefaultInformationOriginate

Redistribute, advertise, or do not originate Type-7 default route into NSSA area. Valid values: `enable`, `always`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssaDefaultInformationOriginateMetric

OSPF default metric.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssaDefaultInformationOriginateMetricType

OSPF metric type for default routes. Valid values: `1`, `2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssaRedistribution

Enable/disable redistribute into NSSA area. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssaTranslatorRole

NSSA translator role type. Valid values: `candidate`, `never`, `always`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shortcut

Enable/disable shortcut option. Valid values: `disable`, `enable`, `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StubType

Stub summary setting. Valid values: `no-summary`, `summary`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Area type setting. Valid values: `regular`, `nssa`, `stub`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterList

_Required_: No

_Type_: List of <a href="filterlistdefinition.md">FilterListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

_Required_: No

_Type_: List of <a href="rangedefinition.md">RangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualLink

_Required_: No

_Type_: List of <a href="virtuallinkdefinition.md">VirtualLinkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

