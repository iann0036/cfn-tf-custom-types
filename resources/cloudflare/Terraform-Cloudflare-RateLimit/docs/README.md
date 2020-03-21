# Terraform::Cloudflare::RateLimit

CloudFormation equivalent of cloudflare_rate_limit

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::RateLimit",
    "Properties" : {
        "<a href="#bypassurlpatterns" title="BypassUrlPatterns">BypassUrlPatterns</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
        "<a href="#correlate" title="Correlate">Correlate</a>" : <i>[ &lt;a href=&#34;correlate.md&#34;&gt;Correlate&lt;/a&gt;, ... ]</i>,
        "<a href="#match" title="Match">Match</a>" : <i>[ &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;, ... ]</i>,
        "<a href="#response" title="Response">Response</a>" : <i>[ &lt;a href=&#34;response.md&#34;&gt;Response&lt;/a&gt;, ... ]</i>,
        "<a href="#request" title="Request">Request</a>" : <i>[ &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::RateLimit
Properties:
    <a href="#bypassurlpatterns" title="BypassUrlPatterns">BypassUrlPatterns</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;</i>
    <a href="#correlate" title="Correlate">Correlate</a>: <i>
      - &lt;a href=&#34;correlate.md&#34;&gt;Correlate&lt;/a&gt;</i>
    <a href="#match" title="Match">Match</a>: <i>
      - &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;</i>
    <a href="#response" title="Response">Response</a>: <i>
      - &lt;a href=&#34;response.md&#34;&gt;Response&lt;/a&gt;</i>
    <a href="#request" title="Request">Request</a>: <i>
      - &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;</i>
</pre>

## Properties

#### BypassUrlPatterns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Correlate

_Required_: No

_Type_: List of &lt;a href=&#34;correlate.md&#34;&gt;Correlate&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Response

_Required_: No

_Type_: List of &lt;a href=&#34;response.md&#34;&gt;Response&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of &lt;a href=&#34;request.md&#34;&gt;Request&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

