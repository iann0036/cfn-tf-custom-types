# Terraform::AWS::AlbListenerRule Condition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#field" title="Field">Field</a>" : <i>String</i>,
    "<a href="#values" title="Values">Values</a>" : <i>[ String, ... ]</i>,
    "<a href="#hostheader" title="HostHeader">HostHeader</a>" : <i>[ &lt;a href=&#34;condition-hostheader.md&#34;&gt;HostHeader&lt;/a&gt;, ... ]</i>,
    "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ &lt;a href=&#34;condition-httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;, ... ]</i>,
    "<a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>" : <i>[ &lt;a href=&#34;condition-httprequestmethod.md&#34;&gt;HttpRequestMethod&lt;/a&gt;, ... ]</i>,
    "<a href="#pathpattern" title="PathPattern">PathPattern</a>" : <i>[ &lt;a href=&#34;condition-pathpattern.md&#34;&gt;PathPattern&lt;/a&gt;, ... ]</i>,
    "<a href="#querystring" title="QueryString">QueryString</a>" : <i>[ &lt;a href=&#34;condition-querystring.md&#34;&gt;QueryString&lt;/a&gt;, ... ]</i>,
    "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>[ &lt;a href=&#34;condition-sourceip.md&#34;&gt;SourceIp&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#field" title="Field">Field</a>: <i>String</i>
<a href="#values" title="Values">Values</a>: <i>
      - String</i>
<a href="#hostheader" title="HostHeader">HostHeader</a>: <i>
      - &lt;a href=&#34;condition-hostheader.md&#34;&gt;HostHeader&lt;/a&gt;</i>
<a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - &lt;a href=&#34;condition-httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;</i>
<a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>: <i>
      - &lt;a href=&#34;condition-httprequestmethod.md&#34;&gt;HttpRequestMethod&lt;/a&gt;</i>
<a href="#pathpattern" title="PathPattern">PathPattern</a>: <i>
      - &lt;a href=&#34;condition-pathpattern.md&#34;&gt;PathPattern&lt;/a&gt;</i>
<a href="#querystring" title="QueryString">QueryString</a>: <i>
      - &lt;a href=&#34;condition-querystring.md&#34;&gt;QueryString&lt;/a&gt;</i>
<a href="#sourceip" title="SourceIp">SourceIp</a>: <i>
      - &lt;a href=&#34;condition-sourceip.md&#34;&gt;SourceIp&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;condition-hostheader.md&#34;&gt;HostHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No
_Type_: List of &lt;a href=&#34;condition-httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestMethod

_Required_: No
_Type_: List of &lt;a href=&#34;condition-httprequestmethod.md&#34;&gt;HttpRequestMethod&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPattern

_Required_: No
_Type_: List of &lt;a href=&#34;condition-pathpattern.md&#34;&gt;PathPattern&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: No
_Type_: List of &lt;a href=&#34;condition-querystring.md&#34;&gt;QueryString&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

_Required_: No
_Type_: List of &lt;a href=&#34;condition-sourceip.md&#34;&gt;SourceIp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

