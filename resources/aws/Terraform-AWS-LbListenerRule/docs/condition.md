# Terraform::AWS::LbListenerRule Condition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#field" title="Field">Field</a>" : <i>String</i>,
    "<a href="#values" title="Values">Values</a>" : <i>[ String, ... ]</i>,
    "<a href="#hostheader" title="HostHeader">HostHeader</a>" : <i>[ <a href="condition-hostheader.md">HostHeader</a>, ... ]</i>,
    "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ <a href="condition-httpheader.md">HttpHeader</a>, ... ]</i>,
    "<a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>" : <i>[ <a href="condition-httprequestmethod.md">HttpRequestMethod</a>, ... ]</i>,
    "<a href="#pathpattern" title="PathPattern">PathPattern</a>" : <i>[ <a href="condition-pathpattern.md">PathPattern</a>, ... ]</i>,
    "<a href="#querystring" title="QueryString">QueryString</a>" : <i>[ <a href="condition-querystring.md">QueryString</a>, ... ]</i>,
    "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>[ <a href="condition-sourceip.md">SourceIp</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#field" title="Field">Field</a>: <i>String</i>
<a href="#values" title="Values">Values</a>: <i>
      - String</i>
<a href="#hostheader" title="HostHeader">HostHeader</a>: <i>
      - <a href="condition-hostheader.md">HostHeader</a></i>
<a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - <a href="condition-httpheader.md">HttpHeader</a></i>
<a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>: <i>
      - <a href="condition-httprequestmethod.md">HttpRequestMethod</a></i>
<a href="#pathpattern" title="PathPattern">PathPattern</a>: <i>
      - <a href="condition-pathpattern.md">PathPattern</a></i>
<a href="#querystring" title="QueryString">QueryString</a>: <i>
      - <a href="condition-querystring.md">QueryString</a></i>
<a href="#sourceip" title="SourceIp">SourceIp</a>: <i>
      - <a href="condition-sourceip.md">SourceIp</a></i>
</pre>

## Properties

#### Field

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostHeader

_Required_: No

_Type_: List of <a href="condition-hostheader.md">HostHeader</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No

_Type_: List of <a href="condition-httpheader.md">HttpHeader</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestMethod

_Required_: No

_Type_: List of <a href="condition-httprequestmethod.md">HttpRequestMethod</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPattern

_Required_: No

_Type_: List of <a href="condition-pathpattern.md">PathPattern</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: No

_Type_: List of <a href="condition-querystring.md">QueryString</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

_Required_: No

_Type_: List of <a href="condition-sourceip.md">SourceIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

