# TF::FortiOS::RouterOspf6 AreaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
    "<a href="#defaultcost" title="DefaultCost">DefaultCost</a>" : <i>Double</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#ipsecauthalg" title="IpsecAuthAlg">IpsecAuthAlg</a>" : <i>String</i>,
    "<a href="#ipsecencalg" title="IpsecEncAlg">IpsecEncAlg</a>" : <i>String</i>,
    "<a href="#keyrolloverinterval" title="KeyRolloverInterval">KeyRolloverInterval</a>" : <i>Double</i>,
    "<a href="#nssadefaultinformationoriginate" title="NssaDefaultInformationOriginate">NssaDefaultInformationOriginate</a>" : <i>String</i>,
    "<a href="#nssadefaultinformationoriginatemetric" title="NssaDefaultInformationOriginateMetric">NssaDefaultInformationOriginateMetric</a>" : <i>Double</i>,
    "<a href="#nssadefaultinformationoriginatemetrictype" title="NssaDefaultInformationOriginateMetricType">NssaDefaultInformationOriginateMetricType</a>" : <i>String</i>,
    "<a href="#nssaredistribution" title="NssaRedistribution">NssaRedistribution</a>" : <i>String</i>,
    "<a href="#nssatranslatorrole" title="NssaTranslatorRole">NssaTranslatorRole</a>" : <i>String</i>,
    "<a href="#stubtype" title="StubType">StubType</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#ipseckeys" title="IpsecKeys">IpsecKeys</a>" : <i>[ <a href="ipseckeysdefinition.md">IpsecKeysDefinition</a>, ... ]</i>,
    "<a href="#range" title="Range">Range</a>" : <i>[ <a href="rangedefinition.md">RangeDefinition</a>, ... ]</i>,
    "<a href="#virtuallink" title="VirtualLink">VirtualLink</a>" : <i>[ <a href="virtuallinkdefinition.md">VirtualLinkDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
<a href="#defaultcost" title="DefaultCost">DefaultCost</a>: <i>Double</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#ipsecauthalg" title="IpsecAuthAlg">IpsecAuthAlg</a>: <i>String</i>
<a href="#ipsecencalg" title="IpsecEncAlg">IpsecEncAlg</a>: <i>String</i>
<a href="#keyrolloverinterval" title="KeyRolloverInterval">KeyRolloverInterval</a>: <i>Double</i>
<a href="#nssadefaultinformationoriginate" title="NssaDefaultInformationOriginate">NssaDefaultInformationOriginate</a>: <i>String</i>
<a href="#nssadefaultinformationoriginatemetric" title="NssaDefaultInformationOriginateMetric">NssaDefaultInformationOriginateMetric</a>: <i>Double</i>
<a href="#nssadefaultinformationoriginatemetrictype" title="NssaDefaultInformationOriginateMetricType">NssaDefaultInformationOriginateMetricType</a>: <i>String</i>
<a href="#nssaredistribution" title="NssaRedistribution">NssaRedistribution</a>: <i>String</i>
<a href="#nssatranslatorrole" title="NssaTranslatorRole">NssaTranslatorRole</a>: <i>String</i>
<a href="#stubtype" title="StubType">StubType</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#ipseckeys" title="IpsecKeys">IpsecKeys</a>: <i>
      - <a href="ipseckeysdefinition.md">IpsecKeysDefinition</a></i>
<a href="#range" title="Range">Range</a>: <i>
      - <a href="rangedefinition.md">RangeDefinition</a></i>
<a href="#virtuallink" title="VirtualLink">VirtualLink</a>: <i>
      - <a href="virtuallinkdefinition.md">VirtualLinkDefinition</a></i>
</pre>

## Properties

#### Authentication

Authentication mode. Valid values: `none`, `ah`, `esp`.

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

#### IpsecAuthAlg

Authentication algorithm. Valid values: `md5`, `sha1`, `sha256`, `sha384`, `sha512`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecEncAlg

Encryption algorithm. Valid values: `null`, `des`, `3des`, `aes128`, `aes192`, `aes256`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyRolloverInterval

Key roll-over interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssaDefaultInformationOriginate

Enable/disable originate type 7 default into NSSA area. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssaDefaultInformationOriginateMetric

OSPFv3 default metric.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NssaDefaultInformationOriginateMetricType

OSPFv3 metric type for default routes. Valid values: `1`, `2`.

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

#### IpsecKeys

_Required_: No

_Type_: List of <a href="ipseckeysdefinition.md">IpsecKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

_Required_: No

_Type_: List of <a href="rangedefinition.md">RangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualLink

_Required_: No

_Type_: List of <a href="virtuallinkdefinition.md">VirtualLinkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

