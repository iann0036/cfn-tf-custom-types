# TF::FortiOS::WafProfile ExceptionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#contentlength" title="ContentLength">ContentLength</a>" : <i>[ <a href="contentlengthdefinition.md">ContentLengthDefinition</a>, ... ]</i>,
    "<a href="#headerlength" title="HeaderLength">HeaderLength</a>" : <i>String</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#linelength" title="LineLength">LineLength</a>" : <i>String</i>,
    "<a href="#malformed" title="Malformed">Malformed</a>" : <i>String</i>,
    "<a href="#maxcookie" title="MaxCookie">MaxCookie</a>" : <i>String</i>,
    "<a href="#maxheaderline" title="MaxHeaderLine">MaxHeaderLine</a>" : <i>String</i>,
    "<a href="#maxrangesegment" title="MaxRangeSegment">MaxRangeSegment</a>" : <i>String</i>,
    "<a href="#maxurlparam" title="MaxUrlParam">MaxUrlParam</a>" : <i>String</i>,
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#paramlength" title="ParamLength">ParamLength</a>" : <i>String</i>,
    "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>,
    "<a href="#regex" title="Regex">Regex</a>" : <i>String</i>,
    "<a href="#urlparamlength" title="UrlParamLength">UrlParamLength</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#contentlength" title="ContentLength">ContentLength</a>: <i>
      - <a href="contentlengthdefinition.md">ContentLengthDefinition</a></i>
<a href="#headerlength" title="HeaderLength">HeaderLength</a>: <i>String</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#linelength" title="LineLength">LineLength</a>: <i>String</i>
<a href="#malformed" title="Malformed">Malformed</a>: <i>String</i>
<a href="#maxcookie" title="MaxCookie">MaxCookie</a>: <i>String</i>
<a href="#maxheaderline" title="MaxHeaderLine">MaxHeaderLine</a>: <i>String</i>
<a href="#maxrangesegment" title="MaxRangeSegment">MaxRangeSegment</a>: <i>String</i>
<a href="#maxurlparam" title="MaxUrlParam">MaxUrlParam</a>: <i>String</i>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#paramlength" title="ParamLength">ParamLength</a>: <i>String</i>
<a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
<a href="#regex" title="Regex">Regex</a>: <i>String</i>
<a href="#urlparamlength" title="UrlParamLength">UrlParamLength</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### Address

Host address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentLength

_Required_: No

_Type_: List of <a href="contentlengthdefinition.md">ContentLengthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderLength

HTTP header length in request. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

Enable/disable hostname check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Exception ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LineLength

HTTP line length in request. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Malformed

Enable/disable malformed HTTP request check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCookie

Maximum number of cookies in HTTP request. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHeaderLine

Maximum number of HTTP header line. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRangeSegment

Maximum number of range segments in HTTP range line. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUrlParam

Maximum number of parameters in URL. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

Enable/disable HTTP method check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParamLength

Maximum length of parameter in URL, HTTP POST request or HTTP body. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pattern

URL pattern.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regex

Enable/disable regular expression based pattern match. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlParamLength

Maximum length of parameter in URL. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Enable/disable HTTP version check. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

