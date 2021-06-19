# TF::FortiOS::WafProfile ConstraintDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#contentlength" title="ContentLength">ContentLength</a>" : <i>[ <a href="contentlengthdefinition.md">ContentLengthDefinition</a>, ... ]</i>,
    "<a href="#exception" title="Exception">Exception</a>" : <i>[ <a href="exceptiondefinition.md">ExceptionDefinition</a>, ... ]</i>,
    "<a href="#headerlength" title="HeaderLength">HeaderLength</a>" : <i>[ <a href="headerlengthdefinition.md">HeaderLengthDefinition</a>, ... ]</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>[ <a href="hostnamedefinition.md">HostnameDefinition</a>, ... ]</i>,
    "<a href="#linelength" title="LineLength">LineLength</a>" : <i>[ <a href="linelengthdefinition.md">LineLengthDefinition</a>, ... ]</i>,
    "<a href="#malformed" title="Malformed">Malformed</a>" : <i>[ <a href="malformeddefinition.md">MalformedDefinition</a>, ... ]</i>,
    "<a href="#maxcookie" title="MaxCookie">MaxCookie</a>" : <i>[ <a href="maxcookiedefinition.md">MaxCookieDefinition</a>, ... ]</i>,
    "<a href="#maxheaderline" title="MaxHeaderLine">MaxHeaderLine</a>" : <i>[ <a href="maxheaderlinedefinition.md">MaxHeaderLineDefinition</a>, ... ]</i>,
    "<a href="#maxrangesegment" title="MaxRangeSegment">MaxRangeSegment</a>" : <i>[ <a href="maxrangesegmentdefinition.md">MaxRangeSegmentDefinition</a>, ... ]</i>,
    "<a href="#maxurlparam" title="MaxUrlParam">MaxUrlParam</a>" : <i>[ <a href="maxurlparamdefinition.md">MaxUrlParamDefinition</a>, ... ]</i>,
    "<a href="#method" title="Method">Method</a>" : <i>[ <a href="methoddefinition.md">MethodDefinition</a>, ... ]</i>,
    "<a href="#paramlength" title="ParamLength">ParamLength</a>" : <i>[ <a href="paramlengthdefinition.md">ParamLengthDefinition</a>, ... ]</i>,
    "<a href="#urlparamlength" title="UrlParamLength">UrlParamLength</a>" : <i>[ <a href="urlparamlengthdefinition.md">UrlParamLengthDefinition</a>, ... ]</i>,
    "<a href="#version" title="Version">Version</a>" : <i>[ <a href="versiondefinition.md">VersionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#contentlength" title="ContentLength">ContentLength</a>: <i>
      - <a href="contentlengthdefinition.md">ContentLengthDefinition</a></i>
<a href="#exception" title="Exception">Exception</a>: <i>
      - <a href="exceptiondefinition.md">ExceptionDefinition</a></i>
<a href="#headerlength" title="HeaderLength">HeaderLength</a>: <i>
      - <a href="headerlengthdefinition.md">HeaderLengthDefinition</a></i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>
      - <a href="hostnamedefinition.md">HostnameDefinition</a></i>
<a href="#linelength" title="LineLength">LineLength</a>: <i>
      - <a href="linelengthdefinition.md">LineLengthDefinition</a></i>
<a href="#malformed" title="Malformed">Malformed</a>: <i>
      - <a href="malformeddefinition.md">MalformedDefinition</a></i>
<a href="#maxcookie" title="MaxCookie">MaxCookie</a>: <i>
      - <a href="maxcookiedefinition.md">MaxCookieDefinition</a></i>
<a href="#maxheaderline" title="MaxHeaderLine">MaxHeaderLine</a>: <i>
      - <a href="maxheaderlinedefinition.md">MaxHeaderLineDefinition</a></i>
<a href="#maxrangesegment" title="MaxRangeSegment">MaxRangeSegment</a>: <i>
      - <a href="maxrangesegmentdefinition.md">MaxRangeSegmentDefinition</a></i>
<a href="#maxurlparam" title="MaxUrlParam">MaxUrlParam</a>: <i>
      - <a href="maxurlparamdefinition.md">MaxUrlParamDefinition</a></i>
<a href="#method" title="Method">Method</a>: <i>
      - <a href="methoddefinition.md">MethodDefinition</a></i>
<a href="#paramlength" title="ParamLength">ParamLength</a>: <i>
      - <a href="paramlengthdefinition.md">ParamLengthDefinition</a></i>
<a href="#urlparamlength" title="UrlParamLength">UrlParamLength</a>: <i>
      - <a href="urlparamlengthdefinition.md">UrlParamLengthDefinition</a></i>
<a href="#version" title="Version">Version</a>: <i>
      - <a href="versiondefinition.md">VersionDefinition</a></i>
</pre>

## Properties

#### ContentLength

_Required_: No

_Type_: List of <a href="contentlengthdefinition.md">ContentLengthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exception

_Required_: No

_Type_: List of <a href="exceptiondefinition.md">ExceptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderLength

_Required_: No

_Type_: List of <a href="headerlengthdefinition.md">HeaderLengthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: List of <a href="hostnamedefinition.md">HostnameDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LineLength

_Required_: No

_Type_: List of <a href="linelengthdefinition.md">LineLengthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Malformed

_Required_: No

_Type_: List of <a href="malformeddefinition.md">MalformedDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCookie

_Required_: No

_Type_: List of <a href="maxcookiedefinition.md">MaxCookieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxHeaderLine

_Required_: No

_Type_: List of <a href="maxheaderlinedefinition.md">MaxHeaderLineDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRangeSegment

_Required_: No

_Type_: List of <a href="maxrangesegmentdefinition.md">MaxRangeSegmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUrlParam

_Required_: No

_Type_: List of <a href="maxurlparamdefinition.md">MaxUrlParamDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: List of <a href="methoddefinition.md">MethodDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParamLength

_Required_: No

_Type_: List of <a href="paramlengthdefinition.md">ParamLengthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlParamLength

_Required_: No

_Type_: List of <a href="urlparamlengthdefinition.md">UrlParamLengthDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: List of <a href="versiondefinition.md">VersionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

