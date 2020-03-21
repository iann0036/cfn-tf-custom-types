# Terraform::OCI::WaasWaasPolicy Origins

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#httpport" title="HttpPort">HttpPort</a>" : <i>Double</i>,
    "<a href="#httpsport" title="HttpsPort">HttpsPort</a>" : <i>Double</i>,
    "<a href="#label" title="Label">Label</a>" : <i>String</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
    "<a href="#customheaders" title="CustomHeaders">CustomHeaders</a>" : <i>[ &lt;a href=&#34;origins-customheaders.md&#34;&gt;CustomHeaders&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#httpport" title="HttpPort">HttpPort</a>: <i>Double</i>
<a href="#httpsport" title="HttpsPort">HttpsPort</a>: <i>Double</i>
<a href="#label" title="Label">Label</a>: <i>String</i>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
<a href="#customheaders" title="CustomHeaders">CustomHeaders</a>: <i>
      - &lt;a href=&#34;origins-customheaders.md&#34;&gt;CustomHeaders&lt;/a&gt;</i>
</pre>

## Properties

#### HttpPort

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsPort

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomHeaders

_Required_: No
_Type_: List of &lt;a href=&#34;origins-customheaders.md&#34;&gt;CustomHeaders&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

